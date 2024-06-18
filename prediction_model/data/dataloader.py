import os
import torch.utils.data
from torchvision import datasets, transforms

def get_dataset(dir_name):
    transform = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.Grayscale(),
        transforms.ToTensor()
    ])

    dataset = datasets.ImageFolder(root=f'../data/dataset/final_symbols_split_ttv/{dir_name}', transform=transform)

    return dataset

def get_loader(dataset, batch_size):
    loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)

    return loader