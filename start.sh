#!/bin/bash

fname="p$1.py"
cp "template.py" $fname
code $fname
