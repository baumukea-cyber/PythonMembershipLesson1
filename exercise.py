balance = 1000
minimum_balance = 200

balance_withdraw = balance - minimum_balance 

withdrawal_amount = int(input("Enter the amount to withdraw: "))


if withdrawal_amount <= balance_withdraw:
    print("Withdrawal successful.")
    
else:
    print("Insufficient funds. Withdrawal failed.")
    