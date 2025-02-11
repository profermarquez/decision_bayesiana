import numpy as np

# Simulación de datos históricos (100 observaciones)
np.random.seed(42)  # Para reproducibilidad
historical_demand = np.random.choice(["Alta", "Baja"], size=100, p=[0.6, 0.4])  # 60% alta, 40% baja

# Simulación de informes del mercado con precisión
accuracy_high_demand = 0.8  # El informe es correcto el 80% de las veces si la demanda es alta
accuracy_low_demand = 0.3   # El informe dice "Alta" el 30% de las veces si la demanda es baja

# Generar informes del mercado
market_reports = []
for demand in historical_demand:
    if demand == "Alta":
        report = np.random.choice(["Alta", "Baja"], p=[accuracy_high_demand, 1 - accuracy_high_demand])
    else:
        report = np.random.choice(["Alta", "Baja"], p=[accuracy_low_demand, 1 - accuracy_low_demand])
    market_reports.append(report)

# Contar frecuencias para calcular las probabilidades previas
prior_H1 = np.mean(historical_demand == "Alta")  # P(H1): Probabilidad de demanda alta
prior_H2 = 1 - prior_H1                           # P(H2): Probabilidad de demanda baja

# Contar cuántos informes predicen "Alta" realmente
E_high_count = market_reports.count("Alta")
E_low_count = market_reports.count("Baja")

# Calcular probabilidades condicionales
P_E_given_H1 = accuracy_high_demand
P_E_given_H2 = accuracy_low_demand

# Teorema de Bayes P(A|B) = P(B|A) * P(A) / P(B)
# : calcular P(H1 | E) (posterior cuando el informe es "Alta")

P_E = (P_E_given_H1 * prior_H1) + (P_E_given_H2 * prior_H2)  # Probabilidad total de la evidencia
P_H1_given_E = (P_E_given_H1 * prior_H1) / P_E  # Probabilidad posterior de demanda alta

# Decisión basada en la probabilidad posterior, por defecto es "Vender"
decision = "Vender" if P_H1_given_E > 0.5 else "No vender"

# Mostrar resultados
print(f"Probabilidad anterior de demanda alta: {prior_H1:.2f}")
print(f"Frecuencia de informes 'Alta': {E_high_count}")
print(f"Probabilidad posterior de demanda alta: {P_H1_given_E:.2f}")
print(f"Decisión del sistema: {decision}")
