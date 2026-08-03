--Number of patientes that after discharge of a heart faiulure event are readmitted in less than 30 days with any heart disease
WITH heart_failure_patients AS (
    SELECT DISTINCT
        co.person_id,
		co.condition_start_date,
        co.condition_end_date,
        co.condition_occurrence_id,
		co.visit_occurrence_id,
		ca.ancestor_concept_id,
		vo.visit_concept_id,
		vo.visit_end_date,
		d.death_date
    FROM {cdm_schema}.condition_occurrence co
    JOIN {vocab_schema}.concept_ancestor ca
        ON co.condition_concept_id = ca.descendant_concept_id
	JOIN {cdm_schema}.visit_occurrence vo
		ON co.visit_occurrence_id = vo.visit_occurrence_id
	FULL JOIN {cdm_schema}.death d
		ON co.person_id = d.person_id
    WHERE (ca.ancestor_concept_id = 316139 or ca.ancestor_concept_id = 321588) 
    AND vo.visit_concept_id = 9201  --inpatient visit
),
readmissions AS (
    SELECT
        hf1.person_id,
        hf1.condition_end_date        AS first_event_date,
		hf1.ancestor_concept_id		  AS first_event_ancestor,
		hf1.visit_occurrence_id		   AS first_event_visit,
		hf1.visit_concept_id		 AS first_type_visit,
        hf2.condition_start_date        AS second_event_date,
		hf2.ancestor_concept_id		  As second_event_ancestor,
		hf2.visit_occurrence_id		   AS second_event_visit, 
		hf2.visit_concept_id 		 AS second_type_visit,
        hf2.condition_start_date - hf1.condition_start_date AS days_between
    FROM heart_failure_patients hf1
    JOIN heart_failure_patients hf2
        ON hf1.person_id = hf2.person_id
        AND hf1.condition_occurrence_id != hf2.condition_occurrence_id
		AND hf1.visit_occurrence_id != hf2.visit_occurrence_id
        AND hf2.condition_start_date > hf1.condition_end_date
        AND hf2.condition_start_date <= hf1.condition_end_date + INTERVAL '30 days'
		AND (hf1.visit_end_date is distinct from hf1.death_date)
)
SELECT COUNT(distinct r.person_id) AS total_patients, p.gender_concept_id, FLOOR((extract( year from r.second_event_date) - p.YEAR_OF_BIRTH) /10) AS age_decile
FROM readmissions r
JOIN {cdm_schema}.person p
    ON r.person_id = p.person_id
WHERE r.first_event_ancestor = 316139   --heart failure
AND r.second_event_ancestor = 321588    --heart dissease
GROUP BY p.gender_concept_id, FLOOR((extract( year from r.second_event_date) - p.YEAR_OF_BIRTH) /10);