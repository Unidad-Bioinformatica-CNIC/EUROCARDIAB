WITH trasplante_valvula AS (
    SELECT DISTINCT
        po.person_id,
        po.procedure_occurrence_id,
        po.procedure_date
    FROM {cdm_schema}.procedure_occurrence po
    JOIN {vocab_schema}.concept_ancestor ca_proc
        ON po.procedure_concept_id = ca_proc.descendant_concept_id
       AND ca_proc.ancestor_concept_id = 36676805
),
infeccion_postop AS (
    SELECT DISTINCT
        co.person_id,
        co.condition_occurrence_id,
        co.condition_start_date
    FROM {cdm_schema}.condition_occurrence co
    JOIN {vocab_schema}.concept_ancestor ca_cond
        ON co.condition_concept_id = ca_cond.descendant_concept_id
       AND ca_cond.ancestor_concept_id = 437474     
)
SELECT
    COUNT(DISTINCT tv.person_id)  AS total_pacientes_trasplantados,
    COUNT(DISTINCT ip.person_id)  AS pacientes_con_infeccion_30dias,
    ROUND(
        100.0 * COUNT(DISTINCT ip.person_id)
              / NULLIF(COUNT(DISTINCT tv.person_id), 0)
    , 2)                          AS porcentaje_infeccion
FROM trasplante_valvula tv
LEFT JOIN infeccion_postop ip
    ON tv.person_id = ip.person_id
   AND ip.condition_start_date >  tv.procedure_date
   AND ip.condition_start_date <= tv.procedure_date + INTERVAL '30 days';