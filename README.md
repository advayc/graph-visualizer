# Graph Visualizer Using Python Matplotlib & Networkx

## Introduction

This project provides a set of Python functions to visualize graphs and paths within graphs using the Matplotlib and Networkx libraries. The primary functions are `showgraph` and `showpath`, which are designed to help users visually understand the structure of their graphs and the paths within them.

## Installation

Ensure you have the required libraries installed:

```bash
pip install networkx matplotlib
```

## Usage

### Importing the Functions

To use the visualization functions, import them from the respective directory:

```python
from graph_visualizer.visualize import showgraph, showpath
```

### Function: `showgraph`

This function visualizes a directed graph.

#### Parameters

- `graph`: A dictionary representing the adjacency list of the graph. Keys are node labels, and values are lists of neighboring nodes.

#### Example

```python
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['A']
}

showgraph(graph)
```
## Contributing

Contributions are welcome! To contribute to this project, please follow these steps:

1. **Fork the Repository**: Click the "Fork" button at the top right corner of this page to create a copy of this repository in your account.

2. **Clone the Repository**: Clone the forked repository to your local machine using the following command:
    ```bash
    git clone https://github.com/advayc/graph-visualizer.git
    ```

3. **Create a Branch**: Create a new branch for your feature or bug fix.
    ```bash
    git checkout -b feature-name
    ```

4. **Make Your Changes**: Make your changes to the codebase.

5. **Commit Your Changes**: Commit your changes with a descriptive commit message.
    ```bash
    git commit -m "Add feature-name"
    ```

6. **Push to the Branch**: Push your changes to your forked repository.
    ```bash
    git push origin feature-name
    ```

7. **Create a Pull Request**: Navigate to the original repository and create a pull request from your branch.

8. **Review Process**: Your pull request will be reviewed, and you may be asked to make additional changes before it is merged.

------
#### How It Works

1. **Graph Creation**: A directed graph `G` is created using Networkx's `DiGraph()` class.
2. **Adding Edges**: Edges are added to `G` by iterating through the adjacency list `graph`.
3. **Node Colors**: Nodes are colored blue by default, with the first node colored red for distinction.
4. **Layout**: The graph layout is calculated using the `spring_layout` algorithm.
5. **Drawing**: Nodes and edges are drawn using Networkx's `draw_networkx_nodes`, `draw_networkx_edges`, and `draw_networkx_labels` functions.
6. **Displaying**: The graph is displayed using Matplotlib's `plt.show()`.

### Function: `showpath`

This function visualizes a directed graph with a highlighted path.

#### Parameters

- `graph`: A dictionary representing the adjacency list of the graph. Keys are node labels, and values are lists of neighboring nodes.
- `path`: A list of nodes representing the path to be highlighted.

#### Example

```python
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['A']
}

path = ['A', 'B', 'D']

showpath(graph, path)
```

#### How It Works

1. **Graph Creation**: A directed graph `G` is created using Networkx's `DiGraph()` class.
2. **Adding Edges**: Edges are added to `G` by iterating through the adjacency list `graph`.
3. **Node Colors and Sizes**: Nodes are colored blue by default. The starting node is colored green, and the ending node is colored orange. Their sizes are increased for emphasis.
4. **Layout**: The graph layout is calculated using the `spring_layout` algorithm.
5. **Drawing**: 
   - Nodes and edges are drawn using Networkx's `draw_networkx_nodes`, `draw_networkx_edges`, and `draw_networkx_labels` functions.
   - The path edges are highlighted in red.
6. **Hover and Click Event Handling**: 
   - A scatter plot is created for hover and click detection.
   - An event handler updates the title based on the hovered node.
7. **Animation**: 
   - An animation is created to showcase the path dynamically using Matplotlib's `FuncAnimation`.

### Example Usage in a Script

```python
from graph_representation.visualize import showgraph, showpath

# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['A']
}

# Visualize the graph
showgraph(graph)

# Define a path to highlight
path = ['A', 'B', 'D']

# Visualize the graph with the highlighted path
showpath(graph, path)
```

## Detailed Function Explanation

### `showgraph`

This function creates a visual representation of a directed graph.

1. **Graph Creation**: 
   ```python
   G = nx.DiGraph()
   ```

