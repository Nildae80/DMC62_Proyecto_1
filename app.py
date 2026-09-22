import streamlit as st
import numpy as np
import pandas as pd
import libreria_funciones_proyecto1 as lf
from librería_clases_proyecto1 import Servidor

st.set_page_config(
    page_title="Proyecto 1 | Python Analytics",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("Especialización en Python for Analytics")
imagen = st.sidebar.image("Python_logo.png", width=200)
modulos = st.sidebar.selectbox("Selecciones el modulo", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])
st.sidebar.image("DMC.png", width=150)

# Creamos 3 columnas
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("Python_logo.png", width=300)
    st.title("PROYECTO 1 📋")
    st.markdown("---")

st.subheader("Proyecto Aplicado en Streamlit – Fundamentos de Programación")

if modulos == "Home":
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("👤 Datos del Estudiante")
        st.markdown("**Nombre completo:** Nilda Echevarria Meza")
        st.markdown("**Información general:** Ingeniero de Sistemas, con experiencia en el sector de más de 5 años")
        
    with col2:
        st.subheader("📚 Información del Curso")
        st.markdown("**Nombre del módulo:** Programación con Python y Streamlit")
        st.markdown("**Año:** 2026")
    
    st.markdown("---")
    
    st.subheader("📌 Descripción del Proyecto")
    st.info("""
    Esta aplicación fue desarrollada como parte de la evaluación práctica del módulo. Su objetivo principal es proveer una interfaz interactiva y fácil de usar para la gestión de registros mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar).
    
    **Principales funcionalidades:**
    - **Flujo de caja con listas:** Formulario dinámico de Registro de Movimientos.
    - **Registro con NumPy, arrays y DataFrame:** Formulario dinámico Registro de Productos.
    - **Uso de funciones desde una librería externa:** Formulario dinámico de registro para calcular el tiempo de transferencia de un archivo con funciones.
    - **Uso de clases desde una librería externa con CRUD:** Formulario dinámico para el monitoreo e inspección del estado, disponibilidad y uso de almacenamiento de servidores mediante POO.
    """)

    st.markdown("---")
    st.subheader("📌 Tecnologías utilizadas:")
    st.info("GIT, Python, Streamlit, NumPy, Pandas.")

## EJERCICIO 1
elif modulos == "Ejercicio 1":
    st.header("Te encuentras en la ventana del Ejercicio 1")
    st.write("En este ejercicio se deberá desarrollar un pequeño módulo para registrar movimientos financieros en una lista vacía.")
   
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    st.subheader("Formulario de Registra tu Movimientos ✏️")

    with st.form("form_movimientos", clear_on_submit=True):
        concepto = st.text_input("Ingresa el concepto del movimiento")
        tipo_Movimiento = st.selectbox("Selecciona el tipo de movimiento", ["Ingreso", "Gasto"], index=None, placeholder="Seleccione tipo de movimiento...")
        importe = float(st.number_input("Ingresa el importe del movimiento S/ ", value=0.00, min_value=0.0, step=0.5, format="%.2f"))
        btn_guardar = st.form_submit_button("Guardar ➕")
      
    if btn_guardar:
        if concepto.strip() == "":
            st.warning("Por favor, ingresa un movimiento antes de presionar el botón.")
        elif tipo_Movimiento is None:
            st.warning("Por favor, ingresa el tipo de movimiento antes de presionar el botón.")
        elif importe <= 0:
            st.warning("Por favor, ingresa un importe mayor a cero.")
        else:
            st.session_state.movimientos.append((concepto, tipo_Movimiento, importe))
            st.toast(f"¡Movimiento '{concepto}' agregado con éxito!", icon="✅")
            st.rerun()

    saldo_total = sum(mov[2] if mov[1] == "Ingreso" else -mov[2] for mov in st.session_state.movimientos)
    ingresos_total = sum(mov[2] if mov[1] == "Ingreso" else 0 for mov in st.session_state.movimientos)
    gastos_total = sum(mov[2] if mov[1] == "Gasto" else 0 for mov in st.session_state.movimientos)

    if len(st.session_state.movimientos) > 0:
        df_movimientos = pd.DataFrame(st.session_state.movimientos, columns=["Concepto", "Tipo de Movimiento", "Importe"])
        
        st.subheader("📊 Listado de movimientos:")
        st.dataframe(
            df_movimientos,
            use_container_width=True,
            column_config={"Importe": st.column_config.NumberColumn("Importe", format="S/ %.2f")}
        )
        st.write("Ingresos total: ", f"{ingresos_total:.2f}")
        st.write("Gastos total: ", f"{gastos_total:.2f}")
        st.write("Saldo total: ", f"{saldo_total:.2f}")
      
        if saldo_total > 0:
            st.metric(label="Flujo de caja", value="A FAVOR", delta="+")
        elif saldo_total < 0:
            st.metric(label="Flujo de caja", value="EN CONTRA", delta="-")
        else:
            st.metric(label="Flujo de caja", value="CUADRADO", delta="+")
    else:
        st.info("Aún no hay movimientos registrados.")

