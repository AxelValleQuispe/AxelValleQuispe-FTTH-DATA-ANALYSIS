import pandas as pd
from pathlib import Path

from data_processing import limpiar_datos, generar_resumen
from power_analysis import analizar_potencia, detectar_degradacion
from alarm_analysis import contar_alarmas, alarmas_por_puerto


RUTA_DATOS = "data/raw/ftth_sample.csv"
RUTA_SALIDA = Path("data/processed")


def main():
    print("=" * 50)
    print("ANÁLISIS DE DATOS FTTH/GPON")
    print("=" * 50)

    # Crear carpeta de resultados
    RUTA_SALIDA.mkdir(parents=True, exist_ok=True)

    # Cargar datos
    df = pd.read_csv(RUTA_DATOS)

    # Limpiar datos
    df = limpiar_datos(df)

    print("\nRESUMEN DE DATOS")
    print("-" * 30)

    resumen = generar_resumen(df)

    for clave, valor in resumen.items():
        print(f"{clave}: {valor}")

    # Análisis de potencia
    print("\nANÁLISIS DE POTENCIA")
    print("-" * 30)

    potencia = analizar_potencia(df)

    print(potencia.head(10))

    potencia.to_csv(
        RUTA_SALIDA / "power_summary.csv",
        index=False
    )

    # Detección de degradación
    print("\nDETECCIÓN DE DEGRADACIÓN")
    print("-" * 30)

    degradacion = detectar_degradacion(df)

    cantidad_degradados = degradacion["degradacion"].sum()

    print(
        f"Registros con posible degradación: "
        f"{cantidad_degradados}"
    )

    degradacion.to_csv(
        RUTA_SALIDA / "degradation_analysis.csv",
        index=False
    )

    # Análisis de alarmas
    print("\nTIPOS DE ALARMA")
    print("-" * 30)

    alarmas = contar_alarmas(df)

    print(alarmas)

    alarmas.to_csv(
        RUTA_SALIDA / "alarm_summary.csv",
        index=False
    )

    # Alarmas por puerto
    print("\nALARMAS POR PUERTO")
    print("-" * 30)

    alarmas_puerto = alarmas_por_puerto(df)

    print(alarmas_puerto.head(10))

    alarmas_puerto.to_csv(
        RUTA_SALIDA / "alarms_by_port.csv",
        index=False
    )

    print("\nResultados guardados correctamente.")
    print(f"Carpeta: {RUTA_SALIDA}")

    print("\nAnálisis finalizado correctamente.")


if __name__ == "__main__":
    main()