"""
This example shows how to define your own dataset and use it to train a
non-trivial GNN with message-passing and pooling layers.
The script also shows how to implement fast training and evaluation functions
in disjoint mode, with early stopping and accuracy monitoring.
The dataset that we create is a simple synthetic task in which we have random
graphs with randomly-colored nodes. The goal is to classify each graph with the
color that occurs the most on its nodes. For example, given a graph with 2
colors and 3 nodes:
x = [[1, 0],
     [1, 0],
     [0, 1]],
the corresponding target will be [1, 0].
"""

import numpy as np
import scipy.sparse as sp
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.metrics import categorical_accuracy
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

import os

!pip install spektral
import spektral
from spektral.data import Dataset, DisjointLoader, Graph, BatchLoader
from spektral.layers import GCSConv, GlobalAvgPool
from spektral.transforms.normalize_adj import NormalizeAdj