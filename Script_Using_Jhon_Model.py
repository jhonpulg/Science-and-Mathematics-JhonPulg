# Script to calculate the distance traveled between floors
# and the number of intermediate floors using Jhon's Model

# =====================================================================
# Direct distance (without list, works for consecutive floors)
# =====================================================================
current_floor = -1       # Floor where I am
destination_floor = 5    # Destination floor

floors_distance = abs(destination_floor - current_floor)

print(f"The distance between floor {current_floor} and floor {destination_floor} is: {floors_distance} floor(s).")


# =====================================================================
# Intermediate floors using Jhon's Model
# Note: no floor 0 (ground floor convention). The list skips it.
# =====================================================================
floors_list = [-3, -2, -1, 1, 2, 3, 4, 5]

# Validation: both floors must exist in the list
if current_floor in floors_list and destination_floor in floors_list:
    index_a = floors_list.index(current_floor)
    index_b = floors_list.index(destination_floor)

    floors_between = abs(index_a - index_b) - 1
    print(f"Between floor {current_floor} and floor {destination_floor} there are exactly {floors_between} floor(s).")
else:
    print("Error: one or both floors are not in the floors list.")
 # _______________________________________________________________________________________________________________________
#Spanih
# Script para calcular la distancia recorrida entre pisos
# y el número de pisos intermedios usando el Modelo de Jhon

# =====================================================================
# Distancia directa (sin lista, funciona para pisos consecutivos)
# =====================================================================
piso_actual = -1       # Piso donde estoy
piso_destino = 5       # Piso de destino

distancia_pisos = abs(piso_destino - piso_actual)

print(f"La distancia entre el piso {piso_actual} y el piso {piso_destino} es: {distancia_pisos} piso(s).")


# =====================================================================
# Pisos intermedios usando el Modelo de Jhon
# Nota: no existe el piso 0 (convención de planta baja). La lista lo omite.
# =====================================================================
lista_pisos = [-3, -2, -1, 1, 2, 3, 4, 5]

# Validación: ambos pisos deben existir en la lista
if piso_actual in lista_pisos and piso_destino in lista_pisos:
    indice_a = lista_pisos.index(piso_actual)
    indice_b = lista_pisos.index(piso_destino)

    pisos_intermedios = abs(indice_a - indice_b) - 1
    print(f"Entre el piso {piso_actual} y el piso {piso_destino} hay exactamente {pisos_intermedios} piso(s).")
else:
    print("Error: uno o ambos pisos no están en la lista de pisos.")
