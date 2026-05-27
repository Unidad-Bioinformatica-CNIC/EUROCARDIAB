########## IMPORTS ##########
import utils 
import os
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine
# from dotenv import load_dotenv  # If implemented in a docker container, this might not be needed, as variables in .env file might be already availabe as environment viariables


########## VARIABLES ##########
# load_dotenv('.env')
dialect=os.getenv('DIALECT')
db_api=os.getenv('DBAPI')
db_user=os.getenv('DB_USER')
db_password=os.getenv('DB_PASSWORD')
db_host=os.getenv('DB_HOST')
db_port=os.getenv('DB_PORT')
db_name=os.getenv('DB_NAME')

engine_url = f"{dialect}+{db_api}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
print(engine_url)

#engine = create_engine(str(os.getenv('DIALECT')+'+'+os.getenv('DBAPI')+'://'+os.getenv('DB_USER')+':'+os.getenv('DB_PASSWORD')+'@'+os.getenv('DB_HOST')+':'+os.getenv('DB_PORT')+'/'+os.getenv('DB_NAME')))
engine = create_engine(engine_url)
substitutiuon_identifiers = {
    'cdm_schema': os.getenv('CDM_SCHEMA'),
    'vocab_schema': os.getenv('VOCAB_SCHEMA')
}
 
#Create empty results dataframe that will store final results before dumping into csv/other file type
persons_columns=['Indicator_id','Total','Male','Female','Unknown_sex','decile_0-10','decile_10-20','decile_20-30','decile_30-40','decile_40-50','decile_50-60','decile_60-70','decile_70-80','decile_80-90','decile_90+','Male_decile_0-10','Male_decile_10-20','Male_decile_20-30','Male_decile_30-40','Male_decile_40-50','Male_decile_50-60','Male_decile_60-70','Male_decile_70-80','Male_decile_80-90','Male_decile_90+','Female_decile_0-10','Female_decile_10-20','Female_decile_20-30','Female_decile_30-40','Female_decile_40-50','Female_decile_50-60','Female_decile_60-70','Female_decile_70-80','Female_decile_80-90','Female_decile_90+','Unknown_decile_0-10','Unknown_decile_10-20','Unknown_decile_20-30','Unknown_decile_30-40','Unknown_decile_40-50','Unknown_decile_50-60','Unknown_decile_60-70','Unknown_decile_70-80','Unknown_decile_80-90','Unknown_decile_90+']
# hour_statistic_columns=['Indicator_id','total_patients','mean_hours','max_hours','median_hours','p25_hours','p75_hours']

diab_persons_results_df = pd.DataFrame(columns=persons_columns)
cvd_persons_results_df = pd.DataFrame(columns=persons_columns)
cvd_hour_statistic_results_df = pd.DataFrame()

########## CODE ##########
#### Diabetes Indicators ####
num_diab_indicators = 14
for i in range(1,num_diab_indicators+1):
    diab_numerator_df = utils.run_sql_script_df(Path(f"SQL/postgres/diab_{i}_numerator.sql"),substitutiuon_identifiers,engine)
    diab_denominator = utils.run_sql_script(Path(f"SQL/postgres/diab_{i}_denominator.sql"),substitutiuon_identifiers,engine).all()[0][0]
    if (diab_denominator == 0):
        print(f"Warning at diabates indicator {i} !!!")
        print(f"Error al calcular el indicador. El denominador del indicador es zero")
    else:
        diab_persons_results_df = utils.fill_persons_df(diab_persons_results_df, f"diab_{i}", diab_numerator_df, diab_denominator)
    print(f"Finished calculating indicator: diab_{i}")

diab_persons_results_df.to_csv('results/diab_persons_indicators.csv', index=False, mode='w')


#### Cardiovascular Indicators ####
num_cvd_indicators=30
for i in range(1,num_cvd_indicators+1):
    if os.path.exists(f"SQL/postgres/cvd_{i}_numerator.sql"):
        cvd_numerator_df = utils.run_sql_script_df(Path(f"SQL/postgres/cvd_{i}_numerator.sql"),substitutiuon_identifiers,engine)
        cvd_denominator = utils.run_sql_script(Path(f"SQL/postgres/cvd_{i}_denominator.sql"),substitutiuon_identifiers,engine).all()[0][0]
        if (cvd_denominator == 0):
            print(f"Warning at diabates indicator {i} !!!")
            print(f"Error al calcular el indicador. El denominador del indicador cvd_{i} es zero")
        else:
            cvd_persons_results_df = utils.fill_persons_df(cvd_persons_results_df, f"cvd_{i}", cvd_numerator_df, cvd_denominator)
            print(f"Finished calculating indicator: diab_{i}")
    else:
        cvd_hour_statistic_df = utils.run_sql_script_df(Path(f"SQL/postgres/cvd_{i}.sql"), substitutiuon_identifiers, engine)
        cvd_hour_statistic_results_df = utils.fill_hour_statistics_df(cvd_hour_statistic_results_df, f"cvd_{i}", cvd_hour_statistic_df)
        print(f"Finished calculating indicator: diab_{i}")
        

cvd_persons_results_df.to_csv('results/cvd_persons_indicators.csv', index=False, mode='w')
cvd_hour_statistic_results_df.to_csv('results/cvd_hour_statistic_indicators.csv', index=False, mode='w')