## EJERCICIO 2
elif modulos == "Ejercicio 2":
    st.header("Te encuentras en la ventana del Ejercicio 2")
    st.write("En este ejercicio se deberá crear un formulario para registrar información usando arreglos de NumPy.")
    
    if "inventario" not in st.session_state:
        st.session_state.inventario = np.empty((0, 5), dtype=object)
    
    st.subheader("Formulario de Registro de Productos ✏️")

    with st.form("form_inventario", clear_on_submit=True):
        nombre = st.text_input("Ingresa el nombre del Producto")
        categoria = st.selectbox("Selecciona la categoría del producto", ["Abarrotes", "Bebidas", "Mascotas", "Libreria"], index=None, placeholder="Seleccione la categoría...")
        precio = float(st.number_input("Ingresa el precio de cada producto (S/) ", value=0.00, min_value=0.0, step=0.5, format="%.2f"))
        cantidad = int(st.number_input("Cantidad", min_value=1, step=1))
        btn_guardar = st.form_submit_button("Guardar ➕")
      
    if btn_guardar:
        if nombre.strip() == "":
            st.warning("Por favor, ingresa un producto.")
        elif categoria is None:
            st.warning("Por favor, selecciona una categoría.")
        elif precio <= 0:
            st.warning("El precio debe ser mayor a cero.")
        else:
            total = precio * cantidad
            nuevo_registro = np.array([[nombre, categoria, precio, cantidad, total]], dtype=object)
            st.session_state.inventario = np.vstack((st.session_state.inventario, nuevo_registro))
            st.toast(f"¡Producto '{nombre}' agregado con éxito!", icon="✅")
            st.rerun()

    if st.session_state.inventario.shape[0] > 0:
        st.subheader("📦 Inventario de productos")
        df_mostrar = pd.DataFrame(st.session_state.inventario, columns=["Producto", "Categoría", "Precio", "Cantidad", "Total"])
        st.dataframe(
            df_mostrar,
            use_container_width=True,
            column_config={
                "Precio": st.column_config.NumberColumn("Precio", format="S/ %.2f"),
                "Total": st.column_config.NumberColumn("Total", format="S/ %.2f"),
            },
        )  
        total_general = np.sum(st.session_state.inventario[:, 4].astype(float))
        st.metric("Importe Total Acumulado", f"S/ {total_general:,.2f}")  
    else:
        st.info("Aún no hay productos registrados.")

