def main():
    try:
        amount = int(input("Enter the amount you want to pay: "))
        duration = int(input("Enter duration: "))
        service = amount_and_duration(amount,duration)
        charge = round(service)
        print (f"Your charge of #{amount} for {duration} month is {str(charge)}")


    except ValueError as ve:
        print(f"{ve} is not accepted")


def amount_and_duration(amount, duration):
    price = 200/12
    a_month = 1000
    
    if duration <= 24  and  amount <= 24000 and amount == a_month * duration:
        service_charge = duration * price

    elif amount == 50000 and duration == 12:
        service_charge = 300

    else:
        service_charge = "Not in the service range"  

    return service_charge      


main()