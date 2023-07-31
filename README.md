# SGtSNEpiPy

## Overview

SGtSNEpiPy is a Python interface, i.e., a wrapper to 'SG-t-SNE-П (https://github.com/fcdimitr/SGtSNEpi.jl)', implemented using the 'JuliaCall (https://cjdoris.github.io/PythonCall.jl/stable/juliacall/)' from 'PythonCall & JuliaCall (https://cjdoris.github.io/PythonCall.jl/stable/)' package.

### Introduction

The algorithm SG-t-SNE and the software t-SNE-Π were first described in Reference **[(Nikos Pitsianis, Alexandros-Stavros Iliopoulos, Dimitris Floros, Xiaobai Sun (2019))](https://ieeexplore.ieee.org/document/8916505)** and released on **[GitHub](https://github.com/fcdimitr/sgtsnepi)** in June 2019 **[(Nikos Pitsianis, Dimitris Floros, Alexandros-Stavros Iliopoulos, Xiaobai Sun (2019))](https://joss.theoj.org/papers/10.21105/joss.01577)**. SG-t-SNE-П is a nonlinear method that directly embeds large, sparse, stochastic graphs into low-dimensional spaces without requiring vertex features to reside in or be transformed into a metric space. The approach is inspired by and builds upon the core principle of t-SNE for nonlinear dimensionality reduction and data visualization. Our implementation provides high-performance software for 1D, 2D, and 3D embedding of large sparse graphs on shared memory multicore computers.


SGtSNEpi, a Julia interface, i.e., a wrapper to SG-t-SNE-Π was released on **[GitHub](https://github.com/fcdimitr/SGtSNEpi.jl)** in 2019. SGtSNEpiPy uses **[JuliaCall](https://cjdoris.github.io/PythonCall.jl/stable/juliacall/)** module to make this Julia interface SGtSNEpi readily deployable to the Python ecosystem.

## Installation

From PyPi

```
$ pip install SGtSNEpiPy
```

The installation is successful if you can import SGtSNEpiPy 
and run the command line tool:

```
$ python -c 'from SGtSNEpiPy.SGtSNEpiPy import sgtsnepipy'
```

**Warning:** 
SGtSNEpiPy is currently not working on Windows and native M1 Macs: Either use WSL2 on Windows or use the package via rosetta2 on M1 Macs.

**Note**: The rest of the content remains unchanged as it does not contain any reST-specific elements.


See **[the full documentation](https://fcdimitr.github.io/SGtSNEpi.jl/stable)** for moredetails.



## Parameters

**SGtSNEpiPy.SGtSNEpiPy.sgtsnepipy**

This package only has one method currently.

```
   Y = sgtsnepi(A)
```


### A: the input CSR sparse matrix representing the data points' pairwise similarities. (Mandatory)

- Data Type: `scipy.sparse.csr.csr_matrix` (The matrix includes row, value, value, whose type are all `numpy.ndarray` with three arrays of `numpy.int32`, `numpy.int32`, `numpy.int64`), that is a CSR sparse matrix generated by package `scipy`.

### Returns Y: array with the coordinates of the embedding of the graph nodes

- Data Type: `numpy.ndarray` with three arrays: `numpy.int32`, `numpy.int32`, `numpy.float4` ** **THIS CANNOT BE CORRECT!!!** **


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

## Examples
Here is an example to use function sgtsnepipy to generate a 2D embedding of an ER model.
You have to use import networkx to generate a ER graph and matplotlib to visualize the embedding


```
    from SGtSNEpiPy.SGtSNEpiPy import sgtsnepipy
    import networkx as nx
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm
    
    # Generate ER Model graph
    n = 1000  # Number of nodes
    p = 0.2  # Probability of an edge between any two nodes
    G = nx.erdos_renyi_graph(n=n, p=p, seed=170)

    G_sparse_matrix = nx.to_scipy_sparse_matrix(G) 
    y = sgtsnepipy(G_sparse_matrix)

    # Now use the SGtSNEpi to show the visualization after embedding
    # Get the degrees of the nodes in the graph
    node_degrees = np.array([G.degree(node) for node in G.nodes])
    # Normalize the degrees to the range [0, 1] for color mapping
    node_degrees_normalized = node_degrees / np.max(node_degrees)
    # Create a color map
    color_map = cm.get_cmap('viridis')  # 'viridis' is just an example, you can use any color map you like
    # Apply the color map to your normalized degrees
    colors = color_map(node_degrees_normalized)

    plt.scatter(y[:,0], y[:,1], c=colors)
    plt.colorbar(label='Node degree')
    plt.title("2D embedding of ER model (n = 1000, p = 0.2, seed = 170)")

    plt.show()
```


## Contact

Chenshuhao(Cody) Qin: chenshuhao.qin@duke.edu

Yihua(Aaron) Zhong: yihua.zhong@duke.edu


## Citation

- Nikos Pitsianis, Alexandros-Stavros Iliopoulos, Dimitris Floros, Xiaobai Sun, **[Spaceland Embedding of Sparse Stochastic Graphs](https://doi.org/10.1109/HPEC.2019.8916505)**, In IEEE High Performance Extreme Computing Conference, 2019.
- Nikos Pitsianis, Dimitris Floros, Alexandros-Stavros Iliopoulos, Xiaobai Sun, **[SG-t-SNE-Π: Swift Neighbor Embedding of Sparse Stochastic Graphs](https://doi.org/10.21105/joss.01577)**, Journal of Open Source Software, 4(39), 1577, 2019.

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
