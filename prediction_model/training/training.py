import torch
import torch.nn as nn

def train_model(data_loader, model, epochs, optimizer, loss_fn):
    size = len(data_loader.dataset)
    model.train()
    for epoch in range(epochs):
        for batch, (inputs, targets) in enumerate(data_loader):
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = loss_fn(outputs, targets)
            loss.backward()
            optimizer.step()

            if batch % 100 == 99:
                loss = loss.item()
                curr = (batch + 1) * len(inputs)
                print(f'loss: {loss}, curr: {curr}/{size}')
        print(f'epoch {epoch + 1}/{epochs} complete. loss: {loss.item()}')
