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
SELECT COUNT (DISTINCT patient) AS total_patients, p.gender_concept_id, FLOOR((extract( year from dp.death_date) - p.YEAR_OF_BIRTH) /10) AS age_decile
FROM dead_patients dp
JOIN {cdm_schema}.person p
    ON dp.person_id = p.person_id
WHERE dp.visit_end_date + INTERVAL '30 days' >= dp.death_date
GROUP BY p.gender_concept_id, FLOOR((extract( year from dp.death_date) - p.YEAR_OF_BIRTH) /10);