import utils
import os
from pathlib import Path
# If implemented in a docker container, this might not be needed, as variables in .env file might be already availabe as environment viariables
from dotenv import load_dotenv

#Import connection parameters from .env file into environment variables
load_dotenv()
cdm_schema= os.getenv('CDM_SCHEMA')
vocab_schema= os.getenv('VOCAB_SCHEMA')

####Calculating indicators
##Diabetes
#Diabetes Indicator 1 - Percentaje of patients with diabetes diagnosed that get their levels of Glycosylated hemoglobin measured 
results_diab_1=utils.exe_sql_script(Path("SQL/postgres/diab_1.sql"),cdm_schema, vocab_schema)
total_diab_patients=results_diab_1[0][0]
total_diab_patients_with_glyc_hemo=results_diab_1[1][0]

print(f"numero total de pacientes con diabetes: {total_diab_patients}")
print(f"numero total de pacientes con diabetes a los que se les controla la hemoglobina glicosilada: {total_diab_patients_with_glyc_hemo}")


#Diabetes Indicator 2 - Percentaje of patients with diabetes diagnosed with their level of Glycosylated hemoglobin measured over 7%
results_diab_2=utils.exe_sql_script(Path("SQL/postgres/diab_2.sql"),cdm_schema, vocab_schema)
total_diab_patients_with_glyc_hemo=results_diab_2[0][0]
total_diab_patients_with_glyc_hemo_7=results_diab_2[1][0]

print(f"numero total de pacientes con diabetes a los que se les controla la hemoglobina glicosilada y tenen niveles > de 7 %: {total_diab_patients_with_glyc_hemo_7}")


#Diabetes Indicator 3 - Percentaje of patients with diabetes diagnosed with their level of Glycosylated hemoglobin measured over 8%
results_diab_3=utils.exe_sql_script(Path("SQL/postgres/diab_3.sql"),cdm_schema, vocab_schema)
total_diab_patients_with_glyc_hemo=results_diab_3[0][0]
total_diab_patients_with_glyc_hemo_8=results_diab_3[1][0]

print(f"numero total de pacientes con diabetes a los que se les controla la hemoglobina glicosilada y tenen niveles > de 8 %: {total_diab_patients_with_glyc_hemo_8}")


#Diabates Indicator 4 - Percentaje of patients with diabetes diagnosed that also have any hypertension disease diagnosed
results_diab_4=utils.exe_sql_script(Path("SQL/postgres/diab_4.sql"),cdm_schema, vocab_schema)
total_diab_patients=results_diab_4[0][0]
total_diab_and_hypertension_patients=results_diab_4[1][0]

print(f"numero total de pacientes con diabetes e hypertension: {total_diab_and_hypertension_patients}")


#Diabetes Indicator 5 - Percentaje of patients with diabetes diagnosed to which blood preasure is measured
results_diab_5=utils.exe_sql_script(Path("SQL/postgres/diab_5.sql"),cdm_schema, vocab_schema)
total_diab_patients=results_diab_5[0][0]
total_diab_patietnts_with_bp_measurement=results_diab_5[1][0]

print(f"numero total de pacientes con diabetes a los que se les mide la presion sanguinea: {total_diab_patietnts_with_bp_measurement}")


#Diabetes Indicator 6 - Percentaje of patientes with diabetes diagnosed to which blood preasure is measured, and have blood preasere levels over 130 mmHg in some moments
results_diab_6=utils.exe_sql_script(Path("SQL/postgres/diab_6.sql"),cdm_schema, vocab_schema)
total_diab_patietnts_with_bp_measurement=results_diab_6[0][0]
total_diab_patietnts_with_bp_measurement_130=results_diab_6[1][0]

print(f"numero total de pacientes con diabetes a los que se les mide la presion sanguinea y en algun momento tienen niveles > de 130 mmHg en algun momento: {total_diab_patietnts_with_bp_measurement_130}")


#Diabaetes Indicator 7 - Percentaje of patientes with diabetes subjected to a diabetic retinopathy screening
results_diab_7=utils.exe_sql_script(Path("SQL/postgres/diab_7.sql"),cdm_schema, vocab_schema)
total_diab_patients=results_diab_7[0][0]
total_diab_and_screened_diabretinopathy_patients=results_diab_7[1][0]

