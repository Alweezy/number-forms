from app.service import errors
from app.service import literals

def compute_output(value):
  if not value.isnumeric():
    raise errors.NotANumberError("Invalid input. A numeric value was expected.")

  output = int(value)
  if output % 7 == 0 and output % 5 == 0:
    return literals.LR
  elif output % 5 == 0:
    return literals.L
  elif output % 7 == 0:
    return literals.R
  else:
    return value