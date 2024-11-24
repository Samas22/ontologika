# 3. Federated Learning (federated_learning.py)
# Implements privacy-preserving model training.

import tensorflow as tf

class FederatedLearning:
    def __init__(self, model):
        self.model = model

    def train_on_device(self, data, epochs=5):
        """
        Train model locally without sharing data.
        """
        self.model.fit(data, epochs=epochs)
        return self.model.get_weights()

    def aggregate_weights(self, local_weights):
        """
        Aggregate weights from multiple devices.
        """
        average_weights = [
            sum(weights) / len(weights) for weights in zip(*local_weights)
        ]
        self.model.set_weights(average_weights)
        return self.model
