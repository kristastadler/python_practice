TICKET_PRICE = 10
tickets_remaining = 100

while tickets_remaining >= 1:

    print("Tickets Remaining: {}".format(tickets_remaining))
    name = input("What is your name? ")
    number_of_tickets = input("How many tickets would you like, {}? ".format(name))
    try:
        number_of_tickets = int(number_of_tickets)
        if number_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining.".format(tickets_remaining))
    except ValueError as err:
        print("Oh no! We ran into an issue. {}".format(err))
    else:
        price = (number_of_tickets * TICKET_PRICE)
        print("That will cost ${}".format(price))
        should_proceed = input("Would you like to proceed? Y/N? ")
        if should_proceed.lower() == "y":
            print("SOLD!")
            tickets_remaining -= number_of_tickets
            #TODO: Gather credit card information and process it.
        else:
            print("Thank you, {}".format(name))

print("Tickets are sold out.")
