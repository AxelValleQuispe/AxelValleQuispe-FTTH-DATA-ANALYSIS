import pandas as pd


def analizar_potencia(df, columna_potencia="potencia_dbm"):
    """
    Calcula estadísticas básicas de potencia óptica
    agrupadas por puerto.
    """

    columnas_requeridas = ["puerto", columna_potencia]

    for columna in columnas_requeridas:
        if columna not in df.columns:
            raise ValueError(
                f"No se encontró la columna requerida: {columna}"
            )

    resumen = (
        df.groupby("puerto")[columna_potencia]
        .agg(
            minimo="min",
            maximo="max",
            promedio="mean",
            mediana="median"
        )
        .reset_index()
    )

    return resumen


def detectar_degradacion(
    df,
    columna_potencia="potencia_dbm",
    umbral=-27
):
    """
    Identifica registros cuya potencia óptica
    se encuentra por debajo del umbral establecido.
    """

    if columna_potencia not in df.columns:
        raise ValueError(
            f"No se encontró la columna: {columna_potencia}"
        )

    df_resultado = df.copy()

    df_resultado["degradacion"] = (
        df_resultado[columna_potencia] < umbral
    )

    return df_resultado


if __name__ == "__main__":
    print("Módulo de análisis de potencia óptica")
    print("Funciones disponibles:")
    print("- analizar_potencia()")
    print("- detectar_degradacion()")