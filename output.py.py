import matplotlib.pyplot as plt

def plot_clusters(df):
    plt.scatter(
        df['Annual Income (k$)'],
        df['Spending Score (1-100)'],
        c=df['Cluster']
    )
    plt.xlabel("Income")
    plt.ylabel("Spending Score")
    plt.title("Customer Segmentation")
    plt.show()


def save_output(df, path):
    df.to_csv(path, index=False)