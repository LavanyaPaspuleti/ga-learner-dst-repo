# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
new_record_arr = np.array(new_record)
census = np.concatenate((data, new_record_arr), axis = 0)

data.shape, census.shape, census

# Create new array 'age' by taking only age values from census

age = census[0:,0]
age


# Find the maximum age in the array 'age'
max_age = np.amax(age)
max_age

# Find the min age and store it in a variable called 'min_age'
min_age = np.amin(age)
min_age


# Find the mean age and the standard deviation in age.
age_mean = np.mean(age)
age_mean

# Find the standard deviation of the age and store it in a variable called age_std
age_std = np.std(age)
age_std

#Create four different arrays by subsetting 'census' array by Race column(Race is the column with index 2) #and save them in 'race_0','race_1', 'race_2', 'race_3' and 'race_4' respectively(Meaning: Store the #array where 'race'column has value 0 in 'race_0', so on and so forth)

race_0 = np.array([])
race_1 = np.array([])
race_2 = np.array([])
race_3 = np.array([])
race_4 = np.array([])
for r in census[0:,2]:
    if(r==0):
        race_0 = np.append(race_0, r)
    elif(r==1):
        race_1 = np.append(race_1, r)
    elif(r==2):
        race_2 = np.append(race_2, r)
    elif(r==3):
        race_3 = np.append(race_3, r)
    elif(r==4):
        race_4 = np.append(race_4, r)

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

#Find out which is the race with the minimum no. of citizens

race_count = list([len_0, len_1, len_2, len_3, len_4])
race_count

minority_race = race_count.index(min(race_count))
minority_race

#Create a new subset array called 'senior_citizens' by filtering 'census' according to age>60 (age is the #column with index 0)

senior_citizens = census[census[0:,0] > 60]

# Add all the working hours(working hours is the column with index 6) of 'senior_citizens' and store it #in a variable called 'working_hours_sum'

working_hours_sum = sum(senior_citizens[0:,6])
working_hours_sum

# Find the length of 'senior_citizens' and store it in a variable called 'senior_citizens_len'

len(senior_citizens)

# average working hours of the senior citizens by dividing 'working_hours_sum' by 'senior_citizens_len' # and store it in a variable called 'avg_working hours'

avg_working_hours = working_hours_sum / len(senior_citizens)
avg_working_hours

# Create two new subset arrays called 'high' and 'low' by filtering 'census' according to #education-num>10 and education-num<=10 (education-num is the column with index 1) respectively.

high = census[census[0:,1] > 10]
low = census[census[0:,1] <= 10]

# Calculating mean of income for both the subsets
avg_pay_high = round(sum(high[0:,7])/len(high), 2)
avg_pay_low = round(sum(low[0:,7])/len(low), 2)
print(avg_pay_high)
print(avg_pay_low)







