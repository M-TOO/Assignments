class DateCalculator:

    def __init__(self, day, month, year):
        self.original_year = year
        self.month = month
        self.day = day
        self.year = year

        # Adjust January and February
        if month == 1 or month == 2:
            self.month = month + 12
            self.year = year - 1

    def calculate_day(self):
        q = self.day
        m = self.month
        K = self.year % 100
        J = self.year // 100

        h =( q+((13*(m+1))//5)+K+(K//4)+(J//4)+(5*J))%7

        days = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
        return days[h]


try:
    print("Please write the date in numeric form!!")
    day = int(input("Enter the Day: "))
    month = int(input("Enter the Month: "))
    year = int(input("Enter the Year: "))

    # Instantiate the class with correct argument order
    calculator = DateCalculator(day, month, year)
    weekday = calculator.calculate_day()
    print(f"\nThe date {day}/{month}/{year} falls on a: {weekday}")

except ValueError:
    print("Please enter valid numeric values for day, month, and year.")