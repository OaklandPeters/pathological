Plan
==========

STRATEGY FOR SIMPLIFYING BUILD PROCESS:
-----------------------------------------
Ignore the randomization aspects, espeically as related to combinators, and only have the 1-d deterministic walk thing.

This does mean that I will have to do very little with things like 'PrintableStrings'

STRATEGY FOR AVOIDING ABSTRACTION:
------------------------------------
Only write the interfaces immediately before I use them.

Build-steps
* stub interfaces: atomic.py, fixed.py
* atomics: for builtins: str, bool, int, float
* unit-tests for atomics
* containers interface: containers.py
* containers: for builtins: dict, list, tuple



Next-steps
=============
* Write unit-test that checks for the actual existance of every file stubbed in folder form atm (serializations/ csv, html, json, txt, xhtml, xml; structural/ callable, generator, hashable, iterator, mapping, mutable_mapping, mutable_sequence, mutable_set, sequence, set; containers/ _dict, _iter, _list, _object, _tuple; atomics/numbers/ )
* draft atomics:
* Reorganize: for scale-ability. Seperate Rangen, data-combiners (concept-monads?), from lists of pathological inputs
* Replace rand-gen, into the new organization


Mid-Range
=============
* Structural - should probably be BOTH a filter, and correspond to some discrete/fixed data (perhaps via union of categories for Python builtins)


Rather-Advanced
=================
* Callable[[], ] - with positional only this is an easier case than Arguments
* Arguments(*, **) tool for calling a function with all combinations. Basically, the Arguments() combinator + distribution


