# unit tests
import pytest

from app.service.service import compute_output
from app.service.service import errors


@pytest.mark.parametrize(
  "input,expected_output",
  [
    pytest.param("70","LR"),
    pytest.param("10","L"),
    pytest.param("28","R"),
    pytest.param("71", "71"),
  ]
)
def test_compute_output_happy_path(input,expected_output):
  output = compute_output(input)
  assert output == expected_output

def test_compute_output_fails_given_non_integer_input():
  with pytest.raises(errors.NotANumberError):
    compute_output("12 string")