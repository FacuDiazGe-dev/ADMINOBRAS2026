import streamlit as st
from services.ids import generar_id
from services.sheets_service import (
    append_row, 
    get_dataframe, 
    update_proveedor
)

def render():
    st.header("Gestión de Proveedores")

    opcion = st.selectbox(
        "Acción",
        ["Alta", "Consulta", "Editar"]
    )

    # =====================================================
    # ALTA
    # =====================================================
    if opcion == "Alta":
        st.subheader("Registrar Nuevo Proveedor")
        with st.form("form_proveedores"):
            nombre = st.text_input("Nombre Proveedor")
            rubro = st.selectbox("Rubro", ["Materiales", "Servicios", "Transporte", "Equipamiento", "Impuestos", "Herramientas", "Logística", "Otros"])
            subrubro = st.text_input("Subrubro")
            contacto = st.text_input("Contacto")
            cuit = st.text_input("CUIT")
            estado_pago = st.selectbox("Estado Pago", ["Pendiente", "Pagado", "Parcial", "Cancelado"])
            observaciones = st.text_area("Observaciones")

            guardar = st.form_submit_button("Registrar Proveedor")

            if guardar:
                proveedor_id = generar_id("PROV")
                nueva_fila = [
                    str(nombre),
                    str(proveedor_id),
                    str(rubro),
                    str(subrubro),
                    str(contacto),
                    str(cuit),
                    str(estado_pago),
                    str(observaciones)
                ]
                append_row("Proveedores", nueva_fila)
                st.success(f"✅ Proveedor registrado: {proveedor_id}")

    # =====================================================
    # CONSULTA
    # =====================================================
    elif opcion == "Consulta":
        st.subheader("Listado de Proveedores")
        df = get_dataframe("Proveedores")
        if not df.empty:
            st.dataframe(df, use_container_width=True)
        else:
            st.warning("No hay proveedores registrados.")

    # =====================================================
    # EDITAR
    # =====================================================
    elif opcion == "Editar":
        st.subheader("Editar Datos de Proveedor")
        df = get_dataframe("Proveedores")

        if df.empty:
            st.warning("No hay datos para editar.")
        else:
            prov_dict = {
                f"{row['NomProv']} ({row['ID_Prov']})": row['ID_Prov']
                for _, row in df.iterrows()
            }
            
            seleccion = st.selectbox("Seleccionar Proveedor", list(prov_dict.keys()))
            prov_id_selec = prov_dict[seleccion]
            prov_data = df[df["ID_Prov"] == prov_id_selec].iloc[0]

            with st.form("edit_proveedor_form"):
                nombre = st.text_input("Nombre Proveedor", value=str(prov_data.get("NomProv", "")))
                
                # Listas para selectores
                rubros = ["Materiales", "Servicios", "Transporte", "Equipamiento", "Impuestos", "Herramientas", "Logística", "Otros"]
                pagos = ["Pendiente", "Pagado", "Parcial", "Cancelado"]

                # Lógica para pre-seleccionar el valor actual
                try: idx_r = rubros.index(prov_data.get("RubProv", "Otros"))
                except: idx_r = 7
                
                try: idx_p = pagos.index(prov_data.get("PagoProv", "Pendiente"))
                except: idx_p = 0

                rubro = st.selectbox("Rubro", rubros, index=idx_r)
                subrubro = st.text_input("Subrubro", value=str(prov_data.get("S_RubProv", "")))
                contacto = st.text_input("Contacto", value=str(prov_data.get("ContProv", "")))
                cuit = st.text_input("CUIT", value=str(prov_data.get("CuitProv", "")))
                estado_pago = st.selectbox("Estado Pago", pagos, index=idx_p)
                observaciones = st.text_area("Observaciones", value=str(prov_data.get("ObsProv", "")))

                actualizar = st.form_submit_button("Guardar Cambios")

                if actualizar:
                    fila_editada = [
                        str(nombre),
                        str(prov_id_selec),
                        str(rubro),
                        str(subrubro),
                        str(contacto),
                        str(cuit),
                        str(estado_pago),
                        str(observaciones)
                    ]
                    
                    if update_proveedor(prov_id_selec, fila_editada):
                        st.success(f"✅ Proveedor {prov_id_selec} actualizado.")
                    else:
                        st.error("Error al actualizar.")
