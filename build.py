from pathlib import Path

import PyInstaller.__main__

import info


def main():
    ressources = Path(__file__).parent / "Ressources"

    PyInstaller.__main__.run(
        [
            "main.py",
            "--onefile",
            "--name",
            f"{info.NAME} - {info.VERSION}",
            f"--add-data={ressources}:Ressources",
            "--noconsole",
            "--noconfirm",
            "--icon",
            str(Path(__file__).parent / "Ressources" / "icon.ico"),
        ]
    )


if __name__ == "__main__":
    main()
