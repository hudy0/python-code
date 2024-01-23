from attrs import define, frozen, field, Factory


@define(kw_only=True)
class User:
    id: int = 0
    name: str = field(default="")
    email: str = field(repr=False)


user = User(id=1, name="<Just A Name", email="justtest@example.com")
print(user)
