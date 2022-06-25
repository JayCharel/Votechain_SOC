
from Crypto.PublicKey import RSA

def initialize_wallet():
    private_key = RSA.generate(2048)
    public_key = key.publickey().export_key()
    return private_key, public_key
    
