import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(values, keys):
    ax = plt.axes()
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 5))
    ax.set_facecolor("yellow")
    plt.pie(values, labels=keys,radius=1.5, colors=[ 'green', 'red','orange'], autopct='%0.2f%%')
  
    graph = get_graph()
    return graph