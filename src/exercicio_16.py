def odd_numbers(n: int) -> list[int]:
    """
    Retorna os números ímpares de 1 até n.

    Args:
        n (int): limite superior

    Returns:
        list[int]: lista de números ímpares
    """
    return [num for num in range(1, n + 1) if num % 2 != 0]
