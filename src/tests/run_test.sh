#!/bin/sh
#python3 -m unittest -v
coverage run -m unittest
coverage html
coverage erase
