--Number of patients with a NSTEMI that are treated with an STENT or fibrinolisys in less than 12h since diagnose
WITH nstemi_patients AS (
    SELECT DISTINCT
        co.person_id,
        co.condition_start_date,
        co.condition_start_datetime
    FROM {cdm_schema}.condition_occurrence co
    JOIN {vocab_schema}.concept_ancestor ca
        ON co.condition_concept_id = ca.descendant_concept_id
    WHERE ca.ancestor_concept_id in (4270024, 45766241)  -- NSTEMI
),
revascularization_procedures AS (
    SELECT DISTINCT
        po.person_id,
        po.procedure_date,
        po.procedure_datetime
    FROM {cdm_schema}.procedure_occurrence po
    JOIN {vocab_schema}.concept_ancestor ca
        ON po.procedure_concept_id = ca.descendant_concept_id
    WHERE ca.ancestor_concept_id = 1243618   -- Stent
       OR ca.ancestor_concept_id = 4216130   -- Percutaneous coronary intervention
       OR ca.ancestor_concept_id in (40757023, 40756967)  -- Instillation of fibrinolytic agent using catheter for fibrinolysis, (initial day, subsequent day)
)
SELECT COUNT(DISTINCT np.person_id) AS total_patients, p.gender_concept_id, FLOOR((extract( year from rp.procedure_date) - p.YEAR_OF_BIRTH) /10) AS age_decile
FROM nstemi_patients np
JOIN revascularization_procedures rp
    ON np.person_id = rp.person_id
    AND rp.procedure_datetime > np.condition_start_datetime
    AND rp.procedure_datetime <= np.condition_start_datetime + INTERVAL '12 hours'
JOIN {cdm_schema}.person p
    ON np.person_id = p.person_id AND rp.person_id = p.person_id
GROUP BY p.gender_concept_id, FLOOR((extract( year from rp.procedure_date) - p.YEAR_OF_BIRTH) /10);