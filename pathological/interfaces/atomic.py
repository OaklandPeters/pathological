"""
Data for unstructured/non-container types.
"""
import typing

from .data_group import DataGroup
from .fixed import Fixed


class Atomic(DataGroup):
    """
    For atomic data-groups, the values are stored in a linear sequence.
    """
    def __repr__(self):
        return "<{0}>".format(self.__class__.__name__)

    def indices(self):
        return range(len(self.values()))

    def __getitem__(self, index):
        return self._values[index]

    def __repr__(self):
        return "<{0}>".format(self.__class__.__name__)



class FixedAtomic(Fixed, Atomic):
    """
    Commonly used, and basic data-group.
    Integers, strings, etc
    """
    def __getitem__(self, index):
        """
        Reimplemented for efficiency
        """
        return self._values[index]






# Typedefs
KeyType = typing.TypeVar('KeyType', bound=int)
ValueType = typing.TypeVar('ValueType')


class Atomic(DataGroup[KeyType, ValueType]):
    """
    Refines the DataGroup abstract interface, to require only a single
    abstract *property* - '_values'.
    '_values' is usually implemented at the class level.
    """
    # Abstractmethods
    @abstractproperty
    def _values(self) -> typing.Sequence:
        return NotImplemented

    # Derived methods
    def values(self):
        return self._values


class RandAtomics(Fixed):
    """Refined convenience abstract class.
    Requires only a single abstract *property*: _values
    Which is usually implemented at the class level
    """   
    @abstractproperty
    def _values(self) -> typing.Sequence:
        return NotImplemented

    # Mixin methods
    def __init__(self, seed=None):
        self.seed = seed
        self.Random = random.Random(self.seed)
        #super().__init__(self, seed=seed)

    def values(self):
        return self._values

    def indices(self):
        return range(len(self.values()))

    def __getitem__(self, index):
        return self._values[index]

    def __repr__(self):
        return "<{0}>".format(self.__class__.__name__)
