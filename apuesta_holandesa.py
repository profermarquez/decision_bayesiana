import numpy as np

# Simulación de datos históricos (100 observaciones)
np.random.seed(42)
historical_demand = np.random.choice(["Alta", "Baja"], size=100, p=[0.6, 0.4])

# Simulación de informes del mercado (Erróneo e Incorrecto)
wrong_accuracy_high_demand = 0.9  # *Error: se sobrestima la precisión*
wrong_accuracy_low_demand = 0.5   # *Error: se asigna mal la probabilidad*

# Simulación de informes del mercado (Correcto y Bayesiano)
correct_accuracy_high_demand = 0.8  # Correcto según datos históricos
correct_accuracy_low_demand = 0.3   # Correcto según datos históricos

# Generar informes del mercado con probabilidades incorrectas y correctas
wrong_market_reports = []
correct_market_reports = []

for demand in historical_demand:
    # Probabilidades incorrectas
    if demand == "Alta":
        report = np.random.choice(["Alta", "Baja"], p=[wrong_accuracy_high_demand, 1 - wrong_accuracy_high_demand])
    else:
        report = np.random.choice(["Alta", "Baja"], p=[wrong_accuracy_low_demand, 1 - wrong_accuracy_low_demand])
    wrong_market_reports.append(report)

    # Probabilidades correctas
    if demand == "Alta":
        report = np.random.choice(["Alta", "Baja"], p=[correct_accuracy_high_demand, 1 - correct_accuracy_high_demand])
    else:
        report = np.random.choice(["Alta", "Baja"], p=[correct_accuracy_low_demand, 1 - correct_accuracy_low_demand])
    correct_market_reports.append(report)

# Contar frecuencias para calcular las probabilidades previas
prior_H1 = np.mean(historical_demand == "Alta")
prior_H2 = 1 - prior_H1

# Contar cuántos informes predicen "Alta" realmente
wrong_E_high_count = wrong_market_reports.count("Alta")
correct_E_high_count = correct_market_reports.count("Alta")

# Calcular probabilidades condicionales incorrectas
P_E_given_H1_wrong = wrong_accuracy_high_demand
P_E_given_H2_wrong = wrong_accuracy_low_demand

# Calcular probabilidades condicionales correctas
P_E_given_H1_correct = correct_accuracy_high_demand
P_E_given_H2_correct = correct_accuracy_low_demand

# Teorema de Bayes (Probabilidades Incorrectas)
P_E_wrong = (P_E_given_H1_wrong * prior_H1) + (P_E_given_H2_wrong * prior_H2)
P_H1_given_E_wrong = (P_E_given_H1_wrong * prior_H1) / P_E_wrong

# Teorema de Bayes (Probabilidades Correctas)
P_E_correct = (P_E_given_H1_correct * prior_H1) + (P_E_given_H2_correct * prior_H2)
P_H1_given_E_correct = (P_E_given_H1_correct * prior_H1) / P_E_correct

# Decisiones basadas en probabilidades incorrectas y correctas
decision_wrong = "Vender" if P_H1_given_E_wrong > 0.5 else "No vender"
decision_correct = "Vender" if P_H1_given_E_correct > 0.5 else "No vender"

# Mostrar resultados
print("\n===== PROBABILIDADES Y DECISIONES =====")
print(f"Probabilidad anterior de demanda alta: {prior_H1:.2f}\n")
print("\n En el modelo incorrecto, el problema no es el 75%% en sí, sino cómo se llegó a ese número.")
print(">> 🛑 CASO INCORRECTO (Dutch Book - Incoherente) <<")
print(f"Frecuencia de informes 'Alta': {wrong_E_high_count}")
print(f"Probabilidad posterior de demanda alta: {P_H1_given_E_wrong:.2f}")
print(f"Decisión del sistema: {decision_wrong}\n")

print(">> ✅ CASO CORRECTO (Bayes Coherente) <<")
print(f"Frecuencia de informes 'Alta': {correct_E_high_count}")
print(f"Probabilidad posterior de demanda alta: {P_H1_given_E_correct:.2f}")
print(f"Decisión del sistema: {decision_correct}")
