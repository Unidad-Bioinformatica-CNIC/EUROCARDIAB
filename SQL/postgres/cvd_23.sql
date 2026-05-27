--Number of patients that are discharged after an event of heart failure
WITH pre AS (SELECT 
		co.person_id,
		co.condition_concept_id,
		ca.ancestor_concept_id,
		vo.visit_concept_id,
		vo.visit_end_date
    FROM {cdm_schema}.condition_occurrence co
    JOIN {vocab_schema}.concept_ancestor ca
        ON co.condition_concept_id = ca.descendant_concept_id
	JOIN {cdm_schema}.visit_occurrence vo
		ON co.visit_occurrence_id = vo.visit_occurrence_id)
SELECT count (DISTINCT pre.person_id) AS total_patients 
	FROM pre
	LEFT JOIN {cdm_schema}.death d
		ON pre.person_id = d.person_id
    WHERE pre.ancestor_concept_id = 316139 AND pre.visit_concept_id = 9201 AND (pre.visit_end_date IS DISTINCT FROM d.death_date); -- 9201 inpatient visit and no dieying in the visit
--Number of patients that die in less than 30 days after disclosure for a heart failure event
WITH pre AS (SELECT 
		co.person_id as patient,
		co.condition_concept_id,
		ca.ancestor_concept_id,
		vo.visit_concept_id,
		vo.visit_end_date
    FROM {cdm_schema}.condition_occurrence co
    JOIN {vocab_schema}.concept_ancestor ca
        ON co.condition_concept_id = ca.descendant_concept_id
	JOIN {cdm_schema}.visit_occurrence vo
		ON co.visit_occurrence_id = vo.visit_occurrence_id),
dead_patients AS (SELECT *
	FROM pre
	JOIN {cdm_schema}.death d
		ON pre.patient = d.person_id
    WHERE pre.ancestor_concept_id = 316139 AND pre.visit_concept_id = 9201 AND (pre.visit_end_date IS DISTINCT FROM d.death_date))
SELECT COUNT (DISTINCT patient) FROM dead_patients
WHERE dead_patients.visit_end_date + INTERVAL '30 days' >= dead_patients.death_date