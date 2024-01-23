from functools import lru_cache

import time


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} took {execution_time:.4f} seconds to execute")
        return result

    return wrapper


@lru_cache(maxsize=128, typed=False)
def count_value(sentence: str) -> int:
    return sum(sentence.count(vowel) for vowel in "AEIUaeiu")


@measure_execution_time
def main() -> None:
    sentences: list[str] = ["Hello, World", "I dunno, must be a king.", "We are three wise men."]

    for sentence in sentences:
        for i in range(1_000_000):
            count_value(sentence)


if __name__ == "__main__":
    main()
