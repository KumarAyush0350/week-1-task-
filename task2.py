input_month = input("Enter the amount of money you will save each month: ")
if input_month.strip().isdigit():
    saving_month = int(input_month)
    anual_saving = saving_month * 12
    total_interest = anual_saving * 0.008
    total_anual_saving =  anual_saving + total_interest
    
    print(f"Total annual savings: £{anual_saving}")
    print(f'Total with interest: £{total_anual_saving:.2f}')
    
else:
    print("Invalid amount")
