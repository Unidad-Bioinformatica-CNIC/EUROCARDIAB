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
    WHERE pre.ancestor_concept_id = 316139	--heart failure
	AND pre.visit_concept_id = 9201 	--inpatient visit
	AND (pre.visit_end_date IS DISTINCT FROM d.death_date); --and no dieying in the visit