--Number of patients with a NSTEMI diagnosed
SELECT COUNT(DISTINCT co.person_id) AS total_patients
FROM {cdm_schema}.condition_occurrence co
JOIN {vocab_schema}.concept_ancestor ca
	ON co.condition_concept_id= ca.descendant_concept_id
WHERE co.condition_concept_id = 4270024;  --NSTEMI
--Number of patients with a NSTEMI that are treated with an STENT or fibrinolisys in less than 12h since diagnose
WITH nstemi_patients AS (
    SELECT DISTINCT
        co.person_id,
        co.condition_start_date,
        co.condition_start_datetime
    FROM {cdm_schema}.condition_occurrence co
    JOIN {vocab_schema}.concept_ancestor ca
        ON co.condition_concept_id = ca.descendant_concept_id
    WHERE ca.ancestor_concept_id = 4270024  -- NSTEMI
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
)
SELECT COUNT(DISTINCT np.person_id) AS total_patients
FROM nstemi_patients np
JOIN revascularization_procedures rp
    ON np.person_id = rp.person_id
    AND rp.procedure_datetime > np.condition_start_datetime
    AND rp.procedure_datetime <= np.condition_start_datetime + INTERVAL '12 hours';
--Number of patients with a NSTEMI that are treated with an STENT or fibrinolisys in more than 12h since diagnose
WITH nstemi_patients AS (
    SELECT DISTINCT
        co.person_id,
        co.condition_start_date,
        co.condition_start_datetime
    FROM {cdm_schema}.condition_occurrence co
    JOIN {vocab_schema}.concept_ancestor ca
        ON co.condition_concept_id = ca.descendant_concept_id
    WHERE ca.ancestor_concept_id = 4270024  -- NSTEMI
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
)
SELECT COUNT(DISTINCT np.person_id) AS total_patients
FROM nstemi_patients np
JOIN revascularization_procedures rp
    ON np.person_id = rp.person_id
    AND rp.procedure_datetime > np.condition_start_datetime
    AND rp.procedure_datetime >= np.condition_start_datetime + INTERVAL '12 hours'