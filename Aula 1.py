import csv
import pprint
from datetime import datetime as dt
import numpy as np

enrollments = []
dailyEngagement = []
projectSubmissons = []

enrollment_filename = 'C:\Users\Usuario\Desktop\Data\enrollments.csv'
dailyEngagement_filename = 'C:\Users\Usuario\Desktop\Data\daily_engagement.csv'
projectSubmissions_filename = 'C:\Users\Usuario\Desktop\Data\project_submissions.csv'

def read_csv(filename): # Opening CSV file
    with open(filename, 'rb') as f:
        reader = csv.DictReader(f)
        return list(reader)

def parse_date(date): #Transforming Str data in date data
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')

def parse_maybe_int(i): #Transforming str data to Integer data
    if i == '':
        return None
    else:
        return int(i)


enrollments = read_csv(enrollment_filename) #Variable is getting the data from the file
dailyEngagement = read_csv(dailyEngagement_filename) #Variable is getting the data from the file
projectSubmissons = read_csv(projectSubmissions_filename) #Variable is getting the data from the file

#Data Wrangle - Cleaning data
for enrollment in enrollments:
    enrollment['account_key'] = parse_maybe_int(enrollment['account_key'])
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled']=='True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])

#Data Wrangle - Cleaning data
for engagement in dailyEngagement:
    engagement['lessons_completed'] = int(float(engagement['lessons_completed']))
    engagement['num_courses_visited'] = int(float(engagement['num_courses_visited']))
    engagement['projects_completed'] = int(float(engagement['projects_completed']))
    engagement['total_minutes_visited'] = float(engagement['total_minutes_visited'])
    engagement['utc_date'] = parse_date(engagement['utc_date'])

#Data Wrangle - Cleaning data
for submissions in projectSubmissons:
    submissions['completion_date'] = parse_date(submissions['completion_date'])
    submissions['creation_date'] = parse_date(submissions['creation_date'])

#Data Wrangle - Cleaning data
#Changing the record named acct to account_key in order to keep it according to the other records
for engagement_record in dailyEngagement:
    engagement_record['account_key'] = engagement_record['acct']
    del[engagement_record['acct']]

#Data exploration - Making a set of account keys in the CSV file
len(enrollments) #Returning a number of items for the object
unique_enrolled_students = set() #Creating a variable type set

for enrollment in enrollments:
    unique_enrolled_students.add(enrollment['account_key'])#Adding the account Keys to the set of account keys
len(unique_enrolled_students)#Returning a number of items for the object

#Data exploration - Making a set of acct in the CSV file
len(dailyEngagement) #Returning a number of items for the object

unique_engagement_students = set()#Creating a variable type set
for engagement_record in dailyEngagement:
    unique_engagement_students.add(engagement_record['account_key'])#Adding the acct Keys to the set of acc keys
len(unique_engagement_students)#Returning a number of items for the object

#Data exploration - Making a set of account_key in the CSV file

len(projectSubmissons) #Returning a number of items for the object

unique_project_submitters = set() #Creating a variable type set
for submission in projectSubmissons:
    unique_project_submitters.add(submission['account_key']) #Adding the account Keys to the set of account keys
len(unique_project_submitters) #Returning a number of items for the object

'''
print('Quantidade de alunos matriculados: ', len(unique_enrolled_students))
print('Quantidade de alunos envolvidos: ', len(unique_engagement_students))
print(len(unique_enrolled_students)-len(unique_engagement_students))
'''

'''
for enrollment in enrollments:
    students = enrollment['account_key']
    if students not in unique_engagement_students:
        print enrollment
        break
'''



#Data exploration - Searching for issues with the data
#Conditional to get the students out of the set unique_engagement_students and with the join date different from the cancel date
num_problem_students = 0
for enrollment in enrollments:
    students = enrollment['account_key']
    if students not in unique_engagement_students \
            and enrollment['join_date'] != enrollment['cancel_date']:
        num_problem_students += 1
        #print enrollment

#print('Problem students: ', num_problem_students)

#Conditional to get the udacity test accounts
udacity_test_account = set()
for enrollment in enrollments:
    if enrollment['is_udacity']:
        udacity_test_account.add(enrollment['account_key'])
len(udacity_test_account)

#print('test account: ', udacity_test_account)

#This function will delete every udacity test account
def remove_udacity_accounts(data):
    non_udacity_data = []
    for data_point in data:
        if data_point['account_key'] not in udacity_test_account :
            non_udacity_data.append(data_point)
    return non_udacity_data

#Creating variables passing them through the function remove_udacity_account
#So in these variables below, we are not going to have any udacity test account
non_udacity_enrollment = remove_udacity_accounts(enrollments)
non_udacity_engagement = remove_udacity_accounts(dailyEngagement)
non_udacity_submissions = remove_udacity_accounts(projectSubmissons)
'''
print('Non udacity enrolled: ',len(non_udacity_enrollment))
print('Non udacity engaged: ',len(non_udacity_engagement))
print('Non udacity submitted: ',len(non_udacity_submissions))
'''
#Creating a dictionary
paid_students = {}

#Creating a condition to add some values in the dictionary above
#Add the account keys that is not with canceled status and the days to cancel the course were more than 7 to the dictionary
#Also, there is one more conditional that add the most updated values to the dictionary
#The main reason to create this dictionary was to get all real paid accounts

for enrollment in non_udacity_enrollment:
    if(not enrollment['is_canceled'] or
            enrollment['days_to_cancel']>7):
        account_key = enrollment['account_key']
        enrollment_date = enrollment['join_date']

        if (account_key not in paid_students  or enrollment_date > paid_students[account_key]):
            paid_students[account_key] = enrollment_date


len(paid_students)

#print('Paid_Students: ',len(paid_students))

#This function returns all accounts created within one week

def within_one_week(join_date,engagement_date):
    time_delta = engagement_date - join_date
    return time_delta < 7

#This function removes all free,trial and canceled accounts

def remove_free_trial_cancel(data):
    new_data = []

    for data_point in data:
        if data_point['account_key']in paid_students:
            new_data.append(data_point)

    return new_data

pprint.pprint(non_udacity_engagement[57])
pprint.pprint(non_udacity_enrollment[5])

#paid_enrollments = remove_free_trial_cancel(non_udacity_enrollment)

paid_engagement = remove_free_trial_cancel(non_udacity_engagement)

paid_submissions = remove_free_trial_cancel(non_udacity_submissions)


#print ('Paid enrollments: ',len(paid_enrollments))
print ('Paid Engaged: ', len(paid_engagement))
print ('Paid Submissions: ', len(paid_submissions))

#Below, we will get all paid accounts engaged in the first week



paid_engagement_in_first_week = []

for engagement_record in paid_engagement:
    account_key = engagement_record['account_key']
    join_date = paid_students[account_key]
    engagement_record_date = engagement_record['utc_date']

    if within_one_week(join_date,engagement_record_date):
        paid_engagement_in_first_week.append(engagement_record)

print(len(paid_engagement_in_first_week))



'''
enrollments = read_csv(enrollment_filename)
pprint.pprint(enrollments[0])
'''

'''
dailyEngagement = read_csv(dailyEngagement_filename)
pprint.pprint(dailyEngagement)

'''
'''
projectSubmissons = read_csv(projectSubmissions_filename)
pprint.pprint(projectSubmissons)
'''
