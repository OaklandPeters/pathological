
Basics
-----------
data_generator.py: the base interface for all categories of data-generators.


Validity
--------------
valid.py: provides data-points from within some category. This is used in unit-testing to confirm that your API handles all of the cases it is supposed to.

invalid.py: data which is not in the category, but which is commonly encountered for that category. Such as string data in a different encoding, or floating point numbers where integers are expected. This is used in unit-testing to confirm that your API does not treat invalid things as valid, and also does not terminally crash on them.

malformed.py: data points which are just incorrectly structured. These are things your API is *supposed* to choke on, such as a JSON file with mismatched brackets.


Sizing
------------
fixed.py: the most common kind of category - which simply has a fixed length sequence of data-points it reads from. This vaguely corresponds to 'counted'/'countable' (ie it is feasible to count all of them at import time).

lazy.py: used for data-generators where generating *all* of the data can be time-consuming, such as ones that need to read files. This can be either Fixed or Unfixed

unfixed.py: data generation which is either infinite, or essentially so, and is created by a generating-function, rather than some pre-defined list of data-points. This is used primarily to create randomized data from a huge category (such as all-integers, or all-expressable strings). This vaguely corresponds to 'uncounted'/'uncountable' (because it is not reasonable to count it, even if it might actually be mathematically countable).


Structure
-------------
atomic.py: data-generators without internal structure.

containers.py: pythonic data-containers, such as lists, dicts. To be able to specify the internal data-types for these in terms of other data-generators, will require a 'Container' combinator.

serializable.py: categories of data corresponding to a file-format

combinator.py: ways to combine categories. Primary and first-draft combinators: union, . This interacts in a complicated way with randomization.

structural.py: **I'm not sure how I want to handle this yet**. Things like, boolean conversions (Truthy, Falsey), mapping, sequence. Not at all sure if this should be a filter over some other classes, or a pre-built list of examples


Randomization
----------------
randomizable.py: used to randomly choose data-points from within the category

distributions.py: essentially, specifying how to randomize over a cominator.


Conveniences
---------------
examples.py: examples of how these should be used.

convenience.py: collected union-ed/filter-ed categories which are commonly used.


STRATEGY FOR SIMPLIFYING BUILD PROCESS:
-----------------------------------------
Ignore the randomization aspects, espeically as related to combinators, and only have the 1-d deterministic walk thing.

This does mean that I will have to do very little with things like 'PrintableStrings'
