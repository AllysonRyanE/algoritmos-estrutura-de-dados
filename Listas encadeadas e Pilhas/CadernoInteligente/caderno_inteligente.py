#PILHAS
manuais = input()
manuaisf = []
for i in range(len(manuais)):
    manuaisf.append(manuais[i])

manuais_desc = manuaisf[:]
index_frente = []
check = False
for i in manuais_desc:
  if i == "F":
    index_frente.append(manuais_desc.index(i))
    manuais_desc[manuais_desc.index(i)] = "X"
  elif i == "V":
    if len(index_frente)==0:
      print(f"Incorreto, devido a capa na posição {manuais_desc.index(i)+1}.")
      check = True
      break
    else:
      index_frente.pop(0)
      manuais_desc[manuais_desc.index(i)] = "Y"



if len(index_frente)==0 and not check:
  print("Correto.")
elif len(index_frente)>0 and not check:
  print(f"Incorreto, devido a capa na posição {index_frente[0]+1}.")
