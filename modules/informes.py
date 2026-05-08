import streamlit as st
import plotly.express as px
from services.sheets_service import get_dataframe


def render():

    st.header("Informes")

    pagos = get_dataframe("Pagos")

    if pagos.empty:
        st.warning("No hay datos")
        return

    total = pagos["Monto"].sum()

    st.metric("Total Movimientos", f"$ {total:,.2f}")

    grafico = px.bar(
        pagos,
        x="Tipo_Movimiento",
        y="Monto"
    )

    st.plotly_chart(grafico, use_container_width=True)
