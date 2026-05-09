from services.sheets_service import get_dataframe


def obtener_obras():

    df = get_dataframe("Obras")

    if df.empty:
        return {}

    return {
        f"{row['NomObr']} ({row['ID_Obr']})": row['ID_Obr']
        for _, row in df.iterrows()
    }


def obtener_contratistas():

    df = get_dataframe("Contratistas")

    if df.empty:
        return {}

    return {
        f"{row['NomCon']} ({row['ID_Con']})": row['ID_Con']
        for _, row in df.iterrows()
    }


def obtener_proveedores():

    df = get_dataframe("Proveedores")

    if df.empty:
        return {}

    return {
        f"{row['NomProv']} ({row['ID_Prov']})": row['ID_Prov']
        for _, row in df.iterrows()
    }


def obtener_presupuestos():

    df = get_dataframe("Presupuestos")

    if df.empty:
        return {}

    return {
        f"{row['ID_Pres']} - ${row['MontoInicialPres']}"
        : row['ID_Pres']
        for _, row in df.iterrows()
    }
