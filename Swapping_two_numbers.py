# ------------------------(method-1)-------------------------------
"""using python function"""
num1=23
num2=45
num1,num2=num2,num1
print(num1, num2)

#-------------------------(method-2)---------------------------------
""" with using third variable"""
num3=67
num4=78
temp=num3
num3=num4
num4=temp
print(num3, num4)

#--------------------------(method-3)----------------------------------
""" without using third variable """
num5=66
num6=77
num5=num5+num6
num6=num5-num6
num5=num5-num6
print(num5,num6)

#-------------------------(method-4)-----------------------------
""" with using bitwise operator"""
a,b=13,12
a,b=(a^b)^((a^b)^b),(a^b)^b
print(a,b)

""" other method"""
a=56
b=13
a=a^b
b=a^b
a=a^b
print(a,b)
