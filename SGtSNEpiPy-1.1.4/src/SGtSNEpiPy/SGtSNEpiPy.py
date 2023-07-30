from juliacall import Main as jl
import scipy.sparse as sp
import numpy
import threading


# This function uses julia package SGtSNEpi within Python to process a sparse array in python
# input of the function can be any type of sparse array, namely COO,CSR or CSC
# If this function does not operate normally, find which path your downloaded juliacall, then use the corresopongding python interepter 
# We use the Conda package manager

def nextprod(nums, x):
    next_num = x + 1
    while True:
        for num in nums:
            if next_num % num != 0:
                break
        else:
            return next_num
        next_num += 1

#Default parameter: version, exact, bound_box

def sgtsnepipy(A, d=2, λ=10, max_iter=1000, early_exag=250, Y0=None, profile=False, np=threading.active_count(), h=1.0, u=10, k=30, eta=200.0, alpha=12, fftw_single=False, drop_leaf=False, list_grid_size=False, bound_box=-1.0, par_scheme_grid_thres=None):

    jl.seval('using Pkg')
    jl.seval('Pkg.add("SGtSNEpi")')
    jl.seval('using SparseArrays')
    jl.seval('using SGtSNEpi')

    row, column, value = sp.find(A)
    row = [x + 1 for x in row]
    column = [y + 1 for y in column]
    row_array = jl.Array(row)
    column_array = jl.Array(column)
    value_array = jl.Array(value)
    m, n = A.shape
    array_jl = jl.SparseArrays.sparse(row_array, column_array, value_array, m, n)

    if list_grid_size == False:
        list_grid_size = [x for x in range(16, 513) if x == nextprod((2, 3, 5), x)]

    if par_scheme_grid_thres is None:
        par_scheme_grid_thres = jl.SGtSNEpi.get_parallelism_strategy_threshold(d, np)

    # Call the Julia function with the parameters
    result = jl.sgtsnepi(array_jl, d=d, λ=λ, max_iter=max_iter, early_exag=early_exag, Y0=Y0, profile=profile, np=np, h=h, u=u, k=k, eta=eta, alpha=alpha, fftw_single=fftw_single, drop_leaf=drop_leaf, list_grid_size=list_grid_size, bound_box=bound_box, par_scheme_grid_thres=par_scheme_grid_thres)

    result_py = numpy.array(result, dtype=numpy.float64)
    return result_py