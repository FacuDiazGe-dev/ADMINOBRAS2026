from services.sheets_service import get_dataframe


def obtener_obras():

    df = get_dataframe("Obras")

    if df.empty:
        return {}

    return {
        f"{row['NomObr']} ({row['ID_Obr']})": row['ID_Obr']
        for _, row in df.iterrows()
    }


def obtener_contratistas_por_obra(obra_id):

    df = get_dataframe("Presupuestos")

    if df.empty:
        return {}

    df_filtrado = df[
        df["ID_Obr"] == obra_id
    ]

    contratistas = {}

    for _, row in df_filtrado.iterrows():

        contratistas[
            f"{row['ID_Con']}"
        ] = row["ID_Con"]

    return contratistas


def obtener_proveedores():

    df = get_dataframe("Proveedores")

    if df.empty:
        return {}

    return {
        f"{row['NomProv']} ({row['ID_Prov']})": row['ID_Prov']
        for _, row in df.iterrows()
    }


def obtener_presupuestos_por_obra(obra_id):

    df = get_dataframe("Presupuestos")

    if df.empty:
        return {}

    df_filtrado = df[
        df["ID_Obr"] == obra_id
    ]

    return {
        f"{row['ID_Pres']} - ${row['MonInicPres']}"
        : row['ID_Pres']
        for _, row in df_filtrado.iterrows()
    }
