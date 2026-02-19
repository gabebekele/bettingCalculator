# Implied probability
def Implied_Probability():
    unit = float(input("How much is your average bet amount?: "))
    odds = float(input("Odds: "))
    if odds >= 0:
        prob = round(abs(float(100/(odds+100)*100)), 2)
    elif odds < 0:
        prob = round(abs(float(odds/(abs(odds)+100)*100)), 2)
    result = "The implied probability of your bet is {:02.2f}%".format(prob)
    print(result)


# Hedge Calculator
def Hedge_Calculator():
    bet = float(input("Bet Amount: "))
    odds = float(input("Odds: "))
    hedge = float(input("Hedge Odds: "))
    if odds >= 0:
        odds = odds/100
    elif odds < 0:
        odds = 100 / abs(odds)
    if hedge >= 0:
        hedge = hedge/100
    elif hedge < 0:
        hedge = 100/abs(hedge)
    orig_prof = float(odds*bet)
    payout = orig_prof + bet
    x = float(payout/(hedge+1))
    choice = int(input("Select one of the options: \n 1. Even Hedge \n 2. Confidence Based \n 3. Make bet back\n 4. Make bet amount in profit\n"))
    
    if choice == 2:
        truss = int(input("What would you rate your confidence on the hedge out of ten?: "))
        if truss < 5:
            x = (1 - ((5-truss)/10))*x
        elif truss > 5:
            x = (1 + ((truss - 5)/10))*x
    elif choice == 3:
        x = bet / hedge
    elif choice == 4:
        x = (bet * 2)/hedge
    
    print("\nResults-----------------------")
    print("Hedge Amount:", round(x, 2))
    orig = (bet * odds) - x
    hedge_pay = (x * hedge) - bet
    print("Profit if original wins: ", round(orig, 2))
    print("Profit if hedge wins: ", round(hedge_pay, 2))
   
# Bet Suggestor
# def Bet_Suggestor():