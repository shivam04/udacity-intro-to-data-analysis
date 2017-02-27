import unicodecsv

enrollments_filename = '/datasets/ud170/udacity-students/enrollments.csv'

## Longer version of code (replaced with shorter, equivalent version below)

# enrollments = []
# f = open(enrollments_filename, 'rb')
# reader = unicodecsv.DictReader(f)
# for row in reader:
#     enrollments.append(row)
# f.close()

with open(enrollments_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)
    
### Write code similar to the above to load the engagement
### and submission data. The data is stored in files with
### the given filenames. Then print the first row of each
### table to make sure that your code works. You can use the
### "Test Run" button to see the output of your code.

engagement_filename = '/datasets/ud170/udacity-students/daily_engagement.csv'
submissions_filename = '/datasets/ud170/udacity-students/project_submissions.csv'
    
daily_engagement = open(engagement_filename)     # Replace this with your code
project_submissions = open(submissions_filename)  # Replace this with your code
daily_engagement = unicodecsv.DictReader(daily_engagement)

daily_engagement = list(daily_engagement)

print daily_engagement[0]

project_submissions = unicodecsv.DictReader(project_submissions)

project_submissions = list(project_submissions)

print project_submissions[0]