import streamlit as st

from services.ids import generar_id
from services.sheets_service import append_row


def render():

    st.header("Proveedores")

    with st.form("form_proveedores"):

        # =========================
        # DATOS PROVEEDOR
        # =========================

        nombre = st.text_input(
            "Nombre Proveedor"
        )

        rubro = st.selectbox(
            "Rubro",
            [
                "Materiales",
                "Servicios",
                "Transporte",
                "Equipamiento",
                "Impuestos",
                "Herramientas",
                "Logística",
                "Otros"
            ]
        )

        subrubro = st.text_input(
            "Subrubro"
        )

        contacto = st.text_input(
            "Contacto"
        )

        cuit = st.text_input(
            "CUIT"
        )

        estado_pago = st.selectbox(
            "Estado Pago",
            [
                "Pendiente",
                "Pagado",
                "Parcial",
                "Cancelado"
            ]
        )

        observaciones = st.text_area(
            "Observaciones"
        )

        # =========================
        # BOTÓN
        # =========================

        guardar = st.form_submit_button(
            "Registrar Proveedor"
        )

        # =========================
        # GUARDAR
        # =========================

        if guardar:

            proveedor_id = generar_id("PROV")

            fila = [
                nombre,
                proveedor_id,
                rubro,
                subrubro,
                contacto,
                cuit,
                estado_pago,
                observaciones
            ]

            append_row(
                "Proveedores",
                fila
            )

            st.success(
                f"Proveedor registrado correctamente: {proveedor_id}"
            )
