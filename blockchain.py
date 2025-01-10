import hashlib
from transaction import Transaction
from block import Block
from quantum_crypto import generate_quantum_key, encrypt_with_quantum

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.difficulty = 2  # Difficulty for proof-of-work

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0", generate_quantum_key())

    def add_block(self, block):
        self.chain.append(block)

    def mine_pending_transactions(self, miner_address):
        block = Block(len(self.chain), self.pending_transactions, self.chain[-1].hash, generate_quantum_key())
        block.mine(self.difficulty)
        self.add_block(block)
        self.pending_transactions = [Transaction(None, miner_address, 100)]  # Miner reward

    def create_transaction(self, sender, recipient, amount):
        self.pending_transactions.append(Transaction(sender, recipient, amount))

    def get_balance(self, address):
        balance = 0
        for block in self.chain:
            for trans in block.transactions:
                if trans.sender == address:
                    balance -= trans.amount
                if trans.recipient == address:
                    balance += trans.amount
        return balance

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


---
