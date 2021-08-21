import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":  
    x_data = np.arange(0,5,0.1)

    y_1 = 8*x_data

    # plot the data

    fig, ax = plt.subplots()
    ax.plot(x_data, y_1)
    
    plt.show()
