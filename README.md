# PoS Blockchain

This is a **Proof of Stake (PoS) based blockchain** implemented in Python. It includes a basic blockchain structure with block creation, transaction handling, and hashing.

## Description
This project is an implementation of a **Proof of Stake blockchain**, where participants stake cryptocurrency to validate transactions and create new blocks. Unlike Proof of Work (PoW), PoS selects validators based on their stake rather than computational power, making it more energy-efficient.

## Features
✅ Blockchain implementation in Python  
✅ Genesis block creation  
✅ Adding new blocks with transactions  
✅ SHA-256 hashing for block security  
✅ **Upcoming:** Proof of Stake mechanism with staking and rewards  
✅ **Upcoming:** REST API for blockchain interaction  

## Prerequisites
Make sure you have Python installed (3.8 or later). You can check your version with:
```bash
python --version
```

## Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/Vipra001/pos-blockchain.git
   cd pos-blockchain
   ```
2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Run the blockchain**
   ```bash
   python blockchain.py
   ```

## How It Works
1. The blockchain starts with a **genesis block** (block index 0).  
2. New blocks are added with transaction data.  
3. Each block contains:
   - **Index** (position in the chain)
   - **Previous block hash**
   - **Transactions** (stored as a list)
   - **Timestamp** (when the block was created)
   - **Current block hash** (generated using SHA-256)
4. The blockchain is printed in the console, showing all blocks and transactions.

## Example Output
```
Index: 0, Hash: abc123..., Prev Hash: 0, Transactions: []
Index: 1, Hash: def456..., Prev Hash: abc123..., Transactions: ['Alice pays Bob 5 BTC']
Index: 2, Hash: ghi789..., Prev Hash: def456..., Transactions: ['Bob pays Charlie 2 BTC']
```

## Roadmap
- ✅ Basic blockchain (completed)
- 🔜 Implement Proof of Stake (PoS) mechanism
- 🔜 Add staking and penalties system
- 🔜 Implement reward distribution for validators
- 🔜 Build a REST API to interact with the blockchain

## Contributing
Pull requests are welcome! If you find a bug or have suggestions, open an issue.

## License
This project is open-source and available under the MIT License.

