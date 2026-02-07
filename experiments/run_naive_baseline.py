from models.baseline.naive_baseline import NaivePersistenceBaseline
from models.evaluation.evaluate import evaluate_predictions


def run_naive_baseline(y_series):
    model = NaivePersistenceBaseline()
    y_pred = model.predict_batch(y_series)

    metrics = evaluate_predictions(y_series, y_pred)

    return metrics


if __name__ == "__main__":
    # Example usage
    y = [10, 12, 11, 15]

    results = run_naive_baseline(y)
    print("Naive Persistence Baseline Results:")
    print(results)
