'''Simulate and score popular dice games.'''

import random

def roll(dice=1, seed=None):  
    '''
    Simulate rolling any number of fair 6-sided dice.
    
    Parameters:
        dice (int): Number of dice to roll
        seed (int): Optional seed
        
    Returns:
        list: Result of simulated dice roll
    '''
    
    # set random seed
    random.seed(seed)
    
    # roll dice
    result = random.choices([1,2,3,4,5,6],k=dice)
    
    return result

def dec_to_pct(dec, digits=2):
    '''
    Convert a decimal to a string in percentage format.
    
    Parameters:
        dec (float): Decimal to convert
        digits (int): Digits to round result to
    
    Returns:
        str: Decimal in percentage format
    
    '''
    
    if not isinstance(dec, float):
        raise TypeError("Input must be a decimal")
        
    pct = round(dec*100,digits)
    string = str(pct)+"%"
    
    return string

def farkel_prob(dice=6):  
    '''
    Generate a probability table for scoring in Farkel with a given number of dice.
    
    Parameters:
        dice (int): Number of dice to roll
    
    Returns:
        dictionary: Probability of rolling each point value
    '''
    
    # return error if dice > 6
    if dice > 6:
        raise ValueError("Farkel uses no more than 6 dice. Enter an integer between 1 and 6.")
    
    d = {}
        
    # Farkel
    #   No 1 or 5
    if dice == 1:
        d["Farkel"] = dec_to_pct((4/6))
    #   No 1 or 5
    elif dice == 2:
        d["Farkel"] = dec_to_pct((4/6)**2)
    #   Any combo of 2,3,4,6 except 3 of a kind 
    #   4*3*2 ways to have singles + 4*3*3 ways to have a pair and single)
    elif dice == 3:
        d["Farkel"] = dec_to_pct((4*3*2 + 4*3*3)*(1/6)**3)
    #   Any combo of 2,3,4,6 except 3 or 4 of a kind 
    #   (4! ways to have singles + 6*6 ways to have two pairs + 4*3*6*2 ways to have a pair and two singles)
    elif dice == 4:
        d["Farkel"] = dec_to_pct((4*3*2 + 6*6 + 4*3*6*2)*(1/6)**4)
    #   Any combo of 2,3,4,6 except 3, 4, or 5 of a kind 
    #   (4*10*3*2 ways to have a pair and 3 singles + 6*2*10*3 ways to have two pairs and a single)
    elif dice == 5:
        d["Farkel"] = dec_to_pct((4*10*3*2 + 6*2*10*3)*(1/6)**5)
    #   Any combo of 2,3,4,6 except 3, 4, 5, or 6 of a kind or 3 pairs
    #   (6*15*6*2 ways to have two pairs and two singles)
    elif dice == 6:
        d["Farkel"] = dec_to_pct((6*15*6*2)*(1/6)**6)
    
    # Two triplets (15 combos of 2 numbers for the triplets * 20 combos of 3 dice in 6 spots)
    if dice < 6:
        d["Two triplets"] = 0
    else:
        d["Two triplets"] = dec_to_pct(15*20*(1/6)**6)
    
    # Three pairs (20 combos of 3 numbers for the pairs * 15 combos of 2 dice in 6 spots * 6 combos of 2 dice in 4 spots)
    if dice < 6:
        d["Three pairs"] = 0
    else:
        d["Three pairs"] = dec_to_pct(20*15*6*(1/6)**6)
    
    # Straight 1-6
    if dice < 6:
        d["Straight"] = 0
    else:
        d["Straight"] = dec_to_pct(6*5*4*3*2*(1/6)**6)
        
    # 6 of a kind
    if dice < 6:
        d["6 of a kind"] = 0
    else:
        d["6 of a kind"] = dec_to_pct(6*(1/6)**6)
    
    # 5 of a kind
    if dice < 5:
        d["5 of a kind"] = 0
    elif dice == 5:
        d["5 of a kind"] = dec_to_pct(6*(1/6)**5)
    elif dice == 6:
        d["5 of a kind"] = dec_to_pct(30*6*(1/6)**6)
    
    # 4 of a kind
    if dice < 4:
        d["4 of a kind"] = 0
    elif dice == 4:
        d["4 of a kind"] = dec_to_pct(6*(1/6)**4)
    elif dice == 5:
        d["4 of a kind"] = dec_to_pct(30*5*(1/6)**5)
    elif dice == 6:
        d["4 of a kind"] = dec_to_pct((60*30+30*15)*(1/6)**6)

    # 3 of a kind
    if dice < 3:
        d["Any 3 of a kind"] = 0
    elif dice == 3:
        d["Any 3 of a kind"] = dec_to_pct(6*(1/6)**3)
    elif dice == 4:
        d["Any 3 of a kind"] = dec_to_pct(30*4*(1/6)**4)
    elif dice == 5:
        d["Any 3 of a kind"] = dec_to_pct((30*10+60*20)*(1/6)**5)
    elif dice == 6:
        d["Any 3 of a kind"] = dec_to_pct((120*60+60*120)*(1/6)**6)
    
    # Specific 3 of a kind
    if dice < 3:
        d["Specific 3 of a kind"] = 0
    elif dice == 3:
        d["Specific 3 of a kind"] = dec_to_pct((1/6)**3)
    elif dice == 4:
        d["Specific 3 of a kind"] = dec_to_pct(5*4*(1/6)**4)
    elif dice == 5:
        d["Specific 3 of a kind"] = dec_to_pct((5*10+10*20)*(1/6)**5)
    elif dice == 6:
        d["Specific 3 of a kind"] = dec_to_pct((20*60+10*120)*(1/6)**6)
    
    # Ones
    d["At Least One 1"] = dec_to_pct(1-(5/6)**dice)
    
    # Fives
    d["At Least One 5"] = dec_to_pct(1-(5/6)**dice)
    
    # Anything (1 minus farkel)
    if dice == 1:
        d["Scoring Something"] = dec_to_pct(1-(4/6))
    elif dice == 2:
        d["Scoring Something"] = dec_to_pct(1-(4/6)**2)
    elif dice == 3:
        d["Scoring Something"] = dec_to_pct(1-(4*3*2 + 4*3*3)*(1/6)**3)
    elif dice == 4:
        d["Scoring Something"] = dec_to_pct(1-(4*3*2 + 6*6 + 4*3*6*2)*(1/6)**4)
    elif dice == 5:
        d["Scoring Something"] = dec_to_pct(1-(4*10*3*2 + 6*2*10*3)*(1/6)**5)
    elif dice == 6:
        d["Scoring Something"] = dec_to_pct(1-(6*15*6*2)*(1/6)**6)
    
    return d

