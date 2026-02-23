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
import logging

#############################################################
# ALL NAMES AND DATA ARE FAKE AND FOR DEMO PURPOSES ONLY!!! #
#############################################################




def main():

    logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(), logging.FileHandler("pdf_filler.log")])
    log = logging.getLogger(__name__)


    log.info("You have started pdf filler")
    with open('customers.json', 'r') as cust_data:
        clients = json.load(cust_data)
        log.info("loaded %d customers", len(clients))
    form, account, instructions, frequency, start_date, flatten = get_customer_info()
    log.info("form=%s account=%s instructions=%s frequency=%s start_date=%s flatten=%s", form, account, instructions, frequency, start_date, flatten)
    if account not in clients:
        raise ValueError(f"Account {account} not found")
    
    blank_pdf = PdfReader(form)
    writer = PdfWriter()
    writer.append(blank_pdf)

#Finds PDF field names and values for mapping
    DEBUG = True
    if DEBUG:
        get_fields(writer)
             



    #Load specific client's data
    client = clients[account]
    field_map = build_field_map(client, start_date)
    file_location = f"{field_map['FirstName']}_{field_map['LastName']}_filled.pdf"
    print(f"Filling pdf for {field_map['FirstName']} {field_map['MI']} {field_map['LastName']}")

#   SUPRESSION
    match form:
        case "test_pip.pdf":
            if instructions == "ibp"or instructions == "1Etf"or instructions == "3Etf":
                field_map["BankAccountNumber"] = ""
                field_map["RoutingNumber"] = ""
                field_map["NameOfBank"] = ""
                field_map["NamesOnAccount"] = ""
        # case "additional form":                               <--- Additional forms may require supression
        #     field_map[required_suppresed_field] = ""          <--- I used match to make adding pdf's simpler
        #
        #
        case _:
            pass
    log.info("suppressed fields")


    #Fills pdf from field map
    log.info("filling output=%s", file_location)
    fill(writer, field_map, instructions, frequency, DEBUG)
    


    #Writes to pdf
    with open(file_location, "wb") as f:
        writer.write(f)
        f.flush()
        os.fsync(f.fileno())

    #Flattening pdf
    if flatten:
        flat_path = f"{field_map['FirstName']}_{field_map['LastName']}_flattened.pdf"
        subprocess.run(["gs", "-o", flat_path, "-sDEVICE=pdfwrite", "-dBATCH", "-dNOPAUSE", "-dSAFER", file_location], check = True)
        log.info("flattening via ghostscript")
        os.replace(flat_path, file_location)
        log.info("Flattening done, overwritten filled PDF with flattened version")


    #Opens Pdf after generation
    webbrowser.open(file_location)
    log.info("done")
    
if __name__ == "__main__":
    main()
