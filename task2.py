input_month = input("Enter the amount of money you will save each month: ")
if input_month.isdigit():
    saving_month = int(input_month)
    anual_saving = saving_month * 12
    total_interest = anual_saving * 0.008
    total_anual_saving =  anual_saving + total_interest
    
    print("The total amount of money you will save in a year is:", total_anual_saving)
    
else:
    print("Invalid amount")
