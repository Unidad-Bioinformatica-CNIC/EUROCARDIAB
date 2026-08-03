--Number of patients presenting chest pain
SELECT COUNT(DISTINCT co.person_id) AS total_patients
FROM {cdm_schema}.condition_occurrence co
JOIN {vocab_schema}.concept_ancestor ca
	ON co.condition_concept_id= ca.descendant_concept_id
JOIN {cdm_schema}.visit_occurrence vo
	ON co.person_id = vo.person_id
WHERE co.condition_concept_id = 77670 	--chest pain
AND vo.admited_from_concept_id = 9203;  --Urgencias