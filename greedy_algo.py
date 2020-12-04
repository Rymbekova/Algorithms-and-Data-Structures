Greedy (v: value, w: weight, W: capacity, V: total value):
	items = {{80, 10}, {120, 20}, {90, 30}}
	W = 50
	V = 0
	for i in items:	
		ratio = vi/wi
		MaxSort(ratio)
		for i in items:
			if W - wi >= 0:
				W = W - wi
				V = V + vi
			else
				fraction = W/wi
				V = vi * fraction
				W = W - (wi*fraction)
		return V

T(n) = O(len log len), where length is the length of both arrays

