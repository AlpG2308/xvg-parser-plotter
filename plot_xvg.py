import matplotlib.pyplot as plt

path = "../Proteins/temperature.xvg"

def xvg_parser (path):
    x,y = [],[]
    x_label = ""
    y_label = ""
    with open(path) as f:
        for line in f:
            if line.startswith("#") or line.startswith("@"):
                if line.startswith("@") and "xaxis" in line:
                    xaxis = line.split('"')
                    x_label = xaxis[1]
                if line.startswith("@") and "yaxis" in line:
                    yaxis = line.split('"')
                    y_label = yaxis[1]
            else:
                data = line.split()
                x.append(float(data[0]))
                y.append(float(data[1]))

    return (x,y,x_label,y_label)

def plot_xvg (xvg):
    plt.plot(xvg[0], xvg[1])
    plt.xlabel(xvg[2])
    plt.ylabel(xvg[3])
    plt.show();

if __name__ == "__main__":
    plot_xvg(xvg_parser(path))

