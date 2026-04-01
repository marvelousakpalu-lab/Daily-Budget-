# Daily Spending Tracker

# Input: Ask user for total budget
total_budget = float(input("Enter your total budget for the day: $"))

# Input: Ask for three separate items
item1_cost = float(input("Enter the cost of item 1 (e.g., lunch): $"))
item2_cost = float(input("Enter the cost of item 2 (e.g., transport): $"))
item3_cost = float(input("Enter the cost of item 3 (e.g., data): $"))

# Calculation: Calculate total spent
total_spent = item1_cost + item2_cost + item3_cost

# Calculation: Calculate remaining balance
remaining_balance = total_budget - total_spent

# Output: Display the results
print("\n" + "="*40)
print("DAILY SPENDING SUMMARY")
print("="*40)
print(f"Total Budget: ${total_budget:.2f}")
print(f"Item 1 Cost: ${item1_cost:.2f}")
print(f"Item 2 Cost: ${item2_cost:.2f}")
print(f"Item 3 Cost: ${item3_cost:.2f}")
print(f"Total Spent: ${total_spent:.2f}")
print(f"Remaining Balance: ${remaining_balance:.2f}")
print("="*40)

# Logic (Bonus): Check if budget exceeded
if remaining_balance < 0:
    print("⚠️  Warning: You have exceeded your budget!")
    print(f"You are over budget by: ${abs(remaining_balance):.2f}")
else:
    print("✓ You are within budget!")
print("="*40)
