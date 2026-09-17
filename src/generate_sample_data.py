import pandas as pd
import numpy as np
from pathlib import Path


np.random.seed(42)


def generar_datos():
    """Genera datos ficticios de una red FTTH/GPON."""

    n = 500

    puertos = [f"PORT-{i:03d}" for i in range(1, 31)]

    tipos_alarma = [
        "SIN_ALARMA",
        "BAJA_POTENCIA",
        "PERDIDA_SEÑAL",
        "INTERMITENCIA",
    ]

    df = pd.DataFrame({
        "puerto": np.random.choice(puertos, n),
        "potencia_dbm": np.round(
            np.random.normal(-22, 4, n), 2
        ),
        "alarma": np.random.choice(
            tipos_alarma,
            n,
            p=[0.65, 0.15, 0.10, 0.10]
        ),
    })

    return df


def guardar_datos(df):
    """Guarda los datos ficticios en data/raw."""

    ruta = Path("data/raw/ftth_sample.csv")
    ruta.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(ruta, index=False)

    print(f"Datos guardados en: {ruta}")
    print(f"Registros generados: {len(df)}")


if __name__ == "__main__":
    datos = generar_datos()

    print("Datos ficticios FTTH/GPON generados.")
    print(datos.head())

    guardar_datos(datos)