import pandas as pd
from tensorflow import keras
import tensorflow as tf
from string import digits
from bentoml import api, env, BentoService, artifacts
from bentoml.artifact import TfKerasModelArtifact, PickleArtifact
from bentoml.handlers import JsonHandler

@artifacts([
  TfKerasModelArtifact('model'),
  PickleArtifact('vectorizer')
])
@env(conda_dependencies=['tensorflow', 'scikit-learn'])
class TextClassificationService(BentoService):
    
    @api(JsonHandler)
    def predict(self, parsed_json):
        text = parsed_json['text']
        remove_digits = str.maketrans('', '', digits)
        text = text.translate(remove_digits)
        text = self.artifacts.vectorizer.transform([text])
        prediction =  self.artifacts.model.predict_classes(text)[0][0]
        if prediction==0:
            response = {'Sentiment': 'Negative'}
        elif prediction==1:
            response = {'Sentiment': 'Positive'}
        
        return response
