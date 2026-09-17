import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


RUTA_PROCESADOS = Path("data/processed")
RUTA_REPORTES = Path("reports")


def crear_grafico_alarmas():
    df = pd.read_csv(
        RUTA_PROCESADOS / "alarm_summary.csv"
    )

    plt.figure(figsize=(9, 5))

    plt.bar(
        df["alarma"],
        df["cantidad"]
    )

    plt.title("Distribución de alarmas FTTH/GPON")
    plt.xlabel("Tipo de alarma")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=20)
    plt.tight_layout()

    plt.savefig(
        RUTA_REPORTES / "alarm_distribution.png",
        dpi=150
    )

    plt.close()


def crear_grafico_potencia():
    df = pd.read_csv(
        RUTA_PROCESADOS / "power_summary.csv"
    )

    plt.figure(figsize=(10, 5))

    plt.bar(
        df["puerto"],
        df["promedio"]
    )

    plt.title("Potencia óptica promedio por puerto")
    plt.xlabel("Puerto")
    plt.ylabel("Potencia (dBm)")
    plt.xticks(rotation=90)
    plt.tight_layout()

    plt.savefig(
        RUTA_REPORTES / "average_power_by_port.png",
        dpi=150
    )

    plt.close()


def main():
    RUTA_REPORTES.mkdir(
        parents=True,
        exist_ok=True
    )

    crear_grafico_alarmas()
    crear_grafico_potencia()

    print("Reportes gráficos generados correctamente.")
    print(f"Carpeta: {RUTA_REPORTES}")


if __name__ == "__main__":
    main()