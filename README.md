PREDICTOR

SUPERVISED MACHINE LEARNING ALGORYTHM

This is an algorithm that predicts a creature based on 
number of legs/limbs, number of mammary glands, length 
of gestation period in days, and average number of young 
produced/layed.

How it works:
This algorithm impliments k-nearest neighbour to predict.

Data source:
The script `predAnimal.py` imports a module `gensamples.py`
which has a function `genCreatures`; this function takes a 
single argument `number` which is the number of creatures
you want it to generate.
The `genCreatures` function then generates creatures randomly
from a list of `['primate','bird','reptile','fish']`.

Data Processing:
Data is first processed and divided into `Test Data` and
`Training Data`.

`Training Data`: is the data whose parameters are used to determine
k nearest neighbours

`Test Data`: is the data we feed in to the algorithm so it can 
predict its class based on comparison of its parameters with 
`Training Data` respective parameters

After neighbors are determined, the prediction is made and accuracy 
of the algorythm calcualted.

The accuracy of the algorythm improves with alrger data input to learn
from.

Cheers!