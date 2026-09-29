import math

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
    value = x
    derivative = 1

    for func in reversed(functions):

        if func == "square":
            derivative *= 2 * value
            value = value ** 2

        elif func == "sin":
            derivative *= math.cos(value)
            value = math.sin(value)

        elif func == "exp":
            derivative *= math.exp(value)
            value = math.exp(value)

        elif func == "log":
            derivative *= 1 / value
            value = math.log(value)

    return derivative