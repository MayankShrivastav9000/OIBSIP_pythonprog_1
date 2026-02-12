# BMI Calculator

# Step 1: Take input from user
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Step 2: Calculate BMI
bmi = weight / (height * height)

# Step 3: Decide BMI category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Step 4: Display result
print("\nYour BMI is:", round(bmi, 2))
print("BMI Category:", category)
