# Script to sum some user supplied numbers at runtime
import numpy as np
import sys


if len(sys.argv) > 1:
  result = sys.argv[1:].sum()
  print(result)
else:
  print("Nothing to sum")
