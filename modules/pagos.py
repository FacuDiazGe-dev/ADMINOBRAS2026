import streamlit as st

from services.ids import generar_id
from services.sheets_service import append_row

from services.selectors import (
    obtener_obras,
    obtener_proveedores,
    obtener_contratistas_por_obra,
    obtener_presupuestos_por_contratista
)


def render():

    st.header("Pagos y Aportes")

    with st.form("form_pagos"):

        # =========================
        # OBRAS
        # =========================

        obras_dict = obtener_obras()

        obra_label = st.selectbox(
            "Obra",
            list(obras_dict.keys())
        )

        obra_id = obras_dict[obra_label]

        # =========================
        # DESTINO DEL PAGO
        # =========================
        
        destinatario = st.radio(
            "Destino del Pago",
            [
                "Contratista",
                "Proveedor"
            ]
        )
        
        contratista_id = None
        proveedor_id = None
        presupuesto_id = None
        
        # ==================================================
        # PAGO A CONTRATISTA
        # ==================================================
        
        if destinatario == "Contratista":
        
            # CONTRATISTAS
            contratistas_dict = obtener_contratistas_por_obra(
                obra_id
            )
        
            if contratistas_dict:
        
                contratista_label = st.selectbox(
                    "Contratista",
                    list(contratistas_dict.keys())
                )
        
                contratista_id = contratistas_dict[
                    contratista_label
                ]
        
                # PRESUPUESTOS DEL CONTRATISTA
                presupuestos_dict = (
                    obtener_presupuestos_por_contratista(
                        obra_id,
                        contratista_id
                    )
                )
        
                if presupuestos_dict:
        
                    presupuesto_label = st.selectbox(
                        "Presupuesto",
                        list(presupuestos_dict.keys())
                    )
        
                    presupuesto_id = presupuestos_dict[
                        presupuesto_label
                    ]
        
                else:
        
                    st.warning(
                        "No hay presupuestos asociados a este contratista."
                    )
        
            else:
        
                st.warning(
                    "No hay contratistas asociados a esta obra."
                )
        
        # ==================================================
        # PAGO A PROVEEDOR
        # ==================================================
        
        elif destinatario == "Proveedor":
        
            proveedores_dict = obtener_proveedores()
        
            if proveedores_dict:
        
                proveedor_label = st.selectbox(
                    "Proveedor",
                    list(proveedores_dict.keys())
                )
        
                proveedor_id = proveedores_dict[
                    proveedor_label
                ]
        
            else:
        
                st.warning(
                    "No hay proveedores registrados."
                )

        # =========================
        # BOTÓN GUARDAR
        # =========================

        guardar = st.form_submit_button(
            "Registrar Pago"
        )

        # =========================
        # GUARDAR DATOS
        # =========================

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

            append_row(
                "Pagos",
                fila
            )

            st.success(
                f"Pago registrado correctamente: {pago_id}"
            )
