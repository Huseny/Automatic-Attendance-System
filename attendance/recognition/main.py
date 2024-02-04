from os import mkdir, path
import pickle
from fisherfaces import *

class Recognizer:
    def __init__(self, labels: list, label_dict: dict):
        self.labels = labels
        self.label_dict = label_dict

        self.model = None
        self.models_dir = 'models'
        self.model_fname = 'fisherfaces.pkl'

    def fit(self, X, y):
        """Fit the model on the given data."""
        
        classifier = FisherFaces(
            n_components=2, pca_components=200, metric='euclidean',
        ).fit(X, y)

        self.model = classifier

        self.__save_model(
            classifier, path.join(self.models_dir, self.model_fname))

    def predict(self, image):
        if self.model is None:
            return

        label_idx, distances = self.model.predict(image, True)
        label_idx, distance = label_idx[0], distances[0][label_idx]

        return self.label_dict[label_idx], label_idx ,distance

    
    def load_model(self, fname):
        """Load the trained model."""
        assert path.exists(fname), 'Model does not exist. Train a model first'

        with open(fname, 'rb') as file_handle:
            self.model = pickle.load(file_handle)
        
        
    def __save_model(self, model, fname):
        """Save the trained model to disk."""
        model_directory = path.dirname(fname)
        if not path.exists(model_directory):
            mkdir(model_directory)

        with open(fname, 'wb') as file_handle:
            pickle.dump(model, file_handle)
