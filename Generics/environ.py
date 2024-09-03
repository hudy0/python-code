import os
from typing import Generic, TypeVar, cast, Callable

T = TypeVar('T')
C = TypeVar('C')


class Environ(Generic[T]):
    def __init__(self,
                 name: str,
                 *,
                 default: str | None = None,
                 converter: Callable[[str | None], C] | None = None,
                 ) -> None:
        self.name = name
        self.default = default
        self.converter = converter

    @property
    def value(self) -> T:
        value = os.environ.get(self.name, self.default)
        if self.converter:
            return cast(T, self.converter(value))

        return cast(T, value)


def as_int(value: str | None) -> int:
    return int(value) if value else 0


if __name__ == '__main__':
    Environ("FOO").value
    Environ("FOO", default="BAR").value
    Environ("FOO", converter=as_int).value
