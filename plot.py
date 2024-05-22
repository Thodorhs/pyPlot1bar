import matplotlib.pyplot as plt
import numpy as np
import config

def parse_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    bars = []
    values = []

    for line in lines:
        line = line.strip()
        if line.startswith('bar='):
            bar = line.split('=')[1]
            bars.append(bar)
        else:
            value = float(line)
            values.append(value)

    return bars, values

def plot_data(bars, values):
    n_bars = len(bars)
    index = np.arange(n_bars)

    figsize = config.quartfigsize
    fig, ax = plt.subplots(figsize=figsize, dpi=config.dpi)

    for bar_index, value in zip(index, values):
        plt.bar(bar_index, value, config.bar_width, color=config.colors[0], edgecolor=config.edgecolor, linewidth=config.linewidth_2)

    plt.xlabel('Storage System', fontsize=config.fontsize)
    plt.ylabel('Latency (usec)', fontsize=config.fontsize)
    plt.xticks(index, bars, fontsize=config.fontsize-2, rotation=60)
    plt.yticks(fontsize=config.fontsize-2)

    # Adjust the position of the bar names
    ax.set_xticks(index)
    ax.set_xticklabels(bars, fontsize=config.fontsize-1)
    for tick in ax.get_xticklabels():
        tick.set_y(config.workload_name_pos)

    plt.tight_layout()
    plt.savefig('plot.eps', bbox_inches='tight', format='eps')

def main(filename):
    bars, values = parse_data(filename)
    plot_data(bars, values)

if __name__ == "__main__":
    main('data.txt')
