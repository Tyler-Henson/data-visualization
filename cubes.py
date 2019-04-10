"""
Data Visualization
"""
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x_values = list(range(1, 5001))
    y_values = [x**3 for x in x_values]

    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.YlOrBr, s=40)

    plt.title("Cubed Numbers")
    plt.xlabel("Value")
    plt.ylabel("Cube of Value")

    plt.show()
