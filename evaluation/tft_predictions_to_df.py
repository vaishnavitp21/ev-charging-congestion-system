import numpy as np
import pandas as pd
from pathlib import Path

def main():
    # Resolve project root
    PROJECT_ROOT = Path(__file__).resolve().parents[1]

    # Input predictions
    preds_path = PROJECT_ROOT / "data" / "processed" / "tft_predictions.npy"

    # Output dataframe
    output_path = PROJECT_ROOT / "data" / "processed" / "tft_predictions.csv"

    print("📥 Loading predictions from:", preds_path)

    preds = np.load(preds_path)  # shape: (N, horizon)

    print("✅ Predictions loaded")
    print("Shape:", preds.shape)

    # Convert to DataFrame
    df = pd.DataFrame(
        preds,
        columns=[f"t+{i+1}" for i in range(preds.shape[1])]
    )

    # Save
    df.to_csv(output_path, index=False)

    print("💾 Saved predictions DataFrame to:")
    print(output_path)
    print("✅ Step 6 complete")

if __name__ == "__main__":
    main()
