from pathlib import Path

def get_cats_info(path):
    cats_list =[]
    
    try:
        with open(path,'r',encoding='utf-8') as file:
            for line in file:
                id, name, age = line.strip().split(',')
                cat_dict = {'id':id,'name':name,'age':age}
                cats_list.append(cat_dict)
                

        return cats_list


    except FileNotFoundError:
        print('file was not found')

for i in get_cats_info('info_cats.txt'):
    print(i)