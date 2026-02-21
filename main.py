from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, BooleanObject
import subprocess
import json
import os
from get_customer import get_customer_info
import webbrowser
from field_map import build_field_map
from get_form_fields import get_fields
from fill_pdf import fill

#############################################################
# ALL NAMES AND DATA ARE FAKE AND FOR DEMO PURPOSES ONLY!!! #
#############################################################


def main():
    print("You have started pdf filler")
    blank_pdf = PdfReader("test_spi.pdf")
    writer = PdfWriter()
    writer.append(blank_pdf)

#Finds PDF field names and values for mapping
    DEBUG = False
    if DEBUG:
        get_fields(writer)
             

    with open('customers.json', 'r') as cust_data:
        clients = json.load(cust_data)
    account, instructions, flatten = get_customer_info()
    if account not in clients:
        raise ValueError(f"Account {account} not found")

    #Load specific client's data
    client = clients[account]
    field_map = build_field_map(client)
    print(f"Filling pdf for {field_map["FirstName"]} {field_map["MI"]} {field_map["LastName"]}")
  
    #Fills pdf from field map
    fill(writer, field_map, instructions)
    
    #Writes to pdf
    with open(f"{field_map["FirstName"]}_{field_map["LastName"]}_filled.pdf", "wb") as f:
        writer.write(f)
        f.flush()
        os.fsync(f.fileno())


    file_location = f"{field_map["FirstName"]}_{field_map["LastName"]}_filled.pdf"
    #Flattening pdf
    if flatten:
        flat_path = f"{field_map["FirstName"]}_{field_map["LastName"]}_flattened.pdf"
        subprocess.run(["gs", "-o", flat_path, "-sDEVICE=pdfwrite", "-dBATCH", "-dNOPAUSE", "-dSAFER", file_location], check = True)
        file_location = flat_path


    #Opens Pdf after generation
    webbrowser.open(file_location)
    
if __name__ == "__main__":
    main()
