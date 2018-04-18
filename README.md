__PREDICTOR

___SUPERVISED MACHINE LEARNING ALGORYTHM

This is an algorithm that predicts a creature based on 
number of legs/limbs, number of mammary glands, length 
of gestation period in days, and average number of young 
produced/layed.

__How it works:__
This algorithm impliments k-nearest neighbour to predict.

__Data source:__
The script `predAnimal.py` imports a module `gensamples.py`
which has a function `genCreatures`; this function takes a 
single argument `number` which is the number of creatures
you want it to generate.
The `genCreatures` method generates creatures randomly
from a list of `['primate','bird','reptile','fish']`.
The characteristics within the method can be altered to generate your
own data; if you need data to practice with.

__Data Processing:__
Data is first processed and divided into `Test Data` and
`Training Data`.

`Training Data`: is the data whose parameters are used to determine
k nearest neighbours

`Test Data`: is the data we feed in to the algorithm so it can 
predict its class based on comparison of its parameters with 
`Training Data` respective parameters

After neighbors are determined, the prediction is made and accuracy 
of the algorythm calcualted.

__Accuracy:__
The algorythm has a prediction accuracy as shown in  the table:

||Number of creatures||Accuracy(%)||
------------------------------------
||       10          || ~20-40    ||
||      20-25        || ~>30      ||
||      30-50        || ~>60      ||
||      50-100       || ~85-98    ||
||      100>         || ~>95      ||
------------------------------------

The accuracy of the algorythm improves with larger data input.

Cheers!