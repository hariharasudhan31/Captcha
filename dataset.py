import pandas as pd
import numpy as np

# Number of samples to generate
num_samples = 1000

# Create bot-like data with mostly 0 for Backspace and Repeated key count
bot_data = {
    "Time spent on page": np.round(np.random.uniform(1.5, 2.7, num_samples), 2),
    "Average mouse speed": np.round(np.random.uniform(100, 1000, num_samples), 2),
    "Average time spent on fields": np.round(np.random.uniform(0.07, 0.25, num_samples), 2),
    "Average interval between fields": np.round(np.random.uniform(0.07, 0.25, num_samples), 2),
    "Average mouse angle change": np.round(np.random.uniform(1, 180, num_samples), 2),
    "Average variance of x-axis clicks": np.round(np.random.uniform(3000, 500000, num_samples), 0),
    "Jitter count": np.ones(num_samples),  # Mostly 1s as per example
    "Tremors count": np.zeros(num_samples),  # Mostly 0s as per example
    "Backspace count": np.zeros(num_samples),  # Set to mostly 0 for bot behavior
    "Repeated key count": np.zeros(num_samples),  # Set to mostly 0 for bot behavior
    "isHuman": ["FALSE"] * num_samples  # Label as bot
}

# Create DataFrame
df_bot = pd.DataFrame(bot_data)

# Save the data to a CSV file
df_bot.to_csv("expanded_bot_data.csv", index=False)

print("Data generation complete. Saved to 'expanded_bot_data.csv'.")
