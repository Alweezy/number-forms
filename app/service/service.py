from app.service import errors

def compute_output(value):

  output = int(value)
  if output % 7 == 0 and output % 5 == 0:
    return "LR"
  elif output % 5 == 0:
    return "L"
  elif output % 7 == 0:
    return "R"
  else:
    return value