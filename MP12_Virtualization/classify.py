import os
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.datasets as dsets
import torchvision.transforms as transforms
from torch.autograd import Variable
import time
import sys

class CNN(nn.Module):
    def __init__(self, num_classes):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 3, 3, 1)
        self.fc1 = nn.Linear(2028, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        output = F.log_softmax(x, dim=1)
        return output

class FFNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(FFNN, self).__init__()                    # Inherited from the parent class nn.Module
        self.fc1 = nn.Linear(input_size, hidden_size)  # 1st Full-Connected Layer: 784 (input data) -> 500 (hidden node)
        self.relu = nn.ReLU()                          # Non-Linear ReLU Layer: max(0,x)
        self.fc2 = nn.Linear(hidden_size, num_classes) # 2nd Full-Connected Layer: 500 (hidden node) -> 10 (output class)
    
    def forward(self, x):                              # Forward pass: stacking each layer together
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

def get_dataset(dataset_name, model_name):
    train_dataset = []
    test_dataset = []
    trans = transforms.ToTensor()
    if model_name == "cnn" or model_name == "cnv":
        trans = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
    if dataset_name == 'mnist':
        train_dataset = dsets.MNIST(root='./data',
                            train=True,
                            transform=trans,
                            download=True)

        test_dataset = dsets.MNIST(root='./data',
                                train=False,
                                transform=trans)
    elif dataset_name == "kmnist":
        train_dataset = dsets.KMNIST(root='./data',
                            train=True,
                            transform=trans,
                            download=True)

        test_dataset = dsets.KMNIST(root='./data',
                                train=False,
                                transform=trans)
    
    return train_dataset, test_dataset

def get_model(model_name, input_size, hidden_size, num_classes):
    if model_name == "ff":
        return FFNN(input_size, hidden_size, num_classes)
    elif model_name == "cnn" or model_name == "cnv":
        return CNN(num_classes)

def main():
    start_time = time.time()
    dataset_name = os.environ["DATASET"]
    model_name = os.environ["TYPE"]
    print("dataset:", dataset_name)

    input_size = 784       # The image size = 28 x 28 = 784
    hidden_size = 500      # The number of nodes at the hidden layer
    num_classes = 10       # The number of output classes. In this case, from 0 to 9
    num_epochs = 5        # The number of times entire dataset is trained
    batch_size = 100       # The size of input data took for one iteration
    learning_rate = 0.001  # The speed of convergence

    train_dataset, test_dataset = get_dataset(dataset_name, model_name)

    train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                            batch_size=batch_size,
                                            shuffle=True)

    test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                            batch_size=batch_size,
                                            shuffle=False)

    net = get_model(model_name, input_size, hidden_size, num_classes)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(net.parameters(), lr=learning_rate)

    for epoch in range(num_epochs):
        for i, (images, labels) in enumerate(train_loader):   # Load a batch of images with its (index, data, class)
            if model_name == "ff":
                images = Variable(images.view(-1, 28*28))         # Convert torch tensor to Variable: change image from a vector of size 784 to a matrix of 28 x 28
            labels = Variable(labels)
            
            optimizer.zero_grad()                             # Intialize the hidden weight to all zeros
            outputs = net(images)                             # Forward pass: compute the output class given a image
            loss = criterion(outputs, labels)                 # Compute the loss: difference between the output class and the pre-given label
            loss.backward()                                   # Backward pass: compute the weight
            optimizer.step()                                  # Optimizer: update the weights of hidden nodes
            
            if (i+1) % 100 == 0:                              # Logging
                print('Epoch [%d/%d], Step [%d/%d], Loss: %.4f'%(epoch+1, num_epochs, i+1, len(train_dataset)//batch_size, loss.data))

    correct = 0
    total = 0
    for images, labels in test_loader:
        if model_name == "ff":
            images = Variable(images.view(-1, 28*28))
        outputs = net(images)
        _, predicted = torch.max(outputs.data, 1)  # Choose the best class from the output: The class with the best score
        total += labels.size(0)                    # Increment the total count
        correct += (predicted == labels).sum()     # Increment the correct count
        
    print('Accuracy of the network on the 10K test images: %d %%' % (100 * correct / total))
    torch.save(net.state_dict(), 'mnist_fnn_model.pkl')

    end_time = time.time()
    print("Time passed: %.2f sec" % (end_time - start_time))

if __name__ == "__main__":
    main()
    sys.exit()