2. **Adding Edges**: 
   ```python
   for node in graph:
       for neighbor in graph[node]:
           G.add_edge(node, neighbor)
   ```

3. **Node Colors**: 
   ```python
   node_colors = {node: 'tab:blue' for node in G.nodes()}
   node_colors[list(G.nodes())[0]] = 'tab:red'
   ```

4. **Layout**: 
   ```python
   pos = nx.spring_layout(G, seed=3113794652)
   ```

5. **Drawing**: 
   ```python
   options = {"edgecolors": "tab:gray", "node_size": 800, "alpha": 0.9}
   node_color_list = [mcolors.CSS4_COLORS.get(node_colors[node], 'tab:blue') for node in G.nodes()]
   nx.draw_networkx_nodes(G, pos, node_color=node_color_list, **options)
   nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
   nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif', font_color="whitesmoke")
   ```

6. **Displaying**: 
   ```python
   plt.title('Graph Visualization')
   plt.axis('off')
   plt.show()
   ```

### `showpath`

This function creates a visual representation of a directed graph with a highlighted path.

1. **Graph Creation**: 
   ```python
   G = nx.DiGraph()
   ```

2. **Adding Edges**: 
   ```python
   for node in graph:
       for neighbor in graph[node]:
           G.add_edge(node, neighbor)
   ```

3. **Node Colors and Sizes**: 
   ```python
   node_colors = {node: '#1f77b4' for node in G.nodes()}
   node_sizes = {node: 800 for node in G.nodes()}
   starting_node = path[0]
   ending_node = path[-1]
   node_colors[starting_node] = '#007300'
   node_colors[ending_node] = '#ff7f0e'
   node_sizes[starting_node] = 1000
   node_sizes[ending_node] = 1000
   ```

4. **Layout**: 
   ```python
   pos = nx.spring_layout(G, seed=3113794652)
   ```

5. **Drawing**: 
   ```python
   options = {"edgecolors": "#333333", "alpha": 0.9}
   node_color_list = [node_colors[node] for node in G.nodes()]
   node_size_list = [node_sizes[node] for node in G.nodes()]

   fig, ax = plt.subplots(figsize=(8, 6))
   fig = pylab.gcf()
   fig.canvas.manager.set_window_title('Visualize The Shortest Path in a Unweighted Graph')

   nx.draw_networkx_nodes(G, pos, node_color=node_color_list, node_size=node_size_list, **options, ax=ax)
   path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
   nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, ax=ax)
   nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=2, alpha=0.7, edge_color="#ff3333", ax=ax)
   nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif', font_color="whitesmoke", ax=ax)

   plt.title('Graph Visualization with Highlighted Path')
   plt.axis('off')
   ```

6. **Hover and Click Event Handling**: 
   ```python
   def on_hover(event):
       if event.inaxes == ax:
           cont, ind = scatter.contains(event)
           if cont:
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

   scatter = ax.scatter(
       [pos[node][0] for node in G.nodes()],
       [pos[node][1] for node in G.nodes()],
       s=[node_sizes[node] for node in G.nodes()],
       c=[node_colors[node] for node in G.nodes()],
       edgecolors=options["edgecolors"],
       alpha=options["alpha"]
   )

   fig.canvas.mpl_connect('motion_notify_event', on_hover)
   ```

7. **Animation**: 
   ```python
   def update(num):
       ax.clear()
       nx.draw_networkx_nodes(G, pos, node_color=node_color_list, node_size=node_size_list, **options, ax=ax)
       nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, ax=ax)
       nx.draw_networkx_edges(G, pos, edgelist=path_edges[:num+1], width=2, alpha=0.7, edge_color="#ff3333", ax=ax)
       nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif', font_color="whitesmoke", ax=ax)
       plt.title('Graph Visualization with Highlighted Path')
       plt.axis('off')

   ani = animation.FuncAnimation(fig, update, frames=len(path_edges)+1, repeat=False, interval=500)
   plt.show()
   ```

## Conclusion

These functions provide a straightforward way to visualize graphs and paths within them, making it easier to understand the structure and flow of the graph. By using Networkx and Matplotlib, the visualizations are both informative and customizable.

