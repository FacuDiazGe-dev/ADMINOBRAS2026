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

                nueva_fila = [
                    obra_id,
                    contratista_id,
                    presupuesto_id,
                    tipo_contrato,
                    str(fecha_inicio),  # Convertir a string
                    str(fecha_fin),     # Convertir a string
                    float(monto_inicial),
                    float(monto_actual),
                    especialidad,
                    codigo_especialidad,
                    estado,
                    causa_estado,
                    observaciones
                ]
                append_row(
                    "Presupuestos",
                    nueva_fila  # Antes decía 'fila'
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
    # EDITAR (CORREGIDO)
    # =====================================================

    elif opcion == "Editar":
        st.subheader("Editar Presupuesto")
        df = get_dataframe("Presupuestos")

        if df.empty:
            st.warning("No hay presupuestos cargados.")
        else:
            presupuestos_dict = {
                str(row["ID_Pres"]): str(row["ID_Pres"])
                for _, row in df.iterrows()
            }

            presupuesto_label = st.selectbox(
                "Seleccionar Presupuesto",
                list(presupuestos_dict.keys())
            )

            presupuesto_id = presupuestos_dict[presupuesto_label]
            presupuesto_df = df[df["ID_Pres"] == presupuesto_id]
            presupuesto = presupuesto_df.iloc[0]

            with st.form("editar_presupuesto"):
                tipo_contrato = st.selectbox(
                    "Tipo Contrato",
                    ["Mano de Obra", "Materiales", "Servicio", "Integral"],
                    index=0 # Podrías buscar el índice actual si quisieras
                )

                # Usamos str() y .fillna() implícito para evitar errores de lectura
                fecha_inicio = st.text_input("Fecha Inicio", value=str(presupuesto.get("FecIncPres", "")))
                fecha_fin = st.text_input("Fecha Fin", value=str(presupuesto.get("FecFinPres", "")))

                # Validación de montos para evitar ValueError si hay NaN
                try:
                    val_ini = float(presupuesto["MonInicPres"])
                except:
                    val_ini = 0.0
                
                try:
                    val_act = float(presupuesto["MonActPres"])
                except:
                    val_act = 0.0

                monto_inicial = st.number_input("Monto Inicial", value=val_ini)
                monto_actual = st.number_input("Monto Actual", value=val_act)

                especialidad = st.text_input("Especialidad", value=str(presupuesto.get("EspPres", "")))
                codigo_especialidad = st.text_input("Código Especialidad", value=str(presupuesto.get("Cdo_EspPres", "")))
                
                estado = st.selectbox("Estado", ["Activo", "Pendiente", "Finalizado", "Cancelado"])
                causa_estado = st.text_input("Causa Estado", value=str(presupuesto.get("CauEstPres", "")))
                observaciones = st.text_area("Observaciones", value=str(presupuesto.get("ObsCon", "")))

                guardar_edicion = st.form_submit_button("Guardar Cambios")

                if guardar_edicion:
                    # LIMPIEZA CRÍTICA: Convertimos todo a tipos básicos (str o float)
                    # Esto elimina los NaNs de Pandas que causan el TypeError
                    nueva_fila = [
                        str(presupuesto["ID_Obr"]),
                        str(presupuesto["ID_Con"]),
                        str(presupuesto_id),
                        str(tipo_contrato),
                        str(fecha_inicio),
                        str(fecha_fin),
                        float(monto_inicial),
                        float(monto_actual),
                        str(especialidad),
                        str(codigo_especialidad),
                        str(estado),
                        str(causa_estado),
                        str(observaciones)
                    ]

                    # Llamada al servicio
                    actualizado = update_presupuesto(presupuesto_id, nueva_fila)

                    if actualizado:
                        st.success(f"✅ Presupuesto actualizado: {presupuesto_id}")
                        # Opcional: st.rerun() para refrescar los datos
                    else:
                        st.error("❌ No se pudo actualizar el presupuesto.")
