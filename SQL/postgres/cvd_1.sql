--Number of patients with heart failure (cardiac insuficiency)
SELECT COUNT(DISTINCT co.person_id) AS total_patients
FROM {cdm_schema}.condition_occurrence co
JOIN {vocab_schema}.concept_ancestor ca
  ON co.condition_concept_id = ca.descendant_concept_id
WHERE ca.ancestor_concept_id = 316139;  --Heart failure
--Number of patients with heart failure that are treated with an intravenous diuretic
SELECT COUNT(DISTINCT co.person_id) AS total_pacientes
FROM {cdm_schema}.condition_occurrence co
JOIN {vocab_schema}.concept_ancestor ca
    ON co.condition_concept_id = ca.descendant_concept_id
   AND ca.ancestor_concept_id = 316139  --Heart failure
JOIN {cdm_schema}.drug_exposure de
    ON co.person_id = de.person_id
   AND co.visit_occurrence_id = de.visit_occurrence_id
JOIN {vocab_schema}.concept_ancestor ca_drug
    ON de.drug_concept_id = ca_drug.descendant_concept_id
   AND ca_drug.ancestor_concept_id = 21601461 and de.route_concept_id = 4171047  -- Diuretico y ruta intravenosa