import tkinter as tk
from tkinter import ttk
import progSintactico


def check_code():
    # Limpia las tablas de tokens 
    for item in token_table.get_children():
        token_table.delete(item)
    for item in error_table.get_children():
        error_table.delete(item)

    code = txt.get("1.0", tk.END).strip()
    if not code:
        result_label.config(text="No hay código para verificar")
        return  

    # Realiza el análisis y obtiene los errores y tokens
    errores, tokens = progSintactico.analizar(code)  
    
    # Muestra los errores en la interfaz gráfica
    for error in errores:
        error_table.insert('', 'end', values=(error,))

    # Muestra los tokens en la interfaz gráfica
    for token_type, token_value in tokens:
        token_table.insert('', 'end', values=(token_type, token_value))
    
    

    if not errores:
        result_label.config(text="Sin errores de sintaxis.")
    else:
        result_label.config(text="Errores encontrados:")

# Configuración de la ventana de Tkinter
root = tk.Tk()
root.title("Analizador Léxico y Sintáctico")
root.configure(bg='lightgray')

main_frame = ttk.Frame(root, padding=10, relief=tk.RAISED)
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
main_frame.pack(padx=10, pady=10)

# área de texto para ingresar código
text_frame = ttk.LabelFrame(main_frame, text="Código", padding=10)
text_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
codigo = '''numero => int(99)'''
txt = tk.Text(text_frame, width=50, height=15, bg='lightblue')
txt.grid(row=0, column=0, padx=10, pady=10)
txt.insert(tk.END, codigo)

# Botón para iniciar el análisis
def on_enter(e):
    btn.config(bg='green', fg='white')

def on_leave(e):
    btn.config(bg='lightblue', fg='black')

btn = tk.Button(main_frame, text="Analizar", command=check_code, width=10, height=2, bg='lightblue', fg='black')
btn.grid(row=0, column=1, padx=10, pady=10)
btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)

#
style = ttk.Style()
style.theme_use("default")

style.configure("Custom.Treeview", background="lightblue", fieldbackground="lightblue", foreground="black")
style.map("Custom.Treeview", background=[('selected', 'blue')], foreground=[('selected', 'white')])

# tokens identificados
token_frame = ttk.LabelFrame(main_frame, text="Tokens", padding=10)
token_frame.grid(row=1, column=0, padx=10, pady=10)

token_table = ttk.Treeview(token_frame, columns=('Type', 'Value'), show='headings', style='Custom.Treeview')
token_table.heading('Type', text='Token')
token_table.heading('Value', text='Valor')
token_table.pack()

# errores sintácticos
error_frame = ttk.LabelFrame(main_frame, text="Errores de Sintaxis", padding=10)
error_frame.grid(row=1, column=1, padx=10, pady=10)

error_table = ttk.Treeview(error_frame, columns=('Error',), show='headings', style='Custom.Treeview')
error_table.heading('Error', text='Mensaje de Error')
error_table.column('Error', width=200)
error_table.pack()

# resultado del análisis
result_label = tk.Label(main_frame, text="", fg="black")
result_label.grid(row=2, column=0, columnspan=2, pady=10)


root.mainloop()