print(f"numero total de pacientes con diabetes sometidos a un screening de retinopatia diabetica: {total_diab_and_screened_diabretinopathy_patients}")


#Diabetes Indicator 8 - Percentaje of patientes with diabetes diagnosed also with diabetic retinopathy
results_diab_8=utils.exe_sql_script(Path("SQL/postgres/diab_8.sql"),cdm_schema, vocab_schema)
total_diab_patients=results_diab_8[0][0]
total_diab_and_diabretinopathy_patients=results_diab_8[1][0]

print(f"numero total de pacientes con diabetes y diagnosticados con retinopatia diabetica: {total_diab_and_diabretinopathy_patients}")


#Diabetes Indicator 9 - Percentaje of patientes with diabetes diagnosed also with diabetic kidney disease
results_diab_9=utils.exe_sql_script(Path("SQL/postgres/diab_9.sql"),cdm_schema, vocab_schema)
total_diab_patients=results_diab_9[0][0]
total_diab_and_diabkidney_patients=results_diab_9[1][0]

print(f"numero total de pacientes con diabetes y diagnosticados con problemas de rinhon de origen diabetico: {total_diab_and_diabkidney_patients}")


#Diabetes Indicator 10 - Percentaje of patientes with diabetes that take medication to control it after its diagnose
results_diab_10=utils.exe_sql_script(Path("SQL/postgres/diab_10.sql"),cdm_schema, vocab_schema)
total_diab_patients=results_diab_10[0][0]
total_diab_medicated_general_patients=results_diab_10[1][0]

print(f"numero total de pacientes con diabetes que tras el diagnostico toman medicamentos para controlarla: {total_diab_medicated_general_patients}")


#Diabetes Indicator 11 - Percentaje of patientes with diabetes that take medication to control it after its diagnose, who specifically take insulin
results_diab_11=utils.exe_sql_script(Path("SQL/postgres/diab_11.sql"),cdm_schema, vocab_schema)
total_diab_medicated_general_patients=results_diab_11[0][0]
total_diab_medicated_insulin_patients=results_diab_11[1][0]

print(f"numero total de pacientes con diabetes que tras el diagnostico toman insulina para controlarla: {total_diab_medicated_insulin_patients}")


#Diabetes Indicator 12 - Percentaje of patientes with diabetes that take medication to control it after its diagnose, who specifically take non-insulin drugs
results_diab_12=utils.exe_sql_script(Path("SQL/postgres/diab_12.sql"),cdm_schema, vocab_schema)
total_diab_medicated_general_patients=results_diab_12[0][0]
total_diab_medicated_non_insulin_patients=results_diab_12[1][0]

print(f"numero total de pacientes con diabetes que tras el diagnostico toman medicamentos diferentes a la insulina para controlar los niveles de glucosa: {total_diab_medicated_non_insulin_patients}")


#Diabetes Indicator 13 - Percentaje of patients with diabetes that take statins root of the diabetes
results_diab_13=utils.exe_sql_script(Path("SQL/postgres/diab_13.sql"),cdm_schema, vocab_schema)
total_diab_patients=results_diab_13[0][0]
total_diab_statins_patients=results_diab_13[1][0]

print(f"numero total de pacientes con diabetes que tras el diagnostico de diabetes comienzan a toman estatinas: {total_diab_statins_patients}")


#Diabetes Indicator 14 - Percentaje of patients with diabetes that take statins 
results_diab_14=utils.exe_sql_script(Path("SQL/postgres/diab_14.sql"),cdm_schema, vocab_schema)
total_diab_patients=results_diab_14[0][0]
total_diab_statins_patients=results_diab_14[1][0]

print(f"numero total de pacientes con diabetes que toman estatinas: {total_diab_statins_patients}")









##Cardiovascular
#Cardiovascular Indicator 1 - Percentaje of patients diagnosed with any heart failure that are treated with an intravenous diuretic.
results_cvd_1=utils.exe_sql_script(Path("SQL/postgres/cvd_1.sql"),cdm_schema, vocab_schema)
total_heart_failure_patients=results_cvd_1[0][0]
total_heart_failure_diuretic_patients=results_cvd_1[1][0]

