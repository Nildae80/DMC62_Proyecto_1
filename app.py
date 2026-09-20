import streamlit as st
import numpy as np
import pandas as pd
import libreria_funciones_proyecto1 as lf

from librería_clases_proyecto1 import Servidor


# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

st.set_page_config(
    page_title="Proyecto 1 | Python Analytics",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CSS + HTML + JAVASCRIPT
# ============================================================

st.markdown("""
<style>

    /* ========================================================
       VARIABLES CORPORATIVAS
       ======================================================== */

    :root {
        --primary: #0B1F33;
        --primary-light: #123B5D;
        --secondary: #00A6D6;
        --secondary-light: #19C3F1;
        --accent: #00D084;
        --warning: #FFB020;
        --danger: #FF5A67;

        --background: #F4F7FB;
        --surface: #FFFFFF;
        --text: #172B4D;
        --text-light: #637083;

        --shadow:
            0 10px 30px rgba(11, 31, 51, 0.10);

        --shadow-hover:
            0 18px 45px rgba(0, 166, 214, 0.20);
    }


    /* ========================================================
       FONDO GENERAL
       ======================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(0,166,214,0.08),
                transparent 25%
            ),
            radial-gradient(
                circle at 90% 90%,
                rgba(0,208,132,0.06),
                transparent 25%
            ),
            var(--background);
    }


    /* ========================================================
       CONTENEDOR PRINCIPAL
       ======================================================== */

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1450px;
    }


    /* ========================================================
       SIDEBAR
       ======================================================== */

    [data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #071624 0%,
                #0B1F33 55%,
                #102E48 100%
            );

        border-right: 1px solid rgba(255,255,255,0.08);
    }

    [data-testid="stSidebar"] * {
        color: #FFFFFF;
    }

    [data-testid="stSidebar"] .stSelectbox label {
        color: #B8CBDC !important;
        font-weight: 600;
    }


    /* ========================================================
       TITULOS
       ======================================================== */

    h1, h2, h3 {
        color: var(--primary);
        font-weight: 750;
        letter-spacing: -0.5px;
    }

    h4 {
        color: var(--primary-light);
    }


    /* ========================================================
       HERO
       ======================================================== */

    .hero {
        position: relative;
        overflow: hidden;

        padding: 42px;
        margin-bottom: 30px;

        border-radius: 24px;

        background:
            linear-gradient(
                135deg,
                #071624 0%,
                #0B1F33 45%,
                #123B5D 100%
            );

        box-shadow:
            0 20px 50px rgba(11,31,51,0.25);

        color: white;

        transition:
            transform .35s ease,
            box-shadow .35s ease;
    }

    .hero:hover {
        transform: translateY(-4px);
        box-shadow:
            0 25px 65px rgba(0,166,214,0.25);
    }

    .hero::before {
        content: "";

        position: absolute;

        width: 350px;
        height: 350px;

        right: -100px;
        top: -150px;

        background:
            radial-gradient(
                circle,
                rgba(0,198,255,0.35),
                transparent 65%
            );

        animation:
            floatingLight 7s ease-in-out infinite;
    }

    .hero::after {
        content: "";

        position: absolute;

        width: 250px;
        height: 250px;

        left: -120px;
        bottom: -150px;

        background:
            radial-gradient(
                circle,
                rgba(0,208,132,0.25),
                transparent 65%
            );
    }

    @keyframes floatingLight {
        0%, 100% {
            transform: translate(0,0);
        }

        50% {
            transform: translate(-40px,35px);
        }
    }

    .hero-content {
        position: relative;
        z-index: 2;
    }

    .hero-badge {
        display: inline-block;

        padding: 7px 14px;

        margin-bottom: 15px;

        border-radius: 30px;

        background:
            rgba(0,166,214,0.15);

        border:
            1px solid rgba(0,198,255,0.35);

        color: #66D9FF;

        font-size: 13px;
        font-weight: 700;

        letter-spacing: 1px;
    }

    .hero-title {
        font-size: 42px;
        font-weight: 800;

        margin: 0;

        color: white;
    }

    .hero-subtitle {
        margin-top: 12px;

        color: #B8CBDC;

        font-size: 17px;
        max-width: 800px;
    }


    /* ========================================================
       TARJETAS
       ======================================================== */

    .card {
        background: rgba(255,255,255,0.95);

        border:
            1px solid rgba(11,31,51,0.07);

        border-radius: 18px;

        padding: 25px;

        margin-bottom: 20px;

        box-shadow: var(--shadow);

        transition:
            transform .3s ease,
            box-shadow .3s ease,
            border-color .3s ease;
    }

    .card:hover {
        transform: translateY(-6px);

        box-shadow:
            var(--shadow-hover);

        border-color:
            rgba(0,166,214,0.25);
    }


    /* ========================================================
       KPI
       ======================================================== */

    .kpi {
        background:
            linear-gradient(
                145deg,
                #FFFFFF,
                #F5FAFD
            );

        border-radius: 18px;

        padding: 22px;

        border-left:
            5px solid var(--secondary);

        box-shadow:
            var(--shadow);

        transition:
            transform .3s ease,
            box-shadow .3s ease;
    }

    .kpi:hover {
        transform:
            translateY(-5px)
            scale(1.015);

        box-shadow:
            0 15px 35px rgba(0,166,214,0.18);
    }

    .kpi-label {
        color: var(--text-light);

        font-size: 13px;

        font-weight: 700;

        text-transform: uppercase;

        letter-spacing: .7px;
    }

    .kpi-value {
        color: var(--primary);

        font-size: 30px;

        font-weight: 800;

        margin-top: 7px;
    }


    /* ========================================================
       ICONOS
       ======================================================== */

    .icon-box {
        display: inline-flex;

        align-items: center;
        justify-content: center;

        width: 48px;
        height: 48px;

        border-radius: 14px;

        background:
            linear-gradient(
                135deg,
                var(--secondary),
                var(--secondary-light)
            );

        color: white;

        font-size: 22px;

        box-shadow:
            0 8px 20px rgba(0,166,214,.25);
    }


    /* ========================================================
       BOTONES
       ======================================================== */

    .stButton > button,
    .stFormSubmitButton > button {

        border: none !important;

        border-radius: 10px !important;

        background:
            linear-gradient(
                135deg,
                #008FBA,
                #00B8E6
            ) !important;

        color: white !important;

        font-weight: 700 !important;

        padding: 10px 22px !important;

        transition:
            all .25s ease !important;

        box-shadow:
            0 7px 20px rgba(0,166,214,.20) !important;
    }

    .stButton > button:hover,
    .stFormSubmitButton > button:hover {

        transform:
            translateY(-2px)
            scale(1.02);

        box-shadow:
            0 12px 28px rgba(0,166,214,.35) !important;
    }


    /* ========================================================
       INPUTS
       ======================================================== */

    input, textarea {

        border-radius: 10px !important;

        border:
            1px solid #D8E2EA !important;

        transition:
            border .25s ease,
            box-shadow .25s ease !important;
    }

    input:focus,
    textarea:focus {

        border-color:
            var(--secondary) !important;

        box-shadow:
            0 0 0 3px
            rgba(0,166,214,.12) !important;
    }


    /* ========================================================
       SELECTBOX
       ======================================================== */

    div[data-baseweb="select"] > div {

        border-radius: 10px;

        border-color: #D8E2EA;

        transition: all .25s ease;
    }

    div[data-baseweb="select"] > div:hover {

        border-color:
            var(--secondary);

        box-shadow:
            0 0 0 3px
            rgba(0,166,214,.08);
    }


    /* ========================================================
       TABLAS
       ======================================================== */

    [data-testid="stDataFrame"] {

        border-radius: 15px;

        overflow: hidden;

        box-shadow:
            0 8px 25px
            rgba(11,31,51,.08);
    }


    /* ========================================================
       ALERTAS
       ======================================================== */

    [data-testid="stAlert"] {

        border-radius: 12px;

        border-left:
            4px solid var(--secondary);
    }


    /* ========================================================
       DIVISORES
       ======================================================== */

    hr {

        border: none;

        height: 1px;

        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(0,166,214,.3),
                transparent
            );
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .footer {

        text-align: center;

        padding: 30px 0 10px;

        color: #7A8795;

        font-size: 13px;
    }


    /* ========================================================
       ANIMACIÓN DE ENTRADA
       ======================================================== */

    .fade-in {

        animation:
            fadeIn .6s ease forwards;
    }

    @keyframes fadeIn {

        from {
            opacity: 0;
            transform:
                translateY(15px);
        }

        to {
            opacity: 1;
            transform:
                translateY(0);
        }
    }


    /* ========================================================
       RESPONSIVE
       ======================================================== */

    @media (max-width: 768px) {

        .hero {
            padding: 28px;
        }

        .hero-title {
            font-size: 30px;
        }

        .hero-subtitle {
            font-size: 15px;
        }

    }

</style>


<script>

document.addEventListener("DOMContentLoaded", function() {

    // Efecto de movimiento suave siguiendo el mouse
    const cards = document.querySelectorAll(".card, .kpi");

    document.addEventListener("mousemove", function(e) {

        const x = (window.innerWidth / 2 - e.clientX) / 100;
        const y = (window.innerHeight / 2 - e.clientY) / 100;

        cards.forEach((card, index) => {

            if (index > 8) return;

            card.style.transform =
                "translate(" +
                (x * 0.15) +
                "px," +
                (y * 0.15) +
                "px)";

        });

    });


    // Efecto de iluminación sobre botones
    const buttons =
        document.querySelectorAll("button");

    buttons.forEach(function(button) {

        button.addEventListener("mousemove", function(e) {

            const rect =
                button.getBoundingClientRect();

            const x =
                e.clientX - rect.left;

            const y =
                e.clientY - rect.top;

            button.style.background =
                "radial-gradient(circle at " +
                x + "px " +
                y + "px, #52D9FF, #008FBA 65%)";

        });

        button.addEventListener("mouseleave", function() {

            button.style.background =
                "linear-gradient(135deg,#008FBA,#00B8E6)";

        });

    });

});

</script>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("""
    <div style="
        text-align:center;
        padding:15px 0 25px 0;
    ">

        <div style="
            font-size:42px;
            margin-bottom:8px;
        ">
            🐍
        </div>

        <div style="
            font-size:19px;
            font-weight:800;
            color:white;
        ">
            PYTHON ANALYTICS
        </div>

        <div style="
            font-size:12px;
            color:#8FAFC5;
            margin-top:5px;
        ">
            ESPECIALIZACIÓN PROFESIONAL
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    modulos = st.selectbox(
        "Navegación",
        [
            "Home",
            "Ejercicio 1",
            "Ejercicio 2",
            "Ejercicio 3",
            "Ejercicio 4"
        ]
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.image("Python_logo.png", width=150)

    st.markdown("""
    <div style="
        text-align:center;
        margin-top:20px;
        color:#8FAFC5;
        font-size:12px;
    ">
        PROYECTO ACADÉMICO<br>
        2026
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# HERO PRINCIPAL
# ============================================================

st.markdown("""
<div class="hero fade-in">

    <div class="hero-content">

        <div class="hero-badge">
            ESPECIALIZACIÓN EN PYTHON FOR ANALYTICS
        </div>

        <div class="hero-title">
            PROYECTO 1
        </div>

        <div class="hero-subtitle">
            Fundamentos de Programación con Python,
            NumPy, Pandas, funciones, POO y Streamlit.
        </div>

    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# HOME
# ============================================================

if modulos == "Home":

    st.markdown("""
    <div class="card fade-in">

        <div style="display:flex;gap:15px;align-items:center;">

            <div class="icon-box">
                👋
            </div>

            <div>
                <h2 style="margin:0;">
                    Bienvenido al proyecto
                </h2>

                <p style="
                    margin:4px 0 0 0;
                    color:#637083;
                ">
                    Plataforma interactiva desarrollada con Streamlit.
                </p>
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)


    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card">

            <div class="icon-box">
                👤
            </div>

            <h3>Datos del estudiante</h3>

            <p>
                <b>Nombre completo:</b><br>
                Nilda Echevarria Meza
            </p>

            <p>
                <b>Perfil:</b><br>
                Ingeniero de Sistemas con más de 5 años
                de experiencia en el sector.
            </p>

            <p>
                <b>Correo:</b><br>
                prueba@gmail.com
            </p>

        </div>
        """, unsafe_allow_html=True)


    with col2:

        st.markdown("""
        <div class="card">

            <div class="icon-box">
                🎓
            </div>

            <h3>Información del curso</h3>

            <p>
                <b>Módulo:</b><br>
                Programación con Python y Streamlit
            </p>

            <p>
                <b>Año:</b><br>
                2026
            </p>

            <p>
                <b>Proyecto:</b><br>
                Proyecto Aplicado 1
            </p>

        </div>
        """, unsafe_allow_html=True)


    st.markdown("""
    <div class="card">

        <h2>📌 Descripción del proyecto</h2>

        <p style="color:#637083;">
            Aplicación interactiva desarrollada como parte de
            la evaluación práctica del módulo.
        </p>

    </div>
    """, unsafe_allow_html=True)


    # KPIs

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="kpi">
            <div class="kpi-label">Ejercicios</div>
            <div class="kpi-value">04</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="kpi">
            <div class="kpi-label">Tecnologías</div>
            <div class="kpi-value">05</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="kpi">
            <div class="kpi-label">Año</div>
            <div class="kpi-value">2026</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="kpi">
            <div class="kpi-label">Framework</div>
            <div class="kpi-value">ST</div>
        </div>
        """, unsafe_allow_html=True)


    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">

        <h2>🚀 Componentes desarrollados</h2>

        <ul style="color:#637083;line-height:2;">

            <li>
                Flujo de caja utilizando listas y operaciones
                financieras.
            </li>

            <li>
                Registro de productos mediante NumPy,
                arrays y DataFrame.
            </li>

            <li>
                Cálculo del tiempo de transferencia utilizando
                funciones externas.
            </li>

            <li>
                Gestión CRUD de servidores mediante
                Programación Orientada a Objetos.
            </li>

        </ul>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# EJERCICIO 1
# ============================================================

elif modulos == "Ejercicio 1":

    st.header("💰 Ejercicio 1 — Flujo de caja")

    st.write(
        "Registra ingresos y gastos para obtener "
        "el estado financiero acumulado."
    )

    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []


    with st.form("form_movimientos", clear_on_submit=True):

        st.subheader("Registrar movimiento")

        col1, col2, col3 = st.columns(3)

        with col1:
            concepto = st.text_input(
                "Concepto",
                placeholder="Ej. Venta de producto"
            )

        with col2:
            tipo_Movimiento = st.selectbox(
                "Tipo de movimiento",
                ["Ingreso", "Gasto"],
                index=None,
                placeholder="Seleccione..."
            )

        with col3:
            importe = float(
                st.number_input(
                    "Importe (S/)",
                    value=0.00,
                    min_value=0.0,
                    step=0.5,
                    format="%.2f"
                )
            )

        btn_guardar = st.form_submit_button(
            "Guardar movimiento ➕"
        )

        if btn_guardar:

            if concepto.strip() == "":
                st.warning(
                    "Ingresa el concepto del movimiento."
                )

            elif tipo_Movimiento is None:
                st.warning(
                    "Selecciona el tipo de movimiento."
                )

            elif importe <= 0:
                st.warning(
                    "El importe debe ser mayor a cero."
                )

            else:

                st.session_state.movimientos.append(
                    (
                        concepto,
                        tipo_Movimiento,
                        importe
                    )
                )

                st.success(
                    f"Movimiento '{concepto}' agregado correctamente."
                )


    ingresos_total = sum(
        mov[2]
        for mov in st.session_state.movimientos
        if mov[1] == "Ingreso"
    )

    gastos_total = sum(
        mov[2]
        for mov in st.session_state.movimientos
        if mov[1] == "Gasto"
    )

    saldo_total = ingresos_total - gastos_total


    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="kpi">
            <div class="kpi-label">Ingresos</div>
            <div class="kpi-value">
                S/ {ingresos_total:,.2f}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="kpi">
            <div class="kpi-label">Gastos</div>
            <div class="kpi-value">
                S/ {gastos_total:,.2f}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="kpi">
            <div class="kpi-label">Saldo</div>
            <div class="kpi-value">
                S/ {saldo_total:,.2f}
            </div>
        </div>
        """, unsafe_allow_html=True)


    if st.session_state.movimientos:

        st.subheader("📊 Historial de movimientos")

        df_movimientos = pd.DataFrame(
            st.session_state.movimientos,
            columns=[
                "Concepto",
                "Tipo de Movimiento",
                "Importe"
            ]
        )

        st.dataframe(
            df_movimientos,
            use_container_width=True,
            column_config={
                "Importe":
                    st.column_config.NumberColumn(
                        "Importe",
                        format="S/ %.2f"
                    )
            }
        )

        if saldo_total > 0:
            st.success(
                "Flujo de caja: A FAVOR"
            )

        elif saldo_total < 0:
            st.error(
                "Flujo de caja: EN CONTRA"
            )

        else:
            st.info(
                "Flujo de caja: CUADRADO"
            )

    else:
        st.info(
            "Aún no hay movimientos registrados."
        )


# ============================================================
# EJERCICIO 2
# ============================================================

elif modulos == "Ejercicio 2":

    st.header("📦 Ejercicio 2 — Inventario")

    st.write(
        "Registro de productos mediante arrays de NumPy."
    )

    if "inventario" not in st.session_state:
        st.session_state.inventario = np.empty(
            (0, 5),
            dtype=object
        )


    with st.form(
        "form_inventario",
        clear_on_submit=True
    ):

        st.subheader(
            "Registrar producto"
        )

        col1, col2 = st.columns(2)

        with col1:

            nombre = st.text_input(
                "Nombre del producto"
            )

            categoria = st.selectbox(
                "Categoría",
                [
                    "Abarrotes",
                    "Bebidas",
                    "Mascotas",
                    "Libreria"
                ],
                index=None,
                placeholder="Seleccione..."
            )

        with col2:

            precio = float(
                st.number_input(
                    "Precio (S/)",
                    value=0.00,
                    min_value=0.0,
                    step=0.5,
                    format="%.2f"
                )
            )

            cantidad = int(
                st.number_input(
                    "Cantidad",
                    min_value=1,
                    step=1
                )
            )

        btn_guardar = st.form_submit_button(
            "Guardar producto ➕"
        )


        if btn_guardar:

            if not nombre.strip():
                st.warning(
                    "Ingresa el nombre del producto."
                )

            elif categoria is None:
                st.warning(
                    "Selecciona una categoría."
                )

            elif precio <= 0:
                st.warning(
                    "El precio debe ser mayor a cero."
                )

            elif cantidad <= 0:
                st.warning(
                    "La cantidad debe ser mayor a cero."
                )

            else:

                total = precio * cantidad

                nuevo_registro = np.array(
                    [[
                        nombre,
                        categoria,
                        precio,
                        cantidad,
                        total
                    ]],
                    dtype=object
                )

                st.session_state.inventario = np.vstack(
                    (
                        st.session_state.inventario,
                        nuevo_registro
                    )
                )

                st.success(
                    f"Producto '{nombre}' agregado correctamente."
                )


    if st.session_state.inventario.shape[0] > 0:

        df_mostrar = pd.DataFrame(
            st.session_state.inventario,
            columns=[
                "Producto",
                "Categoría",
                "Precio",
                "Cantidad",
                "Total"
            ]
        )

        st.subheader("📊 Inventario")

        st.dataframe(
            df_mostrar,
            use_container_width=True,
            column_config={
                "Precio":
                    st.column_config.NumberColumn(
                        "Precio",
                        format="S/ %.2f"
                    ),

                "Total":
                    st.column_config.NumberColumn(
                        "Total",
                        format="S/ %.2f"
                    )
            }
        )

        total_general = np.sum(
            st.session_state.inventario[:, 4]
            .astype(float)
        )

        st.markdown(f"""
        <div class="kpi">

            <div class="kpi-label">
                Valor total del inventario
            </div>

            <div class="kpi-value">
                S/ {total_general:,.2f}
            </div>

        </div>
        """, unsafe_allow_html=True)

    else:

        st.info(
            "Aún no hay productos registrados."
        )


# ============================================================
# EJERCICIO 3
# ============================================================

elif modulos == "Ejercicio 3":

    st.header("⚡ Ejercicio 3 — Transferencia de archivos")

    st.write(
        "Cálculo del tiempo de transferencia mediante "
        "una función externa."
    )

    if "tiempo" not in st.session_state:
        st.session_state.tiempo = np.empty(
            (0, 4),
            dtype=object
        )


    with st.form(
        "form_funcion",
        clear_on_submit=True
    ):

        st.subheader(
            "Calculadora de transferencia"
        )

        tipo_Funcion = st.selectbox(
            "Seleccione el tipo de función",
            [
                "Calcular tiempo de transferencia de archivo",
                "Otro"
            ],
            index=None,
            placeholder="Seleccione..."
        )


        if tipo_Funcion == \
            "Calcular tiempo de transferencia de archivo":

            col1, col2 = st.columns(2)

            with col1:

                tamano_archivo = float(
                    st.number_input(
                        "Tamaño del archivo (MB)",
                        value=0.00,
                        min_value=0.0,
                        step=0.1,
                        format="%.2f"
                    )
                )

            with col2:

                velocidad = float(
                    st.number_input(
                        "Velocidad (MBPS)",
                        value=0.00,
                        min_value=0.0,
                        step=0.1,
                        format="%.2f"
                    )
                )

            btn_guardar = st.form_submit_button(
                "Calcular transferencia ⚡"
            )

            if btn_guardar:

                if (
                    velocidad <= 0
                    or tamano_archivo <= 0
                ):

                    st.error(
                        "El tamaño y la velocidad "
                        "deben ser mayores a 0."
                    )

                else:

                    resultado_tiempo = \
                        lf.calcular_tiempo_transferencia_archivo(
                            tamano_archivo,
                            velocidad
                        )

                    minutos = \
                        resultado_tiempo[
                            "tiempo_minutos"
                        ]

                    segundos = \
                        resultado_tiempo[
                            "tiempo_segundos"
                        ]


                    nuevo_registro = np.array(
                        [[
                            tamano_archivo,
                            velocidad,
                            minutos,
                            segundos
                        ]],
                        dtype=object
                    )

                    st.session_state.tiempo = \
                        np.vstack(
                            (
                                st.session_state.tiempo,
                                nuevo_registro
                            )
                        )


                    st.success(
                        "Cálculo realizado correctamente."
                    )


                    c1, c2 = st.columns(2)

                    with c1:

                        st.markdown(f"""
                        <div class="kpi">

                            <div class="kpi-label">
                                Tiempo en minutos
                            </div>

                            <div class="kpi-value">
                                {minutos:.2f} min
                            </div>

                        </div>
                        """, unsafe_allow_html=True)


                    with c2:

                        st.markdown(f"""
                        <div class="kpi">

                            <div class="kpi-label">
                                Tiempo en segundos
                            </div>

                            <div class="kpi-value">
                                {segundos:.2f} seg
                            </div>

                        </div>
                        """, unsafe_allow_html=True)


        elif tipo_Funcion == "Otro":

            st.info(
                "No se tienen implementadas otras funciones."
            )

        else:

            st.info(
                "Seleccione una función."
            )


    if st.session_state.tiempo.shape[0] > 0:

        st.subheader(
            "📊 Historial de cálculos"
        )

        df_mostrar = pd.DataFrame(
            st.session_state.tiempo,
            columns=[
                "Tamaño (MB)",
                "Velocidad (MBPS)",
                "Tiempo en Minutos",
                "Tiempo en Segundos"
            ]
        )

        st.dataframe(
            df_mostrar,
            use_container_width=True,
            column_config={

                "Tamaño (MB)":
                    st.column_config.NumberColumn(
                        format="%.2f MB"
                    ),

                "Velocidad (MBPS)":
                    st.column_config.NumberColumn(
                        format="%.2f MBPS"
                    ),

                "Tiempo en Minutos":
                    st.column_config.NumberColumn(
                        format="%.2f min"
                    ),

                "Tiempo en Segundos":
                    st.column_config.NumberColumn(
                        format="%.2f seg"
                    )
            }
        )

    else:

        st.info(
            "Aún no hay ejecuciones registradas."
        )


# ============================================================
# EJERCICIO 4
# ============================================================

else:

    st.header("🖥️ Ejercicio 4 — Gestión de servidores")

    st.write(
        "Sistema CRUD para administrar servidores mediante "
        "Programación Orientada a Objetos."
    )


    if (
        "servidores" not in st.session_state
        or st.session_state.servidores.shape[1] != 8
    ):

        st.session_state.servidores = np.empty(
            (0, 8),
            dtype=object
        )


    opcion = st.selectbox(
        "Seleccione la operación",
        [
            "Crear un nuevo Servidor",
            "Ver listado de Servidores",
            "Actualizar informacion del Servidor",
            "Eliminar un Servidor"
        ]
    )


    # ========================================================
    # CREAR
    # ========================================================

    if opcion == "Crear un nuevo Servidor":

        st.subheader(
            "➕ Registrar nuevo servidor"
        )

        with st.form(
            "form_crear_servidor",
            clear_on_submit=True
        ):

            col1, col2 = st.columns(2)

            with col1:

                nombre = st.text_input(
                    "Nombre del servidor"
                )

                tiempo_total = st.number_input(
                    "Tiempo total de operación (h)",
                    min_value=0.0,
                    value=0.0,
                    step=10.0,
                    format="%.2f"
                )

                tiempo_caida = st.number_input(
                    "Tiempo de caída (h)",
                    min_value=0.0,
                    value=0.0,
                    step=0.5,
                    format="%.2f"
                )

            with col2:

                alm_total = st.number_input(
                    "Almacenamiento total (GB)",
                    min_value=0.0,
                    value=0.0,
                    step=50.0,
                    format="%.2f"
                )

                alm_usado = st.number_input(
                    "Almacenamiento usado (GB)",
                    min_value=0.0,
                    value=0.0,
                    step=10.0,
                    format="%.2f"
                )


            btn_guardar = st.form_submit_button(
                "Registrar servidor ➕"
            )


            if btn_guardar:

                if not nombre.strip():

                    st.error(
                        "Ingrese un nombre para el servidor."
                    )

                else:

                    try:

                        srv = Servidor(
                            nombre=nombre.strip(),
                            tiempo_total_h=tiempo_total,
                            tiempo_caida_h=tiempo_caida,
                            almacenamiento_total_gb=alm_total,
                            almacenamiento_usado_gb=alm_usado
                        )

                        resumen = srv.resumen()

                        nueva_fila = np.array(
                            [[
                                srv.nombre,
                                srv.tiempo_total_h,
                                srv.tiempo_caida_h,
                                srv.almacenamiento_total_gb,
                                srv.almacenamiento_usado_gb,
                                resumen[
                                    "disponibilidad_pct"
                                ],
                                resumen[
                                    "uso_almacenamiento_pct"
                                ],
                                resumen["estado"]
                            ]],
                            dtype=object
                        )

                        st.session_state.servidores = \
                            np.vstack(
                                (
                                    st.session_state.servidores,
                                    nueva_fila
                                )
                            )

                        st.success(
                            f"Servidor '{nombre}' registrado correctamente."
                        )

                    except ValueError as err:

                        st.error(
                            f"Error de validación: {err}"
                        )


    # ========================================================
    # LEER
    # ========================================================

    elif opcion == "Ver listado de Servidores":

        st.subheader(
            "📊 Listado de servidores"
        )

        if st.session_state.servidores.shape[0] > 0:

            df_servidores = pd.DataFrame(
                st.session_state.servidores,
                columns=[
                    "Servidor",
                    "Tiempo Total (h)",
                    "Tiempo Caída (h)",
                    "Almacenamiento Total (GB)",
                    "Almacenamiento Usado (GB)",
                    "Disponibilidad (%)",
                    "Uso Almacenamiento (%)",
                    "Estado"
                ]
            )

            st.dataframe(
                df_servidores,
                use_container_width=True,
                column_config={

                    "Disponibilidad (%)":
                        st.column_config.NumberColumn(
                            format="%.2f %%"
                        ),

                    "Uso Almacenamiento (%)":
                        st.column_config.NumberColumn(
                            format="%.2f %%"
                        ),

                    "Tiempo Total (h)":
                        st.column_config.NumberColumn(
                            format="%.2f h"
                        ),

                    "Tiempo Caída (h)":
                        st.column_config.NumberColumn(
                            format="%.2f h"
                        ),

                    "Almacenamiento Total (GB)":
                        st.column_config.NumberColumn(
                            format="%.2f GB"
                        ),

                    "Almacenamiento Usado (GB)":
                        st.column_config.NumberColumn(
                            format="%.2f GB"
                        )
                }
            )

        else:

            st.info(
                "Aún no hay servidores registrados."
            )


    # ========================================================
    # ACTUALIZAR
    # ========================================================

    elif opcion == \
        "Actualizar informacion del Servidor":

        st.subheader(
            "✏️ Modificar servidor"
        )

        if st.session_state.servidores.shape[0] > 0:

            nombres_servidores = \
                st.session_state.servidores[:, 0].tolist()

            servidor_seleccionado = st.selectbox(
                "Servidor",
                nombres_servidores
            )

            idx = np.where(
                st.session_state.servidores[:, 0]
                == servidor_seleccionado
            )[0][0]

            srv_actual = \
                st.session_state.servidores[idx]


            with st.form(
                "form_actualizar_servidor"
            ):

                nuevo_nombre = st.text_input(
                    "Nombre",
                    value=str(srv_actual[0])
                )

                col1, col2 = st.columns(2)

                with col1:

                    nuevo_t_total = st.number_input(
                        "Tiempo Total (h)",
                        min_value=0.0,
                        value=float(srv_actual[1]),
                        step=10.0,
                        format="%.2f"
                    )

                    nuevo_t_caida = st.number_input(
                        "Tiempo Caída (h)",
                        min_value=0.0,
                        value=float(srv_actual[2]),
                        step=0.5,
                        format="%.2f"
                    )

                with col2:

                    nuevo_alm_total = st.number_input(
                        "Almacenamiento Total (GB)",
                        min_value=0.0,
                        value=float(srv_actual[3]),
                        step=50.0,
                        format="%.2f"
                    )

                    nuevo_alm_usado = st.number_input(
                        "Almacenamiento Usado (GB)",
                        min_value=0.0,
                        value=float(srv_actual[4]),
                        step=10.0,
                        format="%.2f"
                    )


                btn_actualizar = \
                    st.form_submit_button(
                        "Actualizar registro 🔄"
                    )


                if btn_actualizar:

                    try:

                        srv_editado = Servidor(
                            nombre=nuevo_nombre.strip(),
                            tiempo_total_h=nuevo_t_total,
                            tiempo_caida_h=nuevo_t_caida,
                            almacenamiento_total_gb=nuevo_alm_total,
                            almacenamiento_usado_gb=nuevo_alm_usado
                        )

                        resumen_editado = \
                            srv_editado.resumen()


                        st.session_state.servidores[idx] = [
                            srv_editado.nombre,
                            srv_editado.tiempo_total_h,
                            srv_editado.tiempo_caida_h,
                            srv_editado.almacenamiento_total_gb,
                            srv_editado.almacenamiento_usado_gb,
                            resumen_editado[
                                "disponibilidad_pct"
                            ],
                            resumen_editado[
                                "uso_almacenamiento_pct"
                            ],
                            resumen_editado["estado"]
                        ]


                        st.success(
                            "Servidor actualizado correctamente."
                        )

                        st.rerun()

                    except ValueError as err:

                        st.error(
                            f"Error de validación: {err}"
                        )

        else:

            st.info(
                "No existen servidores para actualizar."
            )


    # ========================================================
    # ELIMINAR
    # ========================================================

    elif opcion == "Eliminar un Servidor":

        st.subheader(
            "🗑️ Eliminar servidor"
        )

        if st.session_state.servidores.shape[0] > 0:

            nombres_del_srv = \
                st.session_state.servidores[:, 0].tolist()

            srv_a_eliminar = st.selectbox(
                "Servidor",
                nombres_del_srv
            )


            if st.button(
                "Eliminar servidor 🗑️"
            ):

                srv_elim = np.where(
                    st.session_state.servidores[:, 0]
                    == srv_a_eliminar
                )[0][0]

                st.session_state.servidores = \
                    np.delete(
                        st.session_state.servidores,
                        srv_elim,
                        axis=0
                    )

                st.success(
                    f"Servidor '{srv_a_eliminar}' eliminado."
                )

                st.rerun()

        else:

            st.info(
                "No existen servidores para eliminar."
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

    <hr>

    <div style="margin-top:20px;">
        PROYECTO 1 · PYTHON FOR ANALYTICS · STREAMLIT
    </div>

    <div style="margin-top:6px;color:#9AA7B5;">
        Aplicación académica · 2026
    </div>

</div>
""", unsafe_allow_html=True)
