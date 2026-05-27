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
        
        
    
    



#### OLD_MAIN FUNCTIONS ####
# def exe_sql_query (query):
#     '''Create connection to the database using the .env variables, execute the specified query,
#        return single row of the result and close connection.

#         Args:
#             query (string): the SQL query to be executed
        
#         Returns:
#             string: first row of results for the given query

#         Example:
#             >>>exe_sql_query("SELECT version()")
#             "verision of the database"
#     '''
#     connection= psycopg2.connect(
#         dbname =os.getenv("POSTGRES_DB"),
#         user =os.getenv("POSTGRES_USER"),
#         password=os.getenv("POSTGRES_PASSWORD"),
#         host=os.getenv("POSTGRES_HOST"),
#         port=os.getenv("POSTGRES_PORT"),
#     )
#     connection.autocommit = True
#     cursor = connection.cursor()

#     cursor.execute(f"{query}")
#     result = cursor.fetchone() 
#     cursor.close()
#     connection.close()  

#     return result

# def exe_sql_script (script: Path, cdm_schema = '', vocab_schema = ''):
#     '''Create connection to the databse using the .env variables, execute the comands of the specified 
#        script using the specified schemas for dynamic substitution if the script are prepared for it,
#        requires the .sql scripts to use the corresponding placeholders (cdm_schema and vocab_schema),
#        return an array with the first row of the result of each one of the commands in the script

#         Args:
#             script (Path): relative from the execution folder to the path where the script is

#         Optional Args:
#             cdm_schema (string): name of the schema where omop cdm data is located
#             vocab_schema (string): name of the schema where omop vocabulary is located

#         Returns:
#             array: lsit with first row of the resut of each one of the SQL commands in specified script
#                    in the order they are read from the script
#     '''

#     #Checks that the given script path exist, then red file and store the different sql commands of the script as strings in a list
#     if script.exists():
#         with open(script,'r') as file:
#             sql_commands=file.read().split(";")
#     else:
#         print(f"The specified script path: '{script}' does not exist")
#         return
#     #Create connection to the database only when file exists
#     connection= psycopg2.connect(
#         dbname =os.getenv("POSTGRES_DB"),
#         user =os.getenv("POSTGRES_USER"),
#         password=os.getenv("POSTGRES_PASSWORD"),
#         host=os.getenv("POSTGRES_HOST"),
#         port=os.getenv("POSTGRES_PORT"),
#     )

#     results=[]
#     connection.autocommit = True
#     cursor = connection.cursor()
#     for command in sql_commands:
#         if command and command.strip() :
#             #Parse the sql string to dynamically subsitute placeholders for specific set variables
#             query=sql.SQL(command).format(cdm_schema = sql.Identifier(cdm_schema), vocab_schema=sql.Identifier(vocab_schema))
#             #Exceute each sql script query/command
#             cursor.execute(query)
#             #Append the first line of the results of each sql query/command in a list
#             results.append(cursor.fetchone())              
#     cursor.close()
#     connection.close() 

#     return results