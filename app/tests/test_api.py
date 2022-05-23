# integration tests 
import json
import pytest
from http import HTTPStatus

from app import create_app

# let's use the fixture decorator to instanciate a test client
@pytest.fixture()
def test_client_config():
  app = create_app("test")
  return app.test_client()

# let's create a parameter set to use when executing out tests
@pytest.mark.parametrize(
  "input,expected_response,expected_status_code",
  [
    pytest.param("70", {"success": True, "result": "LR"}, 200),
    pytest.param("10", {"success": True, "result": "L"}, 200),
    pytest.param("28", {"success": True, "result": "R"}, 200),
    pytest.param("71", {"success": True, "result": "71"}, 200),
  ]
)
def test_compute_output_happy_path(input, expected_response, expected_status_code, test_client_config):
  response = test_client_config.get(f"/api/v1/number-forms?number={input}")
  assert json.loads(response.data) == expected_response
  assert response.status_code == expected_status_code


def test_compute_output_fails_given_non_integer_input(test_client_config):
  response = test_client_config.get("/api/v1/number-forms?number=non-integer-string")
  assert json.loads(response.data) == {"success": False, "error": "Invalid input. A numeric value was expected."}
  assert response.status_code == HTTPStatus.BAD_REQUEST

def test_missing_number_query_arg(test_client_config):
  response = test_client_config.get("/api/v1/number-forms")
  assert json.loads(response.data) == {"success": False, "error": "argument number is required"}
  assert response.status_code == HTTPStatus.BAD_REQUEST