print(f"numero total de pacientes diagnosticaos con cualquier tipo de insuficiencia cardiaca: {total_heart_failure_patients}")
print(f"numero total de pacientes diagnosticaos con cualquier tipo de insuficiencia cardiaca que son tratados con un diuretico intravenoso: {total_heart_failure_diuretic_patients}")

##Ask NICO
#Cardiovascular Indicator 2 - Percentaje of patients presenting toracic pain and diagnosed with an acute coronary syndrome (STEMI, NSTEMI, Takotsubo, angina de pecho)
results_cvd_2=utils.exe_sql_script(Path("SQL/postgres/cvd_2.sql"),cdm_schema, vocab_schema)
total_chest_pain_patients=results_cvd_2[0][0]
total_chest_pain_coronary_syndrome_patients=results_cvd_2[1][0]
print(f"numero total de pacientes que presentan dolor toracico: {total_chest_pain_patients}")
print(f"numero total de pacientes que presentan dolor toracico y son diagnoticados con un sindrome coronario agudo (STEMI, NSTEMI, Takotsubo- myocardial disease) y (angina de pecho): {total_chest_pain_coronary_syndrome_patients}")


#Cardiovascular Indicator 3 - Percentaje of patients presenting toracic pain and diagnosed with STEMI
results_cvd_3=utils.exe_sql_script(Path("SQL/postgres/cvd_3.sql"),cdm_schema, vocab_schema)
total_chest_pain_patients=results_cvd_3[0][0]
total_chest_pain_STEMI_patients=results_cvd_3[1][0]

print(f"numero total de pacientes que presentan dolor toracico y son diagnosticados con un STEMI: {total_chest_pain_STEMI_patients}")


#Cardiovascular Indicator 4 - Percentaje of patients presenting toracic pain and diagnosed with STEMI that is subjected to a coronary angiography
results_cvd_4=utils.exe_sql_script(Path("SQL/postgres/cvd_4.sql"),cdm_schema, vocab_schema)
total_chest_pain_STEMI_patients=results_cvd_4[0][0]
total_chest_pain_STEMI_coroangio_patients=results_cvd_4[1][0]

print(f"numero total de pacientes que tras presentar dolor toracico son diagnosticados con un STEMI y son sometidos a una angiografia coronaria: {total_chest_pain_STEMI_coroangio_patients}")


#Cardiovascular Indicator 5 - Percentaje of patients presenting toracic pain, diagnosed with STEMI and subjected to a coronary angiography present a coronary oclusion
results_cvd_5=utils.exe_sql_script(Path("SQL/postgres/cvd_5.sql"),cdm_schema, vocab_schema)
total_chest_pain_STEMI_coroangio_patients=results_cvd_5[0][0]
total_chest_pain_STEMI_coroangio_oclusion_patients=results_cvd_5[1][0]

print(f"numero total de pacientes que tras presentar dolor toracico son diagnosticados con STEMI, sometidos a una agiografia y presentan una oclusion coronaria: {total_chest_pain_STEMI_coroangio_oclusion_patients}")


#Cardiovascular Indicator 6 - Percentaje of patients presenting toracic pain, diagnosed with STEMI, subjected to a coronary angiography and presenting a coronary oclusion that are subjected to a STENT procedure
results_cvd_6=utils.exe_sql_script(Path("SQL/postgres/cvd_6.sql"),cdm_schema, vocab_schema)
total_chest_pain_STEMI_coroangio_oclusion_patients=results_cvd_6[0][0]
total_chest_pain_STEMI_coroangio_oclusion_STENT_patients=results_cvd_6[1][0]

print(f"numero total de pacientes que tras presentar dolor toracico son diagnosticados con STEMI, sometidos a una agiografia, presentan una oclusion coronaria y son sometidos a una colocacion de STENT: {total_chest_pain_STEMI_coroangio_oclusion_STENT_patients}")


#Cardiovascular Indicator 7 - Percentaje of patients presenting toracic pain and diagnosed with NSTEMI
results_cvd_7=utils.exe_sql_script(Path("SQL/postgres/cvd_7.sql"),cdm_schema, vocab_schema)
total_chest_pain_patients=results_cvd_7[0][0]
total_chest_pain_NSTEMI_patients=results_cvd_7[1][0]

