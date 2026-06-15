import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(data, column):
    plt.figure(figsize=(8, 5))

    sns.histplot(
        data[column],
        kde=True
    )

    plt.title(f"Distribution of {column}")
    plt.tight_layout()
    plt.show()

def plot_boxplot(data, column):
    plt.figure(figsize=(8, 4))

    sns.boxplot(
        x=data[column]
    )

    plt.title(f"Boxplot of {column}")
    plt.tight_layout()
    plt.show()

def plot_correlation_matrix(data):
    plt.figure(figsize=(8, 6))

    sns.heatmap(
        data.corr(numeric_only=True),
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.show()