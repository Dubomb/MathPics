import torch
import torch.nn as nn
import torch.nn.functional as F

class ModelLinear(nn.Module):
    def __init__(self):
        super.__init__()

        self.flatten_image = nn.Flatten()
        self.model = nn.Sequential(
            nn.Linear(64 * 64, 1024),
            nn.ReLU(),
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, 14)
        )
    
    def forward(self, image):
        image = self.flatten_image(image)
        logits = self.model(image)
        return logits
