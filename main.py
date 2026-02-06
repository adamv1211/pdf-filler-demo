from pypdf import PdfReader, PdfWriter
import json
import os
from get_customer import get_customer_info
#######################################################
# ALL NAMES AND DATA ARE FAKE AND FOR DEMO PURPOSES ONLY!!!
#####################################################


def main():
    print("You have started pdf filler")
    blank_pdf = PdfReader("test_spi.pdf")
    writer = PdfWriter()
    writer.append(blank_pdf)

#Finds field names and values for mapping
    for page in blank_pdf.pages:
        Annots = page.get("/Annots")
        if not Annots:
            continue
        for Annot_ref in Annots:
            field = Annot_ref.get_object()
            name = field.get("/T", "Unnamed")
            value = field.get("/V", "")
            ftype = field.get("/FT", "")
            print(f"{name:25} | value = {value:10} | type= {ftype}")

    with open('customers.json', 'r') as file:
        clients = json.load(file)
    account = get_customer_info()
    if account not in clients:
        raise ValueError(f"Account {account} not found")

    client = clients[account]
    first = client.get("first_name")
    last = client.get("last_name")
    middle = client.get("middle_name")
    suffix = client.get("suffix")
    full_name = f"{first} {middle +  ' ' if middle else ''}{last} {suffix}"
    mi = middle[0] if middle else ""
    print(f"Filling pdf for {first} {mi} {last}")
  
    field_map = {
        "FirstName": first,
        "LastName": last,
        "MiddleName": middle,
        "MI": mi,
        "SSN": client.get("SSN"),
        "AccountNumber": client.get("invest_account_num"),
        "BankAccountNumber": client.get("bank_account_num"),
        "RoutingNumber": client.get("routing_num"),
        "NameOfBank": client.get("bank_name"),
        "NamesOnAccount": ", ".join(client.get("names_on_account", [])),
        "FullName": full_name
    }

    
    
    for page in writer.pages:
        writer.update_page_form_field_values(page, field_map)
    with open(f"{first}_{last}_filled.pdf", "wb") as f:
        writer.write(f)

    os.system(f"xdg-open {first}_{last}_filled.pdf")



if __name__ == "__main__":
    main()
