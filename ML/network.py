from random import randrange
import numpy as np
from math import *

def sigmoid(z):
    return 1.0 / (1 + np.exp(-z))

def dirartive(z):
    return sigmoid(z) * (1-sigmoid(z))

def nodecost(outputs,expected):
    error = 0
    for i in range(len(outputs)):
        error += (outputs[i] - expected[i]) ** 2
    return error

class Layer:
    def __init__(self,num,nodesin):
        self.num = num
        self.nodesin = nodesin
        self.weights = []
        for i in range(nodesin):
            ws = []
            for x in range(num):
                ws.append(randrange(-25,25))
            self.weights.append(ws)
        
        self.biases = []
        for i in range(num):
            self.biases.append(randrange(-25,25))
            
        self.activations = [0] * self.num

    def calcOut(self,inputs):
        
        weightedinputs = []
        for nodeout in range(self.num):
            input = self.biases[nodeout]
            for nodein in range(self.nodesin):
                input += inputs[nodein] * self.weights[nodein][nodeout]
            weightedinputs.append(sigmoid(input))

        self.activations = weightedinputs
        
        return weightedinputs

    def CalcOutNodeValues(self,expected):
        nodeValues = [0] * len(expected)
        for i in range(len(nodeValues)):
            costDirartive = 2 * (self.activations[i] * expected[i])

class Dataset:
    def __init__(self,inputs,outputs) -> None:
        self.inputs = inputs
        self.outputs = outputs

class Network:
    def __init__(self,layers):
        self.layersize = layers
        self.layers = []
        for i in range(len(layers) - 1):
            self.layers.append(Layer(layers[i + 1],layers[i]))

    def networkcost(self,dataset):
        cost = 0
        for i in range(len(dataset.inputs)):
            outputs = self.classify(dataset.inputs[i])
            cost += nodecost(outputs,dataset.outputs[i])

        return cost
    def classify(self,inputs):
        for i in self.layers:
            inputs = i.calcOut(inputs)

        return inputs

    def learn(self,dataset,learnrate):

        cost = self.networkcost(dataset)
        learnedW = self.layers[i].weights
        learnedB = self.layers[i].biases

        for i in range(1,len(self.layers),-1):
            learnedBias = 1

