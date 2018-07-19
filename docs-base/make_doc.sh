#!/bin/sh

sphinx-apidoc -f -o . ../src
sphinx-apidoc -f -o . ../src/Algorithms
sphinx-apidoc -f -o . ../src/Preprocessing
sphinx-apidoc -f -o . ../src/Graphs
sphinx-apidoc -f -o . ../src/PrintHelpers
sphinx-apidoc -f -o . ../src/IOFiles

make html
