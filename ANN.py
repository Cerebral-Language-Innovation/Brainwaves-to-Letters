import tensorflow as tf

# TODO: Continue along with this code. This is an early demonstration of the ideal structure for QCLI code so that
#  models can be reused easily.


class ANN:
    """
    This class will compile create an ANN for EEG machine learning in a reusable format (since this is OOP).
    """
    def __init__(self, X_train):
        self.X_train = X_train
        self.ann = tf.keras.models.Sequential()  # Initializing the ANN with TensorFlow Sequential

    def add_dense_layer(self, units, activation_function, first_layer):
        """
        Creates a new layer in the ANN
        :param units is the size of the output for the layer.
        :param activation_function sets the activation function for that layer.
        :param first_layer is a boolean indicating if it is the first layer added.
        :returns a boolean depending on whether or not the layer was created successfully.
        """
        if units < 1 or activation_function not in ['relu', 'sigmoid', 'softmax', 'softplus', 'softsign', 'tanh',
                                                    'selu', 'elu', 'exponential', ]:
            return False
        if first_layer:
            self.ann.add(tf.keras.layers.Dense(units=units, activation=activation_function, input_shape=self.X_train.shape))
        else:
            self.ann.add(tf.keras.layers.Dense(units=units, activation=activation_function))
        return True
