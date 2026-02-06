import argparse

def get_customer_info():
    parser = argparse.ArgumentParser(description = "Fill a PDF using a chosen customer's data")
    parser.add_argument("--account", required = True, type = str, default = 0,
                        help = "Customer account number"
    )
    return parser.parse_args().account