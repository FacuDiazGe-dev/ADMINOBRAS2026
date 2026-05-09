import streamlit as st

from services.ids import generar_id

from services.sheets_service import (
    append_row,
    get_dataframe,
    update_presupuesto
)

from services.selectors import (
    obtener_obras,
    obtener_contratistas
)


def render():

    st.header(
        "Gestión de Presupuestos"
    )

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

        st.subheader(
            "Nuevo Presupuesto"
        )

        with st.form(
            "form_presupuesto"
        ):

            # OBRAS
            obras_dict = obtener_obras()

            obra_label = st.selectbox(
                "Obra",
                list(obras_dict.keys())
            )

            obra_id = obras_dict[
                obra_label
            ]

            # CONTRATISTAS
            contratistas_dict = (
                obtener_contratistas()
                )
            

            contratista_label = (
                st.selectbox(
                    "Contratista",
                    list(
                        contratistas_dict.keys()
                    )
                )
            )

            contratista_id = (
                contratistas_dict[
                    contratista_label
                ]
            )

            tipo_contrato = st.selectbox(
                "Tipo Contrato",
                [
                    "Mano de Obra",
                    "Materiales",
                    "Servicio",
                    "Integral"
                ]
            )

            fecha_inicio = st.date_input(
                "Fecha Inicio"
            )

            fecha_fin = st.date_input(
                "Fecha Fin"
            )

            monto_inicial = (
                st.number_input(
                    "Monto Inicial",
                    min_value=0.0
                )
            )

            monto_actual = (
                st.number_input(
                    "Monto Actual",
                    min_value=0.0
                )
            )

            especialidad = st.text_input(
                "Especialidad"
            )

            codigo_especialidad = (
                st.text_input(
                    "Código Especialidad"
                )
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

            guardar = (
                st.form_submit_button(
                    "Guardar"
                )
            )

            if guardar:

                presupuesto_id = (
                    generar_id("PRE")
                )

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
                    f"Presupuesto creado: {presupuesto_id}"
                )

    # =====================================================
    # CONSULTA
    # =====================================================

    elif opcion == "Consulta":

        st.subheader(
            "Listado de Presupuestos"
        )

        df = get_dataframe(
            "Presupuestos"
        )

        if not df.empty:

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.warning(
                "No hay presupuestos registrados."
            )

    # =====================================================
    # EDITAR
    # =====================================================

    elif opcion == "Editar":

        st.subheader(
            "Editar Presupuesto"
        )

        df = get_dataframe(
            "Presupuestos"
        )

        if df.empty:

            st.warning(
                "No hay presupuestos cargados."
            )

        else:

            presupuestos_dict = {

                row["ID_Pres"]:
                row["ID_Pres"]

                for _, row in df.iterrows()
            }

            presupuesto_label = (
                st.selectbox(
                    "Seleccionar Presupuesto",
                    list(
                        presupuestos_dict.keys()
                    )
                )
            )

            presupuesto_id = (
                presupuestos_dict[
                    presupuesto_label
                ]
            )

            presupuesto_df = df[
                df["ID_Pres"] ==
                presupuesto_id
            ]

            presupuesto = (
                presupuesto_df.iloc[0]
            )

            with st.form(
                "editar_presupuesto"
            ):

                tipo_contrato = (
                    st.selectbox(
                        "Tipo Contrato",
                        [
                            "Mano de Obra",
                            "Materiales",
                            "Servicio",
                            "Integral"
                        ]
                    )
                )

                fecha_inicio = (
                    st.text_input(
                        "Fecha Inicio",
                        value=presupuesto[
                            "FecIncPres"
                        ]
                    )
                )

                fecha_fin = (
                    st.text_input(
                        "Fecha Fin",
                        value=presupuesto[
                            "FecFinPres"
                        ]
                    )
                )

                monto_inicial = (
                    st.number_input(
                        "Monto Inicial",
                        value=float(
                            presupuesto[
                                "MonInicPres"
                            ]
                        )
                    )
                )

                monto_actual = (
                    st.number_input(
                        "Monto Actual",
                        value=float(
                            presupuesto[
                                "MonActPres"
                            ]
                        )
                    )
                )

                especialidad = (
                    st.text_input(
                        "Especialidad",
                        value=presupuesto[
                            "EspPres"
                        ]
                    )
                )

                codigo_especialidad = (
                    st.text_input(
                        "Código Especialidad",
                        value=presupuesto[
                            "Cdo_EspPres"
                        ]
                    )
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

                causa_estado = (
                    st.text_input(
                        "Causa Estado",
                        value=presupuesto[
                            "CauEstPres"
                        ]
                    )
                )

                observaciones = (
                    st.text_area(
                        "Observaciones",
                        value=presupuesto[
                            "ObsCon"
                        ]
                    )
                )

                guardar_edicion = (
                    st.form_submit_button(
                        "Guardar Cambios"
                    )
                )

                if guardar_edicion:

                    nueva_fila = [
                        presupuesto[
                            "ID_Obr"
                        ],
                        presupuesto[
                            "ID_Con"
                        ],
                        presupuesto_id,
                        tipo_contrato,
                        fecha_inicio,
                        fecha_fin,
                        monto_inicial,
                        monto_actual,
                        especialidad,
                        codigo_especialidad,
                        estado,
                        causa_estado,
                        observaciones
                    ]

                    actualizado = (
                        update_presupuesto(
                            presupuesto_id,
                            nueva_fila
                        )
                    )

                    if actualizado:

                        st.success(
                            f"Presupuesto actualizado: {presupuesto_id}"
                        )

                    else:

                        st.error(
                            "No se pudo actualizar el presupuesto."
                        )
