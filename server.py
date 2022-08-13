import json

from typing import List
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from attrs import asdict
from attrs import define

from caching import _parse_db, _parse_input
from price_calculator import Order
from constants import HOST, PORT


#Format of the returned response
@define
class Output:
    order_id: int
    total: int
    parts: str

#Request Handler
class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        
        # read incoming sent data
        data = self.rfile.read(self._sent_data_size)
        
        # do something with it ...
        response = self._process(data.decode("utf-8"))

        # perpare the (json) response
        jsonbytes = self._prepare_json_response(response)
                    
        # send the (json) response back ...
        self.wfile.write(jsonbytes)

    def _process(self, data: str) -> List[Output]:
        input_value = json.loads(data)['components']
        parsed, message = _parse_input(input_value)
        if(parsed):
            ORDER_ID, total, parts = order_obj.order_item(input_value)
            return Output(ORDER_ID, total, parts)
        else:
            return Output(0, 0, message)

    def _prepare_json_response(self, response: List[Output]) -> bytes:
        self.send_response(201)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        jsonstr = json.dumps(
            response,
            indent=4,
            default=asdict
        )
        return jsonstr.encode()

    @property
    def _sent_data_size(self) -> int:
        return int(self.headers.get("Content-Length"))


#Parsing database, inorder to store the required data as cache
_parse_db()

order_obj = Order()

print("Listening on {} at port {}. Please make a POST request from client.py".format(HOST, PORT))
server = HTTPServer((HOST, PORT), Handler)

server.serve_forever()
server.serve_close()