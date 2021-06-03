import csv
import pandas as pd
import plotly.figure_factory as ff
import random
import statistics
import plotly.graph_objs as go

df = pd.read_csv("bestdata.csv")
data = df["time"].tolist()

def random_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    print("mean of sampaling distribution is", mean)
    fig = ff.create_distplot([df], ["time"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1.5], mode ="lines", name="MEAN"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_mean = random_mean(100)
        mean_list.append(set_mean)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("mean of sampaling distribution is", mean)

setup()

def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_mean = random_mean(100)
        mean_list.append(set_mean)
    sd = statistics.stdev(mean_list)
    print("Standard deviation of sampaling distrubution", sd)

standard_deviation()