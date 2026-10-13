# def cot(num):
#     if num==0:
#         return 0
#     return num%10 +cot(num//10)




# creating dictionary

# d = {"Name":"rohan","Roll no.":"55","Course":"BCA","Mob":"1234"}

# print(type(d))
# print(list(d))
# print(list(d.values()))
# print(d.items())

# tuple=(('Name', 'rohan'), ('Roll no.', '55'), ('Course', 'BCA'), ('Mob', '1234'))
# list1=[('Name', 'rohan'), ('Roll no.', '55'), ('Course', 'BCA'), ('Mob', '1234')]
# list2=[['Name', 'rohan'], ['Roll no.', '55'], ['Course', 'BCA'], ['Mob', '1234']]

# print("tuple=",dict(tuple))
# print("list1=",dict(list1))
# print("list2=",dict(list2))
# key = list(d.keys())
# print(key[0],d[key[0]])
# print(key[1],d[key[1]])
# print(key[2],d[key[2]])
# print(key[3],d[key[3]])
# d = {"Name":"rohan","Roll no.":"55","Course":"BCA","Mob":"1234"}
# print(d.keys())
# def item(d,i):
#     key=list(d.keys())
#     return {key[i]}:{d[key[i]]}

# print(item(d,0))


my_dict = {}
my_dict["Name"]=input("enter your name: ")
my_dict["Course"]=input("enter your course: ")
my_dict["Roll number"]=input("enter your roll number: ")
my_dict["Mobile no"]=input("enter your mobile number: ")
my_dict["Age"]=input("enter your age: ")
my_dict["Address"]=input("enter your address: ")
my_dict["Dist"]=input("enter your distric: ")
my_dict["Reg no"]=input("enter your registatiion number: ")
my_dict["High School %"]=input("enter your high school %: ")
my_dict["Intermediate %"]=input("enter your intgermediate%: ")
my_dict["Pass Out In"]=input("enter your pass out in?: ")




# print("keys=",my_dict.keys())
# print("values=",my_dict.values())
# print("items=",my_dict.items())

print("\n===Student detail===")

for key,value in my_dict.items():
    print(key,";",value)









