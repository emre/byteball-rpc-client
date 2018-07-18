from uuid import uuid4

import requests

from .exceptions import ByteBallRPCException


class Client:

    def __init__(self, base_url, get_detailed_response=False):
        self.base_url = base_url
        self.get_detailed_response = get_detailed_response

    def _generate_request_id(self):
        return str(uuid4())

    def _call_rpc(self, payload):

        if 'params' not in payload:
            payload.update({"params": {}})

        if 'id' not in payload:
            payload.update({"id": self._generate_request_id()})

        payload.update({
            "jsonrpc": "2.0",
        })

        response = requests.post(self.base_url, json=payload).json()
        if 'error' in response:
            raise ByteBallRPCException(
                response["error"]["message"],
                response["error"]["code"],
            )

        if self.get_detailed_response:
            return response
        return response["result"]

    def get_info(self):
        return self._call_rpc({
            "method": "getinfo"
        })

    def validate_address(self, address):
        return self._call_rpc({
            "method": "validateaddress",
            "params": [address, ]
        })

    def get_new_address(self):
        return self._call_rpc({
            "method": "getnewaddress",
        })

    def get_balance(self, address=None):
        payload = {
            "method": "getbalance",
        }
        if address:
            payload.update({
                "params": [address, ],
            })

        return self._call_rpc(payload)

    def list_transactions(self, since_mci=None, address=None, unit=None,
                          asset=None):
        payload = {
            "method": "listtransactions",
        }

        if address:
            payload.update({
                "params": [address, ]
            })
        else:
            params = {}
            if since_mci:
                # query all transactions after a particular
                # main chain index.
                params.update({
                    "since_mci": since_mci,
                })
            if unit:
                # query a individual transaction
                params.update({
                    "unit": unit,
                })
            if asset:
                # query in a particular asset
                params.update({
                    "asset": asset,
                })
            payload.update({
                "params": params,
            })
        return self._call_rpc(payload)

    def send_to_address(self, address, amount, asset=None):

        if not isinstance(amount, int):
            raise ValueError("Amount must be integer.")

        payload = {
            "method": "sendtoaddress",
            "params": [address, amount],
        }

        if asset:
            payload["params"].append(asset)

        return self._call_rpc(payload)