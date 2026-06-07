import random

from flag_generator import create_flag
from sort_names import sort_names


def test_create_flag_small(benchmark):
    img = benchmark(create_flag, 60, 40)
    assert img.size == (60, 40)


def test_create_flag_large(benchmark):
    img = benchmark(create_flag, 1920, 1080)
    assert img.size == (1920, 1080)


def test_sort_names_small(benchmark):
    data = [2, 3, 1, 6, 8, 3, 9, 5, 4, 7, 0]
    result = benchmark(sort_names, data)
    assert result == sorted(data, reverse=True)


def test_sort_names_large(benchmark):
    rng = random.Random(42)
    data = [rng.randint(0, 1_000_000) for _ in range(100_000)]
    result = benchmark(sort_names, data)
    assert len(result) == len(data)
