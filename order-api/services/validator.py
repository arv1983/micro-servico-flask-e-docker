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
  
    def order_validator(data: dict):
        REGISTER = ["user_id", "item_description", "item_quantity", "item_price"]
        return Validator.base(REGISTER, data)

  