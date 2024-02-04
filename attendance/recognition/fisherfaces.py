import numpy as np
from scipy.spatial import distance
from pca import PCA
from lda import LDA

class FisherFaces():
    def __init__(self, pca_components: int = 25, n_components : int = 2, metric: str = 'euclidean'):
        self.pca = None
        self.lda = None
        self.metric = metric
        self.subspace_basis = None
        self.n_components = n_components
        self.pca_components = pca_components

    def fit(self, X, y):
        self.pca = PCA(n_components=self.pca_components).fit(X)
        projected = self.pca.project(X)
        self.lda = LDA(n_components=self.n_components).fit(projected, y)

        self.subspace_basis = np.dot(self.pca.subspace_basis[:, : self.pca.n_components], self.lda.subspace_basis[:, : self.lda.n_components])

        return self
    
    def predict(self, X, return_distances=False):
        assert self.lda is not None, \
            'You must fit %s first' % self.__class__.__name__


        class_means = self.lda.class_means
        projected = self.__project(np.atleast_2d(X))

        distances = distance.cdist(projected, class_means, metric=self.metric)
        min_indices = np.argmin(distances, axis=1)

        if return_distances:
            return min_indices, distances
        return min_indices

    def __project(self, X):
        assert self.subspace_basis is not None, \
            'You must fit %s before you can project' % self.__class__.__name__
        return np.dot(X - self.pca.X_mean, self.subspace_basis)

    def __reconstruct(self, X):
        assert self.subspace_basis is not None, \
            'You must fit %s before you can reconstruct' % self.__class__.__name__
        return X.dot(self.lda.subspace_basis[:, : self.lda.n_components].T).dot(self.pca.subspace_basis[:, : self.pca.n_components].T) + self.pca.X_mean

    