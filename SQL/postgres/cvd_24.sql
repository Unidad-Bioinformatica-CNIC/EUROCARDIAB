WITH nstemi_patients AS (
    SELECT 
        co.person_id,
		co.visit_occurrence_id,
        COALESCE(co.condition_start_datetime, co.condition_start_date::timestamp) AS diagnosis_dt
    FROM {cdm_schema}.condition_occurrence co
    JOIN {vocab_schema}.concept_ancestor ca
        ON co.condition_concept_id = ca.descendant_concept_id
	JOIN h_12_oct.visit_occurrence vo
		ON co.person_id = vo.person_id
    WHERE ca.ancestor_concept_id in (4270024, 45766241)  -- NSTEMI
    AND co.visit_occurrence_id IS NOT NULL
    AND vo.admitting_source_concept_id = 9203 -- Admision por Urgencias
),
first_stent AS (
    SELECT DISTINCT
        po.person_id,
        po.visit_occurrence_id,
        COALESCE(po.procedure_datetime, po.procedure_date::TIMESTAMP) AS first_stent_dt
    FROM {cdm_schema}.procedure_occurrence po
    JOIN {vocab_schema}.concept_ancestor ca
        ON po.procedure_concept_id = ca.descendant_concept_id
	JOIN h_12_oct.visit_occurrence vo
		ON po.person_id = vo.person_id
    WHERE ca.ancestor_concept_id = 1243618  -- Stent
    AND po.visit_occurrence_id IS NOT NULL
    AND vo.admitting_source_concept_id = 9203 -- Admision por Urgencias
),
time_to_stent AS (
    SELECT
        np.person_id,
        np.diagnosis_dt,
        fs.first_stent_dt,
        EXTRACT(EPOCH FROM (fs.first_stent_dt - np.diagnosis_dt)) / 60 AS minutes_to_stent
    FROM nstemi_patients np
    JOIN first_stent fs
        ON np.person_id = fs.person_id
        AND fs.first_stent_dt > np.diagnosis_dt
		AND np.visit_occurrence_id = fs.visit_occurrence_id
)
SELECT
    COUNT(DISTINCT person_id)                        AS total_patients,
    ROUND((AVG(minutes_to_stent) / 60)::numeric, 2)  AS mean_hours,
    ROUND((MIN(minutes_to_stent) / 60)::numeric, 2)  AS min_hours,
    ROUND((MAX(minutes_to_stent) / 60)::numeric, 2)  AS max_hours,
    ROUND(PERCENTILE_CONT(0.50) WITHIN GROUP
          (ORDER BY (minutes_to_stent/60))::numeric, 2)   AS median_hours,
    ROUND(PERCENTILE_CONT(0.25) WITHIN GROUP
          (ORDER BY (minutes_to_stent/60))::numeric, 2)   AS p25_hours,
    ROUND(PERCENTILE_CONT(0.75) WITHIN GROUP
          (ORDER BY (minutes_to_stent/60))::numeric, 2)   AS p75_hours
FROM time_to_stent;