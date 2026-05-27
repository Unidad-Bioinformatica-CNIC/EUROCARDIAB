--Number of patients presenting chest pain, diagnosed with an NSTEMI and subjected to a coronoary angiography that present a coronary oclusion
SELECT COUNT(DISTINCT co.person_id) AS total_patients, p.gender_concept_id, FLOOR((extract( year from co.condition_start_date) - p.YEAR_OF_BIRTH) /10) AS age_decile
FROM {cdm_schema}.condition_occurrence co
JOIN {vocab_schema}.concept_ancestor ca
	ON co.condition_concept_id= ca.descendant_concept_id
JOIN {cdm_schema}.condition_occurrence co2
	ON co.visit_occurrence_id = co2.visit_occurrence_id
JOIN {vocab_schema}.concept_ancestor ca2
	ON co2.condition_concept_id = ca2.descendant_concept_id
JOIN {cdm_schema}.procedure_occurrence po
	ON co.visit_occurrence_id = po.visit_occurrence_id
JOIN {vocab_schema}.concept_ancestor ca3
	ON po.procedure_concept_id = ca3.descendant_concept_id
JOIN {cdm_schema}.condition_occurrence co3
	ON co.visit_occurrence_id = co3.visit_occurrence_id
JOIN {vocab_schema}.concept_ancestor ca4
	ON co3.condition_concept_id = ca4.descendant_concept_id
JOIN {cdm_schema}.person p
    ON co.person_id = p.person_id
WHERE ca.ancestor_concept_id = 77670 and ca2.ancestor_concept_id = 4270024 and ca3.ancestor_concept_id = 4142645 and ca4.ancestor_concept_id = 316995
GROUP BY p.gender_concept_id, FLOOR((extract( year from co.condition_start_date) - p.YEAR_OF_BIRTH) /10);