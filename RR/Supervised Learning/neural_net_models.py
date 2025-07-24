# neural_net_models.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report



# Load dataset
X, y = load_iris(return_X_y=True)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

mlp_clf = MLPClassifier(hidden_layer_sizes=(10, 5), solver='adam', max_iter=1, warm_start=True, random_state=42)
mlp_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('mlp', mlp_clf)
])

# Train model with warm_start for 20 iterations
for i in range(20):
    mlp_pipeline.fit(X_train, y_train)
    print(f"Iteration {i + 1} complete")

# Predict and evaluate
y_pred = mlp_pipeline.predict(X_test)
print(classification_report(y_test, y_pred))

