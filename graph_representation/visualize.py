import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.animation as animation
from matplotlib import pylab

# to use this code you need to import the function from graph_representation.visualize , like this
# from graph_representation.visualize import showgraph, showpath
# then you would be able to use showgraph or showpath anywhere in your code
# to learn more go to the README

def showgraph(graph):
    G = nx.DiGraph()

    # Add edges to the graph
    for node in graph:
        for neighbor in graph[node]:
            G.add_edge(node, neighbor)

    # Define node colors
    node_colors = {node: 'tab:blue' for node in G.nodes()}
    # Customize node color based on your graph's characteristics, if needed
    node_colors[list(G.nodes())[0]] = 'tab:red'

    pos = nx.spring_layout(G, seed=3113794652)  # positions for all nodes

    options = {"edgecolors": "tab:gray", "node_size": 800, "alpha": 0.9}
    node_color_list = [mcolors.CSS4_COLORS.get(node_colors[node], 'tab:blue') for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_color=node_color_list, **options)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif', font_color="whitesmoke")

    plt.title('Visualize A Unweighted Graph')
    plt.axis('off')
    plt.show()

def showpath(graph, path):
    G = nx.DiGraph()

    # Add edges to the graph
    for node in graph:
        for neighbor in graph[node]:
            G.add_edge(node, neighbor)

    # Define node colors and sizes
    node_colors = {node: '#1f77b4' for node in G.nodes()}  # Default color for nodes
    node_sizes = {node: 800 for node in G.nodes()}
    starting_node = path[0]
    ending_node = path[-1]
    node_colors[starting_node] = '#007300'  # Starting node color (green)
    node_colors[ending_node] = '#ff7f0e'  # Ending node color (orange)
    node_sizes[starting_node] = 1000  # Increase size for starting node
    node_sizes[ending_node] = 1000  # Increase size for ending node

    pos = nx.spring_layout(G, seed=3113794652)  # positions for all nodes

    options = {"edgecolors": "#333333", "alpha": 0.9}
    node_color_list = [node_colors[node] for node in G.nodes()]
    node_size_list = [node_sizes[node] for node in G.nodes()]

    fig, ax = plt.subplots(figsize=(8, 6))
    fig = pylab.gcf()
    fig.canvas.manager.set_window_title('Visualize The Path in a Unweighted Graph')

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color=node_color_list, node_size=node_size_list, **options, ax=ax)

    # Highlight the path edges
    path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, ax=ax)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=2, alpha=0.7, edge_color="#ff3333", ax=ax)

    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif', font_color="whitesmoke", ax=ax)

    plt.title('Graph Visualization with Highlighted Path')
    plt.axis('off')

    # Hover and Click Event Handling
    def on_hover(event):
        if event.inaxes == ax:
            cont, ind = scatter.contains(event)
            if cont:
                # Get the index of the hovered node
                index = ind['ind'][0]
                node = list(G.nodes())[index]
                if node == starting_node:
                    ax.set_title('Hovering over the starting node')
                elif node == ending_node:
                    ax.set_title('Hovering over the ending node')
                else:
                    ax.set_title(f'Hovered over node: {node}')
                fig.canvas.draw_idle()
            else:
                ax.set_title('Graph Visualization with Highlighted Path')
                fig.canvas.draw_idle()

    # Create a scatter plot for hover and click detection
    scatter = ax.scatter(
        [pos[node][0] for node in G.nodes()],
        [pos[node][1] for node in G.nodes()],
        s=[node_sizes[node] for node in G.nodes()],
        c=[node_colors[node] for node in G.nodes()],
        edgecolors=options["edgecolors"],
        alpha=options["alpha"]
    )

    fig.canvas.mpl_connect('motion_notify_event', on_hover)

    # Create animation to showcase the path
    def update(num):
        ax.clear()
        nx.draw_networkx_nodes(G, pos, node_color=node_color_list, node_size=node_size_list, **options, ax=ax)
        nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, ax=ax)
        nx.draw_networkx_edges(G, pos, edgelist=path_edges[:num+1], width=2, alpha=0.7, edge_color="#ff3333", ax=ax)
        nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif', font_color="whitesmoke", ax=ax)
        plt.title('Graph Visualization with Highlighted Path')
        plt.axis('off')

    ani = animation.FuncAnimation(fig, update, frames=len(path_edges)+1, repeat=False, interval=500)  # Adjust interval for smoothness

    plt.show()

def showweightedpath(graph, path):
    G = nx.DiGraph()

    # Add edges to the graph with weights
    for node in graph:
        for neighbor, weight in graph[node].items():
            G.add_edge(node, neighbor, weight=weight)

    # Define node colors and sizes
    node_colors = {node: '#1f77b4' for node in G.nodes()}  # Default color for nodes
    node_sizes = {node: 800 for node in G.nodes()}
    starting_node = path[0]
    ending_node = path[-1]
    node_colors[starting_node] = '#007300'  # Starting node color (green)
    node_colors[ending_node] = '#ff7f0e'  # Ending node color (orange)
    node_sizes[starting_node] = 1000  # Increase size for starting node
    node_sizes[ending_node] = 1000  # Increase size for ending node

    pos = nx.spring_layout(G, seed=3113794652)  # positions for all nodes

    options = {"edgecolors": "#333333", "alpha": 0.9}
    node_color_list = [node_colors[node] for node in G.nodes()]
    node_size_list = [node_sizes[node] for node in G.nodes()]

    fig, ax = plt.subplots(figsize=(8, 6))
    fig = pylab.gcf()
    fig.canvas.manager.set_window_title('Visualize The Shortest Path in a Weighted Graph')

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color=node_color_list, node_size=node_size_list, **options, ax=ax)

    # Highlight the path edges
    path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, ax=ax)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=2, alpha=0.7, edge_color="#ff3333", ax=ax)

    # Draw labels and edge weights
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif', font_color="whitesmoke", ax=ax)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', ax=ax)

    plt.title('Weighted Graph Visualization with Highlighted Path')
    plt.axis('off')

    # Create animation to showcase the path
    def update(num):
        ax.clear()
        nx.draw_networkx_nodes(G, pos, node_color=node_color_list, node_size=node_size_list, **options, ax=ax)
        nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, ax=ax)
        nx.draw_networkx_edges(G, pos, edgelist=path_edges[:num+1], width=2, alpha=0.7, edge_color="#ff3333", ax=ax)
        nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif', font_color="whitesmoke", ax=ax)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', ax=ax)
        plt.title('Weighted Graph Visualization with Highlighted Path')
        plt.axis('off')

    ani = animation.FuncAnimation(fig, update, frames=len(path_edges)+1, repeat=False, interval=500)  # Adjust interval for smoothness

    plt.show()

def showweightedgraph(graph):
    G = nx.DiGraph()

    # Add edges to the graph with weights
    for node in graph:
        for neighbor, weight in graph[node].items():
            G.add_edge(node, neighbor, weight=weight)

    # Define node colors
    node_colors = {node: 'tab:blue' for node in G.nodes()}
    node_colors[list(G.nodes())[0]] = 'tab:red'  # Highlight the first node

    pos = nx.spring_layout(G, seed=3113794652)  # positions for all nodes

    options = {"edgecolors": "tab:gray", "node_size": 800, "alpha": 0.9}
    node_color_list = [mcolors.CSS4_COLORS.get(node_colors[node], 'tab:blue') for node in G.nodes()]

    # Draw nodes, edges, and labels
    nx.draw_networkx_nodes(G, pos, node_color=node_color_list, **options)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif', font_color="whitesmoke")

    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.title('Weighted Graph Visualization')
    plt.axis('off')
    plt.show()
