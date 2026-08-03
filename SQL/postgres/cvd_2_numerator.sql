--Number of patients presenting chest pain that are diagnosed with an acute coronary syndrome
SELECT COUNT(DISTINCT co.person_id) AS total_patients, p.gender_concept_id, FLOOR((extract( year from co.condition_start_date) - p.YEAR_OF_BIRTH) /10) AS age_decile
FROM {cdm_schema}.condition_occurrence co
JOIN {vocab_schema}.concept_ancestor ca
	ON co.condition_concept_id= ca.descendant_concept_id
JOIN {cdm_schema}.visit_occurrence vo
	ON co.person_id = vo.person_id
JOIN {cdm_schema}.condition_occurrence co2
	ON co.visit_occurrence_id = co2.visit_occurrence_id
JOIN {vocab_schema}.concept_ancestor ca2
	ON co2.condition_concept_id = ca2.descendant_concept_id
JOIN {cdm_schema}.person p
    ON co.person_id = p.person_id
WHERE ca.ancestor_concept_id = 77670 -- Dolor de pecho
AND vo.admited_from_concept_id = 9203 -- Admision por Urgencias
AND (ca2.ancestor_concept_id in (4296653,3655133,45766114,4270024, 45766241,40479589,315296))    --STEMI, NSTEMI, Takotsubo or preinfarction syndrome (angina de pecho inestable)
GROUP BY p.gender_concept_id, FLOOR((extract( year from co.condition_start_date) - p.YEAR_OF_BIRTH) /10);



-- 312327 Acute myocardial infarction

-- (4296653, 3655133, 45766114) STEMI Definition
-- (4270024, 45766241) NSTEMI Definition
-- 40479589 Takotsubo Definition
-- 315296 Angina de pecho inestable (Preinfarction syndrome)