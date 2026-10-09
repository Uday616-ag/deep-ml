
def calculate_parameters(layers: list[dict]) -> int:
    total = 0

    for layer in layers:

        if layer['type'] == 'dense':
            # Calculate weights
            total += layer['input_size'] * layer['output_size']

            # Add bias parameters if bias is True
            if layer.get('bias', True):
                total += layer['output_size']

        elif layer['type'] == 'conv2d':
            # Calculate weights
            total += (
                layer['in_channels']
                * layer['out_channels']
                * layer['kernel_size'] ** 2
            )

            # Add bias parameters if bias is True
            if layer.get('bias', True):
                total += layer['out_channels']

    return total

