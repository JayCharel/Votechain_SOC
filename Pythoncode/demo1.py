'''
class :
    def __init__(self, ):
        self.
        self.

# transaction == Voting Done Once
# Nodes are sleeping and generating block after some time, calculated by probability
# Block created by miner is broadcast in whole network
# Peers broadcasting to their peers
# Block Receivers doing Same Process again
# If Someone's Getting Block then it's verifying if it's not double voted
# Verify Function, Init_Genesis Block Function,Broadcast Function, Receive Function


#Proof of work make  threshold generates a random no. if no. is less than threshold then it broadcasts, Update Threshold if it's too fast ,
# so that  between random no. and 0 has less prob. to be inside threshold
# If Proof of work satisfies than it mines
# Make Function of Broadcast to Peers
# Transaction/Signature Broadcast for those who have voted
# Broadcast Verification Function
# Class of Node, Block and Blockchain
# Class of Signature/Transaction is equivalent to vote
# Every Node uses/Calls its Own Function Independent of Other Nodes
# Take Care to Mine on Longest Chain
# Function Get The Longest Chain
# Mine on Last Block of the Longest Chain
# Verify Transaction only on Principal Chain
# Each Bloch consists of Votes where vote itself is a class and vote contains signature without that vote is invalid
# Who has voted and what is vote/signature
# Signature  should be Inside vote
# Signature generate function will be with user
# User class will contain call signature generate, verify
# Signature function input public key and message secret key then signature is generated
# Public key has secret key Dictionary mapping
# There's a bit string/random(Signature) corresponding to public key and secret key
# Corresponding public key to signature should match
# Maintain a simple Dictionary, generate two random string to match corresponding pari of public and private key and make it global.


'''

from Crypto.PublicKey import RSA

def initialize_wallet():
    private_key = RSA.generate(2048)
    public_key = key.publickey().export_key()
    return private_key, public_key

def Signature():
    #Takes Message and Generates Signature based on Private Keys of Voter
    #


def proof_of_work(self, block):
    return  # hash

def mine():
# should update Block index
# transaction
# Role of Miner- Verify Transaction