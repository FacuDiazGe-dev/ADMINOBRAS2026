import streamlit as st
import pandas as pd

from services.ids import generar_id
from services.sheets_service import (
    append_row,
    get_dataframe,
    update_obra
)


def render():

    st.header("Gestión de Obras")

    opcion = st.selectbox(
        "Acción",
        [
            "Alta",
            "Consulta",
            "Editar"
        ]
    )

    # =====================================================
    # ALTA DE OBRAS
    # =====================================================

    if opcion == "Alta":

        st.subheader("Nueva Obra")

        with st.form("form_obra"):

            nombre = st.text_input(
                "Nombre Obra"
            )

            comitente = st.text_input(
                "Comitente"
            )

            contacto = st.text_input(
                "Contacto"
            )

            ubicacion = st.text_input(
                "Ubicación"
            )

            tipo = st.selectbox(
                "Tipo",
                [
                    "Nueva",
                    "Ampliación",
                    "Refacción",
                    "Otro"
                ]
            )

            estado = st.selectbox(
                "Estado",
                [
                    "Activa",
                    "Pendiente",
                    "Finalizada",
                    "Suspendida"
                ]
            )

            observaciones = st.text_area(
                "Observaciones"
            )

            guardar = st.form_submit_button(
                "Guardar"
            )

            if guardar:

                obra_id = generar_id("OBR")

                fila = [
                    obra_id,
                    nombre,
                    comitente,
                    contacto,
                    ubicacion,
                    tipo,
                    estado,
                    "",
                    "",
                    observaciones
                ]

                append_row(
                    "Obras",
                    fila
                )

                st.success(
                    f"Obra creada: {obra_id}"
                )

    # =====================================================
    # CONSULTA DE OBRAS
    # =====================================================

    elif opcion == "Consulta":

        st.subheader("Listado de Obras")

        df = get_dataframe("Obras")

        if not df.empty:

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.warning(
                "No hay obras registradas."
            )

    # =====================================================
    # EDICIÓN SIMPLE
    # =====================================================
    
    elif opcion == "Editar":
    
        st.subheader("Editar Obra")
    
        df = get_dataframe("Obras")
    
        if df.empty:
    
            st.warning(
                "No hay obras cargadas."
            )
    
        else:
    
            obras_dict = {
                f"{row['ID_Obr']} - {row['NomObr']}"
                : row['ID_Obr']
                for _, row in df.iterrows()
            }
    
            obra_label = st.selectbox(
                "Seleccionar Obra",
                list(obras_dict.keys())
            )
    
            obra_id = obras_dict[
                obra_label
            ]
    
            obra_df = df[
                df["ID_Obr"] == obra_id
            ]
    
            obra = obra_df.iloc[0]
    
            with st.form("editar_obra"):
    
                nombre = st.text_input(
                    "Nombre Obra",
                    value=obra["NomObr"]
                )
    
                comitente = st.text_input(
                    "Comitente",
                    value=obra["Comitente"]
                )
    
                contacto = st.text_input(
                    "Contacto",
                    value=obra["ContaObr"]
                )
    
                ubicacion = st.text_input(
                    "Ubicación",
                    value=obra["UbicacionObr"]
                )
    
                descripcion = st.text_area(
                    "Descripción",
                    value=obra["DescripcionObr"]
                )
    
                estado = st.selectbox(
                    "Estado",
                    [
                        "Activa",
                        "Pendiente",
                        "Finalizada",
                        "Suspendida"
                    ]
                )
    
                fecha_inicio = st.text_input(
                    "Fecha Inicio",
                    value=obra["FechaInicioObr"]
                )
    
                fecha_fin = st.text_input(
                    "Fecha Fin",
                    value=obra["FechaFinObr"]
                )
    
                observaciones = st.text_area(
                    "Observaciones",
                    value=obra["ObsObr"]
                )
    
                guardar_edicion = (
                    st.form_submit_button(
                        "Guardar Cambios"
                    )
                )
    
            if guardar_edicion:
            
                nueva_fila = [
                    obra_id,
                    nombre,
                    comitente,
                    contacto,
                    ubicacion,
                    descripcion,
                    estado,
                    fecha_inicio,
                    fecha_fin,
                    observaciones
                ]
            
                actualizado = update_obra(
                    obra_id,
                    nueva_fila
                )
            
                if actualizado:
            
                    st.success(
                        f"Obra actualizada correctamente: {obra_id}"
                    )
            
                else:
            
                    st.error(
                        "No se pudo actualizar la obra."
                    )
