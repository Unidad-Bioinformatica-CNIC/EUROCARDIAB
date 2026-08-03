-- Number of patients with any cardiovascular finding that are also diagnosed with hypertension and get their blood preasure measured
SELECT COUNT (DISTINCT co.person_id)
FROM {cdm_schema}.condition_occurrence co
    JOIN {vocab_schema}.concept_ancestor ca 
        ON co.condition_concept_id = ca.descendant_concept_id
    JOIN  {cdm_schema}.condition_occurrence co2
        ON co.person_id = co2.person_id
	JOIN {vocab_schema}.concept_ancestor ca2
		ON co2.condition_concept_id = ca2.descendant_concept_id
    JOIN {cdm_schema}.measurement m
        ON co.person_id = m.person_id
    JOIN {vocab_schema}.concept_ancestor ca3
        ON m.measurement_concept_id = ca3.descendant_concept_id
WHERE ca.ancestor_concept_id = 4023995  --cardiovascular finding 
AND ca2.ancestor_concept_id = 316866    --hipertensive disorder 
AND ca3.ancestor_concept_id = 4326744   --blood preasure measurement
AND co.condition_occurrence_id != co2.condition_occurrence_id;