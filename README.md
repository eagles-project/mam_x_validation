# MAM Cross Validation

This repository contains input data and scripts that can be used to perform
code-to-code comparisons of modal aerosol models with MAM. Each directory is
devoted to a single set of parameterizations for a single aerosol process.

## Tools

The following tools are useful for performing cross validation with the files
in this repository.

### Skywalker

Many of the input files are written in a YAML format used by Skywalker, a
parameter study tool written for the HAERO modal aerosol code. The file format
sets input parameters for various quantities, and lists a set of parameters to
study in an `ensemble` block.

Many of the Skywalker YAML files here are "user tests", which list specific
parameters in `user` and `ensemble:user` blocks. These user tests require you
to write a program that uses Skywalker to read input and generate corresponding
output. Skywalker programs can easily emit Python modules or NCL data files that
can be used to plot figures or perform quantitative comparisons.
