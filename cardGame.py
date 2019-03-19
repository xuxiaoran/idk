#!/bin/python
# http://datagenetics.com/blog/october42014/index.html
# x is the number cards in hand
# y is the number of black cards in hand

def helper(x,y, value_matrix):
    card_remaining = 52-x
    remaining_black = 26-y
    remaining_red = card_remaining - remaining_black
    
    red_in_hand = x-y
    current_score = 1.0*(y - red_in_hand)

    # case when there is only one card left
    if card_remaining == 1:
        if remaining_black == 1:
            # if only one black left, currently have 25 black, 26 red, score is -1
            # need to draw, and the expcted value would be 0
            return 0
        else:
            # if only one red left, currently have 26 black, 25 red, score is 1
            # no need to draw, and the expected value would be 1
            return 1
    elif card_remaining == 0:
    	return 0

    draw_red = 0.0
    draw_black = 0.0

    if remaining_red > 0:
        # draw red
        if value_matrix[x][y-1] == -30:
            value_matrix[x][y-1] = helper(x+1, y,value_matrix)
        draw_red = value_matrix[x][y-1]

    if remaining_black > 0:
        if value_matrix[x][y] == -30:
            value_matrix[x][y] = helper(x+1, y+1,value_matrix)
        draw_black = value_matrix[x][y]

    expected = (1.0*remaining_red/card_remaining)*draw_red + (1.0*remaining_black/card_remaining)*draw_black
    value_matrix[x-1][y-1] = max(current_score,expected)
    return value_matrix[x-1][y-1]

def cardGame(x, y):
    red_in_hand = x-y
    current_score = 1.0*(y - red_in_hand)

    # calculate expected value
    value_matrix = []

    for i in range(52):
    	temp = []
    	for j in range(26):
    		temp.append(-30)
    	value_matrix.append(temp)

    expected = round(helper(x,y, value_matrix),2)
    print "%.2f, %r" % (expected, current_score < expected)

if __name__ == '__main__':
    cardGame(0, 0)