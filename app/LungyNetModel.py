import librosa
import numpy as np
from tensorflow.keras.models import load_model
import tensorflow as tf

class LungyNetModel:
    def __init__(self):
        self.model = load_model('models/LungyNet.h5')
        self.classes = ['Healthy', 'COPD']

    def preprocessing(self, audio_file, mode):
        sr_new = 16000
        x, sr = librosa.load(audio_file, sr=sr_new)
        max_len = 5 * sr_new
        if x.shape[0] < max_len:
            pad_width = max_len - x.shape[0]
            x = np.pad(x, (0, pad_width))
        elif x.shape[0] > max_len:
            x = x[:max_len]
        if mode == 'mfcc':
            feature = librosa.feature.mfcc(y=x, sr=sr_new)
        elif mode == 'log_mel':
            feature = librosa.feature.melspectrogram(y=x, sr=sr_new, n_mels=128, fmax=8000)
            feature = librosa.power_to_db(feature, ref=np.max)
        return feature
    
    def predict(self, audio_file, mode='mfcc'):
        preprocessed_audio = self.preprocessing(audio_file, mode)
        preprocessed_audio = preprocessed_audio.reshape((1, 20, 157, 1))
        prediction = self.model.predict(preprocessed_audio)
        predicted_class = np.argmax(prediction, axis=1)
        return self.classes[predicted_class[0]]
    
    