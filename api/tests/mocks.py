import numpy as np

class MockModel:
    def __init__(self, model_path: str=None):
        self._model = None
        self._model_path = None

    def predict(self, X: np.ndarray) -> np.ndarray:
        n_instances = len(X)
        return np.random.rand(n_instances)

    def train(self, X: np.ndarray, y: np.ndarray):
        return self

    def save(self):
        return self

    def load(self):
        return self

