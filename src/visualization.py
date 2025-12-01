import matplotlib.pyplot as plt

def plot_bar(data, labels, title):
    plt.figure(figsize=(8, 4))
    plt.bar(labels, data)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
