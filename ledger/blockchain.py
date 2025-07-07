import hashlib
import time
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec, utils
from cryptography.hazmat.primitives.asymmetric.utils import encode_dss_signature, decode_dss_signature
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature

class Block:
    def __init__(self, index, transactions, previous_hash, signer_public_key):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions  # List of dicts
        self.previous_hash = previous_hash
        self.signer_public_key = signer_public_key
        self.signature = None
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}{self.signer_public_key}".encode()
        return hashlib.sha256(block_string).hexdigest()

    def sign_block(self, private_key):
        data = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}{self.signer_public_key}".encode()
        signature = private_key.sign(data, ec.ECDSA(hashes.SHA256()))
        self.signature = signature

    def verify_signature(self):
        data = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}{self.signer_public_key}".encode()
        try:
            self.signer_public_key.verify(self.signature, data, ec.ECDSA(hashes.SHA256()))
            return True
        except InvalidSignature:
            return False

class BlockchainTradeLedger:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # Use a dummy key for genesis block
        private_key = ec.generate_private_key(ec.SECP256K1())
        public_key = private_key.public_key()
        genesis_block = Block(0, [], "0", public_key)
        genesis_block.sign_block(private_key)
        self.chain.append(genesis_block)

    def add_block(self, transactions, private_key):
        public_key = private_key.public_key()
        previous_hash = self.chain[-1].hash
        block = Block(len(self.chain), transactions, previous_hash, public_key)
        block.sign_block(private_key)
        if block.verify_signature():
            self.chain.append(block)
            return True
        return False 