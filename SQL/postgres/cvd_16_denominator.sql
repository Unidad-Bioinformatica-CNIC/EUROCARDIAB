--Number of patients presenting chest pain that are diagnosed with a unstable angina pectoris
SELECT COUNT(DISTINCT co.person_id) AS total_patients
FROM {cdm_schema}.condition_occurrence co
JOIN {vocab_schema}.concept_ancestor ca
	ON co.condition_concept_id= ca.descendant_concept_id
JOIN {cdm_schema}.visit_occurrence vo
	ON co.person_id = vo.person_id
JOIN {cdm_schema}.condition_occurrence co2
	ON co.visit_occurrence_id = co2.visit_occurrence_id
JOIN {vocab_schema}.concept_ancestor ca2
	ON co2.condition_concept_id = ca2.descendant_concept_id
WHERE ca.ancestor_concept_id = 77670 	--chest pain
AND vo.{admision_field} = 9203   --Urgencias
and ca2.ancestor_concept_id = 315296;	--unestable angina pectoris