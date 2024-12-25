from flask import json
import h5py
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import LSTM
import tensorflow as tf
import librosa
import numpy as np

class CustomLSTM(LSTM):
    def init(self, args, **kwargs):
        kwargs.pop('time_major', None)  # Remove unsupported argument if present
        super().init(args, **kwargs)

class WheezeCrackleModel:
    def __init__(self):
        self.w_model = tf.keras.models.load_model('models/LSTM_W_97.78.h5', custom_objects={'LSTM': CustomLSTM})
        self.model = tf.keras.models.load_model('models/C_LSTM_CNN_1.h5', custom_objects={'LSTM': CustomLSTM})

    def predict(self, audio_path):
        w_classes = ["Wheezes", "No Wheezes"]
        c_classes = ["Crackles", "No Crackles"]

        data_x, sampling_rate = librosa.load(audio_path)

        features = np.mean(librosa.feature.mfcc(y=data_x, sr=sampling_rate, n_mfcc=52).T, axis=0)

        features = features.reshape(1, 52)

        w_pred = self.w_model.predict(np.expand_dims(features, axis = 2))
        w_classpreds = w_classes[np.argmax(w_pred, axis=1)[0]]
        w_confidence = w_pred.T[w_pred.mean(axis=0).argmax()].mean()

        c_pred = self.model.predict(np.expand_dims(features, axis = 2))
        c_classpreds = c_classes[np.argmax(c_pred, axis=1)[0]]
        c_confidence = c_pred.T[c_pred.mean(axis=0).argmax()].mean()

        return w_classpreds, w_confidence, c_classpreds, c_confidence