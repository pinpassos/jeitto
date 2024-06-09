def calculate_fibonacci_sequence(n_terms: int) -> int:
    """Returns the Fibonacci sequence up to the n-th term.

    Args:
        n_terms (int): The number of terms of the Fibonacci sequence.
    """
    if n_terms < 1:
        raise ValueError("n_terms must be an positive integer")

    elif n_terms == 1:
        return 0

    elif n_terms == 2:
        return 1

    else:
        first_term, second_term = 0, 1
        for _ in range(2, n_terms):
            current_value = first_term + second_term
            first_term, second_term = second_term, current_value
        return current_value


if __name__ == "__main__":
    assert calculate_fibonacci_sequence(10) == 34
    assert calculate_fibonacci_sequence(12) == 89
    assert calculate_fibonacci_sequence(13) == 144
    assert calculate_fibonacci_sequence(20) == 4181
    assert calculate_fibonacci_sequence(30) == 514229
