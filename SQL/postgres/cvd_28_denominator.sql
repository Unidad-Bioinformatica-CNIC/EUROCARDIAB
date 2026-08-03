--Number of patients with any cardiovascular finding 
SELECT COUNT (DISTINCT person_id)
FROM {cdm_schema}.condition_occurrence co
    JOIN {vocab_schema}.concept_ancestor ca 
        ON co.condition_concept_id = ca.descendant_concept_id
WHERE ca.ancestor_concept_id = 4023995; -- cardiovascular finding