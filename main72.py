def min_current_resistance(voltages, resistances):
    currents = [voltage / resistance for voltage, resistance in zip(voltages, resistances)]
    min_current = min(currents)
    return currents.index(min_current) + 1


voltages = [10, 20, 15]  # вольты
resistances = [5, 10, 3] # омы
result = min_current_resistance(voltages, resistances)
print(f"Сопротивление с минимальным током: №{result}")
