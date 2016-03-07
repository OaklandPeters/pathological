"""

On Naming
-----------
This might be better called 'stream' or something like that. Or DataGenerator
'Category' is accurate, but I'm avoiding that because of potential conflicts
with a category-theoretic library I'm building concurrently.


@todo: See if pairs/indices/values can be Iterable, instead of Sequence
"""
import typing
import abc


# Typedefs
ValueType = typing.TypeVar('ValueType')
KeyType = typing.TypeVar('KeyType')
Pair = typing.Tuple[ValueType, KeyType]


class DataGroup(typing.Generic[KeyType, ValueType], metaclass=abc.ABCMeta):
    """
    Base interface for combinable and iterable data-groups.
    This does not correspond directly to either a Sequence or a Mapping.
    Like a sequence: Iterating across it yields it's values
    Like a mapping: it is primarily defined in terms of it's indices, and
        it can have relatively complicated indices, and has
        an equivalent of keys/values
    """
    @abc.abstractmethod
    def keys(self) -> typing.Sequence[KeyType]:
        return NotImplemented

    @abc.abstractmethod
    def __getitem__(self, index: KeyType) -> ValueType:
        return NotImplemented

    def values(self) -> typing.Iterable[ValueType]:
        """For subclasses which directly store the data,
        it can be much more efficient to directly return it
        here."""
        for key in self.keys():
            yield self[key]

    def items(self):
        for key in self.keys():
            yield (key, self[key])

    def __len__(self):
        return len(self.keys())

    def __iter__(self):
        return iter(self.values())