def farkel_score(roll):
    '''
    Calculate maximum Farkel score for a given dice roll.
    
    Parameters:
        roll (list): Dice rolled
    
    Returns:
        dict: "score": int score, "score desc": string score description, "dice remaining": int dice remaining
    '''
    
    # count occurrences of each number
    rolled = len(roll)
    ones = roll.count(1)
    twos = roll.count(2)
    threes = roll.count(3)
    fours = roll.count(4)
    fives = roll.count(5)
    sixes = roll.count(6)
    
    counts = [ones,twos,threes,fours,fives,sixes]
    
    # record scoring events
    
    # Two triplets: 2500
    if counts.count(3) == 2:
        score = 2500
        desc = "Two Triplets"
        dice = 6
    
    # Three pairs: 1500
    elif counts.count(2) == 3:
        score = 1500
        desc = "Three Pairs"
        dice = 6
    
    # Straight 1-6: 1500
    elif counts.count(1) == 6:
        score = 1500
        desc = "Straight"
        dice = 6
    
    # 6 of a kind: 3000
    elif counts.count(6) == 1:
        score = 3000
        desc = "Six-of-a-kind"
        dice = 6
        
    # 5 of a kind: 2000 (check remainder)
    elif counts.count(5) == 1:
        score = 2000
        desc = "Five-of-a-kind"
        # five dice
        if rolled == 5:
            dice = 6
        
        # six dice (five of a kind + 1)
        elif ones == 1:
            score += 100
            desc += "; One"
            dice = 6
        
        # six dice (five of a kind + 5)
        elif fives == 1:
            score += 50
            desc += "; Five"
            dice = 6
        
        # six dice (five of a kind + nothing)
        else:
            dice = 1
    
    # 4 of a kind: 1000 (check remainder)
    elif counts.count(4) == 1:
        score = 1000
        desc = "Four-of-a-kind"
        # four dice
        if rolled == 4:
            dice = 6
        
        # five or six dice
        else:
            if ones == 1 or ones == 2 or fives == 1 or fives == 2:
                score += 100*ones + 50*fives
            if ones == 1 or ones == 2:
                desc += "; One(s)"
            if fives == 1 or fives == 2:
                desc += "; Five(s)"

            if ones == 4 or fives == 4:
                correction = 4
            else: correction = 0
            if rolled - 4 - ones - fives + correction == 0:
                dice = 6
            else:
                dice = rolled - 4 - ones - fives + correction
        
    # 3 of a kind: 300 for 1, 200 for 2, 300 for 3, 400 for 4, 500 for 5, 600 for 6 (check remainder)
    elif counts.count(3) == 1:
        desc = "Three-of-a-kind"
        if ones == 3 or threes == 3:
            score = 300
        elif twos == 3:
            score = 200
        elif fours == 3:
            score = 400
        elif fives == 3:
            score = 500
        elif sixes == 3:
            score = 600
        # three dice
        if rolled == 3:
            dice = 6
        
        # four, five, or six dice
        else:
            if ones == 1 or ones == 2 or fives == 1 or fives == 2:
                score += 100*ones + 50*fives
            if ones == 1 or ones == 2:
                desc += "; One(s)"
            if fives == 1 or fives == 2:
                desc += "; Five(s)"
                
            if ones == 3 or fives == 3:
                correction = 3
            else: correction = 0
            if rolled - 3 - ones - fives + correction == 0:
                dice = 6
            else:
                dice = rolled - 3 - ones - fives + correction
    
    # Ones: 100
    # Fives: 50
    elif ones > 0 or fives > 0:
        score = 100*ones + 50*fives
        if ones > 0 and fives > 0:
            desc = "One(s) And Five(s)"
        elif ones > 0 and fives == 0:
            desc = "One(s)"
        else: 
            desc = "Five(s)"
            
        dice = sum(counts) - fives - ones
        if dice == 0:
            dice = 6
    
    # Farkel
    else:
        score = 0
        desc = "Farkel"
        dice = 0
    
    # Return result
    return {"score": score,
            "score desc": desc,
            "dice remaining": dice}

