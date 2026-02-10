amount_due = 50
while amount_due>0:
    print(f"amount_due: {amount_due}")
    payment = input("insert coin: ")
    payment = int(payment)
    if payment in[25,5,10]:
        #amount_due = amount_due-payment
        amount_due -= payment
    else:
        continue
    print(f"chnage owed:{amount_due}")