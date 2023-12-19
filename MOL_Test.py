import numpy as np
import matplotlib.pyplot as plt

def calculate_measures_of_location(data):
    # Sort the data in ascending order
    sorted_data = np.sort(data)

    # Quartiles for even-sized data
    q1 = np.percentile(sorted_data, 25)
    q2 = np.percentile(sorted_data, 50)  # Median is the 2nd quartile
    q3 = np.percentile(sorted_data, 75)

    # Deciles for even-sized data
    deciles = [np.percentile(sorted_data, i) for i in range(10, 100, 10)]

    # Percentiles for even-sized data
    percentiles = [np.percentile(sorted_data, i) for i in range(1, 101)]

    return {
        "Quartiles": {"Q1": q1, "Q2": q2, "Q3": q3},
        "Deciles": {f"D{i}": deciles[i-1] for i in range(1, 10)},
        "Percentiles": {f"P{i}": percentiles[i-1] for i in range(1, 101)}
    }

# Example usage:
data_even = [12, 7, 3, 9, 5, 4, 11, 6, 8, 10, 15]
result_even = calculate_measures_of_location(data_even)

# Display the results using matplotlib
fig, ax = plt.subplots()

# Plot data points
ax.plot(sorted(data_even), np.zeros_like(data_even), 'o', label='Data Points')

# Plot quartiles
for quartile, value in result_even["Quartiles"].items():
    ax.axvline(value, linestyle='--', label=f'{quartile}: {value}', color='red')

# Plot deciles
for decile, value in result_even["Deciles"].items():
    ax.axvline(value, linestyle='--', label=f'{decile}: {value}', color='green')

# Plot percentiles
for percentile, value in result_even["Percentiles"].items():
    ax.axvline(value, linestyle='--', label=f'{percentile}: {value}', color='blue')

ax.legend()
ax.set_title('Measures of Location')
plt.show()
