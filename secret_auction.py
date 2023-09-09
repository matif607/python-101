bids = {}
bidding_finished = False

def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  #bidding_record = {"Atif": "123", "Anas": "540"}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      bid_amount = highest_bid
      winner = bidder
  print("winner is {}".format(winner))
    

while not bidding_finished:
  name = input("What is your name?:\n")
  price = int(input("your bid price?: $"))
  bids[name] = price
  #take user input whether bidding finished or not
  should_continue = input("Are there any other bidders? type 'yes' or 'no'\n")
  if should_continue == "no":
    bidding_finished = True
    highest_bidder(bids)
