import random

def genCreatures(number):
	Creatures=[]
	types=['primate','bird','reptile','fish']
	for x in range(number):
		creature=[]
		name_of=random.choice(types)
		if name_of=='primate':
			creature.append(name_of)
			legs=random.choice([2,4])
			creature.append(legs)
			if legs==2:
				mammary=2
			else:
				mammary=random.choice([2,4,8,16])
			creature.append(mammary)
			
			gestation=random.choice(range(180,360))
			creature.append(gestation)
			if mammary<=4:
				young=random.choice(range(1,5))
			else:
				young=random.choice(range(1,20))
			creature.append(young)

		elif name_of=='bird':
			creature.append(name_of)
			legs=2
			creature.append(legs)
			mammary=0
			creature.append(mammary)
			
			gestation=random.choice(range(21,36))
			creature.append(gestation)
			young=random.choice(range(3,13))
			creature.append(young)
			
		elif name_of=='reptile':
			creature.append(name_of)
			legs=0
			creature.append(legs)
			mammary=0
			creature.append(mammary)
			
			gestation=random.choice(range(21,36))
			creature.append(gestation)
			young=random.choice(range(10,30))
			creature.append(young)
		else:
			creature.append(name_of)
			legs=0
			creature.append(legs)
			mammary=0
			creature.append(mammary)
			
			gestation=random.choice(range(21,36))
			creature.append(gestation)
			young=random.choice(range(50,300))
			creature.append(young)
		Creatures.append(creature)
	return Creatures