## EJERCICIO 3
elif modulos == "Ejercicio 3":
    st.header("Te encuentras en la ventana del Ejercicio 3")
    st.write("En este ejercicio se usará funciones desde una librería externa.")
    
    if "tiempo" not in st.session_state or st.session_state.tiempo.shape[1] != 4:
        st.session_state.tiempo = np.empty((0, 4), dtype=object)
    
    st.subheader("Formulario de registro para calcular el tiempo de transferencia de un archivo con `funciones` ✏️")

    # --- FORMULARIO DE STREAMLIT ---
    with st.form("form_funcion", clear_on_submit=True):
        tipo_Funcion = st.selectbox(
            "Seleccione el tipo de función",
            ["Calcular tiempo de transferencia de archivo", "Otro"],
            index=None,
            placeholder="Seleccione tipo de opción..."
        )  
        
        # Carga dinámica de inputs según la opción seleccionada
        if tipo_Funcion == "Calcular tiempo de transferencia de archivo":
            tamano_archivo = float(st.number_input(
                "Ingresa el tamaño del archivo (MB)",
                value=0.00,
                min_value=0.0,
                step=0.1,
                format="%.2f"
            ))
            velocidad = float(st.number_input(
                "Ingresa la velocidad de transferencia (MBPS)",
                value=0.00,
                min_value=0.0,
                step=0.1,
                format="%.2f"
            ))
        elif tipo_Funcion == "Otro":
            st.info("No se tiene implementado otras funciones por el momento.")

        # El botón DEBE ir siempre al final del st.form fuera de los condicionales
        btn_guardar = st.form_submit_button("Guardar ➕")
      
    # --- LÓGICA AL PRESIONAR EL BOTÓN ---
    if btn_guardar:
        if tipo_Funcion is None:
            st.warning("Por favor, selecciona una opción del menú desplegable antes de guardar.")
        elif tipo_Funcion == "Otro":
            st.warning("No se puede realizar ningún cálculo con la opción 'Otro'.")
        elif tipo_Funcion == "Calcular tiempo de transferencia de archivo":
            if velocidad <= 0 or tamano_archivo <= 0:
                st.error("El tamaño del archivo y la velocidad deben ser mayores a 0.")
            else:
                resultado_tiempo = lf.calcular_tiempo_transferencia_archivo(tamano_archivo, velocidad)
                minutos = resultado_tiempo["tiempo_minutos"]
                segundos = resultado_tiempo["tiempo_segundos"]
        
                nuevo_registro = np.array([[tamano_archivo, velocidad, minutos, segundos]], dtype=object)
                st.session_state.tiempo = np.vstack((st.session_state.tiempo, nuevo_registro))
                
                st.toast("¡Cálculo realizado y guardado con éxito!", icon="✅")
                st.rerun()

    # --- TABLA HISTÓRICA (Fuera del formulario) ---
    if st.session_state.tiempo.shape[0] > 0:
        st.subheader("⚡ Tabla histórica de resultados obtenidos")
        df_mostrar = pd.DataFrame(
            st.session_state.tiempo,
            columns=["Tamaño (MB)", "Velocidad (MBPS)", "Tiempo en Minutos", "Tiempo en Segundos"]
        )
        st.dataframe(
            df_mostrar,
            use_container_width=True,
            column_config={
                "Tamaño (MB)": st.column_config.NumberColumn("Tamaño (MB)", format="%.2f MB"),
                "Velocidad (MBPS)": st.column_config.NumberColumn("Velocidad (MBPS)", format="%.2f MBPS"),
                "Tiempo en Minutos": st.column_config.NumberColumn("Tiempo (min)", format="%.2f min"),
                "Tiempo en Segundos": st.column_config.NumberColumn("Tiempo (seg)", format="%.2f seg"),
            },
        )
    else:
        st.info("Aún no hay ejecuciones registradas.")


