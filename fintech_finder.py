""" 
This file contains the generated Ethereum account instance.
Displays the account balance associated with your Ethereum account address
Calculates the total value of an Ethereum transaction: the gas estimate
Digitally sign a transaction that pays a Fintech Finder candidate, and sends the transaction to the Ganache blockchain
"""
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

# Import the functions from the "crypto_wallet.py" file:
get
