# %% [markdown]
# **Training the Random Forest Regressor model using the derived hyper parameters**

# %% [code]
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import pickle
import time

# %% [code]
start_time = time.time()

# %% [code]
df = pd.read_csv("preprocessedIndia.csv")
cols = ['likes', 'views', 'comment_count', 'dislikes','views_per_day']
df = df[cols]
df = df[df.notnull().all(axis=1)]

# %% [code] {"_kg_hide-output":false}
X = df[cols[1:]]
Y = df.likes

# %% [code]
n_estimators = 150
max_depth = 30
min_samples_split = 5
min_samples_leaf = 2

# %% [code]
rfr = RandomForestRegressor(n_estimators = n_estimators,max_depth = max_depth,min_samples_split = min_samples_split,min_samples_leaf = min_samples_leaf, n_jobs=-1)
rfr.fit(X, Y)

# %% [code]
print(rfr.score(X, Y))

# %% [code]
filename = "trained_model"
with open(filename, "wb") as f:
    pickle.dump(rfr, f)

# %% [code]
print('Time taken = ' + str(time.time() - start_time))
