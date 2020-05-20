# from django.db import models

# Create your models here.
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import datasets, transforms
import torch.optim as optim


class Net(nn.Module):
    
    def __init__(self):
        super(Net, self).__init__()
        
        #Convolution layers
        self.conv1 = nn.Conv2d(3, 16, 3, stride=3)
        self.conv2 = nn.Conv2d(16, 32, 3, stride=3)
        self.conv3 = nn.Conv2d(32, 64, 3, stride=3)
        
        #Max pooling layers
        self.pool = nn.MaxPool2d(2, 2)
        
        #Fully connected layer
        self.fc1 = nn.Linear(64, 500)
        self.fc2 = nn.Linear(500, 256)
        self.fc3 = nn.Linear(256, 2)
        
        self.drop_out = nn.Dropout(0.25)
        
    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        
        
        x = x.view(-1, 64)
        
        x = self.drop_out(x)
        
        x = F.relu(self.fc1(x))
        
        x = self.drop_out(x)

        x = F.relu(self.fc2(x))
        
        x = self.drop_out(x)

        x = self.fc3(x)
        return x

# is_model_loaded = False

def load_model():
    # if is_model_loaded == False:
    model = Net()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    model.load_state_dict(torch.load('cat_vs_dog_nn.pth', map_location=torch.device('cpu')))
    # is_model_loaded = True
    # model.cuda()
    model.eval()
    return model

