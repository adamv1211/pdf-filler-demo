import argparse
from datetime import date
def get_customer_info():
    date_filled = date.today().strftime("%m/%d/%Y")
    parser = argparse.ArgumentParser(description = "Fill a PDF using a chosen customer's data")
    parser.add_argument("--account", required = False, type = str, default = "000000001", help = "Customer account number")
    parser.add_argument("--instructions", required= False, type = str, help = 'Type of standing payment, "ibp", "1Etf", "3Etf" ')
    parser.add_argument("--flatten", action="store_true", help = "Flatten PDF output using Ghostscript")
    parser.add_argument("--form", required = False, type = str, default = "test_spi.pdf", help = "Name of pdf file to fill in")
    parser.add_argument("--start_date", required = False, type = str, default = date_filled, help = 'Enter starting date "mm/dd/yyyy" ' )
    parser.add_argument("--frequency", required = False, type = str, help = "Enter yearly or monthly")

    args = parser.parse_args()
    return args.form, args.account, args.instructions, args.frequency, args.start_date, args.flatten