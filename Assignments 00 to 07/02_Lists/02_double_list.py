def double_numbers(numbers):
    # Double each element in the list
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2
    return numbers

def main():
    numbers = [6, 8, 10, 12, 14, 16, 18, 20]
    doubled_numbers = double_numbers(numbers)
    print(f"Doubled numbers: {doubled_numbers}")

if __name__ == '__main__':
    main()