print(f"numero total de pacientes que presentan dolor toracico y son diagnosticados con un NSTEMI: {total_chest_pain_NSTEMI_patients}")


#Cardiovascular Indicator 8 - Percentaje of patients presenting toracic pain and diagnosed with NSTEMI that is subjected to a coronary angiography
results_cvd_8=utils.exe_sql_script(Path("SQL/postgres/cvd_8.sql"),cdm_schema, vocab_schema)
total_chest_pain_NSTEMI_patients=results_cvd_8[0][0]
total_chest_pain_NSTEMI_coroangio_patients=results_cvd_8[1][0]

print(f"numero total de pacientes que tras presentar dolor toracico son diagnosticados con un NSTEMI y son sometidos a una angiografia coronaria: {total_chest_pain_NSTEMI_coroangio_patients}")


#Cardiovascular Indicator 9 - Percentaje of patients presenting toracic pain, diagnosed with NSTEMI and subjected to a coronary angiography present a coronary oclusion
results_cvd_9=utils.exe_sql_script(Path("SQL/postgres/cvd_9.sql"),cdm_schema, vocab_schema)
total_chest_pain_NSTEMI_coroangio_patients=results_cvd_9[0][0]
total_chest_pain_NSTEMI_coroangio_oclusion_patients=results_cvd_9[1][0]

print(f"numero total de pacientes que tras presentar dolor toracico son diagnosticados con NSTEMI, sometidos a una agiografia y presentan una oclusion coronaria: {total_chest_pain_NSTEMI_coroangio_oclusion_patients}")


#Cardiovascular Indicator 10 - Percentaje of patients presenting toracic pain, diagnosed with NSTEMI, subjected to a coronary angiography and presenting a coronary oclusion that are subjected to a STENT procedure
results_cvd_10=utils.exe_sql_script(Path("SQL/postgres/cvd_10.sql"),cdm_schema, vocab_schema)
total_chest_pain_NSTEMI_coroangio_oclusion_patients=results_cvd_10[0][0]
total_chest_pain_NSTEMI_coroangio_oclusion_STENT_patients=results_cvd_10[1][0]

print(f"numero total de pacientes que tras presentar dolor toracico son diagnosticados con NSTEMI, sometidos a una agiografia, presentan una oclusion coronaria y son sometidos a una colocacion de STENT: {total_chest_pain_NSTEMI_coroangio_oclusion_STENT_patients}")


#Cardiovascular Indicator 11 - Percentaje of patients presenting toracic pain and diagnosed with Takotsubo cardiomyopathy
results_cvd_11=utils.exe_sql_script(Path("SQL/postgres/cvd_11.sql"),cdm_schema, vocab_schema)
total_chest_pain_patients=results_cvd_11[0][0]
total_chest_pain_Takotsubo_patients=results_cvd_11[1][0]

print(f"numero total de pacientes que presentan dolor toracico y son diagnosticados con Takotsubo: {total_chest_pain_Takotsubo_patients}")


#Cardiovascular Indicator 12 - Percentaje of patients presenting toracic pain and diagnosed with Takotsubo cardiomyopathy that is subjected to a coronary angiography
results_cvd_12=utils.exe_sql_script(Path("SQL/postgres/cvd_12.sql"),cdm_schema, vocab_schema)
total_chest_pain_Takotsubo_patients=results_cvd_12[0][0]
total_chest_pain_Takotsubo_coroangio_patients=results_cvd_12[1][0]

print(f"numero total de pacientes que tras presentar dolor toracico son diagnosticados con Takotsubo y son sometidos a una angiografia coronaria: {total_chest_pain_Takotsubo_coroangio_patients}")


#Cardiovascular Indicator 13 - Percentaje of patients presenting toracic pain, diagnosed with Takotsubo and subjected to a coronary angiography present a coronary oclusion
results_cvd_13=utils.exe_sql_script(Path("SQL/postgres/cvd_13.sql"),cdm_schema, vocab_schema)
total_chest_pain_Takotsubo_coroangio_patients=results_cvd_13[0][0]
total_chest_pain_Takotsubo_coroangio_oclusion_patients=results_cvd_13[1][0]

