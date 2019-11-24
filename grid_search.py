# %% [markdown]
# **Hyperparameter tuning using Grid Search**

# %% [code]
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
import pandas as pd
import time

# %% [code]
start_time = time.time()

# %% [code]
df = pd.read_csv("preprocessedIndia.csv")
cols = ['likes', 'views', 'comment_count', 'dislikes','views_per_day']
df = df[cols]
df = df[df.notnull().all(axis=1)]

# %% [code]
X = df[cols[1:]]
Y = df.likes

# %% [code]
rfr = RandomForestRegressor()
params = {
    'n_estimators':([150,200]),
    'max_depth':([15,25,30]),
    'min_samples_split':([5,15,10]),
    'min_samples_leaf':([2,5])
}

# %% [code]
grid_search = GridSearchCV(rfr, params, n_jobs=-1, scoring='r2')
grid_search.fit(X, Y)

# %% [code]
print("Best score " + str(grid_search.best_score_))
best_params = grid_search.best_estimator_.get_params()
for param_name in params.keys():
    print(param_name,best_params[param_name])

# %% [code]
print('Time taken = ' + str(time.time() - start_time))

