#!/usr/local/bin/python3.6
# -*- coding: utf-8 -*-

import json
import hashlib
from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask
from flask.json import jsonify

from blockchain import BlockChain


app = Flask(__name__)
node_idetifier = str(uuid4()).replace('-', '')

blockchain = BlockChain()


@app.route('/mine', methods=['GET'])
def mine():
    return "We'll mine a new Block"


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We'll add a new transaction"


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5000)
    pass
