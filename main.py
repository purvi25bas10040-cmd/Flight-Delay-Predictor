import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load dataset
data = pd.read_csv("flights.csv")

# Convert categorical data to numbers
data = pd.get_dummies(data, drop_first=True)

# Features & target
X = data.drop("Delay", axis=1)
y = data["Delay"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
print("Enter flight details:")

departure_time = int(input("Departure Time (0-23): "))
distance = int(input("Distance: "))

# Simple input (keeping it basic)
input_data = [[departure_time, distance] + [0]*(X.shape[1]-2)]

prediction = model.predict(input_data)

if prediction[0] == 1:
    print("Flight will be DELAYED")
else:
    print("Flight will be ON TIME")
