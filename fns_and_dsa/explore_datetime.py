import datetime
from datetime import timedelta

def display_current_datetime():
    current_date=datetime.datetime.now()
    print( current_date.strftime("%Y-%m-%d %H:%M:%S "))
    # Ask why return gives nothing

def calculate_future_date():
    now = datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S "))

display_current_datetime()

def calculate_future_date():
    num_of_days = int(input("Enter the number of days to add to the current date:  "))
    current_date = datetime.datetime.now()
    days_to_add = timedelta(days=num_of_days)
    future_date = current_date + days_to_add
    formatted_future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future date: {formatted_future_date}")
calculate_future_date()


# Practice code


# x = datetime.datetime.now()
# print(x)
# from datetime import datetime

# now = datetime.now()
# print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Outputs: "2024-07-31 08:55:44"


# Blessing's code


# import datetime
# from datetime import timedelta

# def display_current_datetime():
#     current_datetime = datetime.datetime.now()
#     formated_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
#     print(f"Current date and time: {formated_datetime}")
# display_current_datetime()

# def calculate_future_date():
#     num_of_days = int(input("Enter the number of days to add to the current date:  "))
#     current_date = datetime.datetime.now()
#     days1 = timedelta(days=num_of_days)
#     future_date = current_date + days1
#     formatted_future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
#     print(f"Future date: {formatted_future_date}")
# calculate_future_date()