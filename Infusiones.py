# Autor: Jorge Menéndez S.
# Licencia: MIT License
#
# Copyright (c) 2024 Jorge Menéndez S.
#
# Por la presente se concede permiso, sin cargo, a cualquier persona que obtenga una copia
# de este software y los archivos de documentación asociados (el "Software"), para tratar
# en el Software sin restricciones, incluyendo sin limitación los derechos
# para usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y/o vender
# copias del Software, y para permitir a las personas a quienes se les proporcione el Software
# hacerlo, sujeto a las siguientes condiciones:
#
# El aviso de copyright anterior y este aviso de permiso se incluirán en todas
# las copias o partes sustanciales del Software.
#
# EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA,
# INCLUYENDO PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD,
# IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O
# LOS TITULARES DEL COPYRIGHT SERÁN RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑO U OTRA RESPONSABILIDAD,
# YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRO MODO, QUE SURJA DE,
# FUERA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTROS TRATOS EN EL
# SOFTWARE.

import tkinter as tk
from tkinter import messagebox

class InfusionCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Velocidad de Infusión")
        
        # Configuración del grid para que se ajuste al ancho de la pantalla
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Valores predeterminados para cada medicamento
        self.default_values = {
            "Norepinefrina": (0.1, 1, 8, 100),       # mcg/kg/min, mg, ml
            "Epinefrina": (0.1, 1, 2, 100),          # mcg/kg/min, mg, ml
            "Vasopresina": (0.01, 0.04, 40, 100),    # UI/min, UI, ml
            "Dopamina": (1, 20, 400, 250),           # mcg/kg/min, mg, ml
            "Dobutamina": (2, 20, 250, 250),         # mcg/kg/min, mg, ml
            "Nitroglicerina": (5, 200, 50, 250),     # mcg/min, mcg, ml
            "Nitroprusiato": (0.3, 10, 50, 250)      # mcg/kg/min, mg, ml
        }

        # Elementos de la interfaz de usuario
        self.setup_ui()

    def setup_ui(self):
        # Etiqueta y entrada para el peso del paciente
        tk.Label(self.root, text="Peso del paciente (kg):", anchor="w").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.weight_entry = tk.Entry(self.root)
        self.weight_entry.insert(0, "70")
        self.weight_entry.grid(row=0, column=1, padx=10, pady=10, sticky="we")

        # Etiqueta y menú desplegable para seleccionar el medicamento
        tk.Label(self.root, text="Seleccione el medicamento:", anchor="w").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.med_var = tk.StringVar(self.root)
        self.med_var.set("Norepinefrina")
        self.med_dropdown = tk.OptionMenu(self.root, self.med_var, *self.default_values.keys(), command=self.update_fields)
        self.med_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky="we")

        # Etiqueta y entrada para la dosis del medicamento
        tk.Label(self.root, text="Ingrese la dosis:", anchor="w").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.dose_entry = tk.Entry(self.root)
        self.dose_entry.grid(row=2, column=1, padx=10, pady=10, sticky="we")

        # Etiqueta para mostrar el rango de dosis del medicamento seleccionado
        self.dose_range_label = tk.Label(self.root, text="", anchor="w")
        self.dose_range_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        # Etiqueta y entrada para la cantidad del medicamento (mg o UI)
        tk.Label(self.root, text="Ingrese la cantidad del medicamento (mg o UI):", anchor="w").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(row=4, column=1, padx=10, pady=10, sticky="we")

        # Etiqueta y entrada para el volumen de la solución (ml)
        tk.Label(self.root, text="Ingrese el volumen de la solución (ml):", anchor="w").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.volume_entry = tk.Entry(self.root)
        self.volume_entry.grid(row=5, column=1, padx=10, pady=10, sticky="we")

        # Botones para calcular y borrar
        self.calculate_button = tk.Button(self.root, text="Calcular", command=self.calculate)
        self.calculate_button.grid(row=6, column=0, padx=10, pady=10, sticky="we")

        self.reset_button = tk.Button(self.root, text="Borrar", command=self.reset_fields)
        self.reset_button.grid(row=6, column=1, padx=10, pady=10, sticky="we")

        # Etiqueta para mostrar el resultado del cálculo
        self.result_label = tk.Label(self.root, text="Velocidad de infusión: ", anchor="w")
        self.result_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        # Actualizar los campos al iniciar la interfaz
        self.update_fields()

    def update_fields(self, *args):
        # Actualizar el rango de dosis según el medicamento seleccionado
        med = self.med_var.get()
        dose_range = self.default_values[med]
        if med == "Nitroglicerina":
            self.dose_range_label.config(text=f"Rango de dosis: {dose_range[0]} - {dose_range[1]} mcg/min")
        elif med == "Vasopresina":
            self.dose_range_label.config(text=f"Rango de dosis: {dose_range[0]} - {dose_range[1]} UI/min")
        else:
            self.dose_range_label.config(text=f"Rango de dosis: {dose_range[0]} - {dose_range[1]} mcg/kg/min")
        
        # Establecer los valores predeterminados para cantidad y volumen
        self.amount_entry.delete(0, tk.END)
        self.amount_entry.insert(0, str(dose_range[2]))
        self.volume_entry.delete(0, tk.END)
        self.volume_entry.insert(0, str(dose_range[3]))
        
        # Limpiar el campo de dosis y el resultado
        self.dose_entry.delete(0, tk.END)
        self.result_label.config(text="Velocidad de infusión: ")

    def reset_fields(self):
        # Restablecer todos los campos a sus valores predeterminados
        self.weight_entry.delete(0, tk.END)
        self.weight_entry.insert(0, "70")
        self.amount_entry.delete(0, tk.END)
        self.volume_entry.delete(0, tk.END)
        self.dose_entry.delete(0, tk.END)
        self.result_label.config(text="Velocidad de infusión: ")
        self.update_fields()

    def calculate(self):
        try:
            # Obtener los valores de los campos
            med = self.med_var.get()
            weight = float(self.weight_entry.get())
            dose = float(self.dose_entry.get())
            amount = float(self.amount_entry.get())
            volume = float(self.volume_entry.get())

            # Calcular la dosis por minuto según el medicamento seleccionado
            if med == "Vasopresina":
                dose_per_min = dose  # Dosis en UI/min
                concentration = amount / volume  # Concentración en UI/ml
            elif med == "Nitroglicerina":
                dose_per_min = dose  # Dosis en mcg/min
                concentration = amount * 1000 / volume  # Concentración en mcg/ml
            else:
                dose_per_min = dose * weight  # Dosis en mcg/kg/min
                concentration = amount * 1000 / volume  # Concentración en mcg/ml

            # Calcular la velocidad de infusión en ml/h
            rate = dose_per_min * 60 / concentration  # ml/h

            # Mostrar el resultado en la etiqueta correspondiente
            self.result_label.config(text=f"Velocidad de infusión: {rate:.2f} ml/h")

        except ValueError:
            # Mostrar un mensaje de error si se ingresan valores no numéricos
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")

if __name__ == "__main__":
    root = tk.Tk()
    app = InfusionCalculator(root)
    root.mainloop()
