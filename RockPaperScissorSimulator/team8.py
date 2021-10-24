import random
'''The function move(my_history, their_history) must return 'r', 'p', or 's'.
my_history and their_history are strings of the same length, perhaps length zero.
'''

strategy_name = 'Special Complicated Strategy'

def move(my_history, their_history):
    '''This player beats its opponent's last move.
    
    Returns whatever would beat their last move, either 'r', 'p', or 's'.
    If there was no last move, returns 'r'.
    '''
    if len(their_history) < 2:
       my_move = random.choice(["r", "p", "s"])
      
    else:
        prediction = predict_they_will_repeat(their_history.lower())
        my_move = beat_prediction(prediction)
    return my_move
    
def predict_they_will_repeat(their_history):
    ''' their_history is a string of the last two moves.
    Returns their last move 's', 'r', or 'p'
    '''
    return their_history[-1 and -2]
        
def beat_prediction(prediction):
    '''prediction is a string of one character: r, p, or s
    returns 'r', 'p', or 's'
    '''
    #Rock
    if prediction =='r' and 'r':
        winning_move = random.choice(["p", "s"])
    elif prediction == 'r' and 's':
        winning_move = 's'
    elif prediction == 'r' and 'p':
        winning_move = 'r'
    #Paper
    elif prediction == 'p' and 'p':
        winning_move = random.choice(["r", "s"])
    elif prediction == 'p' and 'r':
        winning_move == 'r'
    elif prediction == 'p' and 's':
        winning_move = "p"
    #Scissor
    elif prediction == 's' and 's':
        winning_move = random.choice(["r", "p"])
    elif prediction == 's' and 'r':
        winning_move = 's'
    elif prediction == 's' and 'p':
        winning_move == 'p'

    else:
        winning_move = '' 
        print ('Error in beat_prediction(): prediction was not r, p, or s.')
    return winning_move