--Number of patients presenting chest pain and diagnosed with an unstable angina pectoris that are subjected to a coronoary angiography
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
JOIN {cdm_schema}.procedure_occurrence po
	ON co.visit_occurrence_id = po.visit_occurrence_id
JOIN {vocab_schema}.concept_ancestor ca3
	ON po.procedure_concept_id = ca3.descendant_concept_id
WHERE ca.ancestor_concept_id = 77670 	--chest pain
AND vo.{admision_field} = 9203   --Urgencias 
AND ca2.ancestor_concept_id = 315296 	--unestable angina pectoris
AND ca3.ancestor_concept_id = 4142645;	--Coronary angiography