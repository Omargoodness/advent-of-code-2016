bots = {}
done = []

with open('input.txt', 'r') as file:
	lines = [line.rstrip('\n') for line in file]

def add_value(amount, bot_num):
	if bot_num in bots:
		bots[bot_num].append(amount)
	
	elif not bot_num in bots:
		bots[bot_num] = [amount]

def split_hi_lo(bot_num, lo_bot, hi_bot):
	lo_amount = min(bots[bot_num])
	hi_amount = max(bots[bot_num])

	if lo_amount == 17 and hi_amount == 61:
		print('I found the bot! Bot#', bot_num)

	bots[bot_num] = []
	add_value(lo_amount, lo_bot)
	add_value(hi_amount, hi_bot)

while len(done) < len(lines):
	for instruction in lines:
		if instruction in done:
			pass
		
		else:
			if instruction.startswith('value'):
				params = [int(s) for s in instruction.split() if s.isdigit()]
				
				add_value(params[0], params[1])
				done.append(instruction)
			
			elif instruction.startswith('bot'):
				params = [int(s) for s in instruction.split() if s.isdigit()]

				if (params[0] in bots.keys()) and (len(bots[params[0]]) == 2):
					split_hi_lo(params[0], params[1], params[2])
					done.append(instruction)

				else:
					pass