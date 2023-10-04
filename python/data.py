# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import f1_score, precision_score, recall_score
# df = pd.read_csv('child_accident_data.csv')  # データセットのパスは適宜変更してください
# X = df[['Region', 'Time', 'Date', 'Day_of_week', 'Location', 'Gender']]  # 特徴量
# y = df['Accident']  # 事故が発生したかどうかのラベル（1:発生, 0:未発生）
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# clf = RandomForestClassifier(n_estimators=100, random_state=42)
# clf.fit(X_train, y_train)
# y_pred = clf.predict(X_test)

# f1 = f1_score(y_test, y_pred)
# precision = precision_score(y_test, y_pred)
# recall = recall_score(y_test, y_pred)

# print(f'F1 Score: {f1}')
# print(f'Precision: {precision}')
# print(f'Recall: {recall}')
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import make_scorer, f1_score, precision_score, recall_score

# データ読み込み（こちらは一例です）
df = pd.read_csv('your_dataset.csv')

# 特徴量とラベルを分離
X = df.drop('label', axis=1)
y = df['label']

# データを訓練用とテスト用に分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# グリッドサーチで調整したいハイパーパラメータのリスト
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# F1スコアを評価基準とする
scorer = make_scorer(f1_score)

# GridSearchCVを用いてハイパーパラメータ調整
grid_search = GridSearchCV(estimator=RandomForestClassifier(random_state=42),
                           param_grid=param_grid,
                           scoring=scorer,
                           cv=3,
                           verbose=2,
                           n_jobs=-1)

grid_search.fit(X_train, y_train)

# 最適なハイパーパラメータを取得
best_params = grid_search.best_params_

# 最適なハイパーパラメータでモデルを訓練
best_clf = RandomForestClassifier(n_estimators=best_params['n_estimators'],
                                  max_depth=best_params['max_depth'],
                                  min_samples_split=best_params['min_samples_split'],
                                  min_samples_leaf=best_params['min_samples_leaf'],
                                  random_state=42)

best_clf.fit(X_train, y_train)

# 予測と評価
y_pred = best_clf.predict(X_test)

f1 = f1_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print(f'F1 Score: {f1}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
