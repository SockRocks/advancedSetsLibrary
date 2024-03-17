*********************Installation*********************
- Download the zipfiile
- copy all files into your current project directory
- invoke `from newsets import Set`
- Done!

*********************Simple Operations*********************
+ Declare a set `A = Set(1,2,3..., universe=[universal set])`
+ If B is another set to find the union just do `A + B`
+ The intersection of A and B is `A & B`
+ `A.powerSet()` calculates the powerset of A
+ `A - B` outputs the set difference
+ `A*B` calculates the cartesian product of the two sets (to calculate tripple products and higher use `A.cartesianProduct(*sets*)`
+ `A.complement()` returns the complement of A with the input universe
+ `A.setDisplayMode()` displays each element of A one by one by hitting enter
+ Lists and sets can be freely converted between eachother by calling `A.__list__()` to convert A to a list or calling Set(*list*) to convert the list to a set object

___Warning____
As of current, do not create sets of sets by passing in another Set object, instead just pass a list of the elements. This will be fixed soon.
