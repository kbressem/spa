# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/04_classification_models.ipynb (unless otherwise specified).

__all__ = ['SequentialModel']

# Cell
# default_exp models
import sys
sys.path.append('..')
from fastai.basics import *
from fastai.layers import *
from fastai.vision.learner import create_body as create_body_2d

from faimed3d.learner import create_head, create_body, create_cnn_model_3d
from faimed3d.layers import AdaptiveConcatPool3d

# Cell
class SequentialModel(Module):
    def __init__(self, model):

        self.body = nn.Sequential(
            model[0],
            nn.AdaptiveMaxPool3d(1),
        )
        self.head = nn.Sequential(
            AdaptiveConcatPool3d(1),
            model[1][1:])

    def forward(self, x):
        features = [self.body(_x.unsqueeze(1)) for _x in torch.unbind(x, 1)]
        features = torch.cat(features, 2)
        return self.head(features)