print(f"numero total de pacientes que tras presentar dolor toracico son diagnosticados con Takotsubo, sometidos a una agiografia y presentan una oclusion coronaria: {total_chest_pain_Takotsubo_coroangio_oclusion_patients}")


#Cardiovascular Indicator 14 - Percentaje of patients presenting toracic pain, diagnosed with Takotsubo, subjected to a coronary angiography and presenting a coronary oclusion that are subjected to a STENT procedure
results_cvd_14=utils.exe_sql_script(Path("SQL/postgres/cvd_14.sql"),cdm_schema, vocab_schema)
total_chest_pain_Takotsubo_coroangio_oclusion_patients=results_cvd_14[0][0]
total_chest_pain_Takotsubo_coroangio_oclusion_STENT_patients=results_cvd_14[1][0]

print(f"numero total de pacientes que tras presentar dolor toracico son diagnosticados con Takotsubo, sometidos a una agiografia, presentan una oclusion coronaria y son sometidos a una colocacion de STENT: {total_chest_pain_Takotsubo_coroangio_oclusion_STENT_patients}")


#Cardiovascular Indicator 15 - Percentaje of patients presenting toracic pain and diagnosed with unstable angina
results_cvd_15=utils.exe_sql_script(Path("SQL/postgres/cvd_15.sql"),cdm_schema, vocab_schema)
total_chest_pain_patients=results_cvd_15[0][0]
total_chest_pain_anginapectoris_patients=results_cvd_15[1][0]

print(f"numero total de pacientes que presentan dolor toracico y son diagnosticados con angina de pecho: {total_chest_pain_anginapectoris_patients}")


#Cardiovascular Indicator 16 - Percentaje of patients presenting toracic pain and diagnosed with unstable angina pectoris that is subjected to a coronary angiography
results_cvd_16=utils.exe_sql_script(Path("SQL/postgres/cvd_16.sql"),cdm_schema, vocab_schema)
total_chest_pain_anginapectoris_patients=results_cvd_16[0][0]
total_chest_pain_anginapectoris_coroangio_patients=results_cvd_16[1][0]

print(f"numero total de pacientes que tras presentar dolor toracico son diagnosticados con angina de pecho y son sometidos a una angiografia coronaria: {total_chest_pain_anginapectoris_coroangio_patients}")


#Cardiovascular Indicator 17 - Percentaje of patients presenting toracic pain, diagnosed with unstable angina pectoris and subjected to a coronary angiography present a coronary oclusion
results_cvd_17=utils.exe_sql_script(Path("SQL/postgres/cvd_17.sql"),cdm_schema, vocab_schema)
total_chest_pain_anginapectoris_coroangio_patients=results_cvd_17[0][0]
total_chest_pain_anginapectoris_coroangio_oclusion_patients=results_cvd_17[1][0]

print(f"numero total de pacientes que tras presentar dolor toracico son diagnosticados con angina de pecho inestable, sometidos a una agiografia y presentan una oclusion coronaria: {total_chest_pain_anginapectoris_coroangio_oclusion_patients}")


#Cardiovascular Indicator 18 - Percentaje of patients presenting toracic pain, diagnosed with unstable angina pectoris, subjected to a coronary angiography and presenting a coronary oclusion that are subjected to a STENT procedure
results_cvd_18=utils.exe_sql_script(Path("SQL/postgres/cvd_18.sql"),cdm_schema, vocab_schema)
total_chest_pain_anginapectoris_coroangio_oclusion_patients=results_cvd_18[0][0]
total_chest_pain_anginapectoris_coroangio_oclusion_STENT_patients=results_cvd_18[1][0]

print(f"numero total de pacientes que tras presentar dolor toracico son diagnosticados con angina de pecho inestable, sometidos a una agiografia, presentan una oclusion coronaria y son sometidos a una colocacion de STENT: {total_chest_pain_anginapectoris_coroangio_oclusion_STENT_patients}")


