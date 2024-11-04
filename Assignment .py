# To read
# Functions
# For loops
# List, Dictionaries

# Assignment

student_name =['Sandra', 'Patrica', 'Phiona', 'Anitah'] # strings
student_marks = [80, 56, 75, 90] # integers
data = ['Sandra', 90, 'Kamwokya']
print(student_name)

# Appending an item
# Adding new items at the end of the list
student_name.append('Micheal')
print(student_name)

# Inserting an item
# Adds the items in any position using an index
student_name.insert(2, 'Faith')
print(student_name)



# Assignment 

# Print Paritca Phiona and Anitah.
# Add Masha at the fourth position.
# Update the name Phionah to Phionah Aladinnah.
# Display the length of the students list
# Print all the students names having updated the list using a for loop
# Calculate the total marks for the students marks variables

print(student_name [1:4])

student_name.insert(4,'Masha')
print(student_name)

student_name[2]= 'Phionah Aladinah'
print(student_name)

print(len(student_name))

for name in student_name:
    print(student_name)
    
total_marks =sum(student_marks)
print(total_marks)

