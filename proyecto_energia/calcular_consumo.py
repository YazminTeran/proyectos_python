energia_activa = 878.48
Alumbrado_publco = 2327.00
Subsidio = 0.5289



def calcular_consumo_energia_2(pPeriodo_consumo, pMora):
    if int(pPeriodo_consumo) <= 130:
        energia_neta = (energia_activa * int(pPeriodo_consumo))
        valor_subsidio = energia_neta * Subsidio
        valor_T = energia_neta - valor_subsidio
        Total_pagar= valor_T +Alumbrado_publco + float(pMora)
        print(round(Total_pagar))

    else: 
        energia_neta = (energia_activa * int(pPeriodo_consumo))
        Total_pagar=  energia_neta + Alumbrado_publco + float(pMora)
        
        print(round(Total_pagar))



