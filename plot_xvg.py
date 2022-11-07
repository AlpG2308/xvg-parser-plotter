import matplotlib.pyplot as plt
from dataclasses import dataclass
@dataclass
class Xvg_data:
    path: str
    data_x: list
    data_y: list
    x_label: str
    y_label: str
path = "../Proteins/pressure.xvg"
title = "Equilibration - NVT Ensemble\nTemperature"
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
    xvg = Xvg_data(path,x,y,x_label,y_label)
    return xvg
def plot_xvg (xvg):
    mean = sum(xvg.data_y)/len(xvg.data_y) #for equilibration
    plt.plot(xvg.data_x, xvg.data_y)
    #for equilibration
    plt.axhline(mean,color = "red",label = f"Mean = {mean: .2f} {xvg.y_label}") #round to double precision
    plt.xlabel(xvg.x_label)
    plt.ylabel(xvg.y_label)
    plt.title(title)
    plt.legend()
    plt.show()
    #plt.savefig("./EquilibrationNVTTemperature_6cvmH2O.png",format="png")

if __name__ == "__main__":
    plot_xvg(xvg_parser(path))

