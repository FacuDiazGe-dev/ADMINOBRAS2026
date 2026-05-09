import streamlit as st

from services.ids import generar_id

from services.sheets_service import (
    append_row,
    get_dataframe,
    update_contratista
)


def render():

    st.header("Gestión de Contratistas")

    opcion = st.selectbox(
        "Acción",
        [
            "Alta",
            "Consulta",
            "Editar"
        ]
    )

    # =====================================================
    # ALTA
    # =====================================================

    if opcion == "Alta":

        st.subheader("Nuevo Contratista")

        with st.form("form_contratista"):

            nombre = st.text_input(
                "Nombre Contratista"
            )

            tipo = st.selectbox(
                "Tipo Contratista",
                [
                    "Empresa",
                    "Independiente",
                    "Subcontratista",
                    "Profesional",
                    "Otro"
                ]
            )

            especialidad = st.text_input(
                "Especialidad"
            )

            contacto = st.text_input(
                "Contacto"
            )

            fecha_inicio = st.date_input(
                "Fecha Inicio"
            )

            fecha_fin = st.date_input(
                "Fecha Fin"
            )

            estado = st.selectbox(
                "Estado",
                [
                    "Activo",
                    "Pendiente",
                    "Finalizado",
                    "Suspendido"
                ]
            )

            observaciones = st.text_area(
                "Observaciones"
            )

            guardar = st.form_submit_button(
                "Guardar"
            )

            if guardar:

                contratista_id = generar_id(
                    "CON"
                )

                fila = [
                    contratista_id,
                    nombre,
                    tipo,
                    especialidad,
                    contacto,
                    str(fecha_inicio),
                    str(fecha_fin),
                    estado,
                    observaciones
                ]

                append_row(
                    "Contratistas",
                    fila
                )

                st.success(
                    f"Contratista creado: {contratista_id}"
                )

    # =====================================================
    # CONSULTA
    # =====================================================

    elif opcion == "Consulta":

        st.subheader(
            "Listado de Contratistas"
        )

        df = get_dataframe(
            "Contratistas"
        )

        if not df.empty:

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.warning(
                "No hay contratistas registrados."
            )

    # =====================================================
    # EDITAR
    # =====================================================

    elif opcion == "Editar":

        st.subheader(
            "Editar Contratista"
        )

        df = get_dataframe(
            "Contratistas"
        )

        if df.empty:

            st.warning(
                "No hay contratistas cargados."
            )

        else:

            contratistas_dict = {

                f"{row['ID_Con']} - {row['NomCon']}":
                row['ID_Con']

                for _, row in df.iterrows()
            }

            contratista_label = st.selectbox(
                "Seleccionar Contratista",
                list(
                    contratistas_dict.keys()
                )
            )

            contratista_id = (
                contratistas_dict[
                    contratista_label
                ]
            )

            contratista_df = df[
                df["ID_Con"] ==
                contratista_id
            ]

            contratista = (
                contratista_df.iloc[0]
            )

            with st.form(
                "editar_contratista"
            ):

                nombre = st.text_input(
                    "Nombre Contratista",
                    value=contratista[
                        "NomCon"
                    ]
                )

                tipo = st.selectbox(
                    "Tipo Contratista",
                    [
                        "Empresa",
                        "Independiente",
                        "Subcontratista",
                        "Profesional",
                        "Otro"
                    ]
                )

                especialidad = st.text_input(
                    "Especialidad",
                    value=contratista[
                        "EspecialidadCon"
                    ]
                )

                contacto = st.text_input(
                    "Contacto",
                    value=contratista[
                        "ContactoCon"
                    ]
                )

                fecha_inicio = st.text_input(
                    "Fecha Inicio",
                    value=contratista[
                        "FechaInicioCon"
                    ]
                )

                fecha_fin = st.text_input(
                    "Fecha Fin",
                    value=contratista[
                        "FechaFinCon"
                    ]
                )

                estado = st.selectbox(
                    "Estado",
                    [
                        "Activo",
                        "Pendiente",
                        "Finalizado",
                        "Suspendido"
                    ]
                )

                observaciones = st.text_area(
                    "Observaciones",
                    value=contratista[
                        "ObsCon"
                    ]
                )

                guardar_edicion = (
                    st.form_submit_button(
                        "Guardar Cambios"
                    )
                )

                if guardar_edicion:

                    nueva_fila = [
                        contratista_id,
                        nombre,
                        tipo,
                        especialidad,
                        contacto,
                        fecha_inicio,
                        fecha_fin,
                        estado,
                        observaciones
                    ]

                    actualizado = (
                        update_contratista(
                            contratista_id,
                            nueva_fila
                        )
                    )

                    if actualizado:

                        st.success(
                            f"Contratista actualizado: {contratista_id}"
                        )

                    else:

                        st.error(
                            "No se pudo actualizar el contratista."
                        )
