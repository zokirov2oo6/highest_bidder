print(r"""
                         ___________
                         \         /
                          )_______(
                          |"|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"(
                         /_________                         `'-------'`
                       .-------------.
                   jgs/_______________


""")

def highest_bidder (bidding_dictionary):
    winner=""
    highest_bidder=0
    for bidder in bidding_dictionary :
        bid_amount=bidding_dictionary[bidder]
        if bid_amount > highest_bidder :
            highest_bidder=bid_amount
            winner=bidder
    print(f"The winner is {winner} with highest bid amount {highest_bidder}")


bids={}

should_continue = True
while should_continue:
    name = input("Enter your name: ")
    price = int(input("What is your bid ?  "))
    bids[name] = price
    should_continue = input("Are there any other bidders ? type 'yes' or 'no' ").lower()
    if should_continue == "no":
        should_continue = False  # <-- shu yerda to'g'riladik
        highest_bidder(bids)
    elif should_continue == "yes":
        print("\n"*100)