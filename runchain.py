#!/usr/bin/env python3


import chain
import hashlib
import time

import pandas as pd

file = input("Filename, case sensitive: ")
students = pd.read_csv (file, index_col="id")
print(students)


print("\n\nSTARTING\n")
print(chain.blockchain.chain)

chain.blockchain.get_data(
    data = students,
    sender="0", 
    receiver="Blockchain Bootcamp", 
    amount=1,
    previous_hash = chain.last_block.compute_hash,
    block = chain.blockchain.build_block(chain.proof_number, chain.last_proof_number))
    
print("\nCREATION SUCCESSFUL\n\n")
print(chain.blockchain.chain)


print(chain.blockchain.current_data, "\n\n")
print(len(chain.blockchain.chain)-1)
for x in range(len(chain.blockchain.chain)-1):
    print(x, ":\n", chain.blockchain.chain[x])



output=[]
for x in range(len(chain.blockchain.chain)-1):
    if (len(chain.blockchain.chain[x].data) >= 1):
        output.append(chain.blockchain.chain[x].data[0].get("data"))
output.append(chain.blockchain.current_data[0].get("data"))

output=pd.DataFrame(output)
output.to_csv("Graduates.csv")


for x in range(len(chain.blockchain.chain)-1):
    #print(chain.blockchain.chain[x].data)
    if (len(chain.blockchain.chain[x].data) >= 1):
        print(chain.blockchain.chain[x].data[0].get("data"))
        
print("\n\nCurrent Data Block:\n", chain.blockchain.current_data[0].get("data"))