import random

def roll_dice(num_dice):
	roll_list = []
	if num_dice <= 0:
		return
	elif num_dice < 5:
		num_dice = 5
	for i in range(num_dice):
		roll_list.append(random.randint(1, 6))
	return roll_list

def turn(name):
	print()
	rolls = 0
	held_dice = []
	while rolls < 3 and len(held_dice) < 5:
		roll = roll_dice(5-len(held_dice))

		print("%s, your roll is (Indicies 0-4) %s" % (name, roll))

		user_input = input("Which dice(indicies) would you like to hold(separated by spaces): ")
		args = user_input.split()
		if len(args) >= 1 and len(args) <= 5:
			for i in range(len(args)):
				arg = int(args[i])
				held_dice.append(roll[arg])
		else:
			held_dice = roll
		print("Held dice %s" % held_dice)
		rolls += 1
	return hand_check(held_dice)

def hand_check(hand):
	die_counts = {}
	for i in range(1, 7):
		die_counts[i] = hand.count(i)
	for i in hand:
		if die_counts[i] == 5:
			return 7 # Five of a kind
		elif die_counts[i] == 4:
			return 6 # Four of a kind
		elif die_counts[i] == 3:
			for i in hand:
				if die_counts[i] == 2:
					return 5 # Full house
			return 4 # Three of a kind
		elif die_counts[i] == 2:
			for i in hand:
				if die_counts[i] == 2:
					return 3 # Two pair
			return 2 # Pair
		else:
			return 1 # Bust
