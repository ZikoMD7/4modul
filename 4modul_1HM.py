from pathlib import Path



def total_salary(path):
    
    try:
        with open(path,"r",encoding='utf-8') as file:
            
            salary_list = list() 

            for item in file.readlines():
                salary_list.append(item.strip().split(','))

            total_salary = 0

            for item in salary_list:
                total_salary +=int(item[1])

            count_employees = len(salary_list)  
            average = total_salary//count_employees

        return total_salary, average           
    
    except FileNotFoundError:
        print('file was not founded')

total, average = total_salary("Salary_employees/salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
