# Nested_Pandas.ipynb versions: 
This directory contains versions of the `Nested_Pandas.ipynb` notebook.

These versions are essentially the same as the original, except they use an alternate `NestedFrame` creation strategy.

(Also, I had to alter the paths to work for my environment. Hopefully they're pretty simple to change back.)

## Nested_Pandas_1.ipynb has the first batch of changes:
- mainly just altering `convert_ens` and `ens_to_df` to construct nested frames differently
- the trick here is not to have a `NestedFrame` type per cell
- tbh, I followed this on a hunch and fed it into Claude along with a link to the nested pandas ReadTheDocs site!
- so, highly highly recommend looking it over and verifying that it's doing what's desired
- however, the code runs now, all the way until the cell that defines and runs `hats_to_qp`

## Nested_Pandas_2.ipynb will in theory be the rest of the notebook running
- however, I may just go to bed
- sorry if I do, but hopefully the first part is an ok lead
