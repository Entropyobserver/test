import matplotlib.pyplot as plt

def plot_perplexity(perplexities):
    # Fixed training set sizes for this experiment
    training_sizes = [
        18359, 9179, 4589, 2294, 1147, 
        573, 286, 143, 71, 35  # Sizes in descending order
    ]

    # Ensure the input matches the number of sizes
    if len(perplexities) != len(training_sizes):
        raise ValueError("The number of perplexity values must match the number of training set sizes.")

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(training_sizes, perplexities, marker='o', linestyle='-', color='b', label='Perplexity')

    # Reverse x-axis for easier interpretation (large dataset -> small dataset)
    plt.gca().invert_xaxis()

    # Annotations and labels
    plt.title('Perplexity vs Training Set Size (Bigram Model)', fontsize=14)
    plt.xlabel('Training Set Size (Number of Lines)', fontsize=12)
    plt.ylabel('Perplexity', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.xticks(training_sizes, rotation=45)  # Add size values as x-axis ticks

    # Display plot
    plt.tight_layout()
    plt.show()

# Example usage
user_input_perplexities = [
    15.21, 21.56, 27.78, 37.03, 48.21, 
    60.92, 48.21, 37.03, 27.78, 21.56  # Replace with your own values
]
plot_perplexity(user_input_perplexities)
