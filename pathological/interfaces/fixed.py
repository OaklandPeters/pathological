"""
"""
import abc
import typing

from .data_group import DataGroup


# Typedefs
KeyType = typing.TypeVar('KeyType', bound=int)
ValueType = typing.TypeVar('ValueType')


class Fixed(DataGroup[KeyType, ValueType]):
    """
    A data-group which reads from a fixed static variable.

    Refines the DataGroup abstract interface, to require only a single
    abstract *property* - '_values'.
    '_values' is usually implemented at the class level.

    Fixed exists primarily to seperate and contrast with 'Unfixed' and 'Lazy'
    """
    # Abstractmethods
    @abc.abstractproperty
    def _values(self) -> typing.Sequence:
        return NotImplemented

    #
    # Derived methods
    #
    def values(self):
        return self._values
