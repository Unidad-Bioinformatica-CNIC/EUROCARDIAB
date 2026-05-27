--Number of patients presenting chest pain that are diagnosed with an acute coronary syndrome
SELECT COUNT(DISTINCT co.person_id) AS total_patients, p.gender_concept_id, FLOOR((extract( year from co.condition_start_date) - p.YEAR_OF_BIRTH) /10) AS age_decile
FROM {cdm_schema}.condition_occurrence co
JOIN {vocab_schema}.concept_ancestor ca
	ON co.condition_concept_id= ca.descendant_concept_id
JOIN {cdm_schema}.condition_occurrence co2
	ON co.visit_occurrence_id = co2.visit_occurrence_id
JOIN {vocab_schema}.concept_ancestor ca2
	ON co2.condition_concept_id = ca2.descendant_concept_id
JOIN {cdm_schema}.person p
    ON co.person_id = p.person_id
WHERE ca.ancestor_concept_id = 77670 and (ca2.ancestor_concept_id = 4239975 or ca2.ancestor_concept_id = 315296)    --myocardial disease (STEMI NSTEMI Takotsubo) or perinfarction syndrome (angina de pecho inestable)
GROUP BY p.gender_concept_id, FLOOR((extract( year from co.condition_start_date) - p.YEAR_OF_BIRTH) /10);