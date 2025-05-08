
def is_leap(year):
    leap=False
    if(year% 4==0 and year %100!=0)or(year %400==0):
        leap=True
    return leap

while True:
    try:
     year=int(input("Enter a year:"))
     print("It's a leap year"if is_leap(year)else "It's not  a leap year.")

    except ValueError:
     print("Invalid input.Enter a valid year")


    while True:
     another=input("Do you want to enter another year(yes/no):")
     if another=='yes':
         break# Go back to the start to do the loop
     elif another=='no':
         print("Okay")
         exit()
     else:
         print("Please enter yes or no.")


