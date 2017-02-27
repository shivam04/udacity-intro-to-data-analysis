import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        #print list(reader)[0]
        return list(reader)

enrollments = read_csv('/datasets/ud170/udacity-students/enrollments.csv')
daily_engagement = read_csv('/datasets/ud170/udacity-students/daily_engagement.csv')
project_submissions = read_csv('/datasets/ud170/udacity-students/project_submissions.csv')
    
### For each of these three tables, find the number of rows in the table and
### the number of unique students in the table. To find the number of unique
### students, you might want to create a set of the account keys in each table.

enrollment_num_rows = len(enrollments)     # Replace this with your code
print enrollment_num_rows
enrollment_num_unique_students = 0  # Replace this with your code
jk = set()
for enrollment in enrollments:
    jk.add(int(enrollment['account_key']))
enrollment_num_unique_students = len(jk)    
print enrollment_num_unique_students

engagement_num_rows = len( daily_engagement)    # Replace this with your code
print engagement_num_rows
#print daily_engagement[0]
engagement_num_unique_students = 0  # Replace this with your code
jk = set()
for enrollment in daily_engagement:
    jk.add(int(enrollment['acct']))
engagement_num_unique_students = len(jk)    
print engagement_num_unique_students

submission_num_rows = len( project_submissions)             # Replace this with your code
print submission_num_rows
submission_num_unique_students = 0  # Replace this with your code
jk = set()
for enrollment in project_submissions:
    jk.add(int(enrollment['account_key']))
submission_num_unique_students = len(jk)    
print submission_num_unique_students
