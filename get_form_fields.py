def get_fields(writer):
    for page in writer.pages:
            Annots = page.get("/Annots")
            if not Annots:
                continue
            for Annot_ref in Annots:
                field = Annot_ref.get_object()
                name = field.get("/T", "Unnamed")
                value = field.get("/V", "")
                ap = field.get("/AP", "")
                ftype = field.get("/FT", "")
                print(f"{name:25} | value = {value:10} | AP = {ap}| type= {ftype}")