import streamlit as st
import plotly.express as px
from services.sheets_service import get_dataframe


def render():

    st.header("Dashboard Ejecutivo")

    obras = get_dataframe("Obras")
    pagos = get_dataframe("Pagos")
    presupuestos = get_dataframe("Presupuestos")

    total_obras = len(obras)

    total_pagos = 0
    if not pagos.empty:
        total_pagos = pagos["Monto"].sum()

    total_presupuestos = 0
    if not presupuestos.empty:
        total_presupuestos = presupuestos["Monto_Inicial"].sum()

    saldo = total_presupuestos - total_pagos

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Obras", total_obras)
    col2.metric("Pagos", f"$ {total_pagos:,.0f}")
    col3.metric("Presupuestos", f"$ {total_presupuestos:,.0f}")
    col4.metric("Saldo", f"$ {saldo:,.0f}")

    st.divider()

    if not pagos.empty:

        grafico = px.pie(
            pagos,
            names="Tipo_Movimiento",
            values="Monto",
            title="Distribución Financiera"
        )

        st.plotly_chart(grafico, use_container_width=True)

    st.divider()

    st.subheader("Últimos Movimientos")

    if not pagos.empty:
        st.dataframe(pagos.tail(10), use_container_width=True)
