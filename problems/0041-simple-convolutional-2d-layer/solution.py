import numpy as np

def simple_conv2d(input_matrix: np.ndarray,
                  kernel: np.ndarray,
                  padding: int,
                  stride: int):

    # Get input dimensions
    input_height, input_width = input_matrix.shape

    # Get kernel dimensions
    kernel_height, kernel_width = kernel.shape

    # Add padding
    inpmat = np.pad(
        input_matrix,
        pad_width=padding,
        mode='constant'
    )

    # Dimensions after padding
    new_height = input_height + 2 * padding
    new_width = input_width + 2 * padding

    # Output dimensions
    output_height = (new_height - kernel_height) // stride + 1
    output_width = (new_width - kernel_width) // stride + 1

    # Create output matrix
    output = np.zeros((output_height, output_width))

    # Convolution
    for i in range(
        0,
        new_height - kernel_height + 1,
        stride
    ):

        for j in range(
            0,
            new_width - kernel_width + 1,
            stride
        ):

            # Extract window
            window = inpmat[
                i:i + kernel_height,
                j:j + kernel_width
            ]

            # Element-wise multiplication + sum
            result = np.sum(window * kernel)

            # Store result
            output[i // stride, j // stride] = result

    return output