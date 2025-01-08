'''students={
    1:{"name": "sandeep","age":20},
    2:{"name":"bharath","age":19},
    3:{"name":"teja","age":18},
    4:{"name":"mushek","age":25},
    5:{"name":"abhi","age":23,},

}
for student_id,details in students.items():
    print(f"Student_id:{student_id},Name:{details['name']},Age:{details['age']}")
'''


import pandas as pd 
screen_time=[2,4,6,8,9,]
sleep_time=[3,4,7,9,14,]
stu_name=['gova','bharath','sai','mushek','ram']
dict1={
    "screen_time":screen_time,
    "Sleep_time":sleep_time,
    "stu_name":stu_name
}
print(dict1)
df=pd.DataFrame(dict1)
print(df)
