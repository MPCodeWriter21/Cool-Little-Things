import sys
from typing import Any, List, Self


class Cout:

    def __lshift__(self, obj) -> Self:
        sys.stdout.write(str(obj))
        sys.stdout.flush()
        return self


class Cin:

    def __rshift__(self, obj: List[Any]) -> Self:
        n = len(obj) - 1
        if n >= 0:
            data = []
            while n >= 0:
                tmp = sys.stdin.readline()[:-1].split(maxsplit=n)
                data.extend(tmp)
                n -= len(tmp)
                tmp = []
                for i, item in enumerate(data):
                    if obj[i] is None:
                        tmp.append(item)
                    elif isinstance(obj[i], type):
                        try:
                            tmp.append(obj[i](item))
                        except ValueError:
                            tmp.append(obj[i]())
                    else:
                        try:
                            tmp.append(obj[i].__class__(item))
                        except ValueError:
                            tmp.append(obj[i])
                obj[:] = tmp
        else:
            obj[:] = sys.stdin.readline()[:-1].split()

        return self


cout = Cout()
cin = Cin()
