from art import logo

print(logo)
print("๐ฐWELCOME TO THE SECRET AUCTION PROGRAM ๐ฐ")

bidders_dictionary = {}
end_the_bid = False


while not end_the_bid:
    name = input("What is your name ?\n")
    bid = int(input("Can we know the bid amount ?\n$"))

    bidders_dictionary[name] = bid
    # Another way of updating the dictionary ๐๐ป
    # bidders_dictionary.update({name:bid}) #Instead of line 14 you can use this code on line 16

    bid_interest = input("Anyone else interested in bidding(yes/no) ? ")
    if bid_interest.lower() != "yes":
        end_the_bid = True
        high_bid = max(bidders_dictionary,key=bidders_dictionary.get)
        print(f'๐The winner is "{high_bid}" with a bid of "๐ฒ{bidders_dictionary[high_bid]}" ๐')
