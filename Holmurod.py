import math

def math_functions():
    # Square root
    sqrt_value = math.sqrt(16)
    
    # Factorial
    factorial_value = math.factorial(5)
    
    # Power
    power_value = math.pow(2, 3)
    
    # Trigonometric functions
    sin_value = math.sin(math.radians(30))
    cos_value = math.cos(math.radians(60))
    
    return {
        'sqrt': sqrt_value,
        'factorial': factorial_value,
        'power': power_value,
        'sin': sin_value,
        'cos': cos_value
    }

result = math_functions()
print(result)

def additional_math_functions():
    # Logarithm
    log_value = math.log(100)  # Natural logarithm (base e)
    
    # Exponential
    exp_value = math.exp(2)  # e^2
    
    return {
        'log': log_value,
        'exp': exp_value
    }

additional_result = additional_math_functions()
print(additional_result)