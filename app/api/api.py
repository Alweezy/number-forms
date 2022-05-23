from flask_restful import Resource
from flask import request

from app.service import service


class NumberForms(Resource):
  def get(self):
    # get request params
    args = request.args

    # check if number arg is in url
    if "number" not in args:
      return {
        "success": False,
        "error": "argument number is required"
      }, 400

    try:
      output = service.compute_output(args["number"])
      return {
        "success": True,
        "result": output}, 200
    except Exception as e:
      return {
        "success": False,
        "error": str(e)
      }, 400