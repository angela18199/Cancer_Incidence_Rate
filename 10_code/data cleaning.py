import pandas as pd
import numpy as np

#make intermediate table for cancer data
df_f1 = pd.read_table("/Users/yu/Documents/Duke/github/stats_final_project/00_source/cancer incidence data(2012-2016)/female/United States and Puerto Rico Cancer Statistics, 1999-2016 Incidence_1.txt", sep="\t")
df_f2 = pd.read_table("/Users/yu/Documents/Duke/github/stats_final_project/00_source/cancer incidence data(2012-2016)/female/United States and Puerto Rico Cancer Statistics, 1999-2016 Incidence_2.txt", sep="\t")
df_f3 = pd.read_table("/Users/yu/Documents/Duke/github/stats_final_project/00_source/cancer incidence data(2012-2016)/female/United States and Puerto Rico Cancer Statistics, 1999-2016 Incidence_3.txt", sep="\t")
df_f4 = pd.read_table("/Users/yu/Documents/Duke/github/stats_final_project/00_source/cancer incidence data(2012-2016)/female/United States and Puerto Rico Cancer Statistics, 1999-2016 Incidence_4.txt", sep="\t")
df_f5 = pd.read_table("/Users/yu/Documents/Duke/github/stats_final_project/00_source/cancer incidence data(2012-2016)/female/United States and Puerto Rico Cancer Statistics, 1999-2016 Incidence_5.txt", sep="\t")
df_f6 = pd.read_table("/Users/yu/Documents/Duke/github/stats_final_project/00_source/cancer incidence data(2012-2016)/female/United States and Puerto Rico Cancer Statistics, 1999-2016 Incidence_6.txt", sep="\t")
df_f7 = pd.read_table("/Users/yu/Documents/Duke/github/stats_final_project/00_source/cancer incidence data(2012-2016)/female/United States and Puerto Rico Cancer Statistics, 1999-2016 Incidence_7.txt", sep="\t")

df_m1 = pd.read_table("/Users/yu/Documents/Duke/github/stats_final_project/00_source/cancer incidence data(2012-2016)/male/United States and Puerto Rico Cancer Statistics, 1999-2016 Incidence_1.txt", sep='\t')
df_m2 = pd.read_table("/Users/yu/Documents/Duke/github/stats_final_project/00_source/cancer incidence data(2012-2016)/male/United States and Puerto Rico Cancer Statistics, 1999-2016 Incidence_2.txt", sep='\t')
df_m3 = pd.read_table("/Users/yu/Documents/Duke/github/stats_final_project/00_source/cancer incidence data(2012-2016)/male/United States and Puerto Rico Cancer Statistics, 1999-2016 Incidence_3.txt", sep='\t')
df_m4 = pd.read_table("/Users/yu/Documents/Duke/github/stats_final_project/00_source/cancer incidence data(2012-2016)/male/United States and Puerto Rico Cancer Statistics, 1999-2016 Incidence_4.txt", sep='\t')
df_m5 = pd.read_table("/Users/yu/Documents/Duke/github/stats_final_project/00_source/cancer incidence data(2012-2016)/male/United States and Puerto Rico Cancer Statistics, 1999-2016 Incidence_5.txt", sep='\t')
df_m6 = pd.read_table("/Users/yu/Documents/Duke/github/stats_final_project/00_source/cancer incidence data(2012-2016)/male/United States and Puerto Rico Cancer Statistics, 1999-2016 Incidence_6.txt", sep='\t')
df_m7 = pd.read_table("/Users/yu/Documents/Duke/github/stats_final_project/00_source/cancer incidence data(2012-2016)/male/United States and Puerto Rico Cancer Statistics, 1999-2016 Incidence_7.txt", sep='\t')
df_m8 = pd.read_table("/Users/yu/Documents/Duke/github/stats_final_project/00_source/cancer incidence data(2012-2016)/male/United States and Puerto Rico Cancer Statistics, 1999-2016 Incidence_8.txt", sep='\t')

cancerdf_f = [df_f1, df_f2, df_f3, df_f4, df_f5, df_f6, df_f7]
cancerdf_m = [df_m1, df_m2, df_m3, df_m4, df_m5, df_m6, df_m7, df_m8]

print(df_m1.tail())

