import numpy as np

class LDA():
    def __init__(self, auto_components=True, *args, **kwargs):
        self.eigenvalues = None
        self.class_means = None
        self.subspace_basis = None
        self.n_components = None
        self.auto_components = auto_components

    def fit(self, X, y):
        assert X.shape[0] == y.shape[0], 'X and y dimensions do not match.'

        n_classes = np.max(y) + 1
        n_samples, n_features = X.shape

        if self.auto_components:
            self.n_components = n_classes - 1
        else:
            assert self.n_components <= n_classes, \
                'LDA has (c - 1) non-zero eigenvalues. ' \
                'Please change n_components to <= '

        # Compute the class means
        class_means = np.zeros((n_classes, n_features))
        for i in range(n_classes):
            class_means[i, :] = np.mean(X[y == i], axis=0)

        mean = np.mean(class_means, axis=0)

        Sw, Sb = 0, 0
        for i in range(n_classes):
            # Compute the within class scatter matrix
            for j in X[y == i]:
                val = np.atleast_2d(j - class_means[i])
                Sw += np.dot(val.T, val)

            # Compute the between class scatter matrix
            val = np.atleast_2d(class_means[i] - mean)
            Sb += n_samples * np.dot(val.T, val)

        # Get the eigenvalues and eigenvectors in ascending order
        eigvals, eigvecs = np.linalg.eig(np.dot(np.linalg.inv(Sw), Sb))
        sorted_idx = np.argsort(eigvals)[::-1]
        eigvals, eigvecs = eigvals[sorted_idx], eigvecs[:, sorted_idx]

        self.subspace_basis = eigvecs.astype(np.float64)
        self.eigenvalues = eigvals

        self.class_means = np.dot(class_means, self.subspace_basis[:, :self.n_components])

        return self

    def project(self, X):
        assert self.subspace_basis is not None, \
            'You must fit %s before you can project' % self.__class__.__name__
        return np.dot(X, self.subspace_basis[:, :self.n_components])

    def reconstruct(self, X):
        assert self.subspace_basis is not None, \
            'You must fit %s before you can reconstruct' % self.__class__.__name__
        return np.dot(X, self.subspace_basis[:, :self.n_components].T)