import os
import requests
import json
import logging
import stellar_sdk as s_sdk

class PiNetwork:
    def __init__(self):
        # Load API key and network from environment variables
        self.api_key = os.environ.get('PI_API_KEY', '')
        self.network = os.environ.get('PI_NETWORK', ' ')
        self.client = None
        self.account = ''
        self.base_url = os.environ.get('PI_BASE_URL', "https://api.minepi.com")
        self.open_payments = {}
        self.server = None
        self.keypair = ''
        self.fee = None
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)  # Set logging level to DEBUG

        # Define log formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Create console handler and set level to DEBUG
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Add formatter to ch
        ch.setFormatter(formatter)

        # Add ch to logger
        self.logger.addHandler(ch)

    def initialize(self, wallet_private_key, network):
        try:
            if not self.validate_private_seed_format(wallet_private_key):
                raise ValueError("Invalid private seed format")
                
            self.load_account(wallet_private_key, network)
            self.open_payments = {}        
            self.fee = self.server.fetch_base_fee()
            return True
        except Exception as e:
            self.logger.error("Initialization failed: %s", e)
            return False

    def get_balance(self):
        try:
            balances = self.server.accounts().account_id(self.keypair.public_key).call()["balances"]
            for balance in balances:
                if balance["asset_type"] == "native":
                    return float(balance["balance"])
            return 0
        except Exception as e:
            self.logger.error("Failed to get balance: %s", e)
            return 0

    def get_payment(self, payment_id):
        url = f"{self.base_url}/v2/payments/{payment_id}"
        response = requests.get(url, headers=self.get_http_headers())
        self.handle_http_response(response)

    def create_payment(self, payment_data):
        try:
            if not self.validate_payment_data(payment_data):
                if __debug__:
                    self.logger.debug("No valid payments found. Creating a new one...")

            balances = self.server.accounts().account_id(self.keypair.public_key).call()["balances"]
            balance_found = False
            for balance in balances:
                if balance["asset_type"] == "native":
                    balance_found = True
                    if (float(payment_data["amount"]) + (float(self.fee) / 10000000)) > float(balance["balance"]):
                        return ""
                    break

            if not balance_found:
                return ""

            obj = {'payment': payment_data}

            obj = json.dumps(obj)
            url = f"{self.base_url}/v2/payments"
            response = requests.post(url, data=obj, json=obj, headers=self.get_http_headers())
            parsed_response = self.handle_http_response(response)

            identifier = ""
            identifier_data = {}

            if 'error' in parsed_response:
                identifier = parsed_response['payment']["identifier"]
                identifier_data = parsed_response['payment']
            else:
                identifier = parsed_response["identifier"]
                identifier_data = parsed_response

            self.open_payments[identifier] = identifier_data

            return identifier
        except Exception as e:
            self.logger.error("Failed to create payment: %s", e)
            return ""

    def handle_http_response(self, response):
        try:
            response.raise_for_status()
            result = response.json()
            if __debug__:
                self.logger.debug("HTTP Response: %s", result)
            return result
        except Exception as e:
            self.logger.error("HTTP request failed: %s", e)
            return None

    def load_account(self, private_seed, network):
        try:
            self.keypair = s_sdk.Keypair.from_secret(private_seed)
            if network == "Pi Network":
                horizon = "https://api.mainnet.minepi.com"
            else:
                horizon = "https://api.testnet.minepi.com"
            
            self.server = s_sdk.Server(horizon)
            self.account = self.server.load_account(self.keypair.public_key)
        except Exception as e:
            self.logger.error("Failed to load account: %s", e)

    def validate_private_seed_format(self, seed):
        return seed.upper().startswith("S") and len(seed) == 56

    def get_http_headers(self):
        return {'Authorization': f"Key {self.api_key}", "Content-Type": "application/json"}