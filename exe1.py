for stu in student:
    for i in stu.values():
        if name in i:
            print(stu['mobile'])
            break


        # print('string')
# s={1,2,3,4}
# print(s)
# if 1 in s:
#     print('yes')
# else:
#     print('no')
# s={1,2,3,4,5}
# for s1 in s:
#     print(s1)

# s1={1,2,3,4,5}
# s2={5,6,7,8,9}
# union_set = s1|s2
# print(union_set)
# intersectio_set = s1&s2
# print(intersectio_set)

# string concatentations
# f_name='chetan'
# l_name='patel'
# full_name = f_name +' '+ l_name
# print( full_name)
# print(f_name+str(3))
# print(f_name+'3')
# print(f_name * 3)
# print(3 * f_name)


# user = int(input("enter a number"))
# print(user)
# print(user)

# age = input("enter your age")
# print("your age is" +' ' + age)
 

# no1 = int(input("enter a number"))
# no2 = int(input("enter a second number"))
# total = no1+no2
# print(total)
# str(total)
# # print(total)
# type(no1)

# a=10
# type(a)
# student = {'name':'chetan','city':'pithampur','mobile':9009099090}

# name = input("enter a name to find mobile number")
# if name in student.values():
#     print(student['mobile'])
# else:
#     print('no this persion has no mobile number') 

student = [ {'name':'chetan','city':'pithampur','mobile':'00000000'},
            {'name':'rahul','city':'indore','mobile': '11111111'},
            {'name':'tulsi','city':'pithampur','mobile':'22222222'},
            {'name':'bhawati','city':'mhow','mobile':'3333333333'},
            {'name':'maya','city':'rao','mobile':'44444444444'}
]


name = input("enter a name to find mobile number")

# if 'name' in student[i]:
#     print(student[0]['mobile'])
# else:
#     print('no this persion has no mobile number')    
# # print(student)


# name = input("enter a name to find mobile number")
# for i in student:
#     if name in i:
#         print(student[i]['mobile'])
#     else:
#         print('no this persion has no mobile number') 
# 
# for stu in student: 
#     if name in stu.values():
#         print(student[1]['mobile'])
    # else:
    #     print('no this persion has no mobile number') 

# for stu in student: 
#     for i in stu:
#         if name in stu.values():
#             print(i[0]['mobile'])
#         else:
#             print('no this persion has no mobile number')        

# for stu in student: 
#     for i in stu.values():
#         print(i)
#         if name in i:
#             print(stu['mobile'])
#             break
#         else: 
#             print('no')   
#     break


# stu = {'name':'chetan','mobile':'123456','address':'2323'}
# print(list(stu.values()))
# print(stu['mobile'])
