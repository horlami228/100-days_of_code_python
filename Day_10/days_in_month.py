# This program checks if a year is a leap year
# Let us check if the output year is a leap year by performing this operation
# A leap year has an extra day of 366 day in a year with febuarary having 29 days in total

def is_leap_year(year):
    """
    Args:
        year(int): Year to check
    Return:
         True if year is leap year. False otherwise
    """
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    """Get the number of days in a month

    Args: 
        year(char): The year to use
        month(char): The month to use
    Returns:
        return the number of days in the month
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    lenth = len(str(year))
    if lenth > 4 or lenth < 4:
        return "Invalid year"
    if month > 12 or month < 1:
        return "Invalid month"
    if(is_leap_year(year)) == True:
        month_days[1] = 29
    return month_days[month - 1]

"""Ask user for input"""
while(True):
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    days = days_in_month(year, month)
    print(days)
    end_loop = input("Type 'yes' to try again. Type 'no' to end:\n")
    if end_loop in ["no", "NO", "No"]:
        break