#clean female data
count = 0
for d in cancerdf_f:
    #print(d.isnull().sum())
    null_num = d.Count.isnull().sum()
    #print(null_num)
    d = d.iloc[:-null_num,:]
    d = d.drop(["Notes","Leading Cancer Sites Code","States Code","Year Code","Race Code","Age Groups Code"], axis = 1)
    d["Gender"] = "female"
    d.loc[(d["Age Groups"] == "< 1 year") | (d["Age Groups"] == "1-4 years"), "Age Groups"] = "< 5 years"
    d.loc[(d["Age Groups"] == "35-39 years") | (d["Age Groups"] == "40-44 years"), "Age Groups"] = "35-44 years"
    d.loc[(d["Age Groups"] == "45-49 years") | (d["Age Groups"] == "50-54 years"), "Age Groups"] = "45-54 years"
    d.loc[(d["Age Groups"] == "55-59 years") | (d["Age Groups"] == "60-64 years "), "Age Groups"] = "55-64 years"
    d.loc[(d["Age Groups"] == "65-69 years") | (d["Age Groups"] == "70-74 years"), "Age Groups"] = "65-74 years"
    d.loc[(d["Age Groups"] == "75-79 years") | (d["Age Groups"] == "80-84 years"), "Age Groups"] = "75-84 years"
    d = d.groupby(["Leading Cancer Sites","States","Year","Age Groups","Race","Gender"]).sum().reset_index()
    #print(d.tail())
    cancerdf_f[count] = d.copy()
    count = count + 1

print(cancerdf_f[0].tail())

#clean male data
count = 0
for d in cancerdf_m:
    #print(d.isnull().sum())
    null_num = d.Count.isnull().sum()
    #print(null_num)
    d = d.iloc[:-null_num,:]
    d = d.drop(["Notes","Leading Cancer Sites Code","States Code","Year Code","Race Code","Age Groups Code"], axis = 1)
    d["Gender"] = "male"
    d.loc[(d["Age Groups"] == "< 1 year") | (d["Age Groups"] == "1-4 years"), "Age Groups"] = "< 5 years"
    d.loc[(d["Age Groups"] == "35-39 years") | (d["Age Groups"] == "40-44 years"), "Age Groups"] = "35-44 years"
    d.loc[(d["Age Groups"] == "45-49 years") | (d["Age Groups"] == "50-54 years"), "Age Groups"] = "45-54 years"
    d.loc[(d["Age Groups"] == "55-59 years") | (d["Age Groups"] == "60-64 years "), "Age Groups"] = "55-64 years"
    d.loc[(d["Age Groups"] == "65-69 years") | (d["Age Groups"] == "70-74 years"), "Age Groups"] = "65-74 years"
    d.loc[(d["Age Groups"] == "75-79 years") | (d["Age Groups"] == "80-84 years"), "Age Groups"] = "75-84 years"
    d = d.groupby(["Leading Cancer Sites","States","Year","Age Groups","Race","Gender"]).sum().reset_index()
    #print(d.tail())
    cancerdf_m[count] = d.copy()
    count = count + 1

print(cancerdf_m[0].tail())

table_c_f = pd.concat(cancerdf_f)
table_c_m = pd.concat(cancerdf_m)

table_c = [table_c_f, table_c_m]
table_c = pd.concat(table_c)
table_c = table_c.reset_index(drop = True)

print(table_c.head())
print(table_c.tail())

table_c.to_csv(r'/Users/yu/Documents/Duke/github/stats_final_project/20_intermediate_files/cancer incidence data.csv',header = True, index = None)



#make intermediate table for population data
df_pop2012 = pd.read_csv("/Users/yu/Documents/Duke/github/stats_final_project/00_source/population data by sex, age, race, state/2010-2016/nhgis0010_ds189_2012_state.csv")
df_pop2013 = pd.read_csv("/Users/yu/Documents/Duke/github/stats_final_project/00_source/population data by sex, age, race, state/2010-2016/nhgis0010_ds199_2013_state.csv")
df_pop2014 = pd.read_csv("/Users/yu/Documents/Duke/github/stats_final_project/00_source/population data by sex, age, race, state/2010-2016/nhgis0010_ds205_2014_state.csv")
df_pop2015 = pd.read_csv("/Users/yu/Documents/Duke/github/stats_final_project/00_source/population data by sex, age, race, state/2010-2016/nhgis0010_ds214_2015_state.csv")
df_pop2016 = pd.read_csv("/Users/yu/Documents/Duke/github/stats_final_project/00_source/population data by sex, age, race, state/2010-2016/nhgis0010_ds223_2016_state.csv")

df_pop = [df_pop2012, df_pop2013, df_pop2014, df_pop2015, df_pop2016]

race = ["White", "Black or African American", "Asian or Pacific Islander", "Asian or Pacific Islander"]
age = ["< 5 years","5-9 years","10-14 years","15-17 years","18-19 years","20-24 years","25-29 years","30-34 years","35-44 years","45-54 years","55-64 years","65-74 years","75-84 years","85+ years"]


table_p = []

for d_o in df_pop:
    d = d_o.iloc[:, [1,4]].copy()
    d = pd.concat([d, d_o.iloc[:,24:148]], axis = 1).copy()
    print(d.columns)
    print(d.head())

    for table in range(4):
        for col in range(4,18): #male
            pop = d.iloc[:,[0,1, (col+31*table) ]].copy()
            pop["RACE"]= race[table]
            pop["SEX"]= "male"
            pop["AGE"]= age[col-4]
            pop = pop.rename(columns={pop.columns[2]:"POPULATION"})
            #print(pop.head())
            table_p.append(pop.copy())
        for col in range(19,33): #female
            pop = d.iloc[:,[0,1, (col+31*table) ]].copy()
            pop["RACE"]= race[table]
            pop["SEX"]= "female"
            pop["AGE"]= age[col-19]
            pop = pop.rename(columns={pop.columns[2]:"POPULATION"})
            #print(pop.head())
            table_p.append(pop.copy())


table_p = pd.concat(table_p)
table_p = table_p.reset_index(drop = True)
print(table_p.head())
print(table_p.tail())

#combine age and race categories
table_p.loc[(table_p["AGE"] == "15-17 years") | (table_p["AGE"] == "18-19 years"), "AGE"] = "15-19 years"
table_p = table_p.groupby(["YEAR","STATE","RACE","SEX","AGE"]).sum().reset_index()

print(table_p.head())
print(table_p.tail())

table_p.to_csv(r'/Users/yu/Documents/Duke/github/stats_final_project/20_intermediate_files/population data.csv',header = True, index = None)


#merge the two intermediate table to final table
final_table = table_c.merge(table_p, how = "left", left_on = ['States','Year','Age Groups','Race','Gender'], right_on = ['STATE','YEAR','AGE','RACE','SEX'] )
final_table = final_table.drop(["YEAR","STATE","RACE",'SEX','AGE'],axis = 1)
final_table = final_table.rename(columns={'Count':'Incidence'})
final_table.loc[:,"Incidence"] = final_table.loc[:,"Incidence"].astype('int64')
final_table = final_table.rename(columns = {"Leading Cancer Sites":"c_site", "States":"state", "Year":"year", "Age Groups":"age", "Race":"race", "Gender":"sex", "Incidence":"inci", "POPULATION":"pop"})
final_table.to_csv("/Users/yu/Documents/Duke/github/stats_final_project/20_intermediate_files/final dataset.csv",header = True, index = None)

final_table_by_state = final_table.groupby('state').sum().reset_index().drop('year', axis = 1).copy()
final_table_by_state.to_csv("/Users/yu/Documents/Duke/github/stats_final_project/20_intermediate_files/final dataset by state.csv",header = True, index = None)

final_table_by_cancer = final_table.groupby('c_site').sum().reset_index().drop(['year'], axis = 1).copy()
final_table_by_cancer.to_csv("/Users/yu/Documents/Duke/github/stats_final_project/20_intermediate_files/final dataset by cancer.csv",header = True, index = None)

final_table_by_age = final_table.groupby('age').sum().reset_index().drop(['year'], axis = 1).copy()
final_table_by_age.to_csv("/Users/yu/Documents/Duke/github/stats_final_project/20_intermediate_files/final dataset by age.csv",header = True, index = None)

final_table_by_race = final_table.groupby('race').sum().reset_index().drop(['year'], axis = 1).copy()
final_table_by_race.to_csv("/Users/yu/Documents/Duke/github/stats_final_project/20_intermediate_files/final dataset by race.csv",header = True, index = None)

final_table_by_gender = final_table.groupby('sex').sum().reset_index().drop(['year'], axis = 1).copy()
final_table_by_gender.to_csv("/Users/yu/Documents/Duke/github/stats_final_project/20_intermediate_files/final dataset by gender.csv",header = True, index = None)
