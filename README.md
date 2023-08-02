# SGtSNEpiPy

![3d_karate_club_animation](https://github.com/CodyQin/SGtSNEpiPy/assets/125537769/998d13a8-7d2d-4fa3-b435-095783f1bdc0)

## Overview

`SGtSNEpiPy` is a `Python` interface to
[`SG-t-SNE-П`](https://github.com/fcdimitr/SGtSNEpi.jl), a `Julia`
package. It enables the Python users to utilize and take full
advantage of the `SG-t-SNE-П` functionalities within the Python
ecosystem. With SGtSNEpiPy, users can swiftly and directly embed and
visualize a sparse graph in a $d$-dimensional space, $d=1,2,3$.  The
node adjacency on the graph is translated to spatial near-neighbor
proximity, as illustrated in the plots above.

 
The input is a sparse graph $G(V,E)$ represented by its adjacency
matrix A in sparse formats. The graph at input is either directed or
undirected, with the edges weighted or unweighted. The output is the
array of the $d$-dimensional vertex coordinates in the embedding
space.


### Introduction

SG-t-SNE extends [`t-SNE`](https???)[[?]](#??) from point feature data to graph data,
especially sparse graphs represented by their adjacency matrices in
sparse formats.  Here, SNE stands for stochastic near-neighbor
embedding, and SG stands for sparse graph.  `SG-t-SNE` makes a direct
translation of the node adjacency on the graph to spatial proximity in
the embedding space. In comparison, other graph embedding methods
first embed the vertices by spectral decomposition or learning,
followed by SNE.
By our empirical tests, and
by user feedback in [`SCARF`](https://scarf.readthedocs.io/en/latest/#)
[[3]](#3), the SG-t-SNE mapping has higher fidelity and efficiency.

The SG-t-SNE algorithm was first introduced in 2019 in the
[`paper`](https://ieeexplore.ieee.org/document/8916505)[[1]](#1).  A
software [`SG-t-SNE-П`](https://github.com/fcdimitr/sgtsnepi) in
`C/C++` was [released in
(2019](https://joss.theoj.org/papers/10.21105/joss.01577) [[2]](#2)
and then made accessible via Julia in 2021 with
[`SG-t-SNE-Pi`](https://github.com/fcdimitr/SGtSNEpi.jl).  This
package `SGtSNEpiPy` makes SG-t-SNE-Pi deployable to the Python
ecosystem.  This Python wrapper seamlessly converts the data formats
and translates all input and output arguments between Julia and
Python.

## Installation

To install `SGtSNEpiPy` through `Python` from `PyPi`, issue

```shell
$ pip install SGtSNEpiPy
```

The installation is straightforward: import `SGtSNEpiPy` 
and issue the command 

```python
from SGtSNEpiPy.SGtSNEpiPy import sgtsnepipy
```

*Warning:* 
The current version of `SGtSNEpiPy` requires WSL2 on Windows and Rosetta 2 on Apple ARM hardware.

More details can be found in **[the full
documentation](https://fcdimitr.github.io/SGtSNEpi.jl/stable)**.



## Usage

**SGtSNEpiPy.SGtSNEpiPy.sgtsnepipy**

The calling sequence is simple,

```python
Y = sgtsnepi(A, kwargs**)
```

where 
- `A`: the adjacency matrix of a graph G(V, E), in the compressive sparse row (CSR) format.
 Matrix A has $n=|V|$ rows, $n$ columns and $m$ nonzero elements represent the edges in E. 
 The graph is directed or undirected, with weighted or unweighted edges. The graph may
 represent a real-world network or the graph is synthetically generated.
 In the former case, the vertices may represent data feature vecors/points, and the edges represent
 the pariwise similarities of the feature vectors.

  *Data type*: [`scipy.sparse.csr.csr_matrix`](??) 

- `Y`: the $n\times d$ array of vertex coordinates in the $d$-dimensional embedding space.
  
  *Data type*: [`numpy.ndarray`](??).


## Key arguments 

- `d` (Integer): positive, the dimension of the embedding space. Default value: $2$ 

- `λ` (Integer or Float): positive, SG-t-SNE scaling factor. Default Value: $10$

### Optional and adanced SNE arguments (for control of search area and pace) 

- `max_iter` (Integer): the maximum number of iterations for the SNE optimization process.
   Default Value: 1000

- `early_exag` (Integer): the number of early exaggeration iterations. Default Value: 250

- `alpha` (Integer or Float): exaggeration strength for the first early_exag iterations.
   Default Value: 12

- `Y0`: an $n\times d$ numpy array for the initial embedding configuration in the embedding space.
   Default setting: None (the initial configuration is generated randomly). For reproducibility,
   the user is adviced to set and save `Y0`.

- `eta` (Integer or Float): the learning parameter. Default Value: 200.0

- `drop_leaf` (Boolean): if True, remove leaf nodes. Default Value: False

### Optional and advanced SG-t-SNE arguments (for performance tuning)

- `np` (Integer): number of threads (set to 0 to use all available cores).
   Default Value: threading.active_count(), which returns the number of active threads
   in the current process.

- `h` (Float): grid step length. Default Value: 1.0

- `list_grid_size` (a list of integers): the list of FFT grid sizes
   for data interpolation.  Default Value: False. The FFT module tends
   to be more efficient if the transform size can be factorred into
   small prime numbers.

- `profile` (Boolean): if True, 
   the function returns performance profile in a 3-tuple : (Y, t, g),
   where Y is the embedding coordinate array,
   t is the table of the execution times of each module per iteration (size 6 x max_iter),
   and g consists of the grid size, the embedding domain size (maximum(Y) - minimum(Y)),
   and the scaling factor s_k for the band-limited version, per dimension (size 3 x max_iter).
   Default Value: False 

- `fftw_single` (Boolean): if True, use the FFTW (Fast Fourier Transform) in single precision. 
    Default Value: False

## Examples

### 2D Embedding of the social network
[`Zachary's Karate Club`](https://networkx.org/documentation/stable/_modules/networkx/generators/social.html#karate_club_graph)

This simple example illustrates the use of `SGtSNEpiPy` for spatial
embedding and visualization of the Zachary's Karate Club network,
which can be found in [`NetworkX`](??).  The vertex coordinate array
returned by `SGtSNEpiPy` is passed to the plot function
[matplotlib.pyplot](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
for visualization. The vertices represent the club members, they are
colored according to the membership types, eihter 'Mr. Hi' or
'Officer'. The scatter plot is a spatial portrait of the social
network's structure and patterns.

** The 2D embedding code **

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

### 3D Embedding of [`Zachary's Karate Club`](https://networkx.org/documentation/stable/_modules/networkx/generators/social.html#karate_club_graph)

For the 3D embedding, `SGtSNEpiPy` is used the same way as for the 2D embedding.
For the 3D visualization, the graph can be viewed from various view points via rotation.
We created an animation gif file with 
[matplotlib.pyplot](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html),
[matplotlib.animation](https://matplotlib.org/stable/api/animation_api.html),
and
[mpl_toolkits.mplot3d.axes3d.Axes3D](https://matplotlib.org/3.5.1/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.html)
in [`matplotlib`](https://sabopy.com/en/matplotlib-3d-14/).

In order to save the animation to a gif file, install 
[`Pillow`](https://pillow.readthedocs.io/en/stable/) through Python from PyPi by
issuing the command

```
$ pip install SGtSNEpiPy
```

** The 3D embedding code **

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
scatter = ax.scatter(X, Y, Z, c=node_colors, cmap='coolwarm')   # One may choose other colormaps 

# Label the nodes with their names/indices  
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


To see the spatial embedding of larger networks/graphs, visit the website
[`SG-t-SNE-Pi`](https://t-sne-pi.cs.duke.edu/)

## Contact

Cody (Chenshuhao) Qin: chenshuhao.qin@duke.edu

Aaron (Yihua) Zhong: yihua.zhong@duke.edu


## Citation

<a id="1">[1]</a > Nikos Pitsianis, Alexandros-Stavros Iliopoulos,
Dimitris Floros, Xiaobai Sun, [Spaceland Embedding of Sparse
Stochastic Graphs](https://doi.org/10.1109/HPEC.2019.8916505), In
IEEE High Performance Extreme Computing Conference, 2019.

<a id="2">[2]</a > Nikos Pitsianis, Dimitris Floros,
Alexandros-Stavros Iliopoulos, Xiaobai Sun, [SG-t-SNE-Π: Swift
Neighbor Embedding of Sparse Stochastic
Graphs](https://doi.org/10.21105/joss.01577), Journal of Open Source
Software, 4(39), 1577, 2019.

<a id="3">[3]</a > Dhapola, P., Rodhe, J., Olofzon, R. et al. [Scarf
enables a highly memory-efficient analysis of large-scale single-cell
genomics data](https://doi.org/10.1038/s41467-022-32097-3), Nat Commun
13, 4616 (2022).

If you use this software, please cite the following paper:

``` @inproceedings{pitsianis2019sgtsnepi,
author = {Pitsianis, Nikos and Iliopoulos, Alexandros-Stavros and Floros,
          Dimitris and Sun, Xiaobai},
	  doi = {10.1109/HPEC.2019.8916505},
	  booktitle = {IEEE High Performance Extreme Computing Conference},
	  month = {11},
	  title  = {Spaceland Embedding of Sparse Stochastic Graphs}},
	  year = {2019} }
```


