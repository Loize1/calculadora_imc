def imc(x, y):
  if x == 0:
        raise ValueError("Peso não pode ser zero. Tente novamente")
  if y == 0:
        raise ValueError("Altura não pode ser zero. Tente novamente")
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

try:
    x = None
    y = None

    while x is None or x <= 0:
        peso_str = input("Qual o seu peso em kg? Digite assim como o exemplo: '60'  ")
        x = float(peso_str)
        if x <= 0:
            print("O peso deve ser maior do que zero.")
        if x > 600:
            print ("O peso deve ser menor do que 600kg.")
            raise ValueError("Peso inválido")
            

    while y is None or y <= 0:
        altura_str = input("Qual sua altura em metros? Digite sua altura assim como o exemplo: '1.65' ")
        y = float(altura_str)
        if y <= 0:
            print("A altura deve ser maior do que zero.")
        if y > 3:
            print("A altura deve ser menor do que 3 metros")
            raise ValueError("Altura inválida")


    z = imc(x, y)
    print("Seu IMC é:", z)
    print("Isso é considerado:", resultado(z))
except ValueError as e:
    print("Erro:", e)
except Exception as e:
    print("Ocorreu um erro inesperado:", e)