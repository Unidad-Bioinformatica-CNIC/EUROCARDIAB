--Number of patients with diabetes mellitus and hypertension 
SELECT COUNT(DISTINCT co1.person_id) AS total_patients, p.gender_concept_id, FLOOR((extract( year from co1.condition_start_date) - p.YEAR_OF_BIRTH) /10) AS age_decile
FROM {cdm_schema}.condition_occurrence co1
JOIN {vocab_schema}.concept_ancestor ca1
    ON co1.condition_concept_id = ca1.descendant_concept_id
JOIN {cdm_schema}.condition_occurrence co2
    ON co1.person_id = co2.person_id
JOIN {vocab_schema}.concept_ancestor ca2
    ON co2.condition_concept_id = ca2.descendant_concept_id
JOIN {cdm_schema}.person p
    ON co1.person_id = p.person_id
WHERE ca1.ancestor_concept_id = 201820   -- Diabetes mellitus
  AND ca2.ancestor_concept_id = 316866   -- Hypertensive Disorder  
GROUP BY p.gender_concept_id, FLOOR((extract( year from co1.condition_start_date) - p.YEAR_OF_BIRTH) /10);