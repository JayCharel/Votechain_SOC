'''
# import libraries 
import hashlib 
import random 
import string 
import json 
import binascii 
#import numpy as np 
#import pandas as pd 
import pylab as pl 
import logging 
import collections


if self.voter == "Genesis":
   identity = "Genesis"
else:
   identity = self.voter.identity


'''
import binascii 
import datetime 
import Crypto
import Crypto.Random 
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA 
from Crypto.Signature import PKCS1_v1_5

class Voter:
   def __init__(self):
      random = Crypto.Random.new().read
      self._private_key = RSA.generate(1024, random)
      self._public_key = self._private_key.publickey()
      self._signer = PKCS1_v1_5.new(self._private_key)

   @property
   def identity(self):
      return
   binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

class demoVote:
    def __init__(self, voter , mainEntity , vote ):
        self.voter = voter
        self.mainEntity = mainEntity
        self.vote = vote
        self.time = datetime.datetime.now()

Jay = Voter() 
print (Jay.identity)