"""
Replace the following code with your own LightningModule class.
Reference: https://lightning.ai/docs/pytorch/stable/common/lightning_module.html
Example:

import lightning.pytorch as pl
import torch.nn as nn
import torch.nn.functional as F


class LitModel(pl.LightningModule):
    def __init__(self, model):
        super().__init__()
        self.model = model


    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self.model(x)
        loss = F.cross_entropy(y_hat, y)
        return loss

    def configure_optimizers(self):
        return torch.optim.Adam(self.model.parameters())
"""
