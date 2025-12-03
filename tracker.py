#name hitesh
#roll no 2501060090
#section b
print("Welcome to Daily Calorie Tracker!")

meals = []
calories = []

count = int(input("How many meals did you eat today? "))

for i in range(count):
    meal = input("Enter meal name: ")
    cal = float(input("Enter calories for this meal: "))
    
    meals.append(meal)
    calories.append(cal)

total = sum(calories)
avg = total / count

limit = float(input("Enter your daily calorie limit: "))

print("\n----- Calorie Report -----")
print("Meal Name    Calories")
print("------------------------")
for i in range(count):
    print(meals[i], "   ", calories[i])

print("------------------------")
print("Total Calories: ", total)
print("Average Per Meal: ", round(avg, 2))

if total > limit:
    print("Warning: You exceeded your daily limit!")
else:
    print("You are within your daily calorie limit.")