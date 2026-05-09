import streamlit as st

from services.ids import generar_id
from services.sheets_service import append_row

from services.selectors import (
    obtener_obras,
    obtener_contratistas
)


def render():

    st.header("Presupuestos")

    with st.form("form_presupuestos"):

        # OBRAS
        obras_dict = obtener_obras()

        obra_label = st.selectbox(
            "Obra",
            list(obras_dict.keys())
        )

        obra_id = obras_dict[obra_label]

        # CONTRATISTAS
        contratistas_dict = obtener_contratistas()

        contratista_label = st.selectbox(
            "Contratista",
            list(contratistas_dict.keys())
        )

        contratista_id = contratistas_dict[contratista_label]

        # DATOS PRESUPUESTO
        tipo_contrato = st.selectbox(
            "Tipo Contrato",
            [
                "Mano de Obra",
                "Materiales",
                "Servicio",
                "Integral"
            ]
        )

        especialidad = st.text_input(
            "Especialidad"
        )

        codigo_especialidad = st.text_input(
            "Código Especialidad"
        )

        fecha_inicio = st.date_input(
            "Fecha Inicio"
        )

        fecha_fin = st.date_input(
            "Fecha Fin"
        )

        monto_inicial = st.number_input(
            "Monto Inicial",
            min_value=0.0
        )

        monto_actual = st.number_input(
            "Monto Actual",
            min_value=0.0
        )

        estado = st.selectbox(
            "Estado",
            [
                "Activo",
                "Pendiente",
                "Finalizado",
                "Cancelado"
            ]
        )

        causa_estado = st.text_input(
            "Causa Estado"
        )

        observaciones = st.text_area(
            "Observaciones"
        )

        guardar = st.form_submit_button(
            "Registrar Presupuesto"
        )

        if guardar:

            presupuesto_id = generar_id("PRE")

            fila = [
                obra_id,
                contratista_id,
                presupuesto_id,
                tipo_contrato,
                str(fecha_inicio),
                str(fecha_fin),
                monto_inicial,
                monto_actual,
                especialidad,
                codigo_especialidad,
                estado,
                causa_estado,
                observaciones
            ]

            append_row(
                "Presupuestos",
                fila
            )

            st.success(
                f"Presupuesto registrado: {presupuesto_id}"
            )
