x = float(input("Enter your height(m): "))
y = float(input("Enter your weight(kg): "))

process = y / x ** 2 

if process == 18.5: 
    print (f"your bmi is normal {process}.")
    
elif process > 18.5:
    print (f"your bmi is obese {process}.")
    
else:
    print (f"your bmi is underweight {process}.")
