height = float(input("enter your hight in m : "))
weight =float(input("enter your weight in kg : "))
bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"your bmi is {bmi} , you're under weight")
elif bmi < 25:
    print(f"your bmi is {bmi} , you're normal weight")
elif bmi < 30:
    print(f"your bmi is {bmi} , you're over weight")
elif bmi < 35:
    print(f"your bmi is {bmi} , you're obese weight")
else:
    print(f"your bmi is {bmi} , you're clinically obese weight")