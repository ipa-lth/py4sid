from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

from synthetic_data import rand_lds_and_data
from estimation import estimate_parameters_4sid
from util import plot_eigvals

# TODO use multiple sequences to estimate moments
# TODO work out how the complexity scales with data/algorithm parameters
# TODO recovery experiments

if __name__ == '__main__':
    # data parameters
    n, p = 3, 5
    T = 10000

    # algorithm parameters
    i = 40

    # generate a system and simulate from it
    (A,B,C,D), (x,y) = rand_lds_and_data(T,n,p)

    # try to recover parameters (up to similarity transform)
    Ahat, Bhat, Chat, Dhat = estimate_parameters_4sid(y,i,nhat=n)

    # inspect the results a bit
    plt.figure()
    print np.linalg.eigvals(A)
    print np.linalg.eigvals(Ahat)
    plot_eigvals(A,'bo')
    plot_eigvals(Ahat,'rx')

    plt.show()
