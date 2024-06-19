import torch
import torch.nn as nn

def validate_model(device, val_data_loader, model, optimizer, loss_fn):
    val_size = len(val_data_loader.dataset)
    batches = len(val_data_loader)
    model.eval()
    validate_loss = 0
    correct = 0

    with torch.no_grad():
        for inputs, targets in val_data_loader:
            inputs = inputs.to(device)
            targets = targets.to(device)
            outputs = model(inputs)
            validate_loss += loss_fn(outputs, targets).item()
            correct += (outputs.argmax(1) == targets).type(torch.float).sum().item()
    validate_loss /= batches
    correct /= val_size
    print(f'validation accuracy: {100 * correct}%, avg loss: {validate_loss}')

def train_model(device, train_data_loader, val_data_loader, model, epochs, optimizer, loss_fn):
    train_size = len(train_data_loader.dataset)

    for epoch in range(epochs):
        model.train()
        for batch, (inputs, targets) in enumerate(train_data_loader):
            inputs = inputs.to(device)
            targets = targets.to(device)
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = loss_fn(outputs, targets)
            loss.backward()
            optimizer.step()

            if batch % 100 == 99:
                loss = loss.item()
                curr = (batch + 1) * len(inputs)
                print(f'loss: {loss}, curr: {curr}/{train_size}')
        print(f'epoch {epoch + 1}/{epochs} complete. loss: {loss.item()}')

        if epoch % 2 == 1:
            validate_model(device, val_data_loader, model, optimizer, loss_fn)