#Cardiovascular Indicator 19 - Percentaje of patients diagnosed with NSTEMI and have been treated in less than 12 hours with an stent or with fibrinolisys
results_cvd_19=utils.exe_sql_script(Path("SQL/postgres/cvd_19.sql"),cdm_schema, vocab_schema)
total_NSTEMI_patients=results_cvd_19[0][0]
total_NSTEMI_treated_12h=results_cvd_19[1][0]
total_NSTEMI_treated_more_12h=results_cvd_19[2][0]

print(f"numero de pacientes con NSTEMI: {total_NSTEMI_patients}")
print(f"numero de pacientes con NSTEMI tratados con STENT o fibrinolisis antes de 12 h: {total_NSTEMI_treated_12h}")
print(f"numero de pacientes con NSTEMI tratados con STENT o fibrinolisis despues de 12 h: {total_NSTEMI_treated_more_12h}")


#Cardiovascular Indicator 20 - Percentaje of patients that after discharge of a heart failure are readdmited for a heart failure in less than 30 days
results_cvd_20=utils.exe_sql_script(Path("SQL/postgres/cvd_20.sql"),cdm_schema, vocab_schema)
total_heart_failure_inpatients=results_cvd_20[0][0]
total_heart_failure_inpatients_rein_30=results_cvd_20[1][0]

print(f"numero de pacientes que son dados de alta tras un ingreso por problemas de insuficiencia cardiaca: {total_heart_failure_inpatients}")
print(f"numero de pacientes que tras ser dados de alta por un porblema de insuficiencia cardiaca vuelven a ingresar con un problema de insuficiencia cardiaca en menos de 30 dias: {total_heart_failure_inpatients_rein_30}")


#Cardiovascular Indicator 21 - Percentaje of patients that after discharge of a heart failure are readdmited for any heart disease in less than 30 days
results_cvd_21=utils.exe_sql_script(Path("SQL/postgres/cvd_21.sql"),cdm_schema, vocab_schema)
total_heart_failure_inpatients=results_cvd_21[0][0]
total_heart_failure_inpatients_rein_heart_disease_30=results_cvd_21[1][0]

print(f"numero de pacientes que son dados de alta tras un ingreso por problemas de insuficiencia cardiaca: {total_heart_failure_inpatients}")
print(f"numero de pacientes que tras ser dados de alta por un problema de insuficienci cardiaca vuelven a ingresar con cualquier problema de cardiovascular (heart disease) en menos de 30 dias: {total_heart_failure_inpatients_rein_heart_disease_30}")


#Cardiovascular Indicator 22 - Percentaje of patients that in less than 30 dais after being subjected to an aortic valve substitution present a postoperatory infection
results_cvd_22=utils.exe_sql_script(Path("SQL/postgres/cvd_22.sql"),cdm_schema, vocab_schema)
total_TAVI_patient=results_cvd_22[0][0]
total_TAVI_postop_infection_30_patient=results_cvd_22[0][1]

print(f"numero de pacientes sometidos a un proceso quirujico TAVI: {total_TAVI_patient}")
print(f"numero de pacientes que tras ser sometidos a un proceso quirurjico TAVI, en menos de 30 dias, muestran una infeccion postoperatoria: {total_TAVI_postop_infection_30_patient}")


#Cardiovascular Indicator 23 - percentaje of patientes that die in less than 30 days after being discharged for a heart failure
results_cvd_23=utils.exe_sql_script(Path("SQL/postgres/cvd_23.sql"),cdm_schema, vocab_schema)
total_heart_failure_inpatients=results_cvd_23[0][0]
total_heart_failure_inpatients_die_30=results_cvd_23[1][0]

print(f"numero de pacientes que son dados de alta tras un ingreso por problemas de insuficiencia cardiaca: {total_heart_failure_inpatients}")
print(f"numero de pacientes que mueren en menos de 30 dias tras ser dados de alta por un problema de insuficiencia cardica: {total_heart_failure_inpatients_die_30}")


#Cardiocacular Indicator 24 - Median time since a NSTEMI patient arrives to the hospital, to the moment it is treated wiht an STENT [tiempo puesta balon]
results_cvd_24=utils.exe_sql_script(Path("SQL/postgres/cvd_24.sql"),cdm_schema, vocab_schema)
mean_hours_NSTEMI_STENT=results_cvd_24[0][2]
median_hours_NSTEMI_STENT=results_cvd_24[0][5]

