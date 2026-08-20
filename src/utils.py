from pathlib import Path
import pandas as pd
from sqlalchemy import text

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

def fill_persons_df(results_df:pd.DataFrame, indicator_id:str, numerator_df:pd.DataFrame, denominator:int = 1):
    #If numerator is zero and therefore the dataframe is empty
    if numerator_df.empty:
        results_df.loc[len(results_df)]=0
        results_df.iloc[len(results_df)-1, 0]= indicator_id
        return results_df
    else:
        results={'Indicator_id':indicator_id,
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
        