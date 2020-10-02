TICKET_PRICE = 10
tickets_remaining = 100

print("Tickets Remaining: {}".format(tickets_remaining))
name = input("What is your name? ")

number_of_tickets = input("How many tickets would you like, {}? ".format(name))
number_of_tickets = int(number_of_tickets)
price = (number_of_tickets * TICKET_PRICE)
print("That will cost ${}".format(price))
