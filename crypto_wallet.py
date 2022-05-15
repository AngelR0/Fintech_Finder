"""
The Cryptocurrency Wallet

This file contains the Ethereum transaction functions 
"""
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3 import Account, middleware
from bip44 import Wallet
import os
import requests
from dotenv import load_dotenv
load_dotenv()


def generate_account():
    "Creating a digital wallet and Ethereum account from a mnemonic seed phrase."
    # Fetch mnemonic seed.
    mnemonic = os.getenv('MNEMONIC')

    # Create Wallet Object
    wallet = Wallet(mnemonic)

    # Derive Ethereum Private Key
    private, public = wallet.derive_account("eth")

    # Convert Private Key into an Ethereum Account
    account = Account.privateKeyToAccount(private, public)

    # Return the account variable
    return account


def get_balance(w3, address):
    """ Using an Ethereum account address to access the balance of Ether"""
    # Get balance of addres in Wei
    wei_balance = w3.eth.get_balance(address)

    # Convert the Wei Value to Ether
    ether = w3.fromWei(wei_balance, "ether")

    # Return the Value in Ether
    return ether


def send_transaction(w3, account, to, wage):
    """ Send an authorized transaction to the Ganache blockchain. """
    # Set the Gas Price Strategy
    w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

    # Convert Eth Amount to Wei
    value = w3.toWei(wage, "ether")

    # Calculate gas estimate
    gasEstimate = w3.eth.estimateGas(
        {"to": to,
         "from": account.address,
         "value": value
         }
    )

    # Construct a raw transaction
    raw_tx = {
        "to": to,
        "from": account.address,
        "value": value,
        "gas": gasEstimate,
        "gasPrice": 0,
        'nonce': w3.eth.getTransactionCount(account.address)
    }

    # Sign the Raw Transaction with Ethereum Account
    signed_tx = account.signTransaction(raw_tx)

    # Send the Signed Transaction
    return w3.eth.sendRawTransaction(signed_tx.rawTransaction)
