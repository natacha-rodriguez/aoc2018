from collections import Counter

def part_1():
	
	with open('input.txt','r') as file:
		data = file.readlines()

	twice = 0
	trice = 0

	for id in data:
		freq = Counter(id)
		if 2 in freq.values():
			twice += 1
		if 3 in freq.values():
			trice += 1 

	return twice * trice

def part_2():
	with open('input.txt','r') as file:
		data = file.readlines()

	res = None

	for i in data:
		for j in data:
			difference = [i[x] for x in range(len(i)) if i[x] != j[x]]
			#print('is is ', i, 'j is ', j,' diff is ',difference)
			if len(difference) == 1:
				print('  i is ', i, ' j is ', j, ' diff is ', difference)
				res = [i[x] for x in range(len(i)) if i[x] == j[x]]
				break
		if res: 
			break

	return ''.join(str(e) for e in res)

print(part_2())
