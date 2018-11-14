import csv

def get_data(filename):
	f = open(filename, "r")
	li = []
	for line in csv.reader(f):
		li.append(sorted(line))
	return li

def sort_by_frequency(dic):
	print(type(dic))
	dic = sorted(dic, key = lambda d : d[1])
	return dic

def get_unique_items(data):
	li = []
	max_itemset_length = 0
	for itemset in data:
		s = {}
		for item in itemset:
			try:
				s[item] += 1
			except:
				s[item] = 1
		max_itemset_length = max(max_itemset_length, len(s))
		li.append(sort_by_frequency(s))
	#print(li)
	return max_itemset_length, li

def create_fp_tree(data, max_itemset_length):
	i = 0
	while i < max_itemset_length:
		for itemset in data:
			try:
				add(fp_tree, itemset[i])
			except:
				pass
		i += 1


data = get_data("groceries.csv")

max_itemset_length, items = get_unique_items(data)
fp_tree = {}

for item in items:
	try:
		fp_tree[item]["count"] += 1
	except:
		fp_tree[item] = {"count" : 0}


