from art import logo

print(logo)
print("💰WELCOME TO THE SECRET AUCTION PROGRAM 💰")

bidders_dictionary = {}
end_the_bid = False


while not end_the_bid:
    name = input("What is your name ?\n")
    bid = int(input("Can we know the bid amount ?\n$"))

    bidders_dictionary[name] = bid

    bid_interest = input("Anyone else interested in bidding(yes/no) ? ")
    if bid_interest.lower() != "yes":
        end_the_bid = True
        high_bid = max(bidders_dictionary,key=bidders_dictionary.get)
        print(f'🎊The winner is "{high_bid}" with a bid of "💲{bidders_dictionary[high_bid]}" 🎊')
