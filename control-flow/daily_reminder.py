task=input("Enter your task:")
priority=input("Priority (high/medium/low): ")

time_bound=input("Are you time bound?(yes or no)")

match priority:
    case "high":
        if time_bound=="yes":
            print(task, "is a high priority task that requires immediate attention today!")
        elif time_bound=="no":
             print(task, "is a high priority task. Consider completing it soon!")
        else :
            print("Your time bound value is incorrect")
    
    case "medium":
        if time_bound=="yes":
            print(task, "is a medium priority task that requires immediate attention today!")
        elif time_bound=="no":
             print(task, "is a medium priority task. Consider completing it soon!")
        else :
            print("Your time bound value is incorrect")

    case "low":
        if time_bound=="yes":
            print(task, "is a low priority task that requires immediate attention today!")
        elif time_bound=="no":
             print(task, "is a low priority task. Consider completing it soon!")
        else :
            print("Your time bound value is incorrect")
    case _:
        print("Invalid choice")

# task = input('Enter your task: ')
# priority = input('Priority (high/medium/low): ')
# time_bound = input('Is it time-bound? (yes/no): ')

# match priority:
#     case 'high':
#         if time_bound == "yes":
#             print(f"Reminder: \'{task}\' is a {priority} priority task that requires immediate attention today!")
#         else:
#             print(f"Reminder: \'{task}\' is a {priority} priority task. Consider completing it when you have free time.")
#     case 'medium':
#         if time_bound == "yes":
#             print(f"Note: \'{task}\' is a {priority} priority task that requires immediate attention today!")
#         else:
#             print(f"Note: \'{task}\' is a {priority} priority task. Consider completing it when you have free time.")
#     case 'low':
#         if time_bound == "yes":
#             print(f"Note: \'{task}\' is a {priority} priority task that requires immediate attention today!")
#         else:
#             print(f"Note: \'{task}\' is a {priority} priority task. Consider completing it when you have free time.")

    