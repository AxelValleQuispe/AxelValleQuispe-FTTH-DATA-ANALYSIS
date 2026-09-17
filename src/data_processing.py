import pandas as pd


def cargar_datos(ruta):
    """Carga un archivo CSV y devuelve un DataFrame."""
    return pd.read_csv(ruta)


def limpiar_datos(df):
    """Realiza una limpieza básica de los datos."""
    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    df = df.drop_duplicates()

    return df


def generar_resumen(df):
    """Genera un resumen básico de la información."""
    resumen = {
        "registros": len(df),
        "columnas": len(df.columns),
        "valores_nulos": int(df.isna().sum().sum()),
    }

    return resumen


if __name__ == "__main__":
    print("Módulo de procesamiento de datos FTTH/GPON")
    print("Funciones disponibles:")
    print("- cargar_datos()")
    print("- limpiar_datos()")
    print("- generar_resumen()")