import random
strategy_name = "Special Complicated Strategy"

winning_move = ''
#rpslist = ["r", "p", "s"]
#def random_move():
    ## return move
    

def move(my_history, their_history):
    if len(their_history) < 2:
        move = random.choice(["r", "p", "s"])
        
    #elif len(their_history) >= 2:
        
    else:
        our_prediction = predict_their_next_move(their_history.lower())
        move = beat_prediction(our_prediction)
    return move
    
def predict_their_next_move(their_history):
    return their_history[-2]
    
def beat_prediction(our_prediction):
    #Rock
    if our_prediction == "r" and "r" :
        winning_move == random.choice(["r", "p", "s"])
    elif our_prediction == "r"and "s" :
        winning_move == "s"
    elif our_prediction == "r" and "p" :
        winning_move == "r"
    #Paper
    elif our_prediction == "p" and "p" :
        winning_move == random.choice(["r", "p", "s"])
    elif our_prediction == "p"and "r" :
        winning_move == "r"
    elif our_prediction == "p" and "s" :
        winning_move == "p"
    #Scissor
    elif our_prediction == "s" and "s" :
        winning_move == random.choice(["r", "p", "s"])
    elif our_prediction == "s"and "r" :
        winning_move == "s"
    elif our_prediction == "s" and "p" :
        winning_move == "p"
    else:
        winning_move == " "
        print("Error in beat_prediction(): prediction was r, p, or s.")
    return winning_move

        
    

    
        