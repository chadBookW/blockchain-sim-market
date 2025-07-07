from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.private_key = ec.generate_private_key(ec.SECP256K1())
        self.public_key = self.private_key.public_key()

    def sign_transaction(self, transaction):
        data = str(transaction).encode()
        signature = self.private_key.sign(data, ec.ECDSA(hashes.SHA256()))
        return signature

    def get_public_key(self):
        return self.public_key 