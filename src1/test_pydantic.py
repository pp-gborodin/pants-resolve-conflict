import pydantic
from importlib.metadata import version


def test_pydantic_2():
    assert version(pydantic.__name__).startswith("1.")
