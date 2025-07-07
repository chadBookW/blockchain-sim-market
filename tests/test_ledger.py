import pytest
from ledger.blockchain import BlockchainTradeLedger
from agents.base_agent import BaseAgent

def test_block_addition():
    ledger = BlockchainTradeLedger()
    agent = BaseAgent("Alice")
    tx = {"from": "Alice", "to": "Bob", "amount": 10}
    # Agent signs the transaction (not strictly needed for block, but realistic)
    signature = agent.sign_transaction(tx)
    tx["signature"] = signature
    added = ledger.add_block([tx], agent.private_key)
    assert added
    assert len(ledger.chain) == 2
    # Check signature verification for the new block
    assert ledger.chain[-1].verify_signature() 