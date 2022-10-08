# 🚨 Inputting your current age 👇
age = input("What is your current age? ")

# print(type(age))
# type conversion from string to interger
age_int = int(age)
remaining_years = 90 - age_int
remaing_days = remaining_years * 365
remaing_weeks = remaining_years * 52
remaing_months = remaining_years * 12

print(f"You have {remaing_days}  days, {remaing_weeks} weeks, and {remaing_months} months left.")


