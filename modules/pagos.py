import streamlit as st
from services.ids import generar_id
from services.sheets_service import append_row


def render():

    st.header("Pagos y Aportes")

    with st.form("form_pagos"):

        obra = st.text_input("ID Obra")
        contratista = st.text_input("ID Contratista")
        proveedor = st.text_input("ID Proveedor")
        presupuesto = st.text_input("ID Presupuesto")

        tipo = st.selectbox(
            "Tipo Movimiento",
            ["Pago", "Aporte"]
        )

        monto = st.number_input("Monto", min_value=0.0)

        metodo = st.selectbox(
            "Método Pago",
            ["Efectivo", "Transferencia", "Cheque"]
        )

        observaciones = st.text_area("Observaciones")

        guardar = st.form_submit_button("Registrar")

        if guardar:

            pago_id = generar_id("PAG")

            fila = [
                pago_id,
                obra,
                contratista,
                proveedor,
                presupuesto,
                tipo,
                monto,
                "",
                metodo,
                "Activo",
                observaciones
            ]

            append_row("Pagos", fila)

            st.success("Pago registrado")
            append_row("Pagos", fila)

            st.success("Pago registrado")
