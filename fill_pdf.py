from pypdf.generic import NameObject, BooleanObject
import logging

def fill(writer, field_map, instructions, frequency, debug = False):
    log = logging.getLogger(__name__)
    log.debug("filling pdf...")
    for page in writer.pages:
        writer.update_page_form_field_values(page, field_map, auto_regenerate = True)       
        checkbox_options = []
        Annots = page.get("/Annots")
        if not Annots:
            continue    
        for Annot_ref in Annots:
            field = Annot_ref.get_object()
            name = field.get("/T", "Unnamed")
            ftype = field.get("/FT", "")
            if ftype == "/Btn":
                checkbox_options.append(name)
                if name == instructions or name == frequency:
                    field.update({NameObject("/V"): NameObject("/Yes"), NameObject("/AS"): NameObject("/Yes")})
                else:
                    field.update({NameObject("/V"): NameObject("/Off"), NameObject("/AS"): NameObject("/Off")})
        if debug:
            print(checkbox_options)

    if "/AcroForm" in writer._root_object:
        writer._root_object["/AcroForm"][NameObject("/NeedAppearances")] = BooleanObject(True)
        
    return writer
