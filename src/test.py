#### IMPORTS #####
import os
import time
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine, text
from dotenv import load_dotenv                          # If implemented in a docker container, this might not be needed, as variables in .env file might be already availabe as environment viariables
load_dotenv()


#### VARIABLES ####
# Import sql substitution identifiers (schemas, tables, columns) from .env file 
substitutiuon_identifiers = {
    'cdm_schema': os.getenv('CDM_SCHEMA'),
    'vocab_schema': os.getenv('VOCAB_SCHEMA')
}
# Import sql substitution parameters (hour/string values for where clauses) from .env file
substitutiuon_parameters={
    'concept_ancestor': 201820
}
# Create engine with variables from .env file
engine = create_engine(str(os.getenv('DIALECT')+'+'+os.getenv('DBAPI')+'://'+os.getenv('POSTGRES_USER')+':'+os.getenv('POSTGRES_PASSWORD')+'@'+os.getenv('POSTGRES_HOST')+':'+os.getenv('POSTGRES_PORT')+'/'+os.getenv('POSTGRES_DB')))

#Create empty results dataframe that will store fonal results before dumping into csv/other file type
columns=['Indicator_id','Total','Male','Female','Unknown_sex','decile_0-10','decile_10-20','decile_20-30','decile_30-40','decile_40-50','decile_50-60','decile_60-70','decile_70-80','decile_80-90','decile_90+','Male_decile_0-10','Male_decile_10-20','Male_decile_20-30','Male_decile_30-40','Male_decile_40-50','Male_decile_50-60','Male_decile_60-70','Male_decile_70-80','Male_decile_80-90','Male_decile_90+','Female_decile_0-10','Female_decile_10-20','Female_decile_20-30','Female_decile_30-40','Female_decile_40-50','Female_decile_50-60','Female_decile_60-70','Female_decile_70-80','Female_decile_80-90','Female_decile_90+','Unknown_decile_0-10','Unknown_decile_10-20','Unknown_decile_20-30','Unknown_decile_30-40','Unknown_decile_40-50','Unknown_decile_50-60','Unknown_decile_60-70','Unknown_decile_70-80','Unknown_decile_80-90','Unknown_decile_90+']
results_df = pd.DataFrame(columns=columns)

cvd_hour_statistic_results_df = pd.DataFrame()

#### FUNCTIONS ####
def run_sql_script(script: Path, identifiers:dict, engine, params:dict={}):
    if script.exists():
        with open(script,'r') as file:
            raw = file.read()
            formatted= raw.format(**identifiers)
    else:
        print(f"The specified script path: '{script}' does not exist")
    
    with engine.connect() as conn:
        result = conn.execute(text(formatted), params)
        
    return result

def run_sql_script_df(script: Path, identifiers:dict, engine, params:dict={}):
    if script.exists():
        with open(script,'r') as file:
            raw = file.read()
            formatted= raw.format(**identifiers)
    else:
        print(f"The specified script path: '{script}' does not exist")
    
    with engine.connect() as conn:
        result = pd.DataFrame(conn.execute(text(formatted), params))
        
    return result

