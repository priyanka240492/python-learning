
#==================================================
# TRY-EXCEPT Vs IF RAISE Exeception Handling
#==================================================
def divide_numbers_try_except(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Invalid input type. Please provide numbers."
    else: # Optional else block. Can be returned directly without else.
        return result

def divide_numbers_if_raise(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Invalid input type. Please provide numbers.")
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2
# Example usage:
if __name__ == "__main__":
    print("-----Execution started with TRY-EXCEPT-----")

    print(divide_numbers_try_except(10, 2))  # Output: 5.0
    print(divide_numbers_try_except(10, 0))  # Output: Error: Cannot divide by zero.
    print(divide_numbers_try_except(10, 'a'))  # Output: Error: Invalid input type. Please provide numbers.

    print("-----Execution completed without breaking with TRY-EXCEPT Exception-----")

    print("===================================================")

    print("-----Execution started with IF RAISE-----")

    print(divide_numbers_if_raise(20, 2))  # Output: 5.0
    print(divide_numbers_if_raise(10, 0))  # Raises ValueError
    print(divide_numbers_if_raise(10, 'a'))  # Raises TypeError

    print("-----Execution flow broken with IF-RAISE exception -----")


