-- Number of patients with any cardiovascular finding that are also diagnosed with diabetes
SELECT COUNT (DISTINCT co.person_id) AS total_patients, p.gender_concept_id, FLOOR((extract( year from co2.condition_start_date) - p.YEAR_OF_BIRTH) /10) AS age_decile
FROM {cdm_schema}.condition_occurrence co
JOIN {vocab_schema}.concept_ancestor ca 
    ON co.condition_concept_id = ca.descendant_concept_id
JOIN  {cdm_schema}.condition_occurrence co2
    ON co.person_id = co2.person_id
JOIN {vocab_schema}.concept_ancestor ca2
	ON co2.condition_concept_id = ca2.descendant_concept_id
JOIN {cdm_schema}.person p
    ON co.person_id = p.person_id
WHERE ca.ancestor_concept_id = 4023995  --cardiovascular finding
AND ca2.ancestor_concept_id = 201820    --diabetes mellitus
AND co.condition_occurrence_id != co2.condition_occurrence_id 
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
--     where
--         ca.ancestor_concept_id = 4023995
--         and co.condition_occurrence_id != co2.condition_occurrence_id -- 4023995 cardiovascular finding, 316866 hypertensive disorder
--         and co.person_id = p.person_id
--     )
--     and ca2.ancestor_concept_id = 201820
-- GROUP BY p.gender_concept_id, age_decile