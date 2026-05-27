--Number of patients with heart failure (cardiac insuficiency)
SELECT COUNT(DISTINCT co.person_id) AS total_pacientes
FROM {cdm_schema}.condition_occurrence co
JOIN {vocab_schema}.concept_ancestor ca
  ON co.condition_concept_id = ca.descendant_concept_id
WHERE ca.ancestor_concept_id = 316139;  --Heart failure