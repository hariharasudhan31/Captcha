import pandas as pd
import numpy as np

# Define the number of samples
num_samples = 1000

# Create data with similar patterns
data = {
    "Time spent on page": np.round(np.random.uniform(10, 70, num_samples), 2),
    "Average mouse speed": np.round(np.random.uniform(2, 18, num_samples), 2),
    "Average time spent on fields": np.round(np.random.uniform(10, 70, num_samples), 2),
    "Average interval between fields": np.round(np.random.uniform(10, 70, num_samples), 2),
    "Average mouse angle change": np.round(np.random.uniform(50, 100, num_samples), 2),
    "Average variance of x-axis clicks": np.round(np.random.uniform(5000, 100000, num_samples), 0),
    "Jitter count": np.random.choice([0, 1], num_samples, p=[0.3, 0.7]),
    "Tremors count": np.random.randint(50, 200, num_samples),
    "Backspace count": np.random.choice([0, 1, 2, 3], num_samples),
    "Repeated key count": np.where(
        np.random.rand(num_samples) > 0.2,  # 20% chance of missing data
        np.random.randint(1, 6, num_samples),
        np.nan
    ),
    "isHuman": ["TRUE"] * num_samples  # Label as human
}

# Create DataFrame
df = pd.DataFrame(data)

# Save the data to a CSV file
df.to_csv("expanded_human_data.csv", index=False)

print("Data generation complete. Saved to 'expanded_human_data.csv'.")
