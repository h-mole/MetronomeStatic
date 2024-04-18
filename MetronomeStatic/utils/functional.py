import functools

try:
    from IPython import get_ipython

    ip = get_ipython()
    if ip is None:
        pass
    else:
        pass
except:
    pass


from typing import Callable, Generator, Generic, Iterable, Union

from MelodieFuncFlow.functional import VARTYPE, MelodieFrozenGenerator, MelodieGenerator, melodie_generator


# class MelodieGenerator(MelodieGenerator, Generic[VARTYPE]):
#     pass


# class MelodieFrozenGenerator(MelodieFrozenGenerator, Generic[VARTYPE]):
#     def __repr__(self) -> str:
#         return f"<SkyFrozenGenerator {self.inner}>"


# def melodie_generator(
#     f: "Callable[..., Union[Generator[VARTYPE, None, None], MelodieGenerator[VARTYPE]]]",
# ) -> "Callable[..., MelodieGenerator[VARTYPE]]":
#     @functools.wraps(
#         f,
#         assigned=(
#             ("__module__", "__name__", "__qualname__", "__doc__", "__annotation__")
#         ),
#     )
#     def inner(*args, **kwargs):
#         return MelodieGenerator(f(*args, **kwargs))

#     return inner


def to_generator(it: Iterable[VARTYPE]) -> Generator[VARTYPE, None, None]:
    for item in it:
        yield item
