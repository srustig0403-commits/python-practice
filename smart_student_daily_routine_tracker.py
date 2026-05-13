# File Name: smart_student_daily_routine_tracker.py

print('----------- Smart Student Daily Routine Tracker -------------')

# Student Details
details = {
    'name': 'srusti',
    'branch': 'cse',
    'clg_name': 'bitm'
}

print(details['name'])
print(details['branch'])
print(details['clg_name'])

# Subjects List
subjects = ['physics', 'chemistry', 'biology', 'kannada']

print('first subject:', subjects[0])
print('last subject:', subjects[3])
print('total subjects:', len(subjects))

# Add New Subject
subjects.append('english')
print('updated subjects:', subjects)

# Remove Subject
subjects.remove('kannada')
print('after removing subject:', subjects)

# Loop
print('\nSubjects Studied:')
for i in subjects:
    print(i)

# Study Hours Dictionary
study_hours = {
    'physics': 3,
    'chemistry': 2,
    'kannada': 1,
    'biology': 3
}

print(study_hours.values())

# Total Study Hours
total_study_hours = sum(study_hours.values())
print('total studied hours are:', total_study_hours)

# Target Checking
target = 6

if total_study_hours > target:
    print('excellent')
else:
    print('need improvement')

# Attendance
attendance = 80

if attendance < 75:
    print('you need to attend class')
else:
    print('good attendance')

# Set
unique_subjects = set(subjects)
print('unique subjects:', unique_subjects)

# String Indexing and Slicing
print('first letter of student name:', details['name'][0])
print('first 3 letters of college name:', details['clg_name'][0:3])

# Motivational Quote
quote = "Consistency beats talent"
print('quote:', quote)

# Final Summary
print('\n----------- Final Summary -------------')
print('student name:', details['name'])
print('branch:', details['branch'])
print('college:', details['clg_name'])
print('subjects:', subjects)
print('total study hours:', total_study_hours)
print('attendance:', attendance)
print('quote:', quote)
print('thank you')
