import numpy as np
import matplotlib.pyplot as plt


class DrawCurves:
    def __init__(self):
        self.fig, self.ax = plt.subplots(layout='constrained')
        self.fig.set_dpi(500)

    # Hinzufügen eines Plots
    def add_plot(self, x, y, label=None):
        self.ax.plot(x, y, label=label)

    # Ermöglicht das grafische Abbilden einer Punktaddition über den reellen Zahlen
    def add_point_addition(self, x1, y1, x2, y2, x3, y3):
        x = np.linspace(-5, 5, 100000, endpoint=True)

        # Schnittpunkte
        self.ax.scatter(x1, y1)
        self.ax.scatter(x2, y2)
        self.ax.scatter(x3, y3)
        self.ax.scatter(x3, -y3)

        # Schnittgerade
        s = (y2 - y1) / (x2 - x1)
        m = y1 - s * x1
        y = s * x + m
        self.ax.plot(x, y)

        # Spiegelungsgerade
        if y3 > 0:
            self.ax.vlines(x=x3, ymin=-y3, ymax=y3)
        else:
            self.ax.vlines(x=x3, ymin=y3, ymax=-y3)

    # Zeichen der erstellten Plots
    def draw(self):
        plt.grid(True)
        plt.show()
