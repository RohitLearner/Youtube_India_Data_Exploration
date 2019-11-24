# %% [markdown]
# **Predict likes based on trained model**

# %% [code]
import pickle
import pandas as pd
import numpy as np

# %% [code]
filename = 'trained_model'
with open(filename, "rb") as f:
    rfr = pickle.load(f)

# %% [code]
df = pd.read_csv("preprocessedtest2019.csv")
cols = ['likes', 'views', 'comment_count','dislikes', 'views_per_day']

# %% [code]
X = df[cols[1:]]
Y = df.likes

# %% [code]
Y_ = np.ceil(rfr.predict(X))

# %% [code]
print(rfr.score(X, Y))

