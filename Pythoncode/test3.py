import base64
from Crypto import Random
from Crypto.PublicKey import RSA

def toBase64(string):
   return base64.b64encode(string)
def Generate_keys(): #Returns pair of Private and Public Keys
    private_key = RSA.generate(2048, Random.new().read)
    public_key = private_key.publickey()
    return private_key, public_key

private , public = Generate_keys()
print(private, public)
private_key = private.exportKey() #Using Export Key Method
public_key  = public.exportKey() 

print(private_key.decode(),"\n\n\n", public_key.decode() )
