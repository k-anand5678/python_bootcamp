#Variables - that can have multiple values - x , y ,c 
# Constant - do not change their values -- 3 , 6,,7.8 


# variable_name = values 
# x = 5

# If we have to print it 100 times
#Frist case: 1 - directly printing thre message without storing in a variable
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")

# Second case : printing the message by storing in a variable
# message = "Hello"
message = "Python"
# print(message)
# print(message)
# print(message)
# print(message)
# print(message)
# print(message)
print("Hello")
print(message)

# indentation - Python is very strict about indentation

# 1 tab  = 4 spaces  --- tab is preferred

# variables can be ressigned 
print(message)
message = "No Python"
print(message)

# code executes in Top to bottom manner 

x = 300
print(x)
x = 400
print(x)
print(x+500)     #900

y = 45.78
print(y)

z = 300 + y   #345.78 
print(z+10)    #345.78 +10 = 355.78
y = 50
z = 300 + y
print(z) 


z = 300 + y*10   #300 + 457.8
print(z+1)       # 758.8




