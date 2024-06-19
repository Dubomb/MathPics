import sys
import torch
import torch.nn as nn
import torch.optim as optim

sys.path.append('../')
from models.model_linear import ModelLinear
import data.dataloader as dl
import training.training as training
import testing.testing as testing

device = 'cuda' if torch.cuda.is_available() else 'cpu'

model = ModelLinear().to(device)

train_dir = 'train'
validate_dir = 'val'
test_dir = 'test'
batch_size = 64

training_dataset = dl.get_dataset(train_dir)
train_loader = dl.get_loader(training_dataset, batch_size)

validation_dataset = dl.get_dataset(validate_dir)
validation_loader = dl.get_loader(validation_dataset, batch_size)

testing_dataset = dl.get_dataset(test_dir)
test_loader = dl.get_loader(testing_dataset, batch_size)

loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters())

epochs = 5

training.train_model(device, train_loader, validation_loader, model, epochs, optimizer, loss_fn)
testing.test_model(device, test_loader, model, loss_fn)