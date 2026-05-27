-- Number of patients with any cardiovascular finding that take statins
WITH cardiovascular_patients AS (
    SELECT DISTINCT co.person_id
    FROM {cdm_schema}.condition_occurrence co
    JOIN {vocab_schema}.concept_ancestor ca
        ON co.condition_concept_id = ca.descendant_concept_id
    WHERE ca.ancestor_concept_id = 4023995  --4023995 cardiovascular finding
),
statins_drug_patients AS (
    SELECT DISTINCT de.person_id, de.drug_exposure_start_date
    FROM {cdm_schema}.drug_exposure de
    JOIN {vocab_schema}.concept_ancestor ca
        ON de.drug_concept_id = ca.descendant_concept_id
    WHERE ca.ancestor_concept_id = 21601855  -- HMG CoA reductase inhibitors, statins
)
SELECT COUNT(distinct cp.person_id) AS total_patients, p.gender_concept_id, FLOOR((extract( year from sdp.drug_exposure_start_date) - p.YEAR_OF_BIRTH) /10) AS age_decile
FROM cardiovascular_patients cp
JOIN statins_drug_patients sdp
    ON cp.person_id = sdp.person_id
JOIN {cdm_schema}.person p
    ON cp.person_id = p.person_id
GROUP BY p.gender_concept_id, FLOOR((extract( year from sdp.drug_exposure_start_date) - p.YEAR_OF_BIRTH) /10);