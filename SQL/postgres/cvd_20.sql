--Number of patients that are discharged after an event of heart failure
WITH pre as (select 
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
select count (distinct pre.person_id) as total_patients 
	FROM pre
	LEFT JOIN {cdm_schema}.death d
		ON pre.person_id = d.person_id
    WHERE pre.ancestor_concept_id = 316139 AND pre.visit_concept_id = 9201 AND (pre.visit_end_date is distinct from d.death_date); -- 9201 inpatient visit and no dieying in the visit
--Number of patientes that after discharge of a heart faiulure event are readmitted in less than 30 days with a heart failure
WITH heart_failure_patients AS (
    SELECT DISTINCT
        co.person_id,
		co.condition_start_date,
        co.condition_end_date,
        co.condition_occurrence_id,
		co.visit_occurrence_id,
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
    WHERE ca.ancestor_concept_id = 316139 AND vo.visit_concept_id = 9201
),
readmissions AS (
    SELECT
        hf1.person_id,
        hf1.condition_end_date        AS first_event_date,
		hf1.visit_occurrence_id		   AS first_event_visit,
		hf1.visit_concept_id		 AS first_type_visit,
        hf2.condition_start_date        AS second_event_date,
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
SELECT COUNT(distinct person_id) AS total_patients
FROM readmissions
---For Checking in pgadmin---
--WITH heart_failure_patients AS (
--    SELECT DISTINCT
--      co.person_id,
--		co.condition_start_date,
--      co.condition_end_date,
--      co.condition_occurrence_id,
--		co.visit_occurrence_id,
--		vo.visit_concept_id,
--		vo.visit_end_date,
--		d.death_date
--  FROM {cdm_schema}.condition_occurrence co
--  JOIN {vocab_schema}.concept_ancestor ca
--      ON co.condition_concept_id = ca.descendant_concept_id
--	JOIN {cdm_schema}.visit_occurrence vo
--		ON co.visit_occurrence_id = vo.visit_occurrence_id
--	FULL JOIN {cdm_schema}.death d
--		ON co.person_id = d.person_id
--  WHERE ca.ancestor_concept_id = 316139 AND vo.visit_concept_id = 9201
--),
--readmissions AS (
--    SELECT
--      hf1.person_id,
--      hf1.condition_end_date        AS first_event_date,
--		hf1.visit_occurrence_id		   AS first_event_visit,
--		hf1.visit_concept_id		 AS first_type_visit,
--      hf2.condition_start_date        AS second_event_date,
--		hf2.visit_occurrence_id		   AS second_event_visit, 
--		hf2.visit_concept_id 		 AS second_type_visit,
--      hf2.condition_start_date - hf1.condition_start_date AS days_between
--    FROM heart_failure_patients hf1
--    JOIN heart_failure_patients hf2
--        ON hf1.person_id = hf2.person_id
--        AND hf1.condition_occurrence_id != hf2.condition_occurrence_id
--		AND hf1.visit_occurrence_id != hf2.visit_occurrence_id
--        AND hf2.condition_start_date > hf1.condition_end_date
--        AND hf2.condition_start_date <= hf1.condition_end_date + INTERVAL '30 days'
--		AND (hf1.visit_end_date is distinct from hf1.death_date)
--)
--SELECT 
--  person_id,
--  first_event_date,
--	first_event_visit,
--	first_type_visit,
--  second_event_date,
--	second_event_visit,
--	second_type_visit,
--  days_between
--FROM readmissions
--ORDER BY days_between ASC;