def farkel_turn(risk=0.5, force_stop=10000, display=True):
    '''
    Simulate one turn of Farkel.
    
    Parameters:
        risk (float): Maximum probability of farkeling to continue rolling
        force_stop (int): Cumulative score to stop rolling after reaching
        display (bool): Prints result of each turn if true
    
    Returns:
        int: Score for roll
    '''
    
    # initiate variables
    farkel_probs = {1: 4/6, 
                    2: (4/6)**2,
                    3: (4*3*2 + 4*3*3)*(1/6)**3,
                    4: (4*3*2 + 6*6 + 4*3*6*2)*(1/6)**4,
                    5: (4*10*3*2 + 6*2*10*3)*(1/6)**5,
                    6: (6*15*6*2)*(1/6)**6}
    
    farkel_prob = farkel_probs[6]
    if risk < farkel_prob:
        return "Risk must be at least .024 to play farkel"
    
    score = 0
    dice = 6
    turn = 1
    
    # roll as long as the probability of farkeling does not exceed risk,
    #  the cumulative score is less than the force stop score,
    #  and the previous roll was not a farkel
    while risk > farkel_prob and score < force_stop and dice > 0:
        output = roll(dice)
        result = farkel_score(output)
        if display:
            print("Turn Number ", turn)
            print(output)
            print(result)
        dice = result["dice remaining"]
        # if roll was not a farkel, add to the cumulative score and determine farkel probability of next roll
        if result["score"] > 0:
            score += result["score"]
            if display: print("Cumulative Score: ", score)
            farkel_prob = farkel_probs[dice]
            turn += 1
        # farkel
        else:
            if display: print("FARKEL!")
            score = 0
    
    return score