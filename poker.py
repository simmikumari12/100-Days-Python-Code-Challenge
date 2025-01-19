import sys

# takes as input, hand, and returns True if hand is "valid", 
# and False otherwise
def valid_input(hand):
	pass

# takes as input, hand, and returns a "dictionary" whose keys are
# the ranks and the values are the number of cards in the hand for 
# the given rank
def process_ranks(hand):
	pass

# takes as input, hand, and returns a "dictionary" whose keys are
# the suits and the values are the number of cards in the hand for 
# the given suit
def process_suits(hand):
	pass

# takes the ranks_dict for a particular hand as input and returns True 
# if the hand contains a "straight"
def check_straight(ranks_dict):
	pass

# takes the suits_dict for a particular hand as input and returns True 
# if the hand contains a "flush"
def check_flush(suits_dict):
	pass

# takes the ranks_dict for a particular hand as input and returns True 
# if the hand contains a "fours"
def check_fours(ranks_dict):
	pass

# takes the ranks_dict for a particular hand as input and returns True 
# if the hand contains a "threes"
def check_threes(ranks_dict):
	pass

# takes the ranks_dict for a particular hand as input and returns the 
# number of "pairs".
def check_pairs(ranks_dict):
	pass

# takes boolean inputs straight, flush, four, three, pair for a hand
# and returns the highest hand classification.
def hand_type(straight,flush,four,three,pair):
	pass