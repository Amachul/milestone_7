import datetime

monthes_dict = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

def read_db(filename_:str)->list:
    database = []
    with open(filename_, 'r') as file:
        for line in file.readlines():
            if line != '\n':
                item = line.strip().split(',')
                database.append(dict(name=item[0], hiring_date=item[1], department=item[2],
                                     birthday=item[3]))
    return database

def get_bd_list_by_month(mon:int, database:list)->dict:
    employees = []
    for item in database:
        bdate = item.get("birthday")
        month = int(bdate[bdate.index("-")+1:bdate.index("-")+3])
        if mon == month:
            employees.append(item)
    return split_by_dept(employees)

def get_anniv_list_by_month(mon:int, database:list)->dict:
    employees = []
    for item in database:
        bdate = item.get("hiring_date")
        month = int(bdate[bdate.index("-") + 1:bdate.index("-") + 3])
        year = int(bdate[:bdate.index("-")])
        if mon == month and (datetime.datetime.now().year - year) % 10 == 0:
            employees.append(item)
    return split_by_dept(employees)

# {
#         "total": <amount>
#         "departments":{
#             <dept_name>:{
#               "total": <amount>
#               "employees":[
#                   {"id": 1, "name": "John Doe", "birthday": "Apr 18"}
#                ]
#         }
#      }
def split_by_dept(empl_list:list)->dict:
    bd_dict = {'total': len(empl_list), 'departments':{}}
    for item in empl_list:
        if item.get("department") in bd_dict["departments"].keys():
            dept = bd_dict["departments"].get(item.get("department"))
            dept['employees'].append(item)
            dept['total'] = len(dept['employees'])
            # bd_dict.update({item.get("department"): l})
        else:
            bd_dict["departments"][item.get("department")] = {"total":1, "employees":[item]}
    return bd_dict

# {
#     "birthdays":{...}
#     "anniversaries":{...}
# }
def execute_report(filename_:str, month_:str):
    report = dict()
    database = read_db(filename_)
    month = monthes_dict.get(month_.capitalize())
    report["birthdays"] = get_bd_list_by_month(month, database)
    report["anniversaries"] = get_anniv_list_by_month(month, database)
    return report

def execute_report_for_dept(filename_:str, month_:str, dept_:str):
   report = execute_report(filename_, month_)
   report["birthdays"] = report["birthdays"]['departments'].get(dept_)
   report["anniversaries"] = report["anniversaries"]['departments'].get(dept_)
   return report
