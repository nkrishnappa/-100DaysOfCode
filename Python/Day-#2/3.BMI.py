# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
def BodyMassIndex(weight, height):
#    return int(weight)//(float(height) ** 2)
    return round(int(weight)/(float(height) ** 2), 2)

print(BodyMassIndex(weight, height))