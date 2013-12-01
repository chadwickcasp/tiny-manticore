#Scratchwork on Interview Questions

def largest_sub_sum(lst):
	i = 0
	largest_sum = lst[0]
	while i <= len(lst):
		sum = 0
		for x in lst[i:]:
			sum += x
			if sum > largest_sum:
				largest_sum = sum
		i += 1
	return largest_sum
