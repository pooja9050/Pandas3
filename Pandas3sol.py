#1873. Calculate Special Bonus
#List[]
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    mylist = []
    for i in range(len(employees)):
        e_id = employees['employee_id'][i]
        name = employees['name'][i]
        if(e_id % 2 != 0) & (name[0] != 'M'):
            mylist.append([e_id, employees['salary'][i]])
        else:
            mylist.append([e_id,0])
    return pd.DataFrame(mylist, columns=['employee_id','bonus']).sort_values(['employee_id'])


#Alternative
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    for i in range(len(employees)):
        e_id = employees['employee_id'][i]
        name = employees['name'][i]
        if((e_id % 2 ==0) or (name[0] =='M')):
            employees['salary'][i] = 0

    return employees[['employee_id','salary']].rename(columns={'salary':'bonus'}).sort_values(['employee_id'])


#lambda - vectorization
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda x: x['salary'] if (x['employee_id'] % 2) and not (x['name'].startswith('M')) else 0, axis=1)
    return employees[['employee_id', 'bonus']].sort_values(by=['employee_id'])


#1667. Fix Names in a Table
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str[0].str.upper() + users['name'].str[1:].str.lower()
    return users.sort_values(by = ['user_id'])

#Capitalize()
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    return users.sort_values(by='user_id')

#lambda - vectorization
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].apply(lambda x: x[0].upper() + x[1: ].lower())
    return users.sort_values("user_id")

#1527. Patients With a Condition
import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    result = []
    for i in range(len(patients)):
        name =patients['patient_name'][i]
        pid = patients['patient_id'][i]
        conditions = patients['conditions'][i]
        for condition in conditions.split():
            if(condition.startswith('DIAB1')):
                result.append([pid,name,conditions])
                break
    return pd.DataFrame(result,columns=['patient_id','patient_name','conditions'])

#Using contains
import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    df = patients[(patients['conditions'].str.startswith('DIAB1')) | (patients['conditions'].str.contains('DIAB1'))]
    return df

#regex \b => space
import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[(patients['conditions'].str.contains(r'\bDIAB1'))]

#lambda - vectorization
import pandas as pd

def find_diabetes(x):
    lst = x.split(" ")
    if len([v for v in lst if v.startswith("DIAB1")]) > 0:
        return True
    return False

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    s = patients["conditions"].apply(lambda x: find_diabetes(x))
    return patients[s]
