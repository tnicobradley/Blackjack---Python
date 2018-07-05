import string
import random



class playdeck():
	def __init__(self):
		suit = ["Hearts","Diamonds","Clubs","Spades"]
		face = ["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"] 
		self.stringdeck = []
		i = 0
		while(i < 52):
			j = 0
			while(j < 4):
				k = 0
				while(k < 13):
					self.stringdeck.append(face[k] + ' of ' + suit[j])
					i += 1
					k += 1
				j += 1


def shuffleDeck(deck):
	
	for x in range(0,1000):
		ranNum1 = random.randint(0,51)
		ranNum2 = random.randint(0,51)
		temphold = deck[ranNum1]
		deck[ranNum1] = deck[ranNum2]
		deck[ranNum2] = temphold 

def score(hand):
	#value = hand.split(" ")
	score = 0
	score2 = 0

	for i, card in enumerate(hand):
		value = card.split(' ')
		if value[0] == 'Ace':
			if i == 0:
				score2 += 1
			elif score2 != 0 and i > 1:
				if score2 + 11 <= 18:
					score2 += 11
				else:
					score2 += 1

			else:
				score2 = score + 1
			score += 11

		elif value[0] == 'Two':
			score += 2
			if score2 != 0:
				score2 += 2

		elif value[0] == 'Three':
			score += 3
			if score2 != 0:
				score2 += 3
		elif value[0] == 'Four':
			score += 4
			if score2 != 0:
				score2 += 4
		elif value[0] == 'Five':
			score += 5
			if score2 != 0:
				score2 += 5
		elif value[0] == 'Six':
			score += 6
			if score2 != 0:
				score2 += 6
		elif value[0] == 'Seven':
			score += 7
			if score2 != 0:
				score2 += 7
		elif value[0] == 'Eight':
			score += 8
			if score2 != 0:
				score2 += 8
		elif value[0] == 'Nine':
			score += 9
			if score2 != 0:
				score2 += 9
		elif value[0] == 'Ten':
			score += 10
			if score2 != 0:
				score2 += 10
		elif value[0] == 'Jack' or value[0] == 'Queen' or value[0] == 'King':
			score += 10
			if score2 != 0:
				score2 += 10
	return [score,score2]


class player():
	def __init__(self,bankroll):
		self.bankroll = bankroll
		self.wins = 0
		self.loses = 0
		self.ties = 0
playerinfo = player(100)

def deal(playerhand,computerhand,deck):
	playerhand.append(deck.pop(0))
	computerhand.append(deck.pop(0))
	playerhand.append(deck.pop(0))
	computerhand.append(deck.pop(0))
	playerscore = score(playerhand)
	computerscore = score(computerhand)
	return [playerscore,computerscore]
	pass


def hit(deck,hand):
	hand.append(deck.pop(0))
	newscore = score(hand)
	return newscore


