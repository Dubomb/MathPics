import torch
import torch.nn as nn

def test_model(device, data_loader, model, loss_fn):
    size = len(data_loader.dataset)
    batches = len(data_loader)
    model.eval()
    test_loss = 0
    correct = 0

    with torch.no_grad():
        for inputs, targets in data_loader:
            inputs = inputs.to(device)
            targets = targets.to(device)
            outputs = model(inputs)
            test_loss += loss_fn(outputs, targets).item()
            correct += (outputs.argmax(1) == targets).type(torch.float).sum().item()
    test_loss /= batches
    correct /= size
    print(f'test accuracy: {100 * correct}%, avg loss: {test_loss}')
