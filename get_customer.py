import argparse

def get_customer_index():
    parser = argparse.ArgumentParser(description = "Fill a PDF using a chosen customer's data")
    parser.add_argument("--customer", type = int, default = 0,
                        help = "Index of customers.json (default = 0, only 4 customers in test version of json)"
    )
    return parser.parse_args().customer