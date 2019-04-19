from bentoml import BentoService, api, env, artifacts
from bentoml.artifact import PickleArtifact
from bentoml.handlers import JsonHandler

# Explicitly specify it
import pandas as pd 

# You can also import your own python module here and BentoML will automatically
# figure out the dependency chain and package all those python modules

@artifacts([PickleArtifact('model')])
@env(conda_pip_dependencies=["scikit-learn"])
class PassengerClassifier(BentoService):
    
    @api(JsonHandler)
    def predict(self, json):
        # Arbitrary preprocessing or feature fetching code can be placed here 
        query_df = pd.DataFrame(json)
        query = pd.get_dummies(query_df)
        column_names = ['Age',
                     'Embarked_C',
                     'Embarked_Q',
                     'Embarked_S',
                     'Embarked_nan',
                     'Sex_female',
                     'Sex_male',
                     'Sex_nan']
        query = query.reindex(columns=column_names, fill_value=0)
        prediction = self.artifacts.model.predict(query)
    
        return prediction
