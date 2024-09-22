# Simple Linear Regression from scratch

# Function to calculate the mean of a list of numbers
def mean(values):
    return sum(values) / float(len(values))

# Function to calculate covariance
def covariance(x, mean_x, y, mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean_x) * (y[i] - mean_y)
    return covar

# Function to calculate the variance of a list of numbers
def variance(values, mean):
    return sum((x - mean) ** 2 for x in values)

# Function to calculate coefficients for simple linear regression
def coefficients(x, y):
    x_mean, y_mean = mean(x), mean(y)
    b1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
    b0 = y_mean - b1 * x_mean
    return b0, b1

# Function to make predictions with the regression coefficients
def simple_linear_regression(train_x, train_y, test_x):
    b0, b1 = coefficients(train_x, train_y)
    predictions = [b0 + b1 * x for x in test_x]
    return predictions

# Example usage
# Replace the following lists with your actual data
train_x = [1, 2, 3, 4, 5]
train_y = [2, 4, 5, 4, 5]
test_x = [6, 7, 8]

predictions = simple_linear_regression(train_x, train_y, test_x)

print(f"Input Values: {test_x}")
print(f"Predictions: {predictions}")
