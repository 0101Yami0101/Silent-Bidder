#A silent bidding system
from art import logo
from replit import clear

clear()  #To clear screen before running of program
print(logo)


biddings = {}

bidding_continue = True #Flag

while bidding_continue:
   bidder = input("Enter Your Name : \n")
   amount = int(input("Enter the amount you want to bid in $ \n"))

   biddings.update([(bidder, amount)]) #Update data to dictionary

   #Condition to run loop
   if_continue = input("Do you want to pass to the next bidder- 'yes'' or 'no' \n").lower()
   if if_continue == "no":
      bidding_continue = False
   else:
      clear() #Clear screen for next entry

highest_bidder = [] 
highest_bid = 0  #to find highest bidding value

for key in biddings:
   if biddings[key] > highest_bid:
      highest_bidder = key #Add key name to highest_bidder list if it has higher value
      highest_bid = biddings[key] #Assign new value to highest_bid variable if it is higher
  

print(biddings)
print(f"Highest bid is ${highest_bid} and bidder is {highest_bidder}") #result