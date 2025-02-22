def add_numbers(a, b):
    result = a + b
    return result

def multiply_numbers(x, y):
    result = x * y
    return result

def main():
    num1 = 10
    num2 = 5

    sum_result = add_numbers(num1, num2)
    product_result = multiply_numbers(num1, num2)

    print("Debugging ends here!", sum_result, product_result)

if __name__ == "__main__":
    main()
