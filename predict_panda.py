import mlflow
import json
import pandas as pd
from pandas.io.json import json_normalize


# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model('model')

data = [[".@user holds the fate of the republican pay in his tiny, tiny, tiny, little hands.   #gop"], ["@user +zig zag way is show 2b proud of top cast+great backstage team lovely script awesome music #encore #cornish #powerful #funny  "], ["latepost\u00f0\u009f\u0091\u00bb\u00f0\u009f\u0094\u00ab #like #like4like #likeforlike  #goodnight #night  #face #happy    #latepost  #sendiri "], ["ocean commotion!   #vbs2016 @user "], ["you look sexy af and fine @user \u00f0\u009f\u0098\u008d\u00f0\u009f\u0098\u008d\u00f0\u009f\u0098\u008d\u00e2\u009d\u00a4\u00ef\u00b8\u008f\u00f0\u009f\u0098\u0089\u00f0\u009f\u0098\u008b "]]

dp= pd.DataFrame(data, columns = ["tweet"])

print(str(loaded_model.predict(dp)))