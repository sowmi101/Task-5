your_age = int(input("Enter your age:"))
my_age = int(input("Enter your age:"))
if my_age < your_age:
    age_diff = your_age - my_age
    if age_diff == 1:
       print(f"I am {age_diff} year younger than you.")
    else:
       print(f"I am {age_diff} year older than you.")
elif my_age > your_age:
    age_diff = my_age - your_age
    if age_diff == 1:
       print(f" I am {age_diff} year younger than you.")
    else:
       print(f" I am {age_diff} year older than you.")
else:
       print("We are the same age!")