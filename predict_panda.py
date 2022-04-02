import mlflow
import pandas as pd

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model('model')

# Predict on a Pandas DataFrame.


data = pd.read_json('model/input_example.json')
print(loaded_model.predict(pd.DataFrame(data)))