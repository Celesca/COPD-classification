from flask import json
import h5py
from tensorflow.keras.models import load_model
from keras.initializers import Orthogonal
import tensorflow as tf
import librosa
import numpy as np

class WheezeCrackleModel:
    def __init__(self):
        custom_objects = {
            'LSTM': tf.keras.layers.LSTM,
            'Orthogonal': Orthogonal
        }
        self.w_model = load_model('models/Wheeze_LSTM.h5', custom_objects)
        self.model = load_model('models/Crackle_LSTM.h5', custom_objects)

    # def load_model_without_time_major(self, model_path, custom_objects):
    #     # Load the model configuration
    #     with h5py.File(model_path, 'r') as f:
    #         model_config = f.attrs.get('model_config')
    #         if model_config is None:
    #             raise ValueError('No model config found in the file.')
    #         model_config = json.loads(model_config)
        
    #     # Remove 'time_major' from LSTM layers
    #     for layer in model_config['config']['layers']:
    #         if layer['class_name'] == 'LSTM':
    #             layer['config'].pop('time_major', None)
        
    #     # Save the modified configuration back to the file
    #     with h5py.File(model_path, 'w') as f:
    #         f.attrs['model_config'] = json.dumps(model_config)
        
    #     # Load the model with the modified configuration
    #     try:
    #         model = load_model(model_path, custom_objects=custom_objects)
    #     except KeyError as e:
    #         raise ValueError(f"Error loading model: {e}")
        
    #     return model

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