--Number of patients with heart failure that are treated with an intravenous diuretic
SELECT COUNT(DISTINCT co.person_id) AS total_patients, p.gender_concept_id, FLOOR((extract( year from co.condition_start_date) - p.YEAR_OF_BIRTH) /10) AS age_decile
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
JOIN {cdm_schema}.person p
    ON co.person_id = p.person_id
GROUP BY p.gender_concept_id, FLOOR((extract( year from co.condition_start_date) - p.YEAR_OF_BIRTH) /10);