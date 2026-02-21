from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, BooleanObject
def fill(writer, field_map, instructions):
    for page in writer.pages:
        writer.update_page_form_field_values(page, field_map, auto_regenerate = True)       
        checkbox_options = ["Ibp", "1st party Etf", "Third party etf"]
        Annots = page.get("/Annots")
        if not Annots:
            continue    
        for Annot_ref in Annots:
            field = Annot_ref.get_object()
            name = field.get("/T", "Unnamed")
            if name in checkbox_options:  #<--- Unchecks all checkboxes before generating a new form then checks the correct ones.
                if name == instructions:   
                    field.update({NameObject("/V"): NameObject("/Yes"), NameObject("/AS"): NameObject("/Yes")})
                else:
                    field.update({NameObject("/V"): NameObject("/Off"), NameObject("/AS"): NameObject("/Off")})
        
    if "/AcroForm" in writer._root_object:
        writer._root_object["/AcroForm"][NameObject("/NeedAppearances")] = BooleanObject(True)
    return writer