def fibonacci(n):
    """Return a list containing the first n Fibonacci numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib


if __name__ == "__main__":
    count = 20
    print(f"First {count} Fibonacci numbers:")
    print(fibonacci(count))
