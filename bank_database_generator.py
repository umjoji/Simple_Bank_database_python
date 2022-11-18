from name_generator import *
from phone_number_generator import *
from bvn_generator import *
from cust_id_generator import *
from account_number_generator import *
from account_balance_generator import *
import csv
from address_generator import *


def main():
        """This generates a list of random names, phone numbers, BVNs, account numbers
        Customer IDs amd account balances"""
        # header can be changed to fit data
        header = ["Customer ID", "Name", "Phone number", "Address", "BVN", "Account number", "Account balance"]
        # number of clients you want
        number = int(input("Enter how many clients you want to generate: "))
        name = input("Please enter a template name: ")
        cust_id_in = input("Enter the first digit of the customer ID: ")
        acct_no_in = input("Enter the first digit of the account number: ")
        # write result to csv file        
        with open("bank_database.csv", "w") as f:
                writer = csv.writer(f)
                writer.writerow(header)

                for i in range(number):                       
                        name = name_generator(name)
                        phone_number = phone_number_generator()
                        bvn = bvn_generator()                        
                        cust_id = cust_id_generator(cust_id_in)                    
                        acct_no = account_number_generator(acct_no_in)
                        acct_bal = account_balance_generator()
                        address = address_generator()
                        data = [cust_id, name, phone_number, address, bvn, acct_no, round(acct_bal, 2)]
                        writer.writerow(data)   # write data to csv file

main()
        