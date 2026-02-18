import argparse

def get_customer_info():
    parser = argparse.ArgumentParser(description = "Fill a PDF using a chosen customer's data")
    parser.add_argument("--account", required = False, type = str, default = "123456789", help = "Customer account number")
    parser.add_argument("--instructions", required= False, type = str, help = 'Type of standing payment, "Ibp", "1st party Etf"", "Third party etf" ')
    return parser.parse_args().account, parser.parse_args().instructions