print(f"tiempo medio de puesta balón: {mean_hours_NSTEMI_STENT} horas")
print(f"tiempo mediano de puesta balón: {median_hours_NSTEMI_STENT} horas")


#Cardiovascular Indicator 25 - Percentaje of patients with any cardiopaty that are diagnosed as well with hypertension
results_cvd_25=utils.exe_sql_script(Path("SQL/postgres/cvd_25.sql"),cdm_schema, vocab_schema)
total_cardiopathy_patients=results_cvd_25[0][0]
total_cardiopathy_hypertension_patients=results_cvd_25[1][0]

print(f"numero de pacientes con cualquier tipo de cardiopatia: {total_cardiopathy_patients}")
print(f"numero de pacientes con cualquier cardiopatia que tambien presentan hypertension: {total_cardiopathy_hypertension_patients}")


#Cardiovascular Indicator 26 - Percentaje of patientes with any cardiopathy and hypertension that get ther bllod preasure measured
results_cvd_26=utils.exe_sql_script(Path("SQL/postgres/cvd_26.sql"),cdm_schema, vocab_schema)
total_cardiopathy_hypertension_patients=results_cvd_26[0][0]
total_cardiopathy_hypertension_bloodpreasure_patients=results_cvd_26[1][0]

print(f"numero de pacientes con cualquier cardiopatia que tambien presentan hypertension: {total_cardiopathy_hypertension_patients}")
print(f"numero de pacientes con cualquier cadiopatia e hypertension a los que se les mide la presion sanguinea: {total_cardiopathy_hypertension_bloodpreasure_patients}")


#Cardiovascular Indicator 27 - Percentaje of patients with any cardiopathy and hypertension that shows blood preasere levels higher than 130 mmHg
results_cvd_27=utils.exe_sql_script(Path("SQL/postgres/cvd_27.sql"),cdm_schema, vocab_schema)
total_cardiopathy_hypertension_patients=results_cvd_27[0][0]
total_cardiopathy_hypertension_130_patients=results_cvd_27[1][0]

print(f"numero de pacientes con cualquier cadiopatia e hypertension a los que se les mide la presion sanguinea: {total_cardiopathy_hypertension_patients}")
print(f"numero de pacientes con cualquier cardiopatia que presentan hypertension y tienen niveles de mmHg superiores a 130 en algun momento: {total_cardiopathy_hypertension_130_patients}")


#Cardiovascular Indicator 28 - Percentaje of patientes with any cardiopathy that are diagnosed with diabetes
results_cvd_28=utils.exe_sql_script(Path("SQL/postgres/cvd_28.sql"),cdm_schema, vocab_schema)
total_cardiopathy_patients=results_cvd_28[0][0]
total_cardiopathy_diabetes_patients=results_cvd_28[1][0]

print(f"numero de pacientes con cualquier tipo de cadiopatia : {total_cardiopathy_patients}")
print(f"numero de pacientes con cualquier cardiopatia que que tambien son diagnosticados con diabetes: {total_cardiopathy_diabetes_patients}")


#Cardiovascular Indicator 29 - Percentaje of patients with any cardiopathy that smoke
results_cvd_29=utils.exe_sql_script(Path("SQL/postgres/cvd_29.sql"),cdm_schema, vocab_schema)
total_cardiopathy_patients=results_cvd_29[0][0]
total_cardiopathy_smoke_patients=results_cvd_29[1][0]

print(f"numero de pacientes con cualquier tipo de cadiopatia : {total_cardiopathy_patients}")
print(f"numero de pacientes con cualquier cardiopatia que fuman: {total_cardiopathy_smoke_patients}")


#Cardiovascular Indicator 30 - Percentaje of patients with any cardiopathy that is treated with statins
results_cvd_30=utils.exe_sql_script(Path("SQL/postgres/cvd_30.sql"),cdm_schema, vocab_schema)
total_cardiopathy_patients=results_cvd_30[0][0]
total_cardiopathy_statins_patients=results_cvd_30[1][0]

print(f"numero de pacientes con cualquier tipo de cadiopatia : {total_cardiopathy_patients}")
print(f"numero de pacientes con cualquier cardiopatia que toman estatinas: {total_cardiopathy_statins_patients}")