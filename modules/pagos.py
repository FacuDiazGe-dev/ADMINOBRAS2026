import streamlit as st

from datetime import datetime

from services.ids import generar_id
from services.sheets_service import append_row

from services.selectors import (
    obtener_obras,
    obtener_proveedores,
    obtener_presupuestos_por_obra,
    obtener_contratistas_por_obra
)


def render():

    st.header("Pagos y Aportes")

    with st.form("form_pagos"):

        # OBRAS
        obras_dict = obtener_obras()
        
        obra_label = st.selectbox(
            "Obra",
            list(obras_dict.keys())
        )
        
        obra_id = obras_dict[obra_label]

        # CONTRATISTAS
        contratistas_dict = obtener_contratistas_por_obra(
            obra_id
        )

        contratista_label = st.selectbox(
            "Contratista",
            list(contratistas_dict.keys())
        )
        
        contratista_id = contratistas_dict[
            contratista_label
        ]

        # PROVEEDORES
        proveedores_dict = obtener_proveedores()

        proveedor_label = st.selectbox(
            "Proveedor",
            list(proveedores_dict.keys())
        )

        proveedor_id = proveedores_dict[proveedor_label]

        # PRESUPUESTOS
        presupuestos_dict = obtener_presupuestos_por_obra(
            obra_id
        )

        presupuesto_label = st.selectbox(
            "Presupuesto",
            list(presupuestos_dict.keys())
        )
        
        presupuesto_id = presupuestos_dict[
            presupuesto_label
        ]

        # DATOS PAGO
        tipo = st.selectbox(
            "Tipo Movimiento",
            ["Pago", "Aporte"]
        )

        monto = st.number_input(
            "Monto",
            min_value=0.0
        )

        fecha_pago = st.date_input(
            "Fecha Pago"
        )

        metodo = st.selectbox(
            "Método Pago",
            [
                "Efectivo",
                "Transferencia",
                "Cheque"
            ]
        )

        estado = st.selectbox(
            "Estado",
            [
                "Pendiente",
                "Pagado",
                "Cancelado"
            ]
        )

        observaciones = st.text_area(
            "Observaciones"
        )

        guardar = st.form_submit_button(
            "Registrar"
        )

        if guardar:

            pago_id = generar_id("PAG")

            fila = [
                pago_id,
                obra_id,
                contratista_id,
                proveedor_id,
                presupuesto_id,
                monto,
                str(fecha_pago),
                tipo,
                metodo,
                estado,
                observaciones
            ]

            append_row("Pagos", fila)

            st.success(
                f"Pago registrado correctamente: {pago_id}"
            )
