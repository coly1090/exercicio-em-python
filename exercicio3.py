cigs_dia=int(input("cigarrros por dia"))
anos_fumando=int(input("anos fumando:"))

#calculo direto:total de cigarros*
10 min/(minutos em um dia)
total_cigarros= cigs_dia *365* anos_fumando
dias_perdidos=(total_cigarros *10)/(24*60)
print(f"dias de vida perdidos:{dias_perdidos:.1f}")