while True:
    user_year = input("Enter your year of birth: ")
    year = int(user_year)

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"{user_year} is a leap year.")
    else:
        print(f"{user_year} is not a leap year.")
