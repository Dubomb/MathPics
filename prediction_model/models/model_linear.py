import torch
import torch.nn as nn
import torch.nn.functional as F

DROPOUT_RATE = 0.5

class ModelLinear(nn.Module):
    def __init__(self):
        super(ModelLinear, self).__init__()

        self.flatten_image = nn.Flatten()
        self.model = nn.Sequential(
            nn.Linear(32 * 32, 512),
            nn.ReLU(),
            nn.Dropout(p=DROPOUT_RATE),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Dropout(p=DROPOUT_RATE),
            nn.Linear(256, 14)
        )
    
    def forward(self, image):
        image = self.flatten_image(image)
        logits = self.model(image)
        return logits
