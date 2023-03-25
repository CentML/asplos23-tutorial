import torch
import torch.nn as nn
import time

import apex

from model import ResNet50

def skyline_model_provider():
    return ResNet50().cuda()


def skyline_input_provider(batch_size=48):
    return (
        torch.randn((batch_size, 3, 244, 244)).cuda(),
        torch.randint(low=0, high=1000, size=(batch_size,)).cuda(),
    )


def skyline_iteration_provider(model):
    optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)
    loss_fn = torch.nn.CrossEntropyLoss()

    def iteration(*args):
        inputs, targets = args
        optimizer.zero_grad()

        # ---------------------------------------------
        # Optimization: Automatic Mixed Precision
        with torch.autocast(device_type="cuda"):
        # ---------------------------------------------
            out = model(inputs)
            loss = loss_fn(out, targets)

        loss.backward()
        optimizer.step()

    return iteration

