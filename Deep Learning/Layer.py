# base class
class Layer:
    def __init__(self):
        self.input  = None
        self.output = None

    # computes the output Y of a layer for a given input X
    def forward_propagation(self, input):
        raise NotImplementedError

    # compute dE/dX for a given dE/dY (and update parameters in any)
    def back_propagation(self, output_error, learning_rate):
        raise NotImplementedError


if __name__ == "__main__":
    pass