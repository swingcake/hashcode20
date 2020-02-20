#! /usr/bin/python3
from parser import parse
from submission import submit
import sys

context = parse(sys.argv[1])
submit(context, sys.argv[2])
