
students={ "1": {"name": "Bob", "grade": 2.5},
"2": {"name": "Mary", "grade": 3.5},
"3": {"name": "David", "grade": 4.2},
"4": {"name": "John", "grade": 4.1},
"5": {"name": "Alex", "grade": 3.8}}

def averageGrade(students): 
    # "This functions computes the average grade"
    sum = 0.0
    for key in students:
        sum = sum + students[key]["grade"]
        average = sum/len(students)
    return average
avg = averageGrade(students)
print("The average garde is: %0.2f" % avg)