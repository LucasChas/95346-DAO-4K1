import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from correctivo import Correctivo
from maquina import Maquina
from preventivo import Preventivo


class InterfazMantenimiento:

  def __init__(self, root):
    self.root = root
    self.root.title("Gestión de Mantenimientos de Máquinas")
    self.root.geometry("1000x650")
    self.root.minsize(850, 500)

    self.maquina = None

    # Estilos generales
    self.style = ttk.Style()
    self.style.theme_use("clam")

    self._crear_interfaz()

    # Intento de carga automática si existe el archivo por defecto
    ruta_default = "./data/mantenimientos.csv"
    if os.path.exists(ruta_default):
      self._cargar_datos(ruta_default)

  def _crear_interfaz(self):
    # -------------------------------------------------------------
    # 1. Panel de selección de archivo
    # -------------------------------------------------------------
    frame_archivo = ttk.Frame(self.root, padding=10)
    frame_archivo.pack(fill="x")

    self.lbl_ruta = ttk.Label(
        frame_archivo,
        text="Archivo: ./data/mantenimientos.csv",
        font=("Arial", 9, "italic"),
    )
    self.lbl_ruta.pack(side="left", padx=5)

    btn_abrir = ttk.Button(
        frame_archivo,
        text="Seleccionar otro archivo CSV...",
        command=self._seleccionar_archivo,
    )
    btn_abrir.pack(side="right", padx=5)

    # -------------------------------------------------------------
    # 2. Panel de Estadísticas / Resultados
    # -------------------------------------------------------------
    frame_stats = ttk.LabelFrame(
        self.root,
        text=" Resumen y Estadísticas Solicitadas ",
        padding=(15, 10),
    )
    frame_stats.pack(fill="x", padx=15, pady=5)

    self.lbl_gasto_total = ttk.Label(
        frame_stats,
        text="Gasto total acumulado: $ -",
        font=("Arial", 10, "bold"),
    )
    self.lbl_gasto_total.grid(row=0, column=0, sticky="w", pady=3, padx=10)

    self.lbl_caros = ttk.Label(
        frame_stats,
        text="Mantenimientos caros (>$10.000): -",
        font=("Arial", 10),
    )
    self.lbl_caros.grid(row=1, column=0, sticky="w", pady=3, padx=10)

    self.lbl_rotura = ttk.Label(
        frame_stats, text="Rotura más larga: -", font=("Arial", 10)
    )
    self.lbl_rotura.grid(row=2, column=0, sticky="w", pady=3, padx=10)

    # -------------------------------------------------------------
    # 3. Tabla de registros (Treeview)
    # -------------------------------------------------------------
    frame_tabla = ttk.Frame(self.root, padding=15)
    frame_tabla.pack(fill="both", expand=True)

    columnas = (
        "tipo",
        "fecha",
        "operario",
        "repuesto",
        "detalle_esp",
        "gasto_total",
    )
    self.tabla = ttk.Treeview(
        frame_tabla, columns=columnas, show="headings", selectmode="browse"
    )

    # Configuración de cabeceras
    self.tabla.heading("tipo", text="Tipo")
    self.tabla.heading("fecha", text="Fecha")
    self.tabla.heading("operario", text="Operario")
    self.tabla.heading("repuesto", text="Imp. Repuesto")
    self.tabla.heading("detalle_esp", text="Detalle Específico")
    self.tabla.heading("gasto_total", text="Gasto Total")

    # Configuración de columnas
    self.tabla.column("tipo", width=110, anchor="center")
    self.tabla.column("fecha", width=100, anchor="center")
    self.tabla.column("operario", width=160, anchor="w")
    self.tabla.column("repuesto", width=110, anchor="e")
    self.tabla.column("detalle_esp", width=360, anchor="w")
    self.tabla.column("gasto_total", width=120, anchor="e")

    scroll_y = ttk.Scrollbar(
        frame_tabla, orient="vertical", command=self.tabla.yview
    )
    self.tabla.configure(yscrollcommand=scroll_y.set)

    self.tabla.pack(side="left", fill="both", expand=True)
    scroll_y.pack(side="right", fill="y")

  def _seleccionar_archivo(self):
    archivo = filedialog.askopenfilename(
        title="Seleccionar mantenimientos.csv",
        filetypes=[("Archivos CSV", "*.csv"), ("Todos los archivos", "*.*")],
    )
    if archivo:
      self._cargar_datos(archivo)

  def _cargar_datos(self, ruta_archivo):
    try:
      # Instancia de la clase Maquina existente
      self.maquina = Maquina(ruta_archivo)
      self.lbl_ruta.config(text=f"Archivo cargado: {ruta_archivo}")

      # Limpiar tabla
      for item in self.tabla.get_children():
        self.tabla.delete(item)

      # Poblar la tabla con los mantenimientos leídos
      for m in self.maquina.mantenimientos:
        tipo_str = "Preventivo" if m.tipo_mantenimiento == 1 else "Correctivo"

        if isinstance(m, Preventivo):
          res_map = {
              1: "Funciona correctamente",
              2: "Recomienda revisión",
              3: "Detectó rotura",
          }
          resultado_texto = res_map.get(m.resultado, f"Código {m.resultado}")
          detalle = f"Resultado: {resultado_texto} | Insumos: ${m.importe_insumos:,.2f}"
        elif isinstance(m, Correctivo):
          detalle = f"Parada: {m.cantidad_horas_parada} hs | Técnico: ${m.importe_tecnico:,.2f}"
        else:
          detalle = "-"

        self.tabla.insert(
            "",
            "end",
            values=(
                tipo_str,
                m.fecha,
                m.operario,
                f"${m.importe_repuesto:,.2f}",
                detalle,
                f"${m.gastos_mantenimiento():,.2f}",
            ),
        )

      # Actualizar estadísticas usando los métodos de Maquina
      total = self.maquina.suma_gastos()
      caros = self.maquina.cant_mant_caros()
      rotura = self.maquina.rotura_mas_larga()

      self.lbl_gasto_total.config(
          text=f"Gasto total acumulado: ${total:,.2f}"
      )
      self.lbl_caros.config(
          text=f"Cantidad de mantenimientos caros (>$10.000): {caros}"
      )
      self.lbl_rotura.config(text=f"Rotura más larga: {rotura}")

    except FileNotFoundError:
      messagebox.showwarning(
          "Archivo no encontrado",
          f"No se encontró el archivo:\n{ruta_archivo}\n\nSeleccione uno con el botón superior.",
      )
    except Exception as e:
      messagebox.showerror("Error al procesar el archivo", str(e))


if __name__ == "__main__":
  ventana = tk.Tk()
  app = InterfazMantenimiento(ventana)
  ventana.mainloop()