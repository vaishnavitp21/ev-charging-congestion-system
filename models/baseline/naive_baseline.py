import numpy as np


class NaivePersistenceBaseline:
    """
    Naive persistence model for time series congestion prediction.
    Predicts y_t = y_{t-1}.
    """

    def fit(self, y_train):
        """
        No training required for persistence baseline.
        Included for API consistency.
        """
        self.last_observed_ = y_train[-1]
        return self

    def predict(self, y_history):
        """
        Predict next value using the most recent observed value.

        Args:
            y_history (array-like): historical target values

        Returns:
            float: predicted congestion
        """
        if len(y_history) == 0:
            raise ValueError("y_history must contain at least one value")

        return y_history[-1]

    def predict_batch(self, y_series):
        """
        Generate predictions for a full series.
        First prediction is NaN by definition.

        Args:
            y_series (array-like)

        Returns:
            np.ndarray
        """
        y_series = np.asarray(y_series)
        preds = np.empty_like(y_series, dtype=float)
        preds[0] = np.nan

        for t in range(1, len(y_series)):
            preds[t] = y_series[t - 1]

        return preds
