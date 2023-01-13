import re

class Masks:

    def cpf_clean(cpf: str):
        
        return "".join(re.findall(r"\d", str(cpf)))
