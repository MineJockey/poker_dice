import api as a

def main():
	p1 = input("Player 1, enter a name please: ")
	p2 = input("Player 2, enter a name please: ")
	rounds_num = int(input("How many rounds in the match: "))
	round_results = [0, 0]
	# has_won = False
	completed_rounds = 0

	while completed_rounds < rounds_num:
		turn = 0
		p1_hand = 0
		p2_hand = 0
		while turn < 2:
			if turn % 2 == 0:
				p1_hand = a.turn(p1)
			else:
				p2_hand = a.turn(p2)
			turn += 1
				
		print()
		if p1_hand > p2_hand:
				print("%s wins this round" % p1)
				round_results[0] += 1
		elif p1_hand < p2_hand:
			print("%s wins this round" % p2)
			round_results[1] += 1
		elif p1_hand == p2_hand:
			print("This round is a tie.")
		completed_rounds += 1
	if round_results[0] == round_results[1]:
		print("The match ends with a draw!")
	elif round_results[0] > round_results[1]:
		print("%s wins the match!" % p1)
	else:
		print("%s wins the match!" % p2)
		

# On this script is the main program instead of a module call main()
if __name__ == '__main__':
	main()
