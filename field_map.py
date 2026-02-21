def build_field_map(client: dict) -> dict:
    first = client.get("first_name")
    last = client.get("last_name")
    middle = client.get("middle_name")
    suffix = client.get("suffix")
    full_name = f"{first} {middle +  ' ' if middle else ''}{last} {suffix}"
    mi = middle[0] if middle else ""

    map =  {
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

    return map 