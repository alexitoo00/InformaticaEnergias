import tkinter as tk

ventana = tk.Tk()
ventana.title("My Program")

# Definir variable
voltaje = tk.DoubleVar()
intensidad = tk.DoubleVar()
resistencia = tk.DoubleVar()
mensajes = tk.StringVar(ventana, value="")

# Definir funcións


def Calcular():
    global mensajes
    try:
        if voltaje.get() == 0:
            voltaje.set(intensidad.get()*resistencia.get())
        elif intensidad.get() == 0:
            intensidad.set(voltaje.get()/resistencia.get())
        elif resistencia.get() == 0:
            resistencia.set(voltaje.get()/intensidad.get())
        else:
            mensajes.set(
                "Al menos un dos campos debe ser '0' para poder efectuar o cálculo")
            return
        mensajes.set("")
    except:
        mensajes.set("Math Error")


def Salir():
    quit()

# Estructurar un menú


labelEntry = {"Voltaje (V)": voltaje, "Intensidad (A)": intensidad,
              "Resistencia (Ω)": resistencia}


def EstructurarMenu():
    label = ventana.geometry("700x450")

    labelVoltaje = tk.Label(ventana, text="Voltaje (V)", font=("Arial", 10))
    voltajeEntry = tk.Entry(ventana, textvariable=voltaje, font=("Arial", 48))
    labelIntensidad = tk.Label(
        ventana, text="Intensidad (A)", font=("Arial", 10))
    intensidadEntry = tk.Entry(
        ventana, textvariable=intensidad, font=("Arial", 48))
    labelResistencia = tk.Label(
        ventana, text="Resistencia (Ω)", font=("Arial", 10))
    resistenciaEntry = tk.Entry(
        ventana, textvariable=resistencia, font=("Arial", 48))

    botonCalcular = tk.Button(ventana, text="Calcular", command=Calcular, font=(
        "Arial", 24), background="green")
    botonSalir = tk.Button(ventana, text="Salir",
                           command=Salir, font=("Arial", 24), background="red")
    labelMensajes = tk.Label(
        ventana, textvariable=mensajes, font=("Arial", 16))

    # Posición
    labelVoltaje.grid(row=0, column=0)
    voltajeEntry.grid(row=1, column=0)
    labelIntensidad.grid(row=2, column=0)
    intensidadEntry.grid(row=3, column=0)
    labelResistencia.grid(row=4, column=0)
    resistenciaEntry.grid(row=5, column=0)
    labelMensajes.grid(row=6, column=0)
    botonCalcular.grid(row=7, column=0)
    botonSalir.grid(row=8, column=0)


# O programa empeza aquí
EstructurarMenu()
ventana.mainloop()
