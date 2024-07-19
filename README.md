# Infusiones-vasopresores-inotropicos-
Este código proporciona una herramienta gráfica para calcular la velocidad de infusión de diferentes medicamentos inotrópicos o vasopresores, facilitando el ajuste de las dosis y volúmenes requeridos según el medicamento seleccionado. Hace uso de la biblioteca `tkinter` en Python. Esta es una explicación sobre lo que hace el código:

### **Descripción General:**
La aplicación permite a los usuarios ingresar datos relacionados con la infusión de medicamentos y calcular la velocidad de infusión requerida en mililitros por hora (`ml/h`). Está diseñada para calcular infusiones para varios medicamentos comunes.

La fórmula general para calcular la velocidad de infusión en mililitros por hora (ml/h) a partir de una dosis en microgramos por kilogramo por minuto (mcg/kg/min) es la siguiente:

$\text{Velocidad de infusión (ml/h)} = \frac{\text{Dosis (mcg/kg/min)} \times \text{Peso (kg)} \times 60}{\text{Concentración (mcg/ml)}}$

Donde:
- $\text{Dosis}$ $\text{(mcg/kg/min\)}$ es la dosis del medicamento por kilogramo de peso corporal por minuto. Para Nitroglicerina, $\text{Dosis}$ se expresa en $\text{(mcg/min)}$ y para Vasopresina, se expresa en $\text{(UI/min)}$.
- $\text{Peso (kg)}$ es el peso del paciente en kilogramos.
- $\text{Concentración [mg} \times \text{1000]}$ $\text{(mcg/ml)}$ es la concentración del medicamento en la solución (microgramos por mililitro).
- El factor $\(60\)$ convierte el cálculo de minutos a horas.

### **Componentes del Código:**

1. **Configuración Inicial:**
   - **Clase `InfusionCalculator`**: Define la interfaz gráfica y la lógica para el cálculo de la velocidad de infusión.
   - **Método `__init__`**: Configura la ventana principal, establece valores predeterminados para diferentes medicamentos y llama al método `setup_ui` para configurar los elementos de la interfaz gráfica.

2. **Interfaz de Usuario (`setup_ui`):**
   - **Campos de Entrada**: 
     - Peso del paciente.
     - Selección del medicamento desde un menú desplegable.
     - Dosis del medicamento (mcg/kg/min, UI/min, etc.).
     - Cantidad del medicamento (mg o UI).
     - Volumen de la solución (ml).
   - **Botones**:
     - **Calcular**: Llama al método `calculate` para realizar el cálculo.
     - **Borrar**: Llama al método `reset_fields` para limpiar todos los campos.
   - **Etiqueta de Resultado**: Muestra la velocidad de infusión calculada.

3. **Actualización de Campos (`update_fields`):**
   - **Actualiza el Rango de Dosis**: Muestra el rango de dosis permitido según el medicamento seleccionado.
   - **Configura Valores Predeterminados**: Establece los valores predeterminados para la cantidad del medicamento y el volumen de la solución.

4. **Restablecimiento de Campos (`reset_fields`):**
   - **Limpiar Campos**: Restablece todos los campos a sus valores predeterminados y limpia el resultado de la infusión.

5. **Cálculo de la Velocidad de Infusión (`calculate`):**
   - **Obtener Valores de Entrada**: Recoge los datos ingresados por el usuario.
   - **Cálculo**:
     - **Medicamentos Específicos**:
       - **Vasopresina**: Utiliza la dosis en UI/min y calcula la concentración en UI/ml.
       - **Nitroglicerina**: Utiliza la dosis en mcg/min y calcula la concentración en mcg/ml.
       - **Para el resto de medicamentos**: Utiliza la dosis en mcg/kg/min y calcula la concentración en mcg/ml.
     - **Velocidad de Infusión**: Calcula la velocidad de infusión en ml/h.
   - **Mostrar Resultado**: Muestra la velocidad de infusión calculada en la etiqueta correspondiente.

6. **Manejo de Errores**:
   - **Error de Valor**: Muestra un mensaje de error si se ingresan valores no numéricos en los campos de entrada.

### **Cómo Funciona:**

1. **Inicio de la Aplicación**:
   - Se crea una ventana principal (`root`) y se instancia la clase `InfusionCalculator` para inicializar la interfaz gráfica.

2. **Interacción del Usuario**:
   - Los usuarios ingresan datos, seleccionan un medicamento y presionan "Calcular" para obtener la velocidad de infusión o "Borrar" para restablecer los campos.


