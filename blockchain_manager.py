# 4. Blockchain Manager (blockchain_manager.py)
# Validates data integrity with blockchain.

from web3 import Web3

class BlockchainManager:
    def __init__(self, node_url, private_key):
        self.web3 = Web3(Web3.HTTPProvider(node_url))
        self.private_key = private_key

    def validate_data(self, data_hash):
        """
        Verify the data hash against the blockchain.
        """
        return self.web3.eth.getStorageAt("contract_address", data_hash)

    def submit_data(self, data_hash):
        """
        Submit a new data hash to the blockchain.
        """
        txn = {
            "to": "contract_address",
            "value": 0,
            "data": data_hash,
        }
        signed_txn = self.web3.eth.account.signTransaction(txn, self.private_key)
        return self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
