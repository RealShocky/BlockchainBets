import os
from stellar_sdk.keypair import Keypair
from stellar_sdk.server import Server

class PiNetwork:
    def __init__(self):
        self.api_key = os.environ.get("xycst2xcqgvhamvcpjuemmjbym7lixzdf5l2tazov0ldph9a7shpu4dda315khot")
        self.wallet_private_key = os.environ.get("SAIU3MHM7O4LAW4GSZY7T7QZS6FQTGCMDQHOR7SBHGJVKZD3MLQRWZVR")
        self.network = os.environ.get("NETWORK")
        self.server = None
        self.keypair = None

    def initialize(self):
        try:
            if not self.validate_private_seed_format(self.wallet_private_key):
                raise ValueError("Invalid private seed format")
            self.load_account()
            self.server = Server(horizon_url=self.get_horizon_url())
            return True
        except Exception as e:
            raise Exception("Error initializing PiNetwork: " + str(e))

    def get_balance(self):
        try:
            balances = self.server.accounts().account_id(self.keypair.public_key).call()["balances"]
            for balance in balances:
                if balance["asset_type"] == "native":
                    return float(balance["balance"])
            return 0
        except Exception as e:
            raise Exception("Error fetching balance: " + str(e))

    def load_account(self):
        try:
            self.keypair = Keypair.from_secret(self.wallet_private_key)
        except Exception as e:
            raise Exception("Error loading account: " + str(e))

    def validate_private_seed_format(self, seed):
        try:
            if not seed.upper().startswith("S"):
                return False
            elif len(seed) != 56:
                return False
            return True
        except Exception as e:
            raise Exception("Error validating private seed format: " + str(e))

    def get_horizon_url(self):
        if self.network == "Pi Network":
            return "https://api.mainnet.minepi.com"
        else:
            return "https://api.testnet.minepi.com"