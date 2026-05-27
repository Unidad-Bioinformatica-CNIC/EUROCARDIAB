--Number of patients with diabetes mellitus that take mdication to control it after diagnose
WITH diabetes_patients AS (
    SELECT DISTINCT co.person_id, MIN(co.condition_start_date) AS first_diagnosis_date
    FROM {cdm_schema}.condition_occurrence co
    JOIN {vocab_schema}.concept_ancestor ca
        ON co.condition_concept_id = ca.descendant_concept_id
    WHERE ca.ancestor_concept_id = 201820  --Diabetes mellitus
    GROUP BY co.person_id
),
diabetes_drug_patients AS (
    SELECT DISTINCT de.person_id, MIN(de.drug_exposure_start_date) AS first_drug_date
    FROM {cdm_schema}.drug_exposure de
    JOIN {vocab_schema}.concept_ancestor ca
        ON de.drug_concept_id = ca.descendant_concept_id
    WHERE ca.ancestor_concept_id = 21600712   --Drugs used in Diabetes 
    GROUP BY de.person_id
)
SELECT COUNT(*) AS total_patients
FROM diabetes_patients dp
JOIN diabetes_drug_patients ddp
    ON dp.person_id = ddp.person_id
   AND ddp.first_drug_date >= dp.first_diagnosis_date;
--Number of patients with diabetes mellitus that take insuline to control it after its diganose
WITH diabetes_patients AS (
    SELECT DISTINCT co.person_id, MIN(co.condition_start_date) AS first_diagnosis_date
    FROM {cdm_schema}.condition_occurrence co
    JOIN {vocab_schema}.concept_ancestor ca
        ON co.condition_concept_id = ca.descendant_concept_id
    WHERE ca.ancestor_concept_id = 201820   --Diabetes mellitus
    GROUP BY co.person_id
),
diabetes_insulin_patients AS (
    SELECT DISTINCT de.person_id, MIN(de.drug_exposure_start_date) AS first_drug_date
    FROM {cdm_schema}.drug_exposure de
    JOIN {vocab_schema}.concept_ancestor ca
        ON de.drug_concept_id = ca.descendant_concept_id
    WHERE ca.ancestor_concept_id = 21600713 -- Insulins and Anlaogues
    GROUP BY de.person_id
)
SELECT COUNT(*) AS total_patients
FROM diabetes_patients dp
JOIN diabetes_insulin_patients dip
    ON dp.person_id = dip.person_id
   AND dip.first_drug_date >= dp.first_diagnosis_date