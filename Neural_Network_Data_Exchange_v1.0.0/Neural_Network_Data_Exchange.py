# """
# ******************************************************************************/ 
# *                                                                            *
# *                          Neural Network Data Exchange Simulation            *
# *                                                                            *
# * DESCRIPTION:                                                               *
# * This program simulates a simple neural network with one hidden layer.      *
# * It takes input data, processes it through the neural network, and produces *
# * an output. The neural network exchanges data between the input layer,     *
# * hidden layer, and output layer.                                            *
# *                                                                            *
# * Copyright (c) 2024, Nico Fontani                                           *
# * Creation Date: 13 Nov 2024                                                 *
# *                                                                            *
# * Original Author: Nico Fontani                                              *
# * Last Modified: 13 Nov 2024                                                 *
# *                                                                            *
# * Supported by Python and Numpy                                               *
# *                                                                            *
# ******************************************************************************/
# """

import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid for backpropagation
def sigmoid_derivative(x):
    return x * (1 - x)

# Neural Network class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize the weights with random values
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Random weights for input to hidden layer and hidden to output layer
        self.weights_input_hidden = np.random.rand(self.input_size, self.hidden_size)
        self.weights_hidden_output = np.random.rand(self.hidden_size, self.output_size)

        # Biases for hidden and output layers
        self.bias_hidden = np.random.rand(1, self.hidden_size)
        self.bias_output = np.random.rand(1, self.output_size)

    def forward(self, inputs):
        # Forward pass through the network
        self.input_data = inputs
        self.hidden_layer_input = np.dot(self.input_data, self.weights_input_hidden) + self.bias_hidden
        self.hidden_layer_output = sigmoid(self.hidden_layer_input)

        self.output_layer_input = np.dot(self.hidden_layer_output, self.weights_hidden_output) + self.bias_output
        self.output = sigmoid(self.output_layer_input)

        return self.output

    def backward(self, expected_output, learning_rate=0.1):
        # Backward pass (backpropagation)
        output_error = expected_output - self.output
        output_delta = output_error * sigmoid_derivative(self.output)

        hidden_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.hidden_layer_output)

        # Update weights and biases using the gradients
        self.weights_hidden_output += self.hidden_layer_output.T.dot(output_delta) * learning_rate
        self.weights_input_hidden += self.input_data.T.dot(hidden_delta) * learning_rate
        self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
        self.bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate

    def train(self, training_inputs, training_outputs, epochs=10000, learning_rate=0.1):
        # Train the network on the training data
        for epoch in range(epochs):
            self.forward(training_inputs)
            self.backward(training_outputs, learning_rate)

            if epoch % 1000 == 0:  # Print the error every 1000 epochs
                error = np.mean(np.abs(training_outputs - self.output))
                print(f"Epoch {epoch}/{epochs} - Error: {error:.4f}")


# Example usage
if __name__ == "__main__":
    # Input data for training (XOR problem)
    training_inputs = np.array([[0, 0],
                                [0, 1],
                                [1, 0],
                                [1, 1]])

    # Expected output for the XOR problem
    training_outputs = np.array([[0],
                                 [1],
                                 [1],
                                 [0]])

    # Create the neural network (2 input nodes, 2 hidden nodes, 1 output node)
    nn = NeuralNetwork(input_size=2, hidden_size=2, output_size=1)

    # Train the neural network
    nn.train(training_inputs, training_outputs, epochs=10000, learning_rate=0.1)

    # Test the neural network after training
    print("\nTest the neural network after training:")
    for test_input in training_inputs:
        result = nn.forward(test_input)
        print(f"Input: {test_input} - Predicted Output: {result}")