def fill_results_df(results_df:pd.DataFrame, indictor_id:str, numerator_df:pd.DataFrame, denominator:int = 1):
    #If numerator is zero and therefore the dataframe is empty
    if numerator_df.empty:
        results_df.loc[len(results_df)]=0
        results_df.iloc[len(results_df)-1, 0]= indictor_id
        return results_df
    else:
        results={'Indicator_id':indictor_id,
                 'Total':round((numerator_df['total_patients'].sum()/denominator)*100,2),
                 'Male':round((numerator_df.loc[numerator_df['gender_concept_id']==8507, 'total_patients'].sum()/denominator)*100,2),
                 'Female':round((numerator_df.loc[numerator_df['gender_concept_id']==8532, 'total_patients'].sum()/denominator)*100,2),
                 'Unknown_sex':round((numerator_df.loc[numerator_df['gender_concept_id']==0, 'total_patients'].sum()/denominator)*100,2),
                 'decile_0-10':round((numerator_df.loc[numerator_df['age_decile']==0, 'total_patients'].sum()/denominator)*100,2),
                 'decile_10-20':round((numerator_df.loc[numerator_df['age_decile']==1, 'total_patients'].sum()/denominator)*100,2),
                 'decile_20-30':round((numerator_df.loc[numerator_df['age_decile']==2, 'total_patients'].sum()/denominator)*100,2),
                 'decile_30-40':round((numerator_df.loc[numerator_df['age_decile']==3, 'total_patients'].sum()/denominator)*100,2),
                 'decile_40-50':round((numerator_df.loc[numerator_df['age_decile']==4, 'total_patients'].sum()/denominator)*100,2),
                 'decile_50-60':round((numerator_df.loc[numerator_df['age_decile']==5, 'total_patients'].sum()/denominator)*100,2),
                 'decile_60-70':round((numerator_df.loc[numerator_df['age_decile']==6, 'total_patients'].sum()/denominator)*100,2),
                 'decile_70-80':round((numerator_df.loc[numerator_df['age_decile']==7, 'total_patients'].sum()/denominator)*100,2),
                 'decile_80-90':round((numerator_df.loc[numerator_df['age_decile']==8, 'total_patients'].sum()/denominator)*100,2),
                 'decile_90+':round((numerator_df.loc[numerator_df['age_decile']>=9, 'total_patients'].sum()/denominator)*100,2),
                 'Male_decile_0-10':round((numerator_df.loc[(numerator_df['gender_concept_id']==8507) & (numerator_df['age_decile']==0),'total_patients'].sum()/denominator)*100,2),
                 'Male_decile_10-20':round((numerator_df.loc[(numerator_df['gender_concept_id']==8507) & (numerator_df['age_decile']==1),'total_patients'].sum()/denominator)*100,2),
                 'Male_decile_20-30':round((numerator_df.loc[(numerator_df['gender_concept_id']==8507) & (numerator_df['age_decile']==2),'total_patients'].sum()/denominator)*100,2),
                 'Male_decile_30-40':round((numerator_df.loc[(numerator_df['gender_concept_id']==8507) & (numerator_df['age_decile']==3),'total_patients'].sum()/denominator)*100,2),
                 'Male_decile_40-50':round((numerator_df.loc[(numerator_df['gender_concept_id']==8507) & (numerator_df['age_decile']==4),'total_patients'].sum()/denominator)*100,2),
                 'Male_decile_50-60':round((numerator_df.loc[(numerator_df['gender_concept_id']==8507) & (numerator_df['age_decile']==5),'total_patients'].sum()/denominator)*100,2),
                 'Male_decile_60-70':round((numerator_df.loc[(numerator_df['gender_concept_id']==8507) & (numerator_df['age_decile']==6),'total_patients'].sum()/denominator)*100,2),
                 'Male_decile_70-80':round((numerator_df.loc[(numerator_df['gender_concept_id']==8507) & (numerator_df['age_decile']==7),'total_patients'].sum()/denominator)*100,2),
                 'Male_decile_80-90':round((numerator_df.loc[(numerator_df['gender_concept_id']==8507) & (numerator_df['age_decile']==8),'total_patients'].sum()/denominator)*100,2),
                 'Male_decile_90+':round((numerator_df.loc[(numerator_df['gender_concept_id']==8507) & (numerator_df['age_decile']>=9),'total_patients'].sum()/denominator)*100,2),
                 'Female_decile_0-10':round((numerator_df.loc[(numerator_df['gender_concept_id']==8532) & (numerator_df['age_decile']==0),'total_patients'].sum()/denominator)*100,2),
                 'Female_decile_10-20':round((numerator_df.loc[(numerator_df['gender_concept_id']==8532) & (numerator_df['age_decile']==1),'total_patients'].sum()/denominator)*100,2),
                 'Female_decile_20-30':round((numerator_df.loc[(numerator_df['gender_concept_id']==8532) & (numerator_df['age_decile']==2),'total_patients'].sum()/denominator)*100,2),
                 'Female_decile_30-40':round((numerator_df.loc[(numerator_df['gender_concept_id']==8532) & (numerator_df['age_decile']==3),'total_patients'].sum()/denominator)*100,2),
                 'Female_decile_40-50':round((numerator_df.loc[(numerator_df['gender_concept_id']==8532) & (numerator_df['age_decile']==4),'total_patients'].sum()/denominator)*100,2),
                 'Female_decile_50-60':round((numerator_df.loc[(numerator_df['gender_concept_id']==8532) & (numerator_df['age_decile']==5),'total_patients'].sum()/denominator)*100,2),
                 'Female_decile_60-70':round((numerator_df.loc[(numerator_df['gender_concept_id']==8532) & (numerator_df['age_decile']==6),'total_patients'].sum()/denominator)*100,2),
                 'Female_decile_70-80':round((numerator_df.loc[(numerator_df['gender_concept_id']==8532) & (numerator_df['age_decile']==7),'total_patients'].sum()/denominator)*100,2),
                 'Female_decile_80-90':round((numerator_df.loc[(numerator_df['gender_concept_id']==8532) & (numerator_df['age_decile']==8),'total_patients'].sum()/denominator)*100,2),
                 'Female_decile_90+':round((numerator_df.loc[(numerator_df['gender_concept_id']==8532) & (numerator_df['age_decile']>=9),'total_patients'].sum()/denominator)*100,2),
                 'Unknown_decile_0-10':round((numerator_df.loc[(numerator_df['gender_concept_id']==0) & (numerator_df['age_decile']==0),'total_patients'].sum()/denominator)*100,2),
                 'Unknown_decile_10-20':round((numerator_df.loc[(numerator_df['gender_concept_id']==0) & (numerator_df['age_decile']==1),'total_patients'].sum()/denominator)*100,2),
                 'Unknown_decile_20-30':round((numerator_df.loc[(numerator_df['gender_concept_id']==0) & (numerator_df['age_decile']==2),'total_patients'].sum()/denominator)*100,2),
                 'Unknown_decile_30-40':round((numerator_df.loc[(numerator_df['gender_concept_id']==0) & (numerator_df['age_decile']==3),'total_patients'].sum()/denominator)*100,2),
                 'Unknown_decile_40-50':round((numerator_df.loc[(numerator_df['gender_concept_id']==0) & (numerator_df['age_decile']==4),'total_patients'].sum()/denominator)*100,2),
                 'Unknown_decile_50-60':round((numerator_df.loc[(numerator_df['gender_concept_id']==0) & (numerator_df['age_decile']==5),'total_patients'].sum()/denominator)*100,2),
                 'Unknown_decile_60-70':round((numerator_df.loc[(numerator_df['gender_concept_id']==0) & (numerator_df['age_decile']==6),'total_patients'].sum()/denominator)*100,2),
                 'Unknown_decile_70-80':round((numerator_df.loc[(numerator_df['gender_concept_id']==0) & (numerator_df['age_decile']==7),'total_patients'].sum()/denominator)*100,2),
                 'Unknown_decile_80-90':round((numerator_df.loc[(numerator_df['gender_concept_id']==0) & (numerator_df['age_decile']==8),'total_patients'].sum()/denominator)*100,2),
                 'Unknown_decile_90+':round((numerator_df.loc[(numerator_df['gender_concept_id']==0) & (numerator_df['age_decile']>=9),'total_patients'].sum()/denominator)*100,2)}

        results_df.loc[len(results_df)] = results
        return results_df
    
