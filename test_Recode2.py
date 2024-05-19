import Recode2 as RR

def test_range():
    result= [{"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    test=RR.get_employees_by_age_range(38, 45)
    assert(test==result)

def test_salary():
    result=60166.67
    test=round(RR.calculate_average_salary(),2)
    assert(test==result)

def test_departments():
    result=[{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    test=RR.get_employees_by_dept('Engineering')
    assert(test==result)