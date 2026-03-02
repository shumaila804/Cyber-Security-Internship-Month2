import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# 1. Realistic Dataset Simulation
print("Step 1: Generating Balanced Synthetic Data...")
np.random.seed(42)
n_samples = 1000
# Fraud cases ko thora zyada rakha taake model seekh sakay
data = {
    'Time': np.random.uniform(0, 24, n_samples),
    'Amount': np.random.uniform(10, 5000, n_samples),
    'V1': np.random.randn(n_samples),
    'V2': np.random.randn(n_samples),
    'Class': [1 if (i < 200 or np.random.random() < 0.05) else 0 for i in range(n_samples)]
}
df = pd.DataFrame(data)

# 2. Data Splitting
X = df.drop('Class', axis=1)
y = df['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Model Training with Class Weight (Balanced)
print("Step 2: Training Balanced Random Forest Model...")
model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
model.fit(X_train, y_train)

# 4. Final Evaluation
y_pred = model.predict(X_test)
print("\n" + "="*40)
print("FINAL CREDIT CARD FRAUD DETECTION REPORT")
print("="*40)
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