## EJERCICIO 4
else:
    st.header("Te encuentras en la ventana de ejercicio 4")
    st.write("En este ejercicio se usara clases desde una librería externa con CRUD - Gestión e inspección de estado de servidores mediante la clase `Servidor`.✏️")
   
    if "servidores" not in st.session_state or st.session_state.servidores.shape[1] != 8:
        st.session_state.servidores = np.empty((0, 8), dtype=object)
    
    opcion = st.selectbox("Seleccione la operación que desea realizar:", ["Crear un nuevo Servidor", "Ver listado de Servidores", "Actualizar informacion del Servidor", "Eliminar un Servidor"])
    st.divider()
    
    if opcion == "Crear un nuevo Servidor":
        st.subheader("Registrar un nuevo servidor")
    
        with st.form("form_crear_servidor", clear_on_submit=True):
            nombre = st.text_input("Nombre del Servidor")  
            tiempo_total = float(st.number_input("Tiempo Total de Operación (horas)", min_value=0.0, value=0.0, step=10.0, format="%.2f"))
            tiempo_caida = st.number_input("Tiempo de Caída (horas)", min_value=0.0, value=0.0, step=0.5, format="%.2f")
            alm_total = st.number_input("Almacenamiento Total (GB)", min_value=0.0, value=0.0, step=50.0, format="%.2f")
            alm_usado = st.number_input("Almacenamiento Usado (GB)", min_value=0.0, value=0.0, step=10.0, format="%.2f")
            btn_guardar = st.form_submit_button("Guardar ➕")
    
        if btn_guardar:
            if not nombre.strip():
                st.error("Por favor ingrese un nombre para el servidor.")
            else:
                try:
                    srv = Servidor(nombre=nombre.strip(), tiempo_total_h=tiempo_total, tiempo_caida_h=tiempo_caida, almacenamiento_total_gb=alm_total, almacenamiento_usado_gb=alm_usado)
                    resumen = srv.resumen()
                    nueva_fila = np.array([[srv.nombre, srv.tiempo_total_h, srv.tiempo_caida_h, srv.almacenamiento_total_gb, srv.almacenamiento_usado_gb, resumen["disponibilidad_pct"], resumen["uso_almacenamiento_pct"], resumen["estado"]]], dtype=object)
    
                    st.session_state.servidores = np.vstack((st.session_state.servidores, nueva_fila))
                    st.toast(f"Servidor '{nombre}' registrado con éxito.", icon="✅")
                    st.rerun()
                except ValueError as err:
                    st.error(f"Error de validación en la clase: {err}")
             
    elif opcion == "Ver listado de Servidores":
        st.subheader("🖥️ Listado de servidores")
    
        if st.session_state.servidores.shape[0] > 0:
            df_servidores = pd.DataFrame(st.session_state.servidores, columns=["Servidor", "Tiempo Total (h)", "Tiempo Caída (h)", "Almacenamiento Total (GB)", "Almacenamiento Usado (GB)", "Disponibilidad (%)", "Uso Almacenamiento (%)", "Estado"])
            st.dataframe(df_servidores, use_container_width=True,
                column_config={
                    "Disponibilidad (%)": st.column_config.NumberColumn(format="%.2f %%"),
                    "Uso Almacenamiento (%)": st.column_config.NumberColumn(format="%.2f %%"),
                    "Tiempo Total (h)": st.column_config.NumberColumn(format="%.2f h"),
                    "Tiempo Caída (h)": st.column_config.NumberColumn(format="%.2f h"),
                    "Almacenamiento Total (GB)": st.column_config.NumberColumn(format="%.2f GB"),
                    "Almacenamiento Usado (GB)": st.column_config.NumberColumn(format="%.2f GB"),
                },
            )
        else:
            st.info("Aún no hay servidores registrados.")
    
    elif opcion == "Actualizar informacion del Servidor":
        st.subheader("Modificar datos de un servidor existente")
    
        if st.session_state.servidores.shape[0] > 0:
            nombres_servidores = st.session_state.servidores[:, 0].tolist()
            servidor_seleccionado = st.selectbox("Seleccione el servidor a editar:", nombres_servidores)
    
            idx = np.where(st.session_state.servidores[:, 0] == servidor_seleccionado)[0][0]
            srv_actual = st.session_state.servidores[idx]
    
            with st.form("form_actualizar_servidor"):
                nuevo_nombre = st.text_input("Nombre", value=str(srv_actual[0]))
                nuevo_t_total = st.number_input("Tiempo Total (h)", min_value=0.0, value=float(srv_actual[1]), step=10.0, format="%.2f")
                nuevo_t_caida = st.number_input("Tiempo Caída (h)", min_value=0.0, value=float(srv_actual[2]), step=0.5, format="%.2f")
                nuevo_alm_total = st.number_input("Almacenamiento Total (GB)", min_value=0.0, value=float(srv_actual[3]), step=50.0, format="%.2f")
                nuevo_alm_usado = st.number_input("Almacenamiento Usado (GB)", min_value=0.0, value=float(srv_actual[4]), step=10.0, format="%.2f")
                btn_actualizar = st.form_submit_button("Actualizar Registro")
    
            if btn_actualizar:
                try:
                    srv_editado = Servidor(nombre=nuevo_nombre.strip(), tiempo_total_h=nuevo_t_total, tiempo_caida_h=nuevo_t_caida, almacenamiento_total_gb=nuevo_alm_total, almacenamiento_usado_gb=nuevo_alm_usado)
                    resumen_editado = srv_editado.resumen()
                    st.session_state.servidores[idx] = [srv_editado.nombre, srv_editado.tiempo_total_h, srv_editado.tiempo_caida_h, srv_editado.almacenamiento_total_gb, srv_editado.almacenamiento_usado_gb, resumen_editado["disponibilidad_pct"], resumen_editado["uso_almacenamiento_pct"], resumen_editado["estado"]]
                    st.toast("Servidor actualizado correctamente.", icon="✅")
                    st.rerun()
                except ValueError as err:
                    st.error(f"Error de validación al actualizar: {err}")
        else:
            st.info("No hay servidores disponibles para actualizar.")
    
    elif opcion == "Eliminar un Servidor":
        st.subheader("Eliminar servidor")
    
        if st.session_state.servidores.shape[0] > 0:
            nombres_del_srv = st.session_state.servidores[:, 0].tolist()
            srv_a_eliminar = st.selectbox("Seleccione el servidor a eliminar:", nombres_del_srv)
    
            if st.button("Eliminar Servidor"):
                srv_elim = np.where(st.session_state.servidores[:, 0] == srv_a_eliminar)[0][0]  
                st.session_state.servidores = np.delete(st.session_state.servidores, srv_elim, axis=0)  
                st.toast(f"Servidor '{srv_a_eliminar}' eliminado exitosamente.", icon="✅")
                st.rerun()
        else:
            st.info("No hay servidores disponibles para eliminar.")
