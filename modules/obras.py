import streamlit as st
from services.ids import generar_id
from services.sheets_service import append_row


def render():

    st.header("Gestión de Obras")

    opcion = st.selectbox(
        "Acción",
        ["Alta", "Consulta"]
    )

    if opcion == "Alta":

        with st.form("form_obra"):

            nombre = st.text_input("Nombre Obra")
            comitente = st.text_input("Comitente")
            contacto = st.text_input("Contacto")
            ubicacion = st.text_input("Ubicación")

            tipo = st.selectbox(
                "Tipo",
                ["Nueva", "Ampliación", "Refacción", "Otro"]
            )

            observaciones = st.text_area("Observaciones")

            guardar = st.form_submit_button("Guardar")

            if guardar:

                obra_id = generar_id("OBR")

                fila = [
                    obra_id,
                    nombre,
                    comitente,
                    contacto,
                    ubicacion,
                    tipo,
                    "Activa",
                    "",
                    "",
                    observaciones
                ]

                append_row("Obras", fila)

                st.success(f"Obra creada: {obra_id}")
