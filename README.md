#### byteball-rpc-client

byteball-rpc-client is a python library to interact with the [headless byteball](https://github.com/byteball/headless-byteball)'s 
RPC interface. 

In order to access the RPC service, you need to [setup a private headless wallet with RPC enabled](https://github.com/byteball/headless-byteball/wiki/Running-RPC-service). Once you setup it,
you can access to these methods via any programming language.

- getinfo (State of then DAG)
- validateaddress (Byteball Address Validator)
- getnewaddress (Create a new address in the headless wallet)
- getbalance (Get balance of the wallet or a specific address in the wallet)
- listtransactions (Scan transactions in the wallet)
- sendtoaddress (Withdraw funds to any other address)

![bball.jpeg](https://ipfs.busy.org/ipfs/QmSipbrs6EzPS2RqMV31XKDmCLKac5X6edhG9rp471XEPd)
<center><sup>Logo of Byteball</sup></center>

#### Installation

```
$ (sudo) pip install byteball_rpc_client
```

#### Usage

Get a ```Client``` instance first.

```python
from byteball_rpc_client.client import Client
c = Client("your_private_rpc_server")
```

#### Commands
##### getinfo 

```python
c.get_info()
```

Output:

```python
{
    'last_mci': 3074861,
    'last_stable_mci': 0,
    'count_unhandled': 0
}
```

#### validateaddress 

```python
c.validate_address("<any_byteball_address>")
```

Output will be True or False. (bool)

##### getnewaddress

```python
c.get_new_address()
```

Output will be a string. (Ex: ```FRQJM2OLCY5FYPXIIHXPPZM4YYN2JYOZ```)

##### getbalance

Get the balance of the wallet:

```python
c.get_balance()
```

Output:

```python
{
    'base': {
        'stable': 1762691,
        'pending': 0,
        'is_private': None
    }
}
```

Or if you want to get the balance of a single address:

```python
c.get_balance("<address>")
```

##### listtransactions

- Get all transactions related to a particular address

```python
c.list_transactions(address="<address>")
```

Output:

```
[{
    'action': 'sent',
    'amount': 250000,
    'addressTo': '<address>',
    'original_address': None,
    'textAddress': '',
    'claimed': False,
    'mnemonic': None,
    'confirmations': 1,
    'unit': '<unit>',
    'fee': 541,
    'time': '<timestamp>',
    'level': None,
    'mci': <mci>,
    'isTextcoin': False
}, 
]
```

- Get all transactions on the wallet after a particular MCI

```python
c.list_transactions(since_mci="<mci>")
```

- Get a specific transaction

```python
c.list_transactions(unit="<unit_id>")
```

#### sendtoaddress

Withdraw bytes or another asset.

```
c.send_to_address('<receiver_address>', amount)
```

It has an optional **asset** parameter for different assets. Default is bytes.
Amount also should be in bytes.

Response will be the unit ID in string. Ex:

```
wYy4kuIMJTnbnTGopBOmAsaeY16ArhfVD6UKLVZdb0g=
```

#### Notes:

Current RPC server doesn't have any authentication. So, make sure you secure the
access to the RPC server.
