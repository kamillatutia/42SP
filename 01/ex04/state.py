import sys

def state():
	states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
	}
	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}
	if len(sys.argv) != 2:
		return
	capitalKeys = capital_cities.keys()
	stateKeys = states.keys()
	for key1 in capitalKeys:
		if sys.argv[1] == capital_cities[key1]:
			for key2 in stateKeys:
				if key1 == states[key2]:
					print(key2)
					return
	print('Unknown capital city')

if __name__ == '__main__':
	state()