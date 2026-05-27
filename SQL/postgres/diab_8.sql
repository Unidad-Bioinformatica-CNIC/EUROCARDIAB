--Number of patients with diabetes mellitus
SELECT COUNT(DISTINCT co.person_id) AS total_patients
FROM {cdm_schema}.condition_occurrence co
JOIN {vocab_schema}.concept_ancestor ca ON co.condition_concept_id = ca.descendant_concept_id
WHERE ca.ancestor_concept_id = 201820 or co.condition_concept_id = 201820;
--Number of patients with diabetes mellitus and diabetic retinopathy
SELECT COUNT(DISTINCT co.person_id) AS total_patients
FROM {cdm_schema}.condition_occurrence co
JOIN {vocab_schema}.concept_ancestor ca1
    ON co.condition_concept_id = ca1.descendant_concept_id
JOIN {cdm_schema}.condition_occurrence co2
    ON co.person_id = co2.person_id
JOIN {vocab_schema}.concept_ancestor ca2
    ON co2.condition_concept_id = ca2.descendant_concept_id
WHERE ca1.ancestor_concept_id = 201820   -- Diabetes mellitus
  AND ca2.ancestor_concept_id = 4174977  -- Diagnosed diabetic retinopathy conditions