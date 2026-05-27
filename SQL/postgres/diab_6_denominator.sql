--Number of patients with diabetes mellitus to which arterial preasure is measured
SELECT COUNT(DISTINCT co.person_id) AS total_patients
FROM {cdm_schema}.condition_occurrence co
JOIN {vocab_schema}.concept_ancestor ca
    ON co.condition_concept_id = ca.descendant_concept_id
JOIN {cdm_schema}.measurement m
    ON co.person_id = m.person_id
JOIN {vocab_schema}.concept_ancestor ca_bloodp
    ON m.measurement_concept_id = ca_bloodp.descendant_concept_id
WHERE ca.ancestor_concept_id = 201820
  AND ca_bloodp.ancestor_concept_id = 4326744;