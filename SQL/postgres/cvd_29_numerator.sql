-- Number of patients with any cardiovascular finding that smoke
SELECT COUNT (DISTINCT co.person_id) AS total_patients, p.gender_concept_id, FLOOR((extract( year from ob.observation_date) - p.YEAR_OF_BIRTH) /10) AS age_decile
FROM {cdm_schema}.condition_occurrence co
JOIN {vocab_schema}.concept_ancestor ca 
    ON co.condition_concept_id = ca.descendant_concept_id
JOIN  {cdm_schema}.observation ob
    ON co.person_id = ob.person_id
JOIN {cdm_schema}.person p
    ON co.person_id = p.person_id
WHERE ca.ancestor_concept_id = 4023995 AND ob.observation_concept_id in (903652, 4276526, 40766945, 903665, 903655, 36716991, 903664, 903657, 903663, 2617854, 2101895) OR (ob.observation_concept_id = 35811013 AND ob.value_as_concept_id = 35822845) -- 4023995 cardiovascular finding, 4276526 cigarrete smoker - not standard but in data from h12Oct
GROUP BY p.gender_concept_id, FLOOR((extract( year from ob.observation_date) - p.YEAR_OF_BIRTH) /10);