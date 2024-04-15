import tkinter as tk
from tkinter import ttk
import progSintactico
import sys

class TextRedirector(object):
    def __init__(self, widget):
        self.widget = widget

    def write(self, str):
        self.widget.configure(state='normal')
        self.widget.insert('end', str)
        self.widget.see('end')
        self.widget.configure(state='disabled')

    def flush(self):
        pass

def check_code():
    # Limpia las tablas de tokens y errores
    for item in token_table.get_children():
        token_table.delete(item)
    for item in error_table.get_children():
        error_table.delete(item)

    code = txt.get("1.0", tk.END).strip()
    if not code:
        result_label.config(text="No hay código para verificar")
        return  

    errores, tokens = progSintactico.analizar(code)
    for error in errores:
        error_table.insert('', 'end', values=(error,))
    for token_type, token_value in tokens:
        token_table.insert('', 'end', values=(token_type, token_value))

    if not errores:
        result_label.config(text="Sin errores de sintaxis.")
    else:
        result_label.config(text="Errores encontrados:")

root = tk.Tk()
root.title("Analizador Léxico y Sintáctico")
root.configure(bg='lightgray')

# Configuración del frame principal
main_frame = ttk.Frame(root, padding=10, relief=tk.RAISED)
main_frame.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

# Área de texto para ingresar código
text_frame = ttk.LabelFrame(main_frame, text="Código", padding=10)
text_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
txt = tk.Text(text_frame, width=40, height=15, bg='lightblue')
txt.pack(expand=True, fill=tk.BOTH)

# Configuración de la consola de salida para mostrar resultados
output_console = tk.Text(main_frame, state='disabled', width=40, height=15, bg='lightgray')
output_console.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Redirigir stdout
sys.stdout = TextRedirector(output_console)

# Botón para iniciar el análisis
btn = tk.Button(main_frame, text="Analizar", command=check_code, bg='lightblue')
btn.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")

# Frame para tokens y errores
token_frame = ttk.LabelFrame(main_frame, text="Tokens", padding=10)
token_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
token_table = ttk.Treeview(token_frame, columns=('Type', 'Value'), show='headings')
token_table.heading('Type', text='Token')
token_table.heading('Value', text='Valor')
token_table.pack(expand=True, fill=tk.BOTH)

error_frame = ttk.LabelFrame(main_frame, text="Errores de Sintaxis", padding=10)
error_frame.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
error_table = ttk.Treeview(error_frame, columns=('Error',), show='headings')
error_table.heading('Error', text='Mensaje de Error')
error_table.pack(expand=True, fill=tk.BOTH)

# Resultado del análisis
result_label = tk.Label(main_frame, text="", fg="black")
result_label.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

root.mainloop()
