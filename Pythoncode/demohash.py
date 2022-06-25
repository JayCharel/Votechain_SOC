import hashlib
import sys
import sha3

while True:
    string = input()
    encoded = string.encode()
    result = hashlib.sha256(encoded)
    print("Public Key ", result.hexdigest())
    private_key = hashlib.sha3_256(encoded)
    print("Private Key ", private_key.hexdigest())
    if result.hexdigest() == "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9":
        break
print("\n")
print("Voting is Over")




