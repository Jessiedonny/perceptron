
This program is implemented by python3

There are 2 python files in this part:
#1 perceptron.py
#2 perceptronfortable1.py

To run this program, just run the .py file in python with data file name as the only argument.
###important### data folder must be in the same directory as the perceptron.py file.

Follow the below instructions to run the program:

1. Use ionosphere.data as the argument for perceptron.py. Use table1.data as the arguument for perceptrontable1.py. 
You can copy the below command line for convenience:

python3 perceptron.py ionosphere.data

python3 perceptronfortable1.py table1.data


2. ionosphere.data and table1.data are both under the data directory in the same folder as the python file.

--------------------------------------

What does this program do?
>>It splits the ionosphere file into 2 sets randomly. 70% as training set, 30% as testing set.
>>It then use the training set to training the perceptron. A set of weights is the outcome after the perceptron is learned
>>It then use the learned weights to measure the accuracy of the testing set

--------------------------------------
Predictions and accuracy of testing set and the whole training process including each epoch is recorded in sampleoutput.txt. It prints out on the screen as well.

------------------------
#max_iterations is 5000 (hard coded)if the training process doesn't stop converging.



