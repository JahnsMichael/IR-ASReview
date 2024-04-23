from asreview.models.classifiers.base import BaseTrainClassifier
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GRU, Dense, Input


class GatedRecurrentUnit(BaseTrainClassifier):

    name = "gru"

    def __init__(self):

        super().__init__()

        def fit(self, X, y):
            """Fit the model to the data."""
            
            model = Sequential()
            model.add(GRU(128, input_shape=(1, X.shape[1])))
            model.add(Dense(128, activation='relu'))
            model.add(Dense(1, activation='sigmoid'))
            model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
            self._model = model

            X = X.reshape(X.shape[0], 1, X.shape[1])
            
            return self._model.fit(X, y)

        def predict_proba(self, X):
            X = X.reshape(X.shape[0], 1, X.shape[1])
            return self._model.predict_proba(X)
