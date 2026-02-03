from pdfrw import PdfReader, PdfWriter
import json
import os
from get_customer import get_customer_index
#######################################################
# ALL NAMES AND DATA ARE FAKE AND FOR DEMO PURPOSES ONLY!!!
#####################################################



blank_pdf = PdfReader("test_spi.pdf")

def main():
    print("You have started pdf filler")
# Uncomment this to check pdf field names
#    for page in blank_pdf.pages:
#        if page.Annots:
#            for field in page.Annots:
#              if field.V:
#                 print(field.T, field.V, field.AS, field.AP)

    with open('customers.json', 'r') as file:
        clients = json.load(file)
    i = get_customer_index()
    if i >= len(clients):
        raise ValueError(f"Customer index {i} out of range")

    client = clients[i]
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

    





    for page in blank_pdf.pages:
        if page.Annots:
            for field in page.Annots:
                field_string = field.T[1:-1]


                if field_string in field_map:
                    field.V = field_map[field_string]
                    field.AP = None

            
                

       
    filled_pdf = f"filled_{first}_{last}_spi.pdf"
    blank_pdf.Root.NeedAppearances = True
    PdfWriter().write(filled_pdf, blank_pdf)
    print(f"Saved filled PDF as {filled_pdf}")

    os.system(f"xdg-open {filled_pdf}")
                    


if __name__ == "__main__":
    main()
