'''
Python Code to Analyze Student Marks.
'''
def analyze_data(list_variable):
    '''
      This method is used to analyze student marks.
    '''
    print("Result Analysis")
    print("---------------")
    print("Number of Students:",len(list_variable))
    print("Average Score:",sum(list_variable)/len(list_variable))
    print("Maximum Score:",max(list_variable))
    print("Minimum Score:",min(list_variable))
def extract_data():
    '''
      This method is used to extract student marks from text file.
    '''
    file = open('data.txt', 'r')
    list_variable1=[]
    for each in file:
        list_variable=[int(i) for i in each.split(',')]
        list_variable1.append(sum(list_variable))
    analyze_data(list_variable1)
def add_student():
    '''
      This method is used to add marks of a new student in to text file.
    '''
    temp_var=[]
    for i in range(4):
        temp_var.append(input(f"Enter Subject {i+1} marks: "))
    file = open('data.txt','a')
    file.write('\n')
    file.write(','.join(temp_var))
    file.close()
    print("Added Successfully.")
print("Student grade Analysis")
print("Choice 1: Add New student marks")
print("Choice 2: Get Analysis")
print("Choice 3: Quit")
N=0
while N!=3:
    N=int(input("Choice: "))
    if N==1:
        add_student()
    elif N==2:
        extract_data()
    elif N==3:
        print("The End")
    else:
        print("Invalid Choice")
