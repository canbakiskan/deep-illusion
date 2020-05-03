"""
Torch Auxilary tools
"""

import torch
import numpy as np

__all__ = ["cross_entropy_one_hot"]


def cross_entropy_one_hot(y_hat, y, reduction=None):
    """
    Args:
         y_hat: Output of neural net        (Batch)
         y: Original label                  (Batch)
         reduction: Reduce size by func     (Str)
    """
    if reduction == "mean":
        return torch.mean(torch.sum(-y * torch.nn.LogSoftmax(y_hat), dim=1))
    elif reduction == "sum":
        return torch.sum(torch.sum(-y * torch.nn.LogSoftmax(y_hat), dim=1))
    else:
        return torch.sum(-y * torch.nn.LogSoftmax(y_hat), dim=1)
