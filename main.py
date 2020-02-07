helloString = "Hello World"
fruits = ["apple", "orange", "banana", "mango"]
student = { "name":"Mary","id":"8776", "major": "CS" }



fruits = [ "apple" , "orange" , "banana" , "mango" ]
i=0
for item in fruits:
    print("Fruit-%d: %s" % (i,item))


students={
"1": {"name": "Bob", "grade": 2.5},
"2": {"name": "Mary", "grade": 3.5},
"3": {"name": "David", "grade": 4.2},
"4": {"name": "John", "grade": 4.1},
"5": {"name": "Alex", "grade": 3.8}
}

def averageGrade(students): 
    # "This functions computes the average grade"
    sum = 0.0
    for key in students:
        sum = sum + students[key]["grade"]
        average = sum/len(students)
    return average
avg = averageGrade(students)
print("The average garde is: %0.2f" % avg)


#Default Arguments
def displayFruits(fruits=["apple","orange"]):
    print( "There are %d fruits in the list" % (len(fruits)))
for item in fruits:
    print(item)
#Using default arguments
displayFruits()
fruits = ["banana", "pear", "mango"]
displayFruits(fruits)



def displayFruits(fruits):
    print( "There are %d fruits in the list" % (len(fruits)))
    for item in fruits:
        print( item)
    print( "Adding one more fruit")
    fruits.append("mango")

fruits = ["banana", "pear", "apple"]
displayFruits(fruits)

#Adding one more fruit
print( "There are %d fruits in the list" % len(fruits))


#Keyword Arguments
def printStudentRecords(name,age=20,major="CS"):
    print( "Name: " + name)
    print( "Age: " + str(age))
    print( "Major: " + major)
printStudentRecords(name="Alex")



#Variable Length Arguments
def student(name, *varargs):
    print( "Student Name: " + name)
    for item in varargs:
        print (item)
student("Nav")

student("Amy", "Age: 24")

student("Bob", "Age: 20", "Major: CS")



#Modules
import student
student.printRecords(students)