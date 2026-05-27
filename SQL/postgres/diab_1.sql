--Number of patients with diabetes mellitus
SELECT COUNT(DISTINCT co.person_id) AS total_patients
FROM {cdm_schema}.condition_occurrence co
JOIN {vocab_schema}.concept_ancestor ca 
    ON co.condition_concept_id = ca.descendant_concept_id
WHERE ca.ancestor_concept_id = 201820;
--Number of patients with diabetes mellitus to which the  glycosylated hemoglobin is measured
SELECT COUNT(DISTINCT co.person_id) AS total_patients
FROM {cdm_schema}.condition_occurrence co
JOIN {vocab_schema}.concept_ancestor ca
    ON co.condition_concept_id = ca.descendant_concept_id
JOIN {cdm_schema}.measurement m
    ON co.person_id = m.person_id
JOIN {vocab_schema}.concept_ancestor ca_hba1c
    ON m.measurement_concept_id = ca_hba1c.descendant_concept_id
WHERE ca.ancestor_concept_id = 201820
  AND ca_hba1c.ancestor_concept_id in (4184637, 2212393, 724554, 3004410, 3003309, 3005673, 3004410, 40765129, 40762352, 42869630) --List of concepts (concept_set) given by Paula from an study already done