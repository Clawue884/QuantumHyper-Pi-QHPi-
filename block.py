import hashlib
from quantum_crypto import sign_message

class Block:
    def __init__(self, index, transactions, previous_hash, quantum_key):
        self.index = index
        self.timestamp = str(datetime.datetime.now())
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
        self.nonce = 0
        self.quantum_key = quantum_key
        self.signature = self.sign_block()

    def calculate_hash(self):
        return hashlib.sha256((str(self.index) + str(self.transactions) + self.previous_hash + self.timestamp).encode('utf-8')).hexdigest()

    def sign_block(self):
        private_key, public_key = self.quantum_key
        signature = sign_message(self.calculate_hash(), private_key)
        return signature

    def mine(self, difficulty):
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

    def __str__(self):
        return f"Block #{self.index} - {self.timestamp} - {self.hash}"


---