def fill_hour_statistics_df(results_df:pd.DataFrame, indicator_id:str, statistics_df:pd.DataFrame): 
    if results_df.empty:
        statistics_df.insert(0,"Indicator_id",indicator_id)
        return statistics_df
    else:
        statistics_df.insert(0,"Indicator_id",indicator_id)
        results_df = pd.concat([results_df,statistics_df])
        return results_df


#### CODE ####
# # test_result = run_sql_script(Path('SQL/postgres/test.sql'),substitutiuon_identifiers ,engine, substitutiuon_parameters )
test_df = run_sql_script_df(Path('SQL/postgres/cvd_24.sql'),substitutiuon_identifiers ,engine, substitutiuon_parameters )
print(test_df)
cvd_hour_statistic_results_df = fill_hour_statistics_df(cvd_hour_statistic_results_df, f"cvd_24", test_df)
print(cvd_hour_statistic_results_df)
print(f"Finished calculating indicator: diab_24")
test_df = run_sql_script_df(Path('SQL/postgres/cvd_24.sql'),substitutiuon_identifiers ,engine, substitutiuon_parameters )
cvd_hour_statistic_results_df = fill_hour_statistics_df(cvd_hour_statistic_results_df, f"cvd_24", test_df)
print(cvd_hour_statistic_results_df)
print(f"Finished calculating indicator: diab_24")


# # start = time.time()
# results_df = fill_results_df(results_df, "test", test_df, 7290)
# # end = time.time()
# # elapsed = end - start
# # print(f'Time taken: {elapsed:.6f} seconds')
# print(results_df)