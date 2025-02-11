# contexto:
Un minorista tiene dos opciones:
- Vender el producto si cree que la demanda será alta.
- No vender si cree que la demanda será baja.
El sistema utiliza Bayes para actualizar sus creencias sobre la demanda en función de datos históricos y un indicador del mercado.
El sistema ha calculado que la probabilidad posterior de que la demanda sea alta después de recibir el informe es 0.8 (80%). Como esta probabilidad es mayor al 50%, la decisión tomada es: "Vender", caso contrario "No vender"


# apuesta_holandesa
El Teorema del Holandés (Dutch Book Theorem) nos dice que si asignamos probabilidades de forma inconsistente, un adversario (por ejemplo, el mercado o competidores) podría explotar nuestras malas decisiones y hacernos perder dinero de manera sistemática.


# instalar y activar el entorno virtual
/virtualenv env         /env/Scripts/activate.bat
# requisitos
pip install numpy
# Ejecución
py desición
