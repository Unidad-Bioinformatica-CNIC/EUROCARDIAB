-- Number of patients with any cardiovascular finding that are also diagnosed with hypertension
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
WHERE ca.ancestor_concept_id = 4023995 AND ca2.ancestor_concept_id = 316866 AND co.condition_occurrence_id != co2.condition_occurrence_id -- 4023995 cardiovascular finding, 316866 hypertensive disorder
GROUP BY p.gender_concept_id, FLOOR((extract( year from co2.condition_start_date) - p.YEAR_OF_BIRTH) /10);