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

    # =========================================================
    # TABS
    # =========================================================

    tab1, tab2 = st.tabs([
        "Pago Contratista",
        "Pago Proveedor"
    ])

    # =========================================================
    # TAB CONTRATISTAS
    # =========================================================

    with tab1:

        st.subheader("Registrar Pago a Contratista")

        with st.form("form_pago_contratista"):

            # =========================
            # OBRA
            # =========================

            obras_dict = obtener_obras()

            obra_label = st.selectbox(
                "Obra",
                list(obras_dict.keys()),
                key="obra_contratista"
            )

            obra_id = obras_dict[obra_label]

            # =========================
            # CONTRATISTAS
            # =========================

            contratistas_dict = obtener_contratistas_por_obra(
                obra_id
            )

            contratista_id = None
            presupuesto_id = None

            if contratistas_dict:

                contratista_label = st.selectbox(
                    "Contratista",
                    list(contratistas_dict.keys()),
                    key="contratista"
                )

                contratista_id = contratistas_dict[
                    contratista_label
                ]

                # =========================
                # PRESUPUESTOS
                # =========================

                presupuestos_dict = (
                    obtener_presupuestos_por_contratista(
                        obra_id,
                        contratista_id
                    )
                )

                if presupuestos_dict:

                    presupuesto_label = st.selectbox(
                        "Presupuesto",
                        list(presupuestos_dict.keys()),
                        key="presupuesto"
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

            # =========================
            # DATOS DEL PAGO
            # =========================

            tipo = st.selectbox(
                "Tipo Movimiento",
                [
                    "Pago",
                    "Aporte"
                ],
                key="tipo_contratista"
            )

            monto = st.number_input(
                "Monto",
                min_value=0.0,
                key="monto_contratista"
            )

            fecha_pago = st.date_input(
                "Fecha Pago",
                key="fecha_contratista"
            )

            metodo = st.selectbox(
                "Método Pago",
                [
                    "Efectivo",
                    "Transferencia",
                    "Cheque"
                ],
                key="metodo_contratista"
            )

            estado = st.selectbox(
                "Estado",
                [
                    "Pendiente",
                    "Pagado",
                    "Cancelado"
                ],
                key="estado_contratista"
            )

            observaciones = st.text_area(
                "Observaciones",
                key="obs_contratista"
            )

            # =========================
            # BOTÓN
            # =========================

            guardar_contratista = st.form_submit_button(
                "Registrar Pago Contratista"
            )

            # =========================
            # GUARDAR
            # =========================

            if guardar_contratista:

                pago_id = generar_id("PAG")

                fila = [
                    pago_id,
                    obra_id,
                    contratista_id,
                    None,
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
                    f"Pago a contratista registrado: {pago_id}"
                )

    # =========================================================
    # TAB PROVEEDORES
    # =========================================================

    with tab2:

        st.subheader("Registrar Pago a Proveedor")

        with st.form("form_pago_proveedor"):

            # =========================
            # OBRA
            # =========================

            obras_dict = obtener_obras()

            obra_label = st.selectbox(
                "Obra",
                list(obras_dict.keys()),
                key="obra_proveedor"
            )

            obra_id = obras_dict[obra_label]

            # =========================
            # PROVEEDORES
            # =========================

            proveedores_dict = obtener_proveedores()

            proveedor_id = None

            if proveedores_dict:

                proveedor_label = st.selectbox(
                    "Proveedor",
                    list(proveedores_dict.keys()),
                    key="proveedor"
                )

                proveedor_id = proveedores_dict[
                    proveedor_label
                ]

            else:

                st.warning(
                    "No hay proveedores registrados."
                )

            # =========================
            # DATOS DEL PAGO
            # =========================

            tipo = st.selectbox(
                "Tipo Movimiento",
                [
                    "Pago",
                    "Aporte"
                ],
                key="tipo_proveedor"
            )

            monto = st.number_input(
                "Monto",
                min_value=0.0,
                key="monto_proveedor"
            )

            fecha_pago = st.date_input(
                "Fecha Pago",
                key="fecha_proveedor"
            )

            metodo = st.selectbox(
                "Método Pago",
                [
                    "Efectivo",
                    "Transferencia",
                    "Cheque"
                ],
                key="metodo_proveedor"
            )

            estado = st.selectbox(
                "Estado",
                [
                    "Pendiente",
                    "Pagado",
                    "Cancelado"
                ],
                key="estado_proveedor"
            )

            observaciones = st.text_area(
                "Observaciones",
                key="obs_proveedor"
            )

            # =========================
            # BOTÓN
            # =========================

            guardar_proveedor = st.form_submit_button(
                "Registrar Pago Proveedor"
            )

            # =========================
            # GUARDAR
            # =========================

            if guardar_proveedor:

                pago_id = generar_id("PAG")

                fila = [
                    pago_id,
                    obra_id,
                    None,
                    proveedor_id,
                    None,
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
                    f"Pago a proveedor registrado: {pago_id}"
                )
