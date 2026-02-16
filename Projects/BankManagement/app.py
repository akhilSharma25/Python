#Streamlit code done by ai 
#My main logic in main.py file

# Bank Management System - Streamlit Version
# Run with: streamlit run app.py

import streamlit as st
import json
import random
import string
import hashlib
from pathlib import Path
from datetime import datetime

class Bank:
    """Enhanced Bank Management System with security and validation"""
    
    database = Path(__file__).parent / 'data.json'
    
    @staticmethod
    def _load_data():
        """Load data from JSON file"""
        try:
            if Bank.database.exists():
                with open(Bank.database, 'r') as fs:
                    content = fs.read()
                    return json.loads(content) if content else []
            return []
        except Exception as err:
            st.error(f"Error loading data: {err}")
            return []
    
    @staticmethod
    def _save_data(data):
        """Save data to JSON file"""
        try:
            with open(Bank.database, 'w') as fs:
                json.dump(data, fs, indent=2)
            return True
        except Exception as err:
            st.error(f"Error saving data: {err}")
            return False
    
    @staticmethod
    def _hash_pin(pin):
        """Hash PIN for security"""
        return hashlib.sha256(str(pin).encode()).hexdigest()
    
    @staticmethod
    def _generate_account_number():
        """Generate unique account number"""
        alpha = ''.join(random.choices(string.ascii_uppercase, k=3))
        nums = ''.join(random.choices(string.digits, k=6))
        return f"{alpha}{nums}"
    
    @staticmethod
    def _validate_email(email):
        """Basic email validation"""
        return '@' in email and '.' in email.split('@')[1]
    
    @staticmethod
    def create_account(name, age, email, pin):
        """Create a new bank account"""
        # Validation
        if not name or len(name.strip()) < 2:
            return False, "Name must be at least 2 characters long"
        
        if age < 18:
            return False, "You must be 18 or older to create an account"
        
        if not Bank._validate_email(email):
            return False, "Please enter a valid email address"
        
        if len(str(pin)) != 4 or not str(pin).isdigit():
            return False, "PIN must be exactly 4 digits"
        
        # Create account
        data = Bank._load_data()
        
        # Check if email already exists
        if any(acc['email'] == email for acc in data):
            return False, "An account with this email already exists"
        
        account_no = Bank._generate_account_number()
        
        new_account = {
            "name": name.strip(),
            "age": age,
            "email": email.strip().lower(),
            "pin": Bank._hash_pin(pin),
            "accountNo": account_no,
            "balance": 0,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "transactions": []
        }
        
        data.append(new_account)
        
        if Bank._save_data(data):
            return True, f"Account created successfully! Your account number is: {account_no}"
        else:
            return False, "Error creating account. Please try again."
    
    @staticmethod
    def _find_account(account_no, pin):
        """Find and authenticate account"""
        data = Bank._load_data()
        hashed_pin = Bank._hash_pin(pin)
        
        for account in data:
            if account['accountNo'] == account_no and account['pin'] == hashed_pin:
                return account, data
        
        return None, data
    
    @staticmethod
    def deposit_money(account_no, pin, amount):
        """Deposit money into account"""
        if amount <= 0:
            return False, "Amount must be greater than 0"
        
        if amount > 50000:
            return False, "Maximum deposit limit is ₹50,000 per transaction"
        
        account, data = Bank._find_account(account_no, pin)
        
        if not account:
            return False, "Invalid account number or PIN"
        
        # Update balance
        for acc in data:
            if acc['accountNo'] == account_no:
                acc['balance'] += amount
                acc['transactions'].append({
                    "type": "deposit",
                    "amount": amount,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "balance_after": acc['balance']
                })
                break
        
        if Bank._save_data(data):
            return True, f"₹{amount:,.2f} deposited successfully! New balance: ₹{acc['balance']:,.2f}"
        else:
            return False, "Error processing deposit"
    
    @staticmethod
    def withdraw_money(account_no, pin, amount):
        """Withdraw money from account"""
        if amount <= 0:
            return False, "Amount must be greater than 0"
        
        account, data = Bank._find_account(account_no, pin)
        
        if not account:
            return False, "Invalid account number or PIN"
        
        if account['balance'] < amount:
            return False, f"Insufficient balance. Available: ₹{account['balance']:,.2f}"
        
        # Update balance
        for acc in data:
            if acc['accountNo'] == account_no:
                acc['balance'] -= amount
                acc['transactions'].append({
                    "type": "withdrawal",
                    "amount": amount,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "balance_after": acc['balance']
                })
                break
        
        if Bank._save_data(data):
            return True, f"₹{amount:,.2f} withdrawn successfully! New balance: ₹{acc['balance']:,.2f}"
        else:
            return False, "Error processing withdrawal"
    
    @staticmethod
    def get_account_details(account_no, pin):
        """Get account details"""
        account, _ = Bank._find_account(account_no, pin)
        
        if not account:
            return None, "Invalid account number or PIN"
        
        # Remove sensitive data
        safe_account = account.copy()
        safe_account.pop('pin', None)
        
        return safe_account, None
    
    @staticmethod
    def update_details(account_no, pin, name=None, email=None, new_pin=None):
        """Update account details"""
        account, data = Bank._find_account(account_no, pin)
        
        if not account:
            return False, "Invalid account number or PIN"
        
        # Validate and update
        for acc in data:
            if acc['accountNo'] == account_no:
                if name and len(name.strip()) >= 2:
                    acc['name'] = name.strip()
                
                if email and Bank._validate_email(email):
                    # Check if email is already used by another account
                    if any(a['email'] == email.lower() and a['accountNo'] != account_no for a in data):
                        return False, "This email is already registered with another account"
                    acc['email'] = email.strip().lower()
                
                if new_pin and len(str(new_pin)) == 4 and str(new_pin).isdigit():
                    acc['pin'] = Bank._hash_pin(new_pin)
                
                break
        
        if Bank._save_data(data):
            return True, "Account details updated successfully!"
        else:
            return False, "Error updating account details"
    
    @staticmethod
    def delete_account(account_no, pin):
        """Delete account"""
        account, data = Bank._find_account(account_no, pin)
        
        if not account:
            return False, "Invalid account number or PIN"
        
        # Remove account
        data = [acc for acc in data if acc['accountNo'] != account_no]
        
        if Bank._save_data(data):
            return True, "Account deleted successfully!"
        else:
            return False, "Error deleting account"


