--Number of patients with diabetes mellitus that take mdication to control it after diagnose
WITH diabetes_patients AS (
    SELECT DISTINCT co.person_id, co.condition_start_date, MIN(co.condition_start_date) AS first_diagnosis_date
	FROM {cdm_schema}.condition_occurrence co
    JOIN {vocab_schema}.concept_ancestor ca
        ON co.condition_concept_id = ca.descendant_concept_id
    WHERE ca.ancestor_concept_id = 201820   --Diabetes mellitus
    GROUP BY co.person_id, co.condition_start_date
),
diabetes_drug_patients AS (
    SELECT DISTINCT de.person_id, MIN(de.drug_exposure_start_date) AS first_drug_date
    FROM {cdm_schema}.drug_exposure de
    JOIN {vocab_schema}.concept_ancestor ca
        ON de.drug_concept_id = ca.descendant_concept_id
    WHERE ca.ancestor_concept_id = 21600712 --Drugs used in Diabetes 
    GROUP BY de.person_id
)
SELECT COUNT(DISTINCT(p.person_id)) AS total_patients, p.gender_concept_id, FLOOR((extract( year from ddp.first_drug_date) - p.YEAR_OF_BIRTH) /10) AS age_decile
FROM diabetes_patients dp
JOIN diabetes_drug_patients ddp
    ON dp.person_id = ddp.person_id
   AND ddp.first_drug_date >= dp.first_diagnosis_date
JOIN {cdm_schema}.person p
    ON dp.person_id = p.person_id AND ddp.person_id = p.person_id
GROUP BY p.gender_concept_id, FLOOR((extract( year from ddp.first_drug_date) - p.YEAR_OF_BIRTH) /10);