from art import logo

should_continue = True
bids = {}

# TODO-4: Compare bids in dictionary
def find_highest_bidder(bidding_dictionary):
    best_bid = 0
    best_bidder = ""

    for bidder in bidding_dictionary:
        if int(bidding_dictionary[bidder]) > best_bid:
            best_bid = int(bidding_dictionary[bidder])
            best_bidder = bidder

    print(f"The winner is {best_bidder} with a bid of ${bids[best_bidder]}")
    print(f"All the bidders: {bids}")


print(logo)



while should_continue:
    # TODO-1: Ask the user for input
    name = input("What's your name?: ")
    price = input("What's your bid?: $")

    # TODO-2: Save data into dictionary {name: price}

    bids[name] = price

    # TODO-3: Whether if new bids need to be added

    new_bid = input("Are there any other bidders? Type 'yes' or  'no':\n")

    should_continue = False

    if new_bid == "yes":
        should_continue = True
        print("\n" * 100)

find_highest_bidder(bids)
