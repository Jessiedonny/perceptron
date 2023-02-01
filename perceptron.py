import csv
import os
import sys
import random
from genericpath import exists


#take command line argument
try:
    arg = sys.argv[1]
except IndexError:
    raise SystemExit(f"Usage: {sys.argv[0]} <please use ionosphere.data as an argument>")


file_dir=os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
data_dir=file_dir+'/data/'

outputlines=[]


data_insts=[]
with open(data_dir+str(arg) ,newline='') as data_csv:
    csvreader=csv.reader(data_csv,delimiter=' ')
    attributes=next(csvreader)
    for row in csvreader:
        data_insts.append(row)

#transform data - insert dummy features
attributes.insert(0,'w0')
for i in range(len(data_insts)):
    data_insts[i].insert(0,1)

#split data to 2 sets
random.shuffle(data_insts)
k = int(float(len(data_insts))*0.7)
training_insts = data_insts[:k]
test_insts = data_insts[k:]
print(('Data split:\nTraining instances: ')+str(len(training_insts))+'\nTest instances: '+str(len(test_insts)))
outputlines.append(('Data split:\nTraining instances: ')+str(len(training_insts))+'\nTest instances: '+str(len(test_insts)))

#get class label
A='g'
B='b'

w=[]

#randomlise weight
for i in range(len(attributes)-1):
    w.append(round(random.random(),5))

#create perceptron #main algorithm of this program 
def perceptron(features):
    f=features
    while True:
        y=sum(float(w[i])*float(f[i]) for i in range(len(f)-1))
        if y>0:
            if str(f[len(f)-1])==A:                 
                break
            else:
                for j in range(len(f)-1):
                    w[j]=round(float(w[j])-float(f[j]),5)
        else:
            if f[len(f)-1]==B:              
                break
            else:
                for j in range(len(f)-1):
                    w[j]=round(float(w[j])+float(f[j]),5)

#calculate accuracy after each epoch
def check_accuracy(instances):
    c_count=0
    for j in range(len(instances)):
        f=instances[j]
        y=sum(float(w[i])*float(f[i]) for i in range(len(f)-1))        
        if y>0 and str(f[len(f)-1])==A:
            c_count=c_count+1
        if y<=0 and str(f[len(f)-1])==B:
            c_count=c_count+1
    accuracy=round(c_count/float(len(instances)),4)
    return accuracy


#main function to train the perceptron-learn the weights
def train_perceptron(instances):
    max_iteration=5000
    iteration=0
    iteration1=0
    accuracy=check_accuracy(training_insts)
    while True:
        for i in range(len(instances)):
            perceptron(instances[i])
        accuracy0=accuracy
        accuracy=check_accuracy(training_insts)
        print('--Training in process--\n>> #Epoch run: '+str(iteration)+': \n >> Training accuracy='+str(round(accuracy*100,2))+'%\n >> Weights ='+str(w))
        outputlines.append('--Training in process--\n>> #Epoch run: '+str(iteration)+': \n >> Training accuracy='+str(round(accuracy*100,2))+'%\n >> Weights ='+str(w))
        iteration+=1
        if(accuracy==1):
            break
        elif(accuracy-accuracy0<0.01 and accuracy-accuracy0>-0.01): #Stop converging at least 100 iterations
            iteration1+=1
            if iteration1>100:
                break
        elif(iteration==max_iteration):
            break  
    outputlines.append('--------training end--------\n Predictions on testing instances:')

#Function to predict test set
def predict(instances):
    c_count=0
    for j in range(len(instances)):
        f=instances[j]
        y=sum(float(w[i])*float(f[i]) for i in range(len(f)-1))
        if y>0:
            prediction=A
        else:
            prediction=B
        print('Instance '+str(j)+', class: '+str(f[len(f)-1])+', predicted class: '+prediction)        
        outputlines.append('Instance '+str(j)+', class: '+str(f[len(f)-1])+', predicted class: '+prediction)  
        if y>0 and str(f[len(f)-1])==A:
            c_count=c_count+1
        if y<=0 and str(f[len(f)-1])==B:
            c_count=c_count+1
    accuracy=round(c_count/float(len(instances)),4)
    print('Testing accuracy =' + str(round(accuracy*100,2))+'%')
    outputlines.append('Testing accuracy =' + str(round(accuracy*100,2))+'%')


# call the functions 
train_perceptron(training_insts)
predict(test_insts)

#output to sampleoutput.txt
with open(file_dir+'/sampleoutput.txt','w')  as f:
    f.write('\n'.join(outputlines))

