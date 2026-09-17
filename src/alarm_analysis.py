import pandas as pd


def contar_alarmas(df, columna_alarma="alarma"):
    """
    Cuenta la cantidad de registros por tipo de alarma.
    """

    if columna_alarma not in df.columns:
        raise ValueError(
            f"No se encontró la columna: {columna_alarma}"
        )

    resumen = (
        df[columna_alarma]
        .value_counts()
        .reset_index()
    )

    resumen.columns = ["alarma", "cantidad"]

    return resumen


def alarmas_por_puerto(
    df,
    columna_alarma="alarma",
    columna_puerto="puerto"
):
    """
    Resume la cantidad de alarmas registradas
    por puerto.
    """

    columnas_requeridas = [
        columna_alarma,
        columna_puerto
    ]

    for columna in columnas_requeridas:
        if columna not in df.columns:
            raise ValueError(
                f"No se encontró la columna: {columna}"
            )

    resumen = (
        df.groupby(columna_puerto)[columna_alarma]
        .count()
        .reset_index(name="cantidad_alarmas")
        .sort_values(
            "cantidad_alarmas",
            ascending=False
        )
    )

    return resumen


if __name__ == "__main__":
    print("Módulo de análisis de alarmas FTTH/GPON")
    print("Funciones disponibles:")
    print("- contar_alarmas()")
    print("- alarmas_por_puerto()")