def game(deck,bet):
	playerhand = []
	computerhand = []
	shuffleDeck(deck)
	scores = deal(playerhand,computerhand,deck)
	playerscore = scores[0]
	computerscore = scores[1]
	if 21 in playerscore and 21 not in computerscore:
		print("\nHand: \n")
		printhand = ''
		for card in playerhand:
			printhand = printhand + card + ' , '
		print(printhand)
		print("\nDealer Hand: \n")
		printdealer = ''
		for card in computerhand:
			printdealer = printdealer + card + ' , '
		print(printdealer)
		print("\nBlackjack! You Win!\n")

		return(bet+bet*2)
	elif 21 in computerscore and 21 not in playerscore:
		print("\nHand: \n")
		printhand = ''
		for card in playerhand:
			printhand = printhand + card + ' , '
		print(printhand)
		print("\nDealer Hand: \n")
		printdealer = ''
		for card in computerhand:
			printdealer = printdealer + card + ' , '
		print(printdealer)
		print("\nDealer got Blackjack!\nYou Lose!\n")
		return(bet*-1)
	elif 21 in playerscore and 21 in computerscore:
		print("Hand: \n")
		printhand = ''
		for card in playerhand:
			printhand = printhand + card + ' , '
		print(printhand)
		print("Dealer Hand: ")
		printdealer = ''
		for card in computerhand:
			printdealer = printdealer + card + ' , '
		print(printdealer)
		print("\nIt's a Tie!\n")
		return(0)
	else:

		print("\n \nDealer Card Showing: ",computerhand[0])
		print('\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
		print("Your Hand:\n")
		printhand = ''
		for card in playerhand:
			printhand = printhand + card + ' , '
		print(printhand)
		print("\n")
		hitchoice = 'False'
		while(hitchoice != "N" and 21 not in playerscore and (playerscore[0] < 21 or (playerscore[1] < 21 and playerscore[1] != 0))):
			hitchoice = input("\nHit? (Y/N): ")
			hitchoice = hitchoice.upper()
			if hitchoice == 'Y':
				playerscore = hit(deck,playerhand)
				print('Hand: \n')
				for printcard in playerhand:
					print(printcard)
		if (playerscore[0] <= 21 and playerscore[0] > playerscore[1]) or playerscore[1] == 0:
			playeruse = playerscore[0]
		else:
			playeruse = playerscore[1]
		comphit = True
		
		while((computerscore[0] <= 17) or (computerscore[1] <= 17 and computerscore[1] != 0) or (computerscore[0] < playeruse and computerscore[0] <= 18) or (computerscore[1] < playeruse and (computerscore[1] > computerscore[0] and computerscore[1] < 21)) and comphit == True):
			if computerscore[0] == 17:
				tmpscore = computerscore
				for testcard in computerhand:
					testcardsplit = testcard.split(' ')
					if testcardsplit[0] == 'Ace':
						computerscore = hit(deck,computerhand)
				if tmpscore == computerscore:
					comphit = False
					break

			else:
				computerscore = hit(deck,computerhand)

		if (computerscore[0] <= 21 and computerscore[0] > computerscore[1]) or computerscore[1] == 0:
			computeruse = computerscore[0]
		else:
			computeruse = computerscore[1]
		if playeruse > 21:
			print('\nDealer Hand: \n')
			for check in computerhand:
				print(check)
			print("\nYou: ", playeruse, "  Dealer: ",computeruse)
			print("\nBusted!")
			
			return(bet*-1)
		elif computeruse == playeruse:
			print('\nDealer Hand: \n')
			for check in computerhand:
				print(check)
			print("\nYou: ", playeruse, "  Dealer: ",computeruse)
			print("\n It's a Tie! \n")
			
			return(0)
		elif computeruse > playeruse and computeruse <= 21:
			print('\nDealer Hand: \n')
			for check in computerhand:
				print(check)
			print("\nYou: ", playeruse, "  Dealer: ",computeruse)
			print("\n You Lose! \n")
			
			return(bet*-1)
		elif playeruse > computeruse or computeruse > 21:
			
			print('\nDealer Hand: \n')
			for check in computerhand:
				print(check)
			print("\nYou: ", playeruse, "  Dealer: ",computeruse)
			print("\n You Won! \n")
			return(bet)


	pass

def table():
	print("\n \n \n \n \n \n \n***************----Welcome To Blackjack----***************\n \n \n \n \n \n \n")
	playing = True
	print("\nBankroll: ",playerinfo.bankroll)
	while playing:
		
		bet = 0
		while(bet < 1 or (bet > playerinfo.bankroll and bet > 1)):
			bet = int(input("Place your bet: "))
			if bet > playerinfo.bankroll:
				print('You do not have enough to place the bet!')
			if bet < 1:
				print('You must bet at least 1 chip!')
		gamedeck = playdeck()
		playerinfo.bankroll += game(gamedeck.stringdeck,bet)
		choice = None
		if playerinfo.bankroll < 1:
			print("\nYou are Bankrupt! \n Thanks for Playing!\n")
			quit()
		while choice == None:
			print("\nBankroll: ",playerinfo.bankroll)
			choice = input("Continue? (Y/N)")
			choice = choice.upper()
			print(choice)
			if choice == 'Y' or choice == 'N':
				break
			else:
				choice = None
		if choice == 'N':
			playing = False


table()
#game(stringdeck)