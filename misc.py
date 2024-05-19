

'''for item in employee_data:
    if item['name']=='Mike':
        print('Found')
    else:
        print('No')'''


'''l=list()
word=0
for item in employee_data:
    l.append(item['name'])         # list of dict uses .append
print(l)
l.sort()                           # once list is created then use list functions
print(l)
for val in l:
    print(val)
    if len(val)>4:
        word+=1
print(word)'''


'''a=employee_data[-1]    # force to make a dictionary
print(a)
a['name']='Anushka'     # updating the dictionary
print(a)
print(employee_data)    # automatically updates the list of dictionary'''


'''highest=0
for item in employee_data:              # inside this for loop items is running a dict one by one
    if item['salary']>highest: 
        highest=item['salary']
        person=item['name']
print(person, 'has the highest salary')'''


employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]

















































