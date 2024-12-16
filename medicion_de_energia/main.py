from fastapi import FastAPI
from decimal import Decimal, getcontext
from datetime import datetime
from funciones import generar_pdf

app = FastAPI()

getcontext().prec = 10

energia_activa = 878.48
Alumbrado_publco = 2327.00
Subsidio = 0.5289

def calcular_consumo_energia(pPeriodo_consumo, pMora):
    if int(pPeriodo_consumo) <= 130:
        energia_neta = (energia_activa * int(pPeriodo_consumo))
        valor_subsidio = energia_neta * Subsidio
        valor_T = energia_neta - valor_subsidio
        Total_pagar= valor_T +Alumbrado_publco + float(pMora)
        formato_moneda = "$ {:,.0f} PESOS".format(Total_pagar)
        return formato_moneda
    

    else: 
        energia_neta = (energia_activa * int(pPeriodo_consumo))
        Total_pagar=  energia_neta + Alumbrado_publco + float(pMora)
        formato_moneda = "$ {:,.0f} PESOS".format(Total_pagar)
        return formato_moneda


@app.get("/items/{item_id}") 
async def read_item(item_id: int, q: str = None): 
    return {"item_id": item_id, "q": q}

@app.post("/calcular-consumo/")
async def consumo(pPeriodoConsumo: int, pMora: float ):
    mes_facturado = datetime.now()
    valor = calcular_consumo_energia(pPeriodoConsumo, pMora)
    pdf = generar_pdf.PDF
    print(pdf.generar_factura_pdf())
    return {
            "titular":"LENIX ALDAIR PANTOJA VELASQUEZ",
            "apartamento": "202",
            "valor_recibo": valor,
            "mes_facturado": mes_facturado.month,
            "fecha_limite_pago": f"{mes_facturado.day + 3} - {mes_facturado.month} - {mes_facturado.year}",
            "entidad_financiera":f"Bancolombia ahorro a la mano cuenta nro: 03223759015",
            "pdf": ""
            }
