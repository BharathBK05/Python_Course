from functions import summation #Local Modules
from functions import percentage #Local Modules
import math #Standard Modules
import json #Standard Modules

marks_list = {
            "Ram":
                    {
                    "Physics":100,
                    "Chemistry":98,
                    "Maths":97
                    },
            "Raj":
                    {
                    "Physics":97,
                    "Chemistry":99,
                    "Maths":93 
                    }
            }

output_dict = {}
for student in marks_list:
    # s = marks_list[student]
    # physics = s['Physics']
    physics = marks_list[student]['Physics']
    chemistry = marks_list[student]['Chemistry']
    maths = marks_list[student]['Maths']

    total = summation(physics,chemistry,maths)
    percent = percentage(total,300)
    output_dict[student] = percent
    print("Done")

l = []
for stu in output_dict:
    if len(l):
        if output_dict[stu] > output_dict[l[0]]:
            l.append(stu)[0]
        else:
            l.append(stu)
    else:
        l.append(stu) 

print("Rank")
print(l)
     
    