#! /usr/bin/env python3

import json
from flask import Flask
from flask import request
from flask import render_template
from flask import abort
from Parsers import Ikea


app = Flask(__name__)  # , static_url_path='')


@app.route("/")
def index():
    return app.send_static_file("debug.html")  # "Flask dockerized!"


@app.route("/<string:page_name>/")
def get_page(page_name):
    abort(404, "{} not found".format(page_name))
    # return render_template('%s.html' % page_name)


@app.route("/favicon.ico/")
def favicon():
    abort(404)


@app.route("/find", methods=["POST"])
def find():
    result = {}
    req_data = request.data.decode("utf-8")
    # print(req_data)
    # print(type(req_data))
    # print(dir(req_data))
    req_dict = json.loads(req_data)
    # print(req_dict)
    # print(type(req_dict))
    # print(dir(req_dict))
    query = req_dict["query"]
    print("query : {}".format(query))
    # print(query)
    # print(type(query))
    # print(dir(query))
    ikea_search = Ikea()
    result["ikea_result"] = ikea_search.parse_search_results(query)
    return json.dumps(result, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3030)
