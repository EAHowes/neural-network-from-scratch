import numpy as np


# Functions

# Loads and normalizes data returning X_train, y_train, X_test, y_test
def load_mnist():
    # X_train = flattened images
    # y_train = integer class labels (0-9) for each image
    # X_test = same as x_train but for test data
    # y_test = test labels

# Initializes W1, b1, W2, b2
def init_params(input_size, hidden_size, output_size):
    # input_size = features per input 
    # hidden_size = neurons in hidden layer
    # output_size = num of output classes
    # W1 = weight matrix input/hidden
    # b1 = bias vector 
    # W2 = weight matrix for hidden/out
    # b2 = bias vector for output layer

# Activation function
#   Used to remove linearity. Or rather add non linearity.
def relu(x):
    # x = input arr

# Converts logits to probabilities
#   Used to measure each logits score and turn them into probabilities
def softmax(z):
    # z = logits from the output layer

# Returns scalar loss
#   Used to determine how wrong each probability from softmax is so the model can be punished based on its confidence and correctness
def cross_entropy_loss(probs, labels):
    # probs = output probs from the softmax function
    # labels = the true digit labels

# Forward propagation function ... computes all forward steps
def forward(X, W1, b1, W2, b2):
    # X = batch of input images
    # W1, b1, W2, b2 = model params

# Backward propagation function ... computes gradients
def backward(X, y, z1, h1, z2, probs, W2):
    # X = input batch
    # y = true labels
    # z1, h1, z2, probs = intermediate results from forward
    # W2 = for backprop

# Applies SGD updates
def update_params(W1, b1, W2, b2, grads, lr):
    # W1, b1, W2, b2 = current model params
    # grads = computed gradients
    # lr = learning rate

# Computes the percentage of correct predictions
def accuracy(probs, labels):
    # probs = output probs
    # labels = true class labels

# Main training loop
def train(X_train, y_train, X_test, y_test, epochs, lr, batch_size, hidden_size):
    # X_train, y_train = training dataset
    # X_test, y_test = test dataset
    # epochs = number of passes through training data
    # lr = learning rate
    # batch_size = number of samples per grad steps
    # hidden_size = hidden layer width
