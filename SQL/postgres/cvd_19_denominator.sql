--Number of patients with a NSTEMI diagnosed
SELECT COUNT(DISTINCT co.person_id) AS total_patients
FROM {cdm_schema}.condition_occurrence co
JOIN {vocab_schema}.concept_ancestor ca
	ON co.condition_concept_id= ca.descendant_concept_id
WHERE co.condition_concept_id = (4270024, 45766241);  --NSTEMI