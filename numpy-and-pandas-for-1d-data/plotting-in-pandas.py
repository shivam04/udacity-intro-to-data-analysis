import pandas as pd
import seaborn as sns

# The following code reads all the Gapminder data into Pandas DataFrames. You'll
# learn about DataFrames next lesson.

path = '/datasets/ud170/gapminder/'
employment = pd.read_csv(path + 'employment_above_15.csv', index_col='Country')
female_completion = pd.read_csv(path + 'female_completion_rate.csv', index_col='Country')
male_completion = pd.read_csv(path + 'male_completion_rate.csv', index_col='Country')
life_expectancy = pd.read_csv(path + 'life_expectancy.csv', index_col='Country')
gdp = pd.read_csv(path + 'gdp_per_capita.csv', index_col='Country')

# The following code creates a Pandas Series for each variable for the United States.
# You can change the string 'United States' to a country of your choice.

employment_us = employment.loc['United States']
female_completion_us = female_completion.loc['United States']
male_completion_us = male_completion.loc['United States']
life_expectancy_us = life_expectancy.loc['United States']
gdp_us = gdp.loc['United States']
#print female_completion_us.index
# Uncomment the following line of code to see the available country names
print employment_us.plot()
#print female_completion_us.plot()
#print life_expectancy_us.plot()
#print gdp_us.plot()
#idx = employment.index.values

#female_completion_us = pd.Series(female_completion_us,index=idx)
#male_completion_us = pd.Series(male_completion_us,index=idx)
#life_expectancy_us = pd.Series(life_expectancy_us,index=idx)
#gdp_us = pd.Series(gdp_us,index=idx)

# the country of your choice. You will only be able to display one plot at a time
# with each "Test Run".