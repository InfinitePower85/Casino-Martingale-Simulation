import random 
def roll_fair():
    # return reward 
    r = random.randint(1, 38)
    if r % 2 == 1:
        return 1
    return 0

def roll_american():
    r = random.randint(1, 40)
    if r >= 39: # two losses for americans 
        return 0
    if r % 2 == 1:
        return 1
    return 0

def roll_european():
    r = random.randint(1, 40)
    if r == 39:
        return 0
    if r % 2 == 1:
        return 1
    return 0
    
def martingale(init, rounds, bet_fxn, max_bet = -1, debug=False):
    # set the maximum to 500 or smmething 
    win = 0
    tot = 0
    currBet = init 
    for _ in range(rounds):
        if debug:
            print("currBet", currBet, "Total", tot, "win" if win > 0 else "loss")
        win = bet_fxn()
        if not win:
            tot -= currBet 
            currBet *= 2 # under a loss, we will bet the lost amount times 2 
            if max_bet > 0 and currBet > max_bet:
                if debug:
                    print("OH NOOOO, MAXIMUM MONEY LIMIT REACHED!!! YOU LOST MONEY!!!") 
                currBet = max_bet
        else:
            tot += currBet 
            currBet = init 
    print("Total won/lost:", tot)

martingale(2, 10000, roll_fair) # after 100 rounds, we won $196 and are $6 down the current round 
print("=============================================== Nerf Martingale")
martingale(2, 10000, roll_fair, max_bet=500) # lost $1400 on the nerfed martingale, crazy. this isn't even american style!!!
print("=============================================== Nerf V2")
martingale(2, 10000, roll_american, max_bet=500) # double nerf martingale 
# you can still lose money after 100 rounds lol, best to take the guarenteed money while you're up
# after all, the $2 really doesn't guard against mass losses. Any savings can be wiped out pretty quickly 
# sometimes you get lucky, but other times, you will lose. 