--Number of patients with any cardiovascular finding 
SELECT COUNT (DISTINCT person_id)
FROM {cdm_schema}.condition_occurrence co
    JOIN {vocab_schema}.concept_ancestor ca 
        ON co.condition_concept_id = ca.descendant_concept_id
WHERE ca.ancestor_concept_id = 4023995; -- 4023995 cardiovascular finding
-- Number of patients with any cardiovascular finding that are also diagnosed with diabetes
SELECT COUNT (DISTINCT co.person_id)
FROM {cdm_schema}.condition_occurrence co
    JOIN {vocab_schema}.concept_ancestor ca 
        ON co.condition_concept_id = ca.descendant_concept_id
    JOIN  {cdm_schema}.condition_occurrence co2
        ON co.person_id = co2.person_id
	JOIN {vocab_schema}.concept_ancestor ca2
		ON co2.condition_concept_id = ca2.descendant_concept_id
WHERE ca.ancestor_concept_id = 4023995 AND ca2.ancestor_concept_id = 201820 AND co.condition_occurrence_id != co2.condition_occurrence_id -- 4023995 cardiovascular finding, 201820 diabetes mellitus