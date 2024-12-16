import pandas as pd
from .base_model import Model
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


class LogisticRegressionModel(Model):
    def __init__(self, **kwargs):
        self.model = LogisticRegression(**kwargs)
        
    def train(self, X: pd.DataFrame, y: pd.Series) -> None:
        """
        Train the logistic model on the provided data.
        Args:
            X(pd.DataFrame): A pandas DataFrame containing the training data.
            y(pd.Series): A pandas Series containing the labels of the training data.
        """
        print("Training logistic model on data")
        self.model.fit(X, y)
        
    def predict(self, X: pd.DataFrame) -> pd.Series:
        """
        Predict using the logistic model.
        Args:
            X(pd.DataFrame): A pandas DataFrame containing the data for prediction.
        Returns:
            pd.Series: A Series with model predictions.
        """
        predictions = self.model.predict(X)
        return pd.Series(predictions, index=X.index)