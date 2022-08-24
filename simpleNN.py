"""
Simple 2 dim -> 2 dim neural net, purely functional. For learning to visualize.
"""

# each input to output 1
weight11, weight21 = 0, 0
# each input to output 2
weight12, weight22 = 0, 0

def classify(input1: float, input2: float):
    """
    Take two inputs and classify outputs.
    The outputs are the weighted sum of the inputs
    """
    output1: float = input1 * weight11 + input2 * weight21
    output2: float = input1 * weight12 + input2 * weight22

    # return true if output1 is smallest. Otherwise return false
    # output2 is thus true and output1 is false
    return output1 < output2