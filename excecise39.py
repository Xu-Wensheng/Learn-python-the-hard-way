# Dictionary

# create a mapping of state to abbreviation

states = {
		'Oregon': 'OR',
		'Florida': 'FL',
		'California': 'CA',
		'New York': 'NY',
		'Michigan': 'MI'	
}

# creare a basic set of states and some sities in them

cities = {
		'CA': 'San Fancisco',
		'MI': 'Detroit',
		'FL': 'Jacksonville'
		}
#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print some cities
print '-' * 10
print " NY State has: ", cities['NY']
print " OR states has:", cities['OR']

#print some states
print '-' * 10
print " Michigan's abbreviation is:", states['Michigan']
print " Florida's abbreviation is:", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print " Michigan has:", cities[states['Michigan']]
print " Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abrev in state.items():
	print " %s is abbreviated %s " %(state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities. items():
	print " %s has the city %s" %( abbrev, city)

# now do both at the same  time
print '-' * 10
for state abbrev in states.items():
	print " %s state is abbrevated %s and has city %s " % (
			state, abbrev, cities[abbrev])

print '-' * 10
# safe get a abbreviation by state that might not by there
state = states.get('Texas')

if not state:
	pritn " Sorry, no Texas."

# ger a city with a default value
city = cities.get('TX', 'Does not Exist.')
print " The city for the state 'TX' is: %s" % city

