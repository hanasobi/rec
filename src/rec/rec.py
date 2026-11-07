type Primitive = str | int | float | bool

_allowed = (str, int, float, bool)

class RecValue:
    def __init__(self, expected: Primitive, actual: Primitive):
        """ Stores and compares two primitive values.

        """
        for val in (expected, actual):
            if type(val) not in _allowed:
                raise TypeError(
                    f"Allowed are str, int, float and bool but not {type(val).__name__}"
               )
        self.expected = expected
        self.actual = actual

    def __repr__(self) -> str:
        return f"RecValue({self.expected!r},{self.actual!r})"
