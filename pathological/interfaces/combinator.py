"""
WARNING:
    I've already gone too complicated with this, and am falling down a rabbit
    hole of category-theory.
    ... Make it simple, and use basic form of:
        Union
        Containers

There are a lot of ways that these data-generators can be combined.

Simplest basis case:
    Deterministic, indexed (and hence bounded-linear ~countable), ordering
    - eg a walk through all the cases.
    This doesn't work for infinite (or massive) generators.
    The point of this, it is easy to form some probability distribution on this
    indexered ordering


COMBINATORS:
---------------
Some combiners functions - idea splat. So some of these may not be used.
IMPORTANT NOTE: These all relate to the way to combine *the-data*,
NOT type-inclusion/subclassing - although that might be related.
    union
    container
    filter/refinement/projection
    intersection

The conserved structure of all of these combinators is:
    The combined structure has a 1-dimensional bounded ordering (index segment)
    and this index segment maps into the component categories.


Union Combinators: we have to garuntee that all component elements are mapped.
    Thus the elements of the index-segment of the union must be 1-to-1 to the
    elements of the index-segment of the component categories.

Container Combinators: ~generic containers (which of course == container-monads).
    Basically, the generators for these will have two parts: some rules for
    generating the various cases of structure of the container, and a function
    expecting input data generators. For example: Dict[Key, Value] - has some
    rules for generating structure, and those are defined in terms of Key, Value
    - where Key, Value are other generator structures.

Filter Combinator: carve out some subset of the category. This can be a simple
    filter function, or by writing a category carved out of the Universal/Any
    (this is an Existential) and taking the intersection between it and the
    subject category.
"""
