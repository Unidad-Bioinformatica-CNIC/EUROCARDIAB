--Number of patients with diabetes mellitus
SELECT COUNT(DISTINCT co.person_id) AS total_patients
FROM {cdm_schema}.condition_occurrence co
JOIN {vocab_schema}.concept_ancestor ca ON co.condition_concept_id = ca.descendant_concept_id
WHERE ca.ancestor_concept_id = 201820;
--Number of patients with diabetes mellitus and that has been screened for diabetic retinopathy
SELECT COUNT(DISTINCT co.person_id) AS total_patients
FROM {cdm_schema}.condition_occurrence co
JOIN {vocab_schema}.concept_ancestor ca1
    ON co.condition_concept_id = ca1.descendant_concept_id
JOIN {cdm_schema}.measurement m
    ON co.person_id = m.person_id
JOIN {vocab_schema}.concept_ancestor ca2
    ON m.measurement_concept_id = ca2.descendant_concept_id
WHERE ca1.ancestor_concept_id = 201820   -- Diabetes mellitus
  AND ca2.ancestor_concept_id = 4047556  -- Diabetic retinopathy screening  