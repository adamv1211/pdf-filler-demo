import argparse

def get_customer_info():
    parser = argparse.ArgumentParser(description = "Fill a PDF using a chosen customer's data")
    parser.add_argument("--account", required = False, type = str, default = "123456789", help = "Customer account number")
    parser.add_argument("--instructions", required= False, type = str, help = 'Type of standing payment, "Ibp", "1st party Etf"", "Third party etf" ')
    parser.add_argument("--flatten", action="store_true", help = "Flatten PDF output using Ghostscript")
    args = parser.parse_args()
    return args.account, args.instructions, args.flatten