import matplotlib.pyplot as plt
import time


class Graph:
    def __init__(self, func, args, name):
        self.name = name
        _, self.ax = plt.subplots(figsize=(10, 10))
        plt.title(self.name, color="#ff00f0", fontsize=50)
        for arg in args:
            self.call(func, arg)
        self.graph()

    def call(self, func, args):
        start = time.time()
        func(*(args[1:]), len(args[1]), len(args[2]))
        end = time.time()
        print(end - start)
        self.ax.plot(
            args[0],
            end - start,
            linestyle='solid',
            label=f"{args[0]} elementos",
            marker='.')

    def graph(self):
        self.ax.legend(
            loc='center left',
            bbox_to_anchor=(1, 0.5),
            fancybox=True,
            shadow=True, ncol=1)
        self.ax.set_ylim(bottom=0)
        self.ax.set_xlabel("Input", labelpad=5)
        self.ax.set_ylabel("Tiempo")

        plt.style.use('seaborn-ticks')
        plt.grid(True)
        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    args = [(x, str(randrange(5, 8)), str(randrange(5, 8))) for x in range(20)]
    Graph(lcs, args, "Longest Common Subsequence")
        