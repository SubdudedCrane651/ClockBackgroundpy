import subprocess
from pathlib import Path

IRFANVIEW = Path(r"C:\Program Files\IrfanView\i_view64.exe")

def svg_to_png(svg_file, png_file):
    if not IRFANVIEW.exists():
        raise FileNotFoundError("IrfanView not found at expected path.")

    subprocess.run([
        str(IRFANVIEW),
        svg_file,
        "/convert=" + png_file
    ], check=True)

    print(f"Converted: {svg_file} -> {png_file}")

# Example:
svg_to_png("countdown_app.svg", "countdown_app.png")
svg_to_png("countdown_windows.svg", "countdown_windows.png")
