'''
Author : Pierre SICALLAC
Date : 02/03/2022

This is a dumbed script for launch some dice, i'm bored so... why not !?

Type only a number : Launch x * dice 6
Type xdn : Launch x * dice n
'''
import random
import os 

def launch_dice(input: str) -> int:
	if 'd' in input:
		number_dice, max_dice_value = input.split('d')[0], input.split('d')[1]
		try:
			number_dice = int(number_dice)
			max_dice_value = int(max_dice_value)
			rSeed = random.seed()
			return sum([random.randint(1, max_dice_value) for i in range(number_dice)])
		except:
			print('Not a valid enter')
			return 0
	else:
		if input == 0:
			return 0
		try:
			input = int(input)
			rSeed = random.seed()
			return sum([random.randint(1, 6) for i in range(input)])
		except:
			print('Not a valid enter')
			return 0

os.system('cls' if os.name == 'nt' else 'clear')
print('Hello and welcome to a boring dice project (not a project)')

while True:
	print('Launch dice ? (0 to exit)', end=' ')
	dice = input()
	result = launch_dice(dice)
	if result == 0:
		break
	else:
		os.system('cls' if os.name == 'nt' else 'clear')
		print('Result of {} : {}'.format(dice, result))