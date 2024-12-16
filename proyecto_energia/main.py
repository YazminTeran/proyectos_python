from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"mensaje":"Sistema de energia funcionando!!!"}

@app.post("/calcular-consumo")

def calcular_consumo_energia(pPeriodo_consumo:int, pMora: float, pNombre_usuario:str, pNumero_apartamento:int):

    energia_activa = 878.48
    Alumbrado_publco = 2327.00
    Subsidio = 0.5289
     
    
    if int(pPeriodo_consumo) <= 130:
        energia_neta = (energia_activa * int(pPeriodo_consumo))
        valor_subsidio = energia_neta * Subsidio
        valor_T = energia_neta - valor_subsidio
        Total_pagar= valor_T +Alumbrado_publco + float(pMora)
        print(round(Total_pagar))
        return {
                    "USUARIO" : pNombre_usuario,
                    "APARTAMENTO" : pNumero_apartamento,
                    "VALOR_MORA": pMora,
                    "VALOR_A_FACTURAR" : round(Total_pagar),
                    "FECHA_LIMITE_PAGO" : "15-12-2024"
                }

    else: 
        energia_neta = (energia_activa * int(pPeriodo_consumo))
        Total_pagar=  energia_neta + Alumbrado_publco + float(pMora)
        
        print(round(Total_pagar))
        return {
                    "USUARIO" : pNombre_usuario,
                    "APARTAMENTO" : pNumero_apartamento,
                    "VALOR_MORA": pMora,
                    "VALOR_A_FACTURAR" : round(Total_pagar),
                    "FECHA_LIMITE_PAGO" : "15-12-2024"
                }
        
        
    





@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}