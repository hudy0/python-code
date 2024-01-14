from dataclasses import dataclass, asdict, astuple


@dataclass(frozen=True, order=True)
class Comment:
    id: int
    text: str


def main():
    comment = Comment(1, "I Write python")
    print(comment)
    print(asdict(comment))
    print(astuple(comment))


if __name__ == "__main__":
    main()
