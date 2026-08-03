-- Number of patients with any cardiovascular finding and diagnosed hypertension that shows levels of blood preasure > 130 mmHg
SELECT COUNT (DISTINCT co.person_id) AS total_patients, p.gender_concept_id, FLOOR((extract( year from co2.condition_start_date) - p.YEAR_OF_BIRTH) /10) AS age_decile
FROM {cdm_schema}.condition_occurrence co
JOIN {vocab_schema}.concept_ancestor ca 
    ON co.condition_concept_id = ca.descendant_concept_id
JOIN  {cdm_schema}.condition_occurrence co2
    ON co.person_id = co2.person_id
JOIN {vocab_schema}.concept_ancestor ca2
	ON co2.condition_concept_id = ca2.descendant_concept_id
JOIN {cdm_schema}.measurement m
    ON co.person_id = m.person_id
JOIN {vocab_schema}.concept_ancestor ca3
    ON m.measurement_concept_id = ca3.descendant_concept_id
JOIN {cdm_schema}.person p
    ON co.person_id = p.person_id
WHERE ca.ancestor_concept_id = 4023995  --cardiovascular finding 
AND ca2.ancestor_concept_id = 316866    --hipertensive disorder
AND ca3.ancestor_concept_id = 4326744   --blood preasure measurement
AND co.condition_occurrence_id != co2.condition_occurrence_id 
AND m.unit_concept_id = 8876    --mmHg
AND m.value_as_number >= 130
GROUP BY p.gender_concept_id, FLOOR((extract( year from co2.condition_start_date) - p.YEAR_OF_BIRTH) /10);


--OPTIMAL
-- SELECT COUNT (DISTINCT p.person_id) AS total_patients, p.gender_concept_id, FLOOR((extract( year from co2.condition_start_date) - p.YEAR_OF_BIRTH) /10) AS age_decile
-- FROM {cdm_schema}.condition_occurrence co2
-- JOIN {vocab_schema}.concept_ancestor ca2
--     ON co2.condition_concept_id = ca2.descendant_concept_id
-- JOIN {cdm_schema}.person p
--     ON co2.person_id = p.person_id
-- WHERE exists ( select 1
--     from {cdm_schema}.condition_occurrence co
--     join {vocab_schema}.concept_ancestor ca ON co.condition_concept_id = ca.descendant_concept_id
--     JOIN {cdm_schema}.measurement m ON co.person_id = m.person_id
--     JOIN {vocab_schema}.concept_ancestor ca3 ON m.measurement_concept_id = ca3.descendant_concept_id
--     where
--         ca.ancestor_concept_id = 4023995
--         and co.condition_occurrence_id != co2.condition_occurrence_id -- 4023995 cardiovascular finding, 316866 hypertensive disorder
--         and ca3.ancestor_concept_id = 4326744
--         and co.person_id = p.person_id
--         and m.unit_concept_id = 8876 
--         and m.value_as_number >= 130
--     )
--     and ca2.ancestor_concept_id = 316866
-- GROUP BY p.gender_concept_id, age_decile