# Streamlit UI
def main():
    st.set_page_config(
        page_title="Bank Management System",
        page_icon="🏦",
        layout="wide"
    )
    
    st.title("🏦 Bank Management System")
    st.markdown("---")
    
    # Initialize session state
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.account_no = None
        st.session_state.pin = None
    
    # Sidebar navigation
    with st.sidebar:
        st.header("Navigation")
        
        if not st.session_state.logged_in:
            page = st.radio(
                "Select an option:",
                ["Create Account", "Login"]
            )
        else:
            st.success(f"Logged in: {st.session_state.account_no}")
            page = st.radio(
                "Select an option:",
                ["Dashboard", "Deposit Money", "Withdraw Money", "Update Details", "Delete Account"]
            )
            
            if st.button("Logout", type="secondary"):
                st.session_state.logged_in = False
                st.session_state.account_no = None
                st.session_state.pin = None
                st.rerun()
    
    # Page routing
    if not st.session_state.logged_in:
        if page == "Create Account":
            create_account_page()
        elif page == "Login":
            login_page()
    else:
        if page == "Dashboard":
            dashboard_page()
        elif page == "Deposit Money":
            deposit_page()
        elif page == "Withdraw Money":
            withdraw_page()
        elif page == "Update Details":
            update_details_page()
        elif page == "Delete Account":
            delete_account_page()


def create_account_page():
    st.header("Create New Account")
    
    with st.form("create_account_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Full Name*")
            age = st.number_input("Age*", min_value=1, max_value=120, value=18)
        
        with col2:
            email = st.text_input("Email Address*")
            pin = st.text_input("4-Digit PIN*", type="password", max_chars=4)
        
        submit = st.form_submit_button("Create Account", type="primary")
        
        if submit:
            if not all([name, email, pin]):
                st.error("Please fill in all required fields")
            else:
                try:
                    success, message = Bank.create_account(name, int(age), email, int(pin))
                    if success:
                        st.success(message)
                        st.balloons()
                    else:
                        st.error(message)
                except ValueError:
                    st.error("PIN must be a 4-digit number")


def login_page():
    st.header("Login to Your Account")
    
    with st.form("login_form"):
        account_no = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        
        submit = st.form_submit_button("Login", type="primary")
        
        if submit:
            if not account_no or not pin:
                st.error("Please enter both account number and PIN")
            else:
                try:
                    account, error = Bank.get_account_details(account_no, int(pin))
                    if account:
                        st.session_state.logged_in = True
                        st.session_state.account_no = account_no
                        st.session_state.pin = int(pin)
                        st.success("Login successful!")
                        st.rerun()
                    else:
                        st.error(error)
                except ValueError:
                    st.error("Invalid PIN format")


def dashboard_page():
    st.header("Account Dashboard")
    
    account, error = Bank.get_account_details(
        st.session_state.account_no,
        st.session_state.pin
    )
    
    if account:
        # Account Overview
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Account Holder", account['name'])
        with col2:
            st.metric("Current Balance", f"₹{account['balance']:,.2f}")
        with col3:
            st.metric("Account Number", account['accountNo'])
        
        st.markdown("---")
        
        # Account Details
        st.subheader("Account Information")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"**Email:** {account['email']}")
            st.write(f"**Age:** {account['age']}")
        
        with col2:
            st.write(f"**Created:** {account.get('created_at', 'N/A')}")
        
        # Transaction History
        if account.get('transactions'):
            st.markdown("---")
            st.subheader("Recent Transactions")
            
            transactions = account['transactions'][-10:]  # Last 10 transactions
            transactions.reverse()
            
            for txn in transactions:
                with st.expander(f"{txn['type'].title()} - {txn['timestamp']}"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Amount:** ₹{txn['amount']:,.2f}")
                    with col2:
                        st.write(f"**Balance After:** ₹{txn['balance_after']:,.2f}")
        else:
            st.info("No transactions yet")
    else:
        st.error(error)


def deposit_page():
    st.header("Deposit Money")
    
    with st.form("deposit_form"):
        amount = st.number_input("Amount to Deposit (₹)", min_value=1.0, step=100.0)
        
        submit = st.form_submit_button("Deposit", type="primary")
        
        if submit:
            success, message = Bank.deposit_money(
                st.session_state.account_no,
                st.session_state.pin,
                amount
            )
            
            if success:
                st.success(message)
            else:
                st.error(message)


def withdraw_page():
    st.header("Withdraw Money")
    
    # Show current balance
    account, _ = Bank.get_account_details(
        st.session_state.account_no,
        st.session_state.pin
    )
    
    if account:
        st.info(f"Available Balance: ₹{account['balance']:,.2f}")
    
    with st.form("withdraw_form"):
        amount = st.number_input("Amount to Withdraw (₹)", min_value=1.0, step=100.0)
        
        submit = st.form_submit_button("Withdraw", type="primary")
        
        if submit:
            success, message = Bank.withdraw_money(
                st.session_state.account_no,
                st.session_state.pin,
                amount
            )
            
            if success:
                st.success(message)
            else:
                st.error(message)


def update_details_page():
    st.header("Update Account Details")
    
    account, _ = Bank.get_account_details(
        st.session_state.account_no,
        st.session_state.pin
    )
    
    if account:
        st.info("Leave fields empty if you don't want to change them")
        
        with st.form("update_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                new_name = st.text_input("New Name", placeholder=account['name'])
                new_email = st.text_input("New Email", placeholder=account['email'])
            
            with col2:
                new_pin = st.text_input("New PIN (4 digits)", type="password", max_chars=4)
                confirm_pin = st.text_input("Confirm New PIN", type="password", max_chars=4)
            
            submit = st.form_submit_button("Update Details", type="primary")
            
            if submit:
                if new_pin and new_pin != confirm_pin:
                    st.error("PINs do not match!")
                else:
                    try:
                        pin_to_update = int(new_pin) if new_pin else None
                        success, message = Bank.update_details(
                            st.session_state.account_no,
                            st.session_state.pin,
                            new_name if new_name else None,
                            new_email if new_email else None,
                            pin_to_update
                        )
                        
                        if success:
                            st.success(message)
                            if new_pin:
                                st.info("PIN updated! Please login again with your new PIN.")
                                st.session_state.logged_in = False
                                st.session_state.account_no = None
                                st.session_state.pin = None
                        else:
                            st.error(message)
                    except ValueError:
                        st.error("Invalid PIN format")


def delete_account_page():
    st.header("Delete Account")
    
    st.warning("⚠️ This action cannot be undone!")
    
    st.write("Are you sure you want to delete your account?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Cancel", use_container_width=True):
            st.info("Account deletion cancelled")
    
    with col2:
        if st.button("Delete Account", type="primary", use_container_width=True):
            success, message = Bank.delete_account(
                st.session_state.account_no,
                st.session_state.pin
            )
            
            if success:
                st.success(message)
                st.session_state.logged_in = False
                st.session_state.account_no = None
                st.session_state.pin = None
                st.rerun()
            else:
                st.error(message)


if __name__ == "__main__":
    main()