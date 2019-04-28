# Stubs for xml.etree.ElementPath (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Tuple, List, Union, TypeVar, Callable, Optional
from .ElementTree import _ElementInterface

xpath_tokenizer_re = ... # type: Callable[..., List[Tuple[str, str]]]


class xpath_descendant_or_self: ...

_T = TypeVar('_T')

class Path:
    def __init__(self, path: str) -> None: ...
    def find(self, element: _ElementInterface) -> Optional[_ElementInterface]: ...
    def findtext(self, element: _ElementInterface, default: _T=...) -> Union[str, _T]: ...
    def findall(self, element: _ElementInterface) -> List[_ElementInterface]: ...

def find(element: _ElementInterface, path: str) -> Optional[_ElementInterface]: ...

def findtext(element: _ElementInterface, path: str, default: _T=...) -> Union[str, _T]: ...

def findall(element: _ElementInterface, path: str) -> List[_ElementInterface]: ...
