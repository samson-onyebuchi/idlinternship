def main():
    amount = input("Enter the amount you want to pay: ")
    duration = input("Enter duration: ")
    service = amount_and_duration(amount,duration)
    print (f"Your charge for #{amount} for {duration} is {service}")

def amount_and_duration(amount, duration):
    if duration == "12" and amount == 12000:
        service_charge = "#200"

    elif duration == "6" and amount == 6000:
        service_charge = "#100"

    elif duration == "3" and amount == 3000:
        service_charge = "50"

    elif duration == "1" and amount == 1000:
        service_charge = "25"

    elif duration == "12" and amount == 50000:
        service_charge = "300"

    else:
        service_charge = None

    return service_charge

main()