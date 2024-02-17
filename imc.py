def imc(x, y):
  return x/(y**2)

def resultado (calculo):
  if calculo < 16:
    return "magreza grave"
  elif calculo > 16  and calculo < 17:
    return "magreza moderada"
  elif calculo > 17 and calculo < 18.5:
    return "magreza leve"
  elif calculo > 18.5 and calculo < 25:
    return "saudavel"
  elif calculo > 25 and calculo < 30:
    return "sobrepeso"
  elif calculo > 30 and calculo < 35:
    return "obesidade grau um"
  elif calculo > 35 and calculo < 40:
    return "obesidade grau dois - severa"
  elif calculo > 40:
    return "obesidade grau três - mórbida"

x = float(input("Qual o seu peso em kg? Digite assim como o exemplo: '60' "))
y = float(input("Qual sua altura em metros? Digite sua altura assim como o exemplo: '1.65' "))

z = imc(x, y)
print("Seu IMC é:", z)
print("Isso é considerado:", resultado(z))
