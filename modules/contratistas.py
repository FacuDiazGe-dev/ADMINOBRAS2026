import streamlit as st
from services.ids import generar_id
from services.sheets_service import append_row


def render():

    st.header("Contratistas")

    with st.form("form_contratistas"):

        nombre = st.text_input("Nombre")

        tipo = st.selectbox(
            "Tipo",
            ["MdeO", "Mat + MdeO"]
        )

        especialidad = st.selectbox(
            "Especialidad",
            [
                "Albañilería",
                "Electricidad",
                "Sanitaria",
                "Techista",
                "Yesero",
                "Otros"
            ]
        )

        contacto = st.text_input("Contacto")

        observaciones = st.text_area("Observaciones")

        guardar = st.form_submit_button("Guardar")

        if guardar:

            contratista_id = generar_id("CON")

            fila = [
                contratista_id,
                nombre,
                tipo,
                especialidad,
                contacto,
                "Activo",
                "",
                "",
                observaciones
            ]

            append_row("Contratistas", fila)

            st.success("Contratista guardado")
