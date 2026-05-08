import streamlit as st

from modules import obras
from modules import contratistas
from modules import proveedores
from modules import presupuestos
from modules import pagos
from modules import informes

st.set_page_config(
    page_title="Administración de Obras",
    layout="wide"
)

st.title("Sistema Administración de Obras")

menu = st.sidebar.selectbox(
    "Menú Principal",
    [
        "Dashboard",
        "Obras",
        "Contratistas",
        "Proveedores",
        "Presupuestos",
        "Pagos",
        "Informes"
    ]
)

if menu == "Dashboard":
    st.subheader("Dashboard General")
    st.info("Panel general del sistema")

elif menu == "Obras":
    obras.render()

elif menu == "Contratistas":
    contratistas.render()

elif menu == "Proveedores":
    proveedores.render()

elif menu == "Presupuestos":
    presupuestos.render()

elif menu == "Pagos":
    pagos.render()

elif menu == "Informes":
    informes.render()
