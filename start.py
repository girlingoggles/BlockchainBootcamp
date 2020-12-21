#!/usr/bin/env python3


import hashlib
import time
import chain



blockchain = BlockChain()

last_block = blockchain.latest_block

last_proof_number = last_block.proof_number

proof_number = blockchain.proof_of_work(last_proof_number)

print("SUCCESS")

