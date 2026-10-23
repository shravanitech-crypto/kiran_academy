balance = 5000
amount= int(input("Enter the amout to pay:"))

if amount > 0 :
    if amount < balance:
        balance -= amount
        print("Payment successful. Remaining balance:", balance)
    elif amount==balance:
        print("Payment Successful, account khali haiiiii")
    else:
        print("Insufficient balance. Payment failed.")
else:
    print("Invalid amount. Payment failed.")