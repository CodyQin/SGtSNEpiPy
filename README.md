# SGtSNEpiPy

![3d_karate_club_animation](https://github.com/CodyQin/SGtSNEpiPy/assets/125537769/998d13a8-7d2d-4fa3-b435-095783f1bdc0)

## Overview

`SGtSNEpiPy` is a `Python` interface to
[`SG-t-SNE-П`](https://github.com/fcdimitr/SGtSNEpi.jl), a `Julia`
package. This allows Python users to utilize and take full advantage
of the 'SG-t-SNE-П' functionalities while remaining in the Python
environment. With SGtSNEpiPy, users can swiftly and directly embed and
visualize a sparse graph in a d-dimensional space, d=1,2,3.  The node
adjacency on the graph is translated to spatial near-neighbor
proximity, as illustrated in the plots above.

 This Python wrapper is implemented using
[`JuliaCall`](https://cjdoris.github.io/PythonCall.jl/stable/juliacall/)
in the package
[`PythonCall`&`JuliaCall`](https://cjdoris.github.io/PythonCall.jl/stable/).

The input is a sparse graph G(V,E) represented by its adjacency matrix
A in sparse formats. The graph at input can be directed or undirected,
the edges can be weighted or unweighted. The output is the array of
the $d$-dimensional vertex coordinates in the embedding space. The
Python wrapper converts the data formats and translate all input and
output arguments between Julia and Python.


### Introduction

SG-t-SNE extends t-SNE from point feature data to graph data,
especially sparse graphs represented by their adjacency matrices in
sparse formats.  Here, SNE stands for stochastic near-neighbor
embedding, and SG stands for sparse graph.  The SG-t-SNE algorithm was
first introduced in 2019 in the
[`paper`](https://ieeexplore.ieee.org/document/8916505)*[[1]](#1).  A
software [`SG-t-SNE-Pi`](https://github.com/fcdimitr/sgtsnepi) in Julia
was released in 2019.
(2019))](https://joss.theoj.org/papers/10.21105/joss.01577)**
[[2]](#2).  SG-t-SNE-П makes a direct translation of the node
adjacency on the graph to spatial proximity in the embedding space. In
comparison, other graph embedding methods first embed the vertices by
spectral decomposition or learning, followed by SNE. By our impirical
tests and user feedback [`??`](???), the SG-t-SNE mapping has higher
fidelity and efficiency.

`SGtSNEpi`, a `Julia` interface, i.e., a wrapper to `SG-t-SNE-Π` was released on **[GitHub](https://github.com/fcdimitr/SGtSNEpi.jl)** in 2019. SGtSNEpiPy uses **[JuliaCall](https://cjdoris.github.io/PythonCall.jl/stable/juliacall/)** module to make this Julia interface `SGtSNEpi` readily deployable to the Python ecosystem.

## Installation

To install `SGtSNEpiPy` through `Python` from `PyPi`, issue

```shell
$ pip install SGtSNEpiPy
```

The installation is straightford: import `SGtSNEpiPy` 
and issue the command 

```python
from SGtSNEpiPy.SGtSNEpiPy import sgtsnepipy
```

**Warning:** 
The current version of `SGtSNEpiPy` requires WSL2 on Windows or Apple ARM harward via rosetta2.

See **[the full documentation](https://fcdimitr.github.io/SGtSNEpi.jl/stable)** for more details.



## Parameters 

**SGtSNEpiPy.SGtSNEpiPy.sgtsnepipy**

This package only has one method currently.

```python
   Y = sgtsnepi(A)
```


### A: the input CSR sparse matrix representing the data points' pairwise similarities. (Mandatory)

- Data Type: `scipy.sparse.csr.csr_matrix` (The matrix includes row, value, value, whose type are all `numpy.ndarray` with three arrays of `numpy.int32`, `numpy.int32`, `numpy.int64`), that is a CSR sparse matrix generated by package `scipy`.

### Returns Y: array with the coordinates of the embedding of the graph nodes

- Data Type: `numpy.ndarray`, a 2-dimensional array of `numpy.float64`.
   - Number of rows: the number of rows or columns in the CSR matrix (the input).
   - Number of columns: the number of dimensions of the embedding space.


## Optional input parameters

### d: the number of dimensions of the embedding space. (Optional)

<ul>
<li>Data Type: Integer</li>
<li>Default Value: 2</li>
</ul>

### λ: SG-t-SNE scaling factor. (Optional)

<ul>
<li>Data Type: Integer or Float</li>
<li>Default Value: 10</li>
</ul>

### max_iter: the maximum number of iterations for the optimization process. (Optional)

<ul>
<li>Data Type: Integer</li>
<li>Default Value: 1000</li>
</ul>

### early_exag: the number of early exageration iterations. (Optional)

<ul>
<li>Data Type: Integer</li>
<li>Default Value: 250</li>
</ul>

### Y0: initial distribution in embedding space (randomly generated if nothing).(Optional)

<ul>
<li>Data Type: A numpy array of shape (number of data points, d).</li>
<li>Default Value: None</li>
<li>You should set this parameter to generate reproducible results.</li>
</ul>

### profile: whether to enable profiling for the algorithm. (Optional)

<ul>
<li>Data Type: Boolean</li>
<li>Default Value: False</li>
<li>Meaning: disable/enable profiling. If enabled the function return a 3-tuple: (Y, t, g), where Y is the embedding coordinates, t are the execution times of each module per iteration (size 6 x max_iter) and g contains the grid size, the embedding domain size (maximum(Y) - minimum(Y)), and the scaling factor s_k for the band-limited version, per dimension (size 3 x max_iter).</li>
</ul>

### np: number of threads (set to 0 to use all available cores) (Optional)

<ul>
<li>Data Type: Integer</li>
<li>Default Value: threading.active_count(), which returns the number of active threads in the current process.</li>
</ul>

### h: grid side length (Optional)

<ul>
<li>Data Type: Float</li>
<li>Default Value: 1.0</li>
</ul>

### u: either perplexity or value of λ (Optional)

<ul>
<li>Data Type: Integer</li>
<li>Default Value: 10</li>
</ul>

### k: number of nearest neighbors (for kNN formation) (Optional)

<ul>
<li>Data Type: Integer</li>
<li>Default Value: 30</li>
</ul>

### eta: learning parameter (Optional)

<ul>
<li>Data Type: Integer or Float</li>
<li>Default Value: 200.0</li>
</ul>

### alpha: exaggeration strength (applicable for first early_exag iterations). (Optional)

<ul>
<li>Data Type: Integer or Float</li>
<li>Default Value: 12</li>
</ul>

### fftw_single: Whether to use single-precision FFTW (Fast Fourier Transform) library. (Optional)

<ul>
<li>Data Type: Boolean</li>
<li>Default Value: False</li>
</ul>

### drop_leaf: remove edges connecting to leaf nodes. (Optional)

<ul>
<li>Data Type: Boolean</li>
<li>Default Value: False</li>
</ul>

### list_grid_size: the list of allowed grid size along each dimension. (Optional)

<ul>
<li>Data Type: A list of integers</li>
<li>Default Value: False.</li>
<li>Affects FFT performance; most efficient if the size is a product of small primes. </li>
</ul>

**Warning:** 

Because there is currently no replacement for Enum type in SGtSNEpy, we are missing the reduction of parameter you can change in Julia: **version**. Thus, the value will be its default value in Python.

### version: the version of the algorithm for computing repulsive terms. (Optional)

<ul>
<li>Data Type: Enum (Julia)</li>
<li>Default Value: NUCONV_BL</li>
<li>Options are:
</ul>
<li>SGtSNEpi.NUCONV_BL (default): band-limited, approximated via non-uniform convolution</li>
<li>SGtSNEpi.NUCONV: approximated via non-uniform convolution (higher resolution than SGtSNEpi.NUCONV_BL, slower execution time)</li>
<li>SGtSNEpi.EXACT: no approximation; quadratic complexity, use only with small datasets</li>
</ul>

## Returns

- Data Type: **numpy.ndarray** with three arrays: **numpy.int32, numpy.int32, numpy.float4**

## Examples

### 2D SG-t-SNE-П Embedding of **[Zachary's Karate Club graph](https://networkx.org/documentation/stable/_modules/networkx/generators/social.html#karate_club_graph)**

This example demonstrates the application of function `SGtSNEpiPy` using the **[SG-t-SNE-П](https://fcdimitr.github.io/SGtSNEpi.jl/stable/)** algorithm to visualize **[Zachary's Karate Club graph](https://networkx.org/documentation/stable/_modules/networkx/generators/social.html#karate_club_graph)** in `NetworkX`. The algorithm creates a low-dimensional embedding of the nodes in 2D while preserving their structural relationships. After the embedding, the example uses **[matplotlib.pyplot](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)** to visualize 2D embedding. Nodes are colored based on their club membership ('Mr. Hi' or 'Officer'). The scatter plot helps understand the social network's structure and patterns based on club affiliations.


```python
   from SGtSNEpiPy.SGtSNEpiPy import sgtsnepipy
   import networkx as nx
   import numpy as np
   import matplotlib.pyplot as plt

   # 'G' is the Zachary's Karate Club graph with 'club' attribute for each node
   
   G = nx.karate_club_graph()
   G_sparse_matrix = nx.to_scipy_sparse_matrix(G) 
   y = sgtsnepipy(G_sparse_matrix,d=2)
   
   # Separate the X and Y coordinates from the embedding 'y'
   X = y[:, 0]
   Y = y[:, 1]
   
   # Get the color for each node based on the 'club' attribute
   node_colors = ['red' if G.nodes[node]['club'] == 'Mr. Hi' else 'blue' for node in G.nodes]
   
   # Create a scatter plot to visualize the embedding and color the nodes
   plt.scatter(X, Y, c=node_colors, alpha=0.7)
   
   # Label the nodes with their numbers (node names)
   for node, (x, y) in enumerate(zip(X, Y)):
       plt.text(x, y, str(node))
   
   plt.title("2D SG-t-SNE-П Embedding of Zachary's Karate Club")
   plt.xlabel("Dimension 1")
   plt.ylabel("Dimension 2")
   plt.show()
```

<img width="599" alt="2D SG-t-SNE-Π Embedding of Zachary’s Karate CLub" src="https://github.com/CodyQin/SGtSNEpiPy/assets/125537769/7e299fc0-4162-4f0f-b39e-dfba6c6f59cc">

### 3D SG-t-SNE-П Embedding of **[Zachary's Karate Club graph](https://networkx.org/documentation/stable/_modules/networkx/generators/social.html#karate_club_graph)**

This example demonstrates the 3D embedding of same **[Zachary's Karate Club graph](https://networkx.org/documentation/stable/_modules/networkx/generators/social.html#karate_club_graph)** in `NetworkX`. 

After useing **[matplotlib.pyplot](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)** to generate a 3D graph, the example  refers to **[the website](https://sabopy.com/en/matplotlib-3d-14/)** that uses **[matplotlib.animation](https://matplotlib.org/stable/api/animation_api.html)** and **[mpl_toolkits.mplot3d.axes3d.Axes3D](https://matplotlib.org/3.5.1/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.html)** to create a gif file to rotate the 3D graph.

To save the animation to a gif file, please make sure you have **[Pillow](https://pillow.readthedocs.io/en/stable/)** in your `Python`. 
To install **[Pillow](https://pillow.readthedocs.io/en/stable/)** through Python from PyPi, issue

```
$ pip install SGtSNEpiPy
```

**The codes of 3D embedding**

```python
from SGtSNEpiPy.SGtSNEpiPy import sgtsnepipy
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import axes3d

G = nx.karate_club_graph()
G_sparse_matrix = nx.to_scipy_sparse_matrix(G) 
y = sgtsnepipy(G_sparse_matrix,d=3)

# Get the color for each node based on the 'club' attribute
node_colors = ['red' if G.nodes[node]['club'] == 'Mr. Hi' else 'blue' for node in G.nodes]

# Separate the X, Y, and Z coordinates from the 3D embedding 'y'
X = y[:, 0]
Y = y[:, 1]
Z = y[:, 2]

# Create the 3D scatter plot to visualize the embedding
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(X, Y, Z, c=node_colors, cmap='coolwarm')   # You can choose other colormaps too

# Label the nodes with their numbers (node names)
for node, (x, y, z) in zip(G.nodes, zip(X, Y, Z)):
    ax.text(x, y, z, node)

ax.set_title("3D SG-t-SNE-П Embedding of Zachary's Karate Club")
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Function to initialize the animation
def init():
    scatter.set_offsets(np.column_stack([X, Y, Z]))  # Update the scatter plot data
    return scatter,

# Function to update the plot for each frame of the animation
def animate(i):
    ax.view_init(elev=30., azim=3.6*i)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=100, interval=100, blit=True)

# Save the animation to a gif file
ani.save('3d_karate_club_animation.gif', writer='pillow')
```

![3d_karate_club_animation](https://github.com/CodyQin/SGtSNEpiPy/assets/125537769/998d13a8-7d2d-4fa3-b435-095783f1bdc0)


## Contact

Chenshuhao(Cody) Qin: chenshuhao.qin@duke.edu

Yihua(Aaron) Zhong: yihua.zhong@duke.edu


## Citation

<a id="1">[1]</a > Nikos Pitsianis, Alexandros-Stavros Iliopoulos, Dimitris Floros, Xiaobai Sun, **[Spaceland Embedding of Sparse Stochastic Graphs](https://doi.org/10.1109/HPEC.2019.8916505)**, In IEEE High Performance Extreme Computing Conference, 2019.

<a id="2">[2]</a > Nikos Pitsianis, Dimitris Floros, Alexandros-Stavros Iliopoulos, Xiaobai Sun, **[SG-t-SNE-Π: Swift Neighbor Embedding of Sparse Stochastic Graphs](https://doi.org/10.21105/joss.01577)**, Journal of Open Source Software, 4(39), 1577, 2019.

If you use this software, please cite the following paper.

```
@inproceedings{pitsianis2019sgtsnepi,
   author = {Pitsianis, Nikos and Iliopoulos, Alexandros-Stavros and Floros, Dimitris and Sun, Xiaobai},
   doi = {10.1109/HPEC.2019.8916505},
   booktitle = {IEEE High Performance Extreme Computing Conference},
   month = {11},
   title = {{Spaceland Embedding of Sparse Stochastic Graphs}},
   year = {2019}
}
```


