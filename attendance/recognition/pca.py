import numpy as np

class PCA():
    def __init__(self, *args, **kwargs):
        self.X_mean = None
        self.eigenvalues = None
        self.subspace_basis = None
        self.n_components = None

    def fit(self, X, y=None):
        assert X.ndim == 2, 'X can only be a 2-d matrix'

        # Center the data
        self.X_mean = np.mean(X, axis=0)
        X = X - self.X_mean


        use_dual_pca = X.shape[1] > X.shape[0]

        if use_dual_pca:
            X = X.T

        # Estimate the covariance matrix
        C = np.dot(X.T, X) / (X.shape[0] - 1)

        U, S, V = np.linalg.svd(C)

        if use_dual_pca:
            U = X.dot(U).dot(np.diag(1 / np.sqrt(S * (X.shape[0] - 1))))

        self.subspace_basis = U
        self.eigenvalues = S

        return self

    def project(self, X):
        assert self.subspace_basis is not None, \
            'You must fit %s before you can project' % self.__class__.__name__
        X = X - self.X_mean
        return np.dot(X, self.subspace_basis[:, :self.n_components])

    def reconstruct(self, X):
        assert self.subspace_basis is not None, \
            'You must fit %s before you can reconstruct' % self.__class__.__name__
        return np.dot(X, self.subspace_basis[:, :self.n_components].T) + self.X_mean

