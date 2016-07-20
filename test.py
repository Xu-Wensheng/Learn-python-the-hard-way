a = "class%%%(%%%)"
b = "Make a class named %%% that is-a %%%"
word = ['z', 'z', 'z', 'z', 'z']

def f(a, b):
	results= []
	for w in a, b:
		result = w[:]
		for i in word:
			result = result.replace("%%%", i, 1)
		for j in word:
			result = result.replace("%%%", j, 1)
		results.append(result)

	return results

c, d = f(a, b)
print c
print d
