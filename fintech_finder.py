""" 
This file contains the generated Ethereum account instance.
Displays the account balance associated with your Ethereum account address
Calculates the total value of an Ethereum transaction: the gas estimate
Digitally sign a transaction that pays a Fintech Finder candidate, and sends the transaction to the Ganache blockchain
"""
# Imports
from crypto_wallet import generate_account, get_balance, send_transaction
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

# Import the functions from the "crypto_wallet.py" file:

# This the database of candidates:
# Including their Name, Digital Address, Rating, Hourly Cost per Ether, and picture of themselves
candidate_database = {
    "Lane": ["Lane", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", "4.3", .20, "Images/lane.jpeg"],
    "Ash": ["Ash", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", "5.0", .33, "Images/ash.jpeg"],
    "Jo": ["Jo", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.7", .19, "Images/jo.jpeg"],
    "Kendall": ["Kendall", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.1", .16, "Images/kendall.jpeg"]
}

# A list of the Fintech Finder candidates first names
people = ['Lane', 'Ash', 'Jo', 'Kendell']


def get_people(w3):
    """Display the database of Fintech Finders candidates information"""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("Rating of FinTech Professional: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], 'eth')
        st.text("\n")


# Streamlit Application Headings
st.markdown("# FinTech Finder")
st.markdown("## Hire a FinTech Professional")
st.text("\n")

# Streamlit Application Sidebar
st.sidebar.markdown(" ## Client Account Address and Ethernet Balance in Ether")

# Create a variable and set the variable equal to a call on the 'generate_account' function
account = generate_account()

# The clients Ethereum account address to the sidebar
st.sidebar.write(account.address)

# A sidebar that displays the balance of the customers account
st.sidebar.write(get_balance(w3, account.address))
