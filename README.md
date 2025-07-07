# Distributed Trade Ledger - Blockchain Simulation

## Overview

A decentralized trading system simulation. Multiple parties can record and verify trade transactions without a central authority. Implements a digital ledger using blockchain principles.

## Core Concepts

### Blockchain
- Chain of blocks, each containing multiple transactions
- Each block links to the previous via cryptographic hash
- Immutable record: changes break the chain

### Digital Signatures
- Each participant has a public/private key pair
- Transactions are signed with the private key
- Signatures are verified with the public key

### Distributed Consensus
- Multiple parties agree on valid transactions
- No single point of failure
- Fault tolerance

## Process

1. Agent creation: Each trader has a cryptographic identity
2. Transaction creation: Agents create transactions
3. Digital signing: Transactions are signed
4. Block formation: Transactions are grouped into blocks
5. Block signing: Blocks are signed
6. Chain linking: Each block links to the previous
7. Verification: Signatures and chain integrity are checked

## Architecture

```
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│   Block #1    │<───│   Block #2    │<───│   Block #3    │
│               │    │               │    │               │
│ Transactions  │    │ Transactions  │    │ Transactions  │
│ - Alice→Bob:10│    │ - Bob→Charlie:│    │ - Charlie→Dave│
│ - Eve→Frank:15│    │ - Grace→Henry:│    │ - Irene→Jack: │
│               │    │               │    │               │
│ Hash: abc123  │    │ Hash: def456  │    │ Hash: ghi789  │
│ Signature: xyz│    │ Signature: uvw│    │ Signature: rst│
└───────────────┘    └───────────────┘    └───────────────┘
```

## Components

### ledger/blockchain.py
- BlockchainTradeLedger: manages the chain of blocks
- Block: contains transactions and metadata
- Handles block creation, linking, and signature verification

### agents/base_agent.py
- BaseAgent: represents a trader
- Generates key pairs
- Signs transactions

### tests/test_ledger.py
- Tests block addition
- Tests digital signature functionality
- Ensures chain integrity

## Key Features

- Trustless: no central authority
- Transparent: all transactions are visible
- Immutable: transactions cannot be changed
- Secure: cryptographic signatures
- Resilient: system continues if some participants fail

## Requirements
- Python 3.8+
- cryptography
- pytest
- matplotlib

## Setup

```bash
pip3 install -r requirements.txt
python3 -m pytest tests/ -v
```

## Blockchain Visualization

Visualize the blockchain using matplotlib. Each block shows:
- Block index
- Number of transactions
- Truncated block hash
- Block creator (Genesis for the first block, Agent for others)

Example:

```python
from ledger.blockchain import BlockchainTradeLedger
from agents.base_agent import BaseAgent
from visuals.chain_plot import plot_chain

ledger = BlockchainTradeLedger()
alice = BaseAgent('Alice')
ledger.add_block([{'from': 'Alice', 'to': 'Bob', 'amount': 10}], alice.private_key)
plot_chain(ledger)
```

Running this code displays a diagram of the blockchain structure and connections. 