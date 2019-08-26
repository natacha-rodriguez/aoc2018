def freq_part1():
	freq = 0

	with open('input.txt','r') as file:
		data = file.readlines()

	for change in data:
		freq = freq + int(change)

	print(freq)


def freq_part2():
	freq = 0
	freqs = [0]
	repeated = None
	with open('input.txt','r') as file:
		data = file.readlines()

	
	while repeated == None:
	#for i in range(5):
		for change in data:
			freq = freq + int(change)
			
			if freq in freqs:
				repeated = freq
				break
			else:
				freqs.append(freq)
		
	print(repeated)

freq_part1()
freq_part2()