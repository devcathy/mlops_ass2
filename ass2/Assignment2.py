#!/usr/bin/env python
# coding: utf-8

# # Data preprocessing

# In[9]:


import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_excel('Pumpkin_Seeds_Dataset.xlsx')
X = df.drop('Class', axis=1)
y = df['Class']
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=777)


# # Setting the AutoML

# In[10]:


from supervised.automl import AutoML
import optuna

# 돌릴때 마다 같은 방식으로 돌리도록 seed 설정해줌
sampler = optuna.samplers.TPESampler(seed=777)

automl = AutoML(
    mode="Optuna",            
    # 전체 탐색 시간 30분
    total_time_limit=1800,     
    # 사용 알고리즘 
    algorithms=["Random Forest", "Xgboost", "LightGBM"],

    # ▶ 각 알고리즘별 Optuna 탐색 시간 = 10분
    optuna_time_budget=600,

    # 알고리즘별 
    optuna_init_params={
        "Random Forest": {
            "n_estimators":      {"low": 100,  "high": 500, "step": 50,  "distribution": "int_uniform"},
            "max_depth":         {"low": 3,    "high": 20,  "step": 1,   "distribution": "int_uniform"},
            "min_samples_split": {"low": 2,    "high": 10,  "step": 1,   "distribution": "int_uniform"},
        },
        "Xgboost": {
            "n_estimators":      {"low": 100,  "high": 300, "step": 50,  "distribution": "int_uniform"},
            "max_depth":         {"low": 3,    "high": 9,   "step": 1,   "distribution": "int_uniform"},
            "learning_rate":     {"low": 0.01, "high": 0.2,               "distribution": "log_uniform"},
        },
        "LightGBM": {
            "n_estimators":      {"low": 100,  "high": 400, "step": 50,  "distribution": "int_uniform"},
            "num_leaves":        {"low": 31,   "high": 128,              "distribution": "int_uniform"},
            "learning_rate":     {"low": 0.01, "high": 0.1,               "distribution": "log_uniform"},
        },
    },

    explain_level=2,          # SHAP 플롯 등 설명 레벨
)

automl.fit(X_train, y_train)


# In[11]:


y_pred = automl.predict(X_val)


# In[12]:


from sklearn.metrics import accuracy_score, f1_score, classification_report
print(classification_report(y_val, y_pred))


# In[13]:


automl.report()


# In[ ]:




