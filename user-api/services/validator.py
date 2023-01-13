from validate_docbr import CPF


class Validator:
    def base(requered: dict, data: dict):
        requered = [req for req in requered if req not in data]
        
        if requered:
            response = {
                "erro": "Faltam campos obrigatórios",
                "recebido": [inf for inf in data],
                "faltantes": {
                    "Campos": requered,
                },
            },
            
            return response      
  
    def register_validator(data: dict):
        REGISTER = ["name", "cpf", "email", "phone_number"]
        return Validator.base(REGISTER, data)

    def check_cpf_is_true(cpf: str):

        return CPF().validate(cpf)

