--Number of patients with diabetes mellitus
SELECT COUNT(DISTINCT co.person_id) AS total_patients
FROM {cdm_schema}.condition_occurrence co
JOIN {vocab_schema}.concept_ancestor ca ON co.condition_concept_id = ca.descendant_concept_id
WHERE ca.ancestor_concept_id = 201820 or co.condition_concept_id = 201820;
--Number of patients with diabetes mellitus that take statins
WITH diabetes_patients AS (
    SELECT DISTINCT co.person_id
    FROM {cdm_schema}.condition_occurrence co
    JOIN {vocab_schema}.concept_ancestor ca
        ON co.condition_concept_id = ca.descendant_concept_id
    WHERE ca.ancestor_concept_id = 201820  --Diabetes mellitus
),
statins_drug_patients AS (
    SELECT DISTINCT de.person_id
    FROM {cdm_schema}.drug_exposure de
    JOIN {vocab_schema}.concept_ancestor ca
        ON de.drug_concept_id = ca.descendant_concept_id
    WHERE ca.ancestor_concept_id = 21601855  -- HMG CoA reductase inhibitors, statins
)
SELECT COUNT(*) AS total_patients
FROM diabetes_patients dp
JOIN statins_drug_patients sdp
    ON dp.person_id = sdp.person_id;