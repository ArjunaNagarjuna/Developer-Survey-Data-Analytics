# %%
import pandas as pd
data = pd.read_csv("survey_results_public.csv")
data.info()

# %%
data.head(20)

# %%
pd.set_option('display.max_columns',85)
data


# %%
data.Employment.value_counts()

# %%
data['OpSysPersonal use'].value_counts()

# %%
data.Employment[89182]

# %%
data['DevType'].value_counts()

# %%
macos_users = data[data['OpSysProfessional use']=='MacOS']

# %%
macos_users


# %%
data['Country'].value_counts()

# %%
usa_developers = data[data['Country']=="United States of America"]
usa_developers

# %%
india_developers = data[data['Country']=="India"]
india_developers

# %%
usa_developers['Age'].value_counts()

# %%
india_developers['Age'].value_counts()

# %%
data[(data["Country"]=='India') &(data['CodingActivities']=='Hobby')  & (data['Employment']=="Employed, full-time")]

# %%
filter = (data['Country']=='India') & (data['RemoteWork']=='Remote') & (data['ConvertedCompYearly']>100000)
data[filter].LanguageWantToWorkWith.value_counts()

# %%
data = pd.read_csv("survey_results_public.csv",index_col='ResponseId')
data

# %%
survey = pd.read_csv("survey_results_schema.csv",index_col='qname')
survey

# %%
survey.loc['TBranch'].question

# %%
data[data["Country"]=='United States of America']

# %%
data.query('Country =="United States of America"')

# %%
data.query('ConvertedCompYearly>100000 & Country =="India" & RemoteWork=="Remote" & YearsCodePro=="8"')

# %%
data['YearsCodePro'] = pd.to_numeric(data['YearsCodePro'],errors='coerce')

# %%
sample_devs = data.query('ConvertedCompYearly>100000 & Country =="India" & RemoteWork=="Remote" & YearsCodePro<12')


# %%
sample_devs['LanguageWantToWorkWith'].value_counts()

# %%
max_value = data['ConvertedCompYearly'].max()
second_highest = data[data['ConvertedCompYearly']<max_value]['ConvertedCompYearly']
second_highest.sort_values(ascending=False).head(20)


# %%
max_salary =  data['ConvertedCompYearly'].quantile(0.999)

# %%
data[data['ConvertedCompYearly'] > max_salary]

# %%
data = data[data['ConvertedCompYearly'] < max_salary]
    

# %%
data['ConvertedCompYearly'].max()


# %%
data[data['ConvertedCompYearly']==data['ConvertedCompYearly'].max()]

# %%
data['ConvertedCompYearly'].min()

# %%
import numpy as np
emp_data = data[(data['Employment']=='Employed') & data['ConvertedCompYearly']!=np.nan]
emp_data['ConvertedCompYearly'].min()

# %%
min_salary = emp_data['ConvertedCompYearly'].quantile(0.02)
min_salary

# %%
data = data[emp_data['ConvertedCompYearly'] > min_salary]

# %%
data['ConvertedCompYearly'].sort_values().head(40)

# %%
indian_devs = data[data['Country']=="India"]
max_indian_salary = indian_devs['ConvertedCompYearly'].max()

# %%
indian_devs[indian_devs['ConvertedCompYearly']== max_indian_salary]

# %%
min_indian_salary = indian_devs['ConvertedCompYearly'].min()

# %%
indian_devs[indian_devs['ConvertedCompYearly']== min_indian_salary]

# %%
indian_devs['ConvertedCompYearly'].mean()*80

# %%
indian_devs[indian_devs['YearsCodePro']==7]['ConvertedCompYearly'].mean()

# %%
indian_devs[indian_devs['YearsCodePro']==7]['ConvertedCompYearly'].max()

# %%
indian_devs[indian_devs['YearsCodePro']==7]['ConvertedCompYearly'].min()

# %%
usa_devs = data[data['Country']=="United States of America"]
usa_devs['ConvertedCompYearly'].min()

# %%
data[data['LanguageHaveWorkedWith']=="Python"]['ConvertedCompYearly'].mean()

# %%
data['ConvertedCompYearly'].sum()

# %%
data.groupby('Country').sum()['ConvertedCompYearly'].sort_values(ascending=False)

# %%
data['RemoteWork'].value_counts()

# %%
data['EdLevel'].value_counts(normalize=True)*100

# %%
from matplotlib import pyplot as plt
percent_spread = data['EdLevel'].value_counts(normalize=True)*100
percent_spread = percent_spread.sort_values()
percent_spread.plot(kind = 'barh')
plt.title("Distribution of education leveles")
plt.xlabel("Percentage")
plt.ylabel("Education Level")
plt.show()

# %%
learn_methods = data['LearnCode'].str.split(";").explode()
method_counts = learn_methods.value_counts()
method_percentage =( method_counts / 89184)*100
method_percentage

# %%
from matplotlib import pyplot as plt
method_percentage = method_percentage.sort_values()
method_percentage.plot(kind='barh')
plt.title('Learning methods')
plt.xlabel('Percentage')
plt.ylabel('learn code Methods')
for index ,value in enumerate(method_percentage):
    plt.text(value,index,f'{value:2f}%',va = 'center')
plt.show()

# %%
data


# %%
online_methods = data['LearnCodeOnline'].str.split(';').explode()
online_method_counts = online_methods.value_counts()
online_method_percentage = (online_method_counts/89184)*100
online_method_percentage

# %%
from matplotlib import pyplot as plt
online_method_percentage = online_method_percentage.sort_values()
online_method_percentage.plot(kind='barh')
plt.title(' Online Learning methods')
plt.xlabel('Percentage')
plt.ylabel('learn code  Online Methods')
for index ,value in enumerate(online_method_percentage):
    plt.text(value,index,f'{value:2f}%',va = 'center')
plt.show()

# %%
data


# %%
online_platform_responses = data[data['LearnCodeCoursesCert']!=np.nan]
response_count = online_platform_responses['LearnCodeCoursesCert'].count()
online_platform = data['LearnCodeCoursesCert'].str.split(";").explode()
online_platform_counts = online_platform.value_counts()
online_platform_percentage = (online_platform_counts/response_count)*100
online_platform_percentage

# %%
from matplotlib import pyplot as plt
online_platform_percentage = online_platform_percentage.sort_values()
online_platform_percentage.plot(kind='barh')
plt.title(' Online Platforms')
plt.xlabel('Percentage')
plt.ylabel('learn code  Online Methods')
for index ,value in enumerate(online_platform_percentage):
    plt.text(value,index,f'{value:2f}%',va = 'center')
plt.show()

# %%

