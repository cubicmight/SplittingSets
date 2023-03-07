import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('result.txt', low_memory=False)

# Let's say we want to split the data in 80:10:10 for train:valid:test dataset
train_size = 0.8

X = df.drop(columns=['phrases']).copy()
y = df['phrases']

# In the first step we will split the data in training and remaining dataset
X_train, X_rem, y_train, y_rem = train_test_split(X, y, train_size=0.8)

# Now since we want the valid and test size to be equal (10% each of overall data).
# we have to define valid_size=0.5 (that is 50% of remaining data)
test_size = 0.5
X_valid, X_test, y_valid, y_test = train_test_split(X_rem, y_rem, test_size=0.5)

print(X_train.shape), print(y_train.shape)
print(X_valid.shape), print(y_valid.shape)
print(X_test.shape), print(y_test.shape)
