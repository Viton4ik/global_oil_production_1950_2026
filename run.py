import os
import sys
import subprocess
import shutil
import venv

VENV_DIR = ".venv_oil_race"
TEMP_DIR = ".temp_oil_assets"


def create_venv():
    if not os.path.exists(VENV_DIR):
        print("[1/5] Creating isolated virtual environment (.venv_oil_race)...")
        venv.create(VENV_DIR, with_pip=True)


def get_venv_python():
    if sys.platform == "win32":
        return os.path.join(VENV_DIR, "Scripts", "python.exe")
    return os.path.join(VENV_DIR, "bin", "python")


def run_bootstrap():
    print("=====================================================================")
    print("  3D VIDEO GENERATOR: GLOBAL CRUDE OIL PRODUCTION (1950 - 2026)      ")
    print("=====================================================================")

    os.makedirs(TEMP_DIR, exist_ok=True)
    create_venv()
    venv_python = get_venv_python()

    print("[2/5] Installing required libraries and portable FFmpeg into virtual environment...")
    subprocess.check_call([venv_python, "-m", "pip", "install", "--upgrade", "pip", "-q"])
    subprocess.check_call([
        venv_python, "-m", "pip", "install",
        "pandas", "numpy", "matplotlib", "requests", "pillow", "imageio-ffmpeg", "-q"
    ])

    try:
        print("[3/5] Launching beveled 3D rendering, audio synthesis, and MP4 assembly...")
        subprocess.check_call([venv_python, os.path.abspath(__file__), "--worker"])
    finally:
        print("[4/5] Self-cleanup: removing virtual environment and temporary assets...")
        shutil.rmtree(TEMP_DIR, ignore_errors=True)
        shutil.rmtree(VENV_DIR, ignore_errors=True)
        print("[5/5] Cleanup complete! Final MP4 video and license files are ready in the project folder.")


def create_industrial_flag(code, width=80, height=52, radius=3):
    from PIL import Image, ImageDraw
    import numpy as np

    canvas = Image.new("RGBA", (width + 8, height + 8), (0, 0, 0, 0))

    mask = Image.new("L", (width, height), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([0, 0, width - 1, height - 1], radius=radius, fill=255)

    shadow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    sh_draw = ImageDraw.Draw(shadow)
    sh_draw.rounded_rectangle([0, 0, width - 1, height - 1], radius=radius, fill=(4, 3, 2, 220))
    canvas.paste(shadow, (4, 4))

    img = Image.new("RGBA", (width, height), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)
    w, h = width, height

    if code == "us":
        stripe_h = h / 13.0
        for i in range(13):
            color = (178, 34, 52) if i % 2 == 0 else (245, 247, 250)
            draw.rectangle([0, int(i * stripe_h), w, int((i + 1) * stripe_h)], fill=color)
        draw.rectangle([0, 0, int(w * 0.42), int(h * 7 / 13.0)], fill=(40, 53, 107))
        for r in range(3):
            for c in range(4):
                cx = int(w * 0.06 + c * (w * 0.09))
                cy = int(h * 0.08 + r * (h * 0.16))
                draw.ellipse([cx - 1, cy - 1, cx + 1, cy + 1], fill=(255, 255, 255))
    elif code == "ru":
        draw.rectangle([0, 0, w, h // 3], fill=(248, 250, 252))
        draw.rectangle([0, h // 3, w, 2 * h // 3], fill=(0, 57, 166))
        draw.rectangle([0, 2 * h // 3, w, h], fill=(213, 43, 30))
    elif code == "sa":
        draw.rectangle([0, 0, w, h], fill=(0, 108, 53))
        draw.rectangle([int(w * 0.22), int(h * 0.62), int(w * 0.78), int(h * 0.68)], fill=(255, 255, 255))
    elif code == "ca":
        draw.rectangle([0, 0, w // 4, h], fill=(216, 6, 33))
        draw.rectangle([w // 4, 0, 3 * w // 4, h], fill=(248, 250, 252))
        draw.rectangle([3 * w // 4, 0, w, h], fill=(216, 6, 33))
        r = int(h * 0.18)
        draw.polygon([(w // 2, h // 2 - r), (w // 2 - r, h // 2 + r // 2), (w // 2 + r, h // 2 + r // 2)], fill=(216, 6, 33))
    elif code == "iq":
        draw.rectangle([0, 0, w, h // 3], fill=(206, 17, 38))
        draw.rectangle([0, h // 3, w, 2 * h // 3], fill=(248, 250, 252))
        draw.rectangle([0, 2 * h // 3, w, h], fill=(15, 15, 15))
        draw.rectangle([int(w * 0.35), h // 2 - 2, int(w * 0.65), h // 2 + 2], fill=(0, 122, 61))
    elif code == "cn":
        draw.rectangle([0, 0, w, h], fill=(222, 41, 16))
        draw.ellipse([int(w * 0.1), int(h * 0.15), int(w * 0.28), int(h * 0.42)], fill=(255, 222, 0))
    elif code == "ir":
        draw.rectangle([0, 0, w, h // 3], fill=(35, 159, 64))
        draw.rectangle([0, h // 3, w, 2 * h // 3], fill=(248, 250, 252))
        draw.rectangle([0, 2 * h // 3, w, h], fill=(218, 0, 0))
        draw.ellipse([w // 2 - 4, h // 2 - 4, w // 2 + 4, h // 2 + 4], fill=(218, 0, 0))
    elif code == "ae":
        draw.rectangle([0, 0, w, h // 3], fill=(0, 115, 47))
        draw.rectangle([0, h // 3, w, 2 * h // 3], fill=(248, 250, 252))
        draw.rectangle([0, 2 * h // 3, w, h], fill=(15, 15, 15))
        draw.rectangle([0, 0, int(w * 0.26), h], fill=(255, 0, 0))
    elif code == "br":
        draw.rectangle([0, 0, w, h], fill=(0, 156, 59))
        draw.polygon([(w // 2, int(h * 0.12)), (int(w * 0.88), h // 2), (w // 2, int(h * 0.88)), (int(w * 0.12), h // 2)], fill=(255, 223, 0))
        r = int(h * 0.18)
        draw.ellipse([w // 2 - r, h // 2 - r, w // 2 + r, h // 2 + r], fill=(0, 39, 118))
    elif code == "kw":
        draw.rectangle([0, 0, w, h // 3], fill=(0, 122, 61))
        draw.rectangle([0, h // 3, w, 2 * h // 3], fill=(248, 250, 252))
        draw.rectangle([0, 2 * h // 3, w, h], fill=(206, 17, 38))
        draw.polygon([(0, 0), (int(w * 0.26), h // 3), (int(w * 0.26), 2 * h // 3), (0, h)], fill=(15, 15, 15))
    elif code == "mx":
        draw.rectangle([0, 0, w // 3, h], fill=(0, 104, 71))
        draw.rectangle([w // 3, 0, 2 * w // 3, h], fill=(248, 250, 252))
        draw.rectangle([2 * w // 3, 0, w, h], fill=(206, 17, 38))
        draw.ellipse([w // 2 - 4, h // 2 - 4, w // 2 + 4, h // 2 + 4], fill=(139, 69, 19))
    elif code == "no":
        draw.rectangle([0, 0, w, h], fill=(186, 12, 47))
        draw.rectangle([int(w * 0.28), 0, int(w * 0.44), h], fill=(255, 255, 255))
        draw.rectangle([0, int(h * 0.38), w, int(h * 0.62)], fill=(255, 255, 255))
        draw.rectangle([int(w * 0.32), 0, int(w * 0.40), h], fill=(0, 32, 91))
        draw.rectangle([0, int(h * 0.43), w, int(h * 0.57)], fill=(0, 32, 91))
    elif code == "ng":
        draw.rectangle([0, 0, w // 3, h], fill=(0, 135, 81))
        draw.rectangle([w // 3, 0, 2 * w // 3, h], fill=(248, 250, 252))
        draw.rectangle([2 * w // 3, 0, w, h], fill=(0, 135, 81))
    elif code == "ve":
        draw.rectangle([0, 0, w, h // 3], fill=(252, 209, 22))
        draw.rectangle([0, h // 3, w, 2 * h // 3], fill=(0, 56, 147))
        draw.rectangle([0, 2 * h // 3, w, h], fill=(206, 17, 38))
    elif code == "gb":
        draw.rectangle([0, 0, w, h], fill=(1, 33, 105))
        draw.line([(0, 0), (w, h)], fill=(255, 255, 255), width=7)
        draw.line([(0, h), (w, 0)], fill=(255, 255, 255), width=7)
        draw.line([(0, 0), (w, h)], fill=(200, 16, 46), width=3)
        draw.line([(0, h), (w, 0)], fill=(200, 16, 46), width=3)
        draw.rectangle([w // 2 - 6, 0, w // 2 + 6, h], fill=(255, 255, 255))
        draw.rectangle([0, h // 2 - 6, w, h // 2 + 6], fill=(255, 255, 255))
        draw.rectangle([w // 2 - 3, 0, w // 2 + 3, h], fill=(200, 16, 46))
        draw.rectangle([0, h // 2 - 3, w, h // 2 + 3], fill=(200, 16, 46))
    elif code == "kz":
        draw.rectangle([0, 0, w, h], fill=(0, 175, 202))
        r = int(h * 0.22)
        draw.ellipse([w // 2 - r, h // 2 - r, w // 2 + r, h // 2 + r], fill=(254, 197, 12))
    elif code == "ly":
        draw.rectangle([0, 0, w, h // 4], fill=(231, 0, 19))
        draw.rectangle([0, h // 4, w, 3 * h // 4], fill=(15, 15, 15))
        draw.rectangle([0, 3 * h // 4, w, h], fill=(35, 158, 70))
        draw.ellipse([w // 2 - 5, h // 2 - 5, w // 2 + 5, h // 2 + 5], fill=(255, 255, 255))
    elif code == "id":
        draw.rectangle([0, 0, w, h // 2], fill=(255, 0, 0))
        draw.rectangle([0, h // 2, w, h], fill=(248, 250, 252))

    rounded_flag = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    rounded_flag.paste(img, (0, 0), mask=mask)
    rim_draw = ImageDraw.Draw(rounded_flag)
    rim_draw.rounded_rectangle([0, 0, width - 1, height - 1], radius=radius, outline=(217, 119, 6, 185), width=2)
    canvas.paste(rounded_flag, (0, 0), mask=rounded_flag)
    return np.array(canvas)


def make_beveled_rect_polygon(x0, y0, width, height, rx, ry, n_arc=8):
    import numpy as np

    ry = min(ry, height * 0.16)
    rx = min(rx, width * 0.25)

    angles_br = np.linspace(-np.pi / 2, 0, n_arc)
    angles_tr = np.linspace(0, np.pi / 2, n_arc)
    angles_tl = np.linspace(np.pi / 2, np.pi, n_arc)
    angles_bl = np.linspace(np.pi, 3 * np.pi / 2, n_arc)

    x_br = (x0 + width - rx) + rx * np.cos(angles_br)
    y_br = (y0 + ry) + ry * np.sin(angles_br)

    x_tr = (x0 + width - rx) + rx * np.cos(angles_tr)
    y_tr = (y0 + height - ry) + ry * np.sin(angles_tr)

    x_tl = (x0 + rx) + rx * np.cos(angles_tl)
    y_tl = (y0 + height - ry) + ry * np.sin(angles_tl)

    x_bl = (x0 + rx) + rx * np.cos(angles_bl)
    y_bl = (y0 + ry) + ry * np.sin(angles_bl)

    xs = np.concatenate([x_br, x_tr, x_tl, x_bl])
    ys = np.concatenate([y_br, y_tr, y_tl, y_bl])
    return np.column_stack([xs, ys])


def build_restrained_oil_3d_texture(norm_rank, delta_rate, flow_phase, alpha=1.0, h_px=64, w_px=220):
    import numpy as np

    y_norm = np.linspace(0.0, 1.0, h_px)[:, None]
    x_norm = np.linspace(0.0, 1.0, w_px)[None, :]

    surge = float(np.clip(delta_rate * 6.0, -0.25, 0.35))

    # Restrained horizontal gradient (~16% variation across the bar)
    r_left = 0.52 + 0.14 * norm_rank
    g_left = 0.31 + 0.10 * norm_rank
    b_left = 0.08 + 0.04 * norm_rank

    r_right = 0.68 + 0.16 * norm_rank + 0.08 * max(0.0, surge)
    g_right = 0.43 + 0.14 * norm_rank + 0.07 * surge
    b_right = 0.12 + 0.06 * norm_rank

    r_base = r_left + (r_right - r_left) * x_norm
    g_base = g_left + (g_right - g_left) * x_norm
    b_base = b_left + (b_right - b_left) * x_norm

    # Chiseled 3-facet rectangular 3D profile along Y
    facet_light = np.where(
        y_norm < 0.18,
        0.56 + 0.8 * y_norm,
        np.where(
            y_norm < 0.78,
            0.88 + 0.18 * ((y_norm - 0.18) / 0.60),
            1.18 - 0.15 * ((y_norm - 0.78) / 0.22)
        )
    )
    ridge_line = 0.18 * np.exp(-((y_norm - 0.78) ** 2) / (2 * 0.0008))

    wave_pos = flow_phase % 1.0
    flow_wave = 0.07 * np.exp(-((x_norm - wave_pos) ** 2) / (2 * 0.025))

    r = np.clip(r_base * facet_light + ridge_line + flow_wave, 0.0, 1.0)
    g = np.clip(g_base * facet_light + ridge_line * 0.85 + flow_wave * 0.80, 0.0, 1.0)
    b = np.clip(b_base * facet_light + ridge_line * 0.55 + flow_wave * 0.40, 0.0, 1.0)
    a = np.full_like(r, alpha)

    return np.dstack([r, g, b, a])


def run_worker():
    import math
    import wave
    import pandas as pd
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    import matplotlib.animation as animation
    from matplotlib.patches import Polygon, FancyBboxPatch
    from matplotlib.offsetbox import OffsetImage, AnnotationBbox
    import imageio_ffmpeg

    FPS = 30
    DURATION_SEC = 40
    TOTAL_FRAMES = FPS * DURATION_SEC

    COUNTRIES_ISO = {
        "United States": "us", "Russia / USSR": "ru", "Saudi Arabia": "sa", "Canada": "ca",
        "Iraq": "iq", "China": "cn", "Iran": "ir", "UAE": "ae",
        "Brazil": "br", "Kuwait": "kw", "Mexico": "mx", "Norway": "no",
        "Nigeria": "ng", "Venezuela": "ve", "United Kingdom": "gb", "Kazakhstan": "kz",
        "Libya": "ly", "Indonesia": "id"
    }

    START_YEAR = 1950.0
    END_YEAR = 2026.83
    TITLE_MAIN = "BLACK GOLD: OIL PRODUCTION"
    TITLE_SUB = "CRUDE OIL EXTRACTION IN MILLION BARRELS PER DAY (1950 - OCT 2026)"
    FINAL_OUTPUT = "global_oil_production_1950_2026_shorts.mp4"

    # Historical Crude Oil Production in Million Barrels per Day (Mb/d) — U.S. EIA & Energy Institute Statistical Review
    ANCHORS = {
        "United States":  {1950: 5.41, 1960: 7.04, 1970: 9.64, 1980: 8.60, 1990: 7.36, 2000: 5.82, 2010: 5.48, 2015: 9.43, 2020: 11.32, 2026: 13.40},
        "Russia / USSR":  {1950: 0.76, 1960: 2.96, 1970: 7.06, 1980: 12.03, 1988: 12.50, 1995: 6.17, 2000: 6.48, 2010: 10.27, 2020: 10.50, 2026: 9.80},
        "Saudi Arabia":   {1950: 0.55, 1960: 1.31, 1970: 3.80, 1980: 9.90, 1985: 3.39, 1990: 6.41, 2000: 8.40, 2010: 8.90, 2020: 9.21, 2026: 9.60},
        "Canada":         {1950: 0.08, 1960: 0.52, 1970: 1.26, 1980: 1.44, 1990: 1.55, 2000: 2.04, 2010: 2.86, 2020: 4.45, 2026: 5.15},
        "Iraq":           {1950: 0.14, 1960: 0.97, 1970: 1.55, 1979: 3.48, 1983: 1.00, 1990: 2.04, 1995: 0.56, 2000: 2.57, 2010: 2.40, 2020: 4.10, 2026: 4.45},
        "China":          {1950: 0.01, 1960: 0.10, 1970: 0.60, 1980: 2.11, 1990: 2.77, 2000: 3.25, 2010: 4.07, 2020: 3.90, 2026: 4.28},
        "Iran":           {1950: 0.66, 1953: 0.03, 1960: 1.07, 1970: 3.83, 1974: 6.02, 1980: 1.47, 1990: 3.10, 2000: 3.69, 2010: 4.08, 2020: 2.05, 2026: 3.45},
        "UAE":            {1950: 0.00, 1960: 0.00, 1965: 0.28, 1970: 0.78, 1980: 1.71, 1990: 2.12, 2000: 2.40, 2010: 2.57, 2020: 3.15, 2026: 3.35},
        "Brazil":         {1950: 0.01, 1960: 0.08, 1970: 0.17, 1980: 0.19, 1990: 0.65, 2000: 1.27, 2010: 2.06, 2020: 2.95, 2026: 3.55},
        "Kuwait":         {1950: 0.34, 1960: 1.69, 1970: 2.99, 1972: 3.28, 1980: 1.66, 1990: 1.18, 1991: 0.19, 2000: 2.08, 2010: 2.31, 2020: 2.45, 2026: 2.65},
        "Mexico":         {1950: 0.20, 1960: 0.27, 1970: 0.43, 1980: 1.94, 1990: 2.55, 2000: 3.01, 2004: 3.38, 2010: 2.62, 2020: 1.71, 2026: 1.85},
        "Norway":         {1950: 0.00, 1970: 0.00, 1975: 0.19, 1980: 0.53, 1990: 1.63, 2000: 3.22, 2010: 1.87, 2020: 1.72, 2026: 1.82},
        "Nigeria":        {1950: 0.00, 1960: 0.02, 1970: 1.08, 1980: 2.06, 1990: 1.81, 2000: 2.16, 2010: 2.46, 2020: 1.78, 2026: 1.52},
        "Venezuela":      {1950: 1.50, 1960: 2.85, 1970: 3.71, 1980: 2.17, 1990: 2.14, 2000: 3.16, 2010: 2.42, 2020: 0.55, 2026: 0.92},
        "United Kingdom": {1950: 0.01, 1960: 0.02, 1970: 0.02, 1976: 0.25, 1980: 1.62, 1985: 2.53, 1990: 1.82, 1999: 2.68, 2010: 1.23, 2020: 0.95, 2026: 0.68},
        "Kazakhstan":     {1950: 0.02, 1960: 0.03, 1970: 0.26, 1980: 0.37, 1990: 0.52, 2000: 0.72, 2010: 1.61, 2020: 1.76, 2026: 1.92},
        "Libya":          {1950: 0.00, 1960: 0.00, 1965: 1.22, 1970: 3.32, 1980: 1.79, 1990: 1.38, 2000: 1.41, 2010: 1.65, 2020: 0.40, 2026: 1.22},
        "Indonesia":      {1950: 0.13, 1960: 0.41, 1970: 0.85, 1980: 1.58, 1990: 1.46, 2000: 1.42, 2010: 0.95, 2020: 0.71, 2026: 0.62}
    }

    print(" -> Generating industrial beveled 3D flags for all countries...")
    flags = {country: create_industrial_flag(code, 80, 52, 3) for country, code in COUNTRIES_ISO.items()}

    print(" -> Synthesizing royalty-free soundtrack (Black Gold Industrial Bass - CC0 License)...")
    audio_path = os.path.join(TEMP_DIR, "black_gold_industrial.wav")
    license_lines = [
        "MUSIC LICENSE CERTIFICATE (CC0 1.0 Universal - Public Domain Dedication)",
        "=======================================================================",
        "Track Title: Black Gold Industrial Bass (Heavy Sub-Bass & Mechanical Percussion Score)",
        "License: Creative Commons Zero (CC0 1.0 Universal)",
        "Status: 100% Royalty-Free / Safe for YouTube Shorts, Instagram Reels, TikTok monetization.",
        "Permissions: Commercial and non-commercial use, modification, and distribution permitted without attribution."
    ]
    with open("MUSIC_LICENSE_CC0.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(license_lines) + "\n")

    sample_rate = 44100
    n_samples = sample_rate * DURATION_SEC
    t = np.linspace(0, DURATION_SEC, n_samples, endpoint=False)

    # Dark cinematic industrial progression: C minor -> Ab major -> Fm -> G7
    freqs_base = np.select(
        [(t % 10) < 2.5, (t % 10) < 5.0, (t % 10) < 7.5, (t % 10) >= 7.5],
        [65.41, 51.91, 43.65, 49.00]
    )

    # Heavy pumping oil-rig sub-bass groove (2 Hz slow mechanical pump)
    pump_lfo = 0.60 + 0.40 * np.sin(2 * math.pi * 2.0 * t)
    sub_bass = (0.26 * np.sin(2 * math.pi * freqs_base * t) + 0.10 * np.tanh(2.5 * np.sin(2 * math.pi * (freqs_base * 2.0) * t))) * pump_lfo

    # Dark brassy industrial drone pad
    drone_l = 0.12 * np.sin(2 * math.pi * (freqs_base * 3.0) * t + 0.4 * np.sin(2 * math.pi * 0.3 * t))
    drone_r = 0.12 * np.sin(2 * math.pi * (freqs_base * 4.0) * t + 0.8)

    # Metallic mechanical derrick tick every 0.5s (120 BPM quarter-note industrial clank)
    tick_phase = (t * 2.0) % 1.0
    tick_env = np.exp(-18.0 * tick_phase) * (1.0 - np.exp(-120.0 * tick_phase))
    metallic_tick = 0.09 * (np.sin(2 * math.pi * 440.0 * t) + 0.6 * np.sin(2 * math.pi * 710.0 * t)) * tick_env

    envelope = np.ones_like(t)
    fade_len = sample_rate * 2
    envelope[:fade_len] = np.linspace(0, 1, fade_len)
    envelope[-fade_len:] = np.linspace(1, 0, fade_len)

    stereo_left = np.clip((sub_bass + drone_l + metallic_tick) * envelope, -0.95, 0.95)
    stereo_right = np.clip((sub_bass + drone_r + metallic_tick * 0.85) * envelope, -0.95, 0.95)

    interleaved = np.empty((n_samples * 2,), dtype=np.int16)
    interleaved[0::2] = (stereo_left * 32767).astype(np.int16)
    interleaved[1::2] = (stereo_right * 32767).astype(np.int16)

    with wave.open(audio_path, "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(interleaved.tobytes())

    print(" -> Building 1950-2026 crude oil production matrix with smooth Hann-window rank transitions...")
    fine_years = np.linspace(START_YEAR, END_YEAR, TOTAL_FRAMES)
    val_dict = {}
    for country, anchors in ANCHORS.items():
        yrs = sorted(list(anchors.keys()))
        vals = [anchors[y] for y in yrs]
        val_dict[country] = np.interp(fine_years, yrs, vals)

    df_values = pd.DataFrame(val_dict, index=fine_years)
    df_values = df_values.where(df_values > 0.01, np.nan)

    df_deltas = df_values.pct_change(periods=15).fillna(0.0)
    df_deltas_smooth = df_deltas.rolling(window=20, min_periods=1, center=True).mean().fillna(0.0)

    df_ranks = df_values.rank(axis=1, method='first', ascending=True).fillna(0.0)
    win_size = 35
    hann_win = np.hanning(win_size)
    hann_win /= hann_win.sum()
    df_ranks_smooth = df_ranks.apply(
        lambda col: np.convolve(np.pad(col.values, (win_size // 2, win_size // 2), mode='edge'), hann_win, mode='valid')[:len(col)]
    )

    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    plt.rcParams['animation.ffmpeg_path'] = ffmpeg_exe

    print(f" -> Rendering 40-second beveled 3D HD 9:16 video ({TOTAL_FRAMES} frames at {FPS} FPS)...")
    BG_OUTER = '#090807'
    BG_PLOT = '#120f0d'

    fig = plt.figure(figsize=(9, 16), dpi=120)
    fig.patch.set_facecolor(BG_OUTER)

    # Viscous rising crude-amber droplets in background
    drop_ax = fig.add_axes([0, 0, 1, 1], frameon=False)
    drop_ax.set_xlim(0, 1)
    drop_ax.set_ylim(0, 1)
    drop_ax.set_xticks([])
    drop_ax.set_yticks([])

    np.random.seed(55)
    n_drops = 70
    base_px = np.random.uniform(0.04, 0.96, n_drops)
    base_py = np.random.uniform(0.04, 0.96, n_drops)
    base_ps = np.random.uniform(10, 48, n_drops)
    base_pa = np.random.uniform(0.06, 0.26, n_drops)
    drop_scatter = drop_ax.scatter(
        base_px, base_py, s=base_ps, color='#d97706', alpha=0.18, edgecolors='#f59e0b', linewidths=0.5
    )

    # Industrial Beveled Header Panel
    header_box = FancyBboxPatch(
        (0.04, 0.882), 0.92, 0.092,
        boxstyle="round,pad=0.01,rounding_size=0.014",
        transform=fig.transFigure,
        facecolor='#18130f', edgecolor='#d97706', linewidth=1.8, alpha=0.96, zorder=2
    )
    fig.patches.append(header_box)

    fig.text(
        0.5, 0.946, TITLE_MAIN,
        color='#fef3c7', fontsize=21.0, fontweight='bold', fontfamily='DejaVu Sans', ha='center', va='center', zorder=4
    )
    fig.text(
        0.5, 0.916, TITLE_SUB,
        color='#f59e0b', fontsize=9.5, fontweight='bold', fontfamily='DejaVu Sans Mono', ha='center', va='center', zorder=4
    )

    prog_bg = FancyBboxPatch(
        (0.10, 0.893), 0.80, 0.006,
        boxstyle="round,pad=0,rounding_size=0.001",
        transform=fig.transFigure,
        facecolor='#29211a', edgecolor='none', alpha=0.9, zorder=3
    )
    prog_fg = FancyBboxPatch(
        (0.10, 0.893), 0.01, 0.006,
        boxstyle="round,pad=0,rounding_size=0.001",
        transform=fig.transFigure,
        facecolor='#f59e0b', edgecolor='none', alpha=0.95, zorder=4
    )
    fig.patches.extend([prog_bg, prog_fg])

    ax = fig.add_axes([0.38, 0.06, 0.58, 0.79])

    top_n = 12
    max_rank = len(COUNTRIES_ISO)
    min_visible_rank = max_rank - top_n + 1.0

    ax_w_in = 0.58 * 9.0
    ax_h_in = 0.79 * 16.0
    bar_h = 0.55
    ry = bar_h * 0.12

    def update(frame_idx):
        ax.clear()
        ax.set_facecolor(BG_PLOT)

        progress = (frame_idx + 1) / float(TOTAL_FRAMES)
        prog_fg.set_width(max(0.01, 0.80 * progress))

        # Slow viscous upward rise of oil droplets + gentle size expansion
        cur_py = (base_py + frame_idx * 0.00055) % 1.0
        cur_px = (base_px + 0.004 * np.sin(frame_idx * 0.03 + np.arange(n_drops))) % 1.0
        drop_scatter.set_offsets(np.column_stack([cur_px, cur_py]))
        cur_sizes = base_ps * (0.85 + 0.25 * np.sin(frame_idx * 0.08 + np.arange(n_drops)))
        drop_scatter.set_sizes(cur_sizes)

        current_time = df_values.index[frame_idx]
        year_int = int(current_time)
        month_int = min(12, max(1, int((current_time - year_int) * 12) + 1))
        month_names = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
        date_str = f"{month_names[month_int - 1]} {year_int}"

        vals_row = df_values.iloc[frame_idx]
        ranks_row = df_ranks_smooth.iloc[frame_idx]
        deltas_row = df_deltas_smooth.iloc[frame_idx]

        visible = ranks_row[ranks_row >= min_visible_rank - 0.7].dropna()
        max_val = max(vals_row.max(), 2.0)

        x_max = max_val * 1.35
        y_min, y_max = min_visible_rank - 0.65, max_rank + 0.65
        ax.set_xlim(0, x_max)
        ax.set_ylim(y_min, y_max)

        ax.xaxis.grid(True, color='#2e251d', linestyle='--', linewidth=1.0, alpha=0.75, zorder=0)
        ax.set_axisbelow(True)

        rx = ry * (x_max / (y_max - y_min)) * (ax_h_in / ax_w_in) * 0.85
        dx_3d = max_val * 0.012
        dy_3d = 0.065
        flow_global = (frame_idx * 0.018) % 1.0

        for country, smooth_y in visible.items():
            val = vals_row[country]
            if pd.isna(val) or val <= 0:
                continue

            alpha = 1.0
            if smooth_y < min_visible_rank:
                alpha = max(0.0, min(1.0, (smooth_y - (min_visible_rank - 0.7)) / 0.7))

            norm_rank = np.clip((smooth_y - min_visible_rank) / max(1, top_n - 1), 0, 1)
            rank_num = max(1, min(top_n, int(round(max_rank - smooth_y + 1))))
            y0 = smooth_y - bar_h / 2.0
            d_rate = float(deltas_row[country])

            vis_val = max(val, max_val * 0.04)

            # 1. Heavy 3D Cast Shadow behind block
            shadow_verts = make_beveled_rect_polygon(
                dx_3d * 1.35, y0 - dy_3d * 1.45, vis_val, bar_h, rx, ry, n_arc=8
            )
            shadow_poly = Polygon(
                shadow_verts, closed=True, facecolor='#030201', alpha=0.88 * alpha, edgecolor='none', zorder=2
            )
            ax.add_patch(shadow_poly)

            # 2. 3D Extruded Bottom-Right Metallic Side Block
            side_color = '#451a03' if d_rate >= -0.015 else '#3f1d1d'
            side_verts = make_beveled_rect_polygon(
                dx_3d * 0.75, y0 - dy_3d * 0.75, vis_val, bar_h, rx, ry, n_arc=8
            )
            side_poly = Polygon(
                side_verts, closed=True, facecolor=side_color, edgecolor='#78350f',
                linewidth=0.8, alpha=0.95 * alpha, zorder=2.5
            )
            ax.add_patch(side_poly)

            # 3. Main Beveled Rectangular 3D Block with Restrained Copper-Amber Gradient
            bar_verts = make_beveled_rect_polygon(0, y0, vis_val, bar_h, rx, ry, n_arc=8)
            clip_poly = Polygon(bar_verts, closed=True, facecolor='none', edgecolor='none', zorder=3)
            ax.add_patch(clip_poly)

            tex = build_restrained_oil_3d_texture(
                norm_rank, d_rate, flow_phase=flow_global - norm_rank * 0.30, alpha=alpha
            )
            im = ax.imshow(
                tex, extent=[0, vis_val, y0, y0 + bar_h],
                aspect='auto', origin='lower', interpolation='bicubic', zorder=3.5
            )
            im.set_clip_path(clip_poly)

            # 4. Crisp 3D Metallic Rim Outline
            rim_color = '#fbbf24' if d_rate > 0.025 else '#d97706'
            rim_poly = Polygon(
                bar_verts, closed=True, facecolor='none',
                edgecolor=rim_color, linewidth=1.15, alpha=0.80 * alpha, zorder=4.5
            )
            ax.add_patch(rim_poly)

            # 5. Rank Badge
            rank_color = '#f59e0b' if rank_num <= 3 else '#78716c'
            ax.text(
                -0.62, smooth_y, f"#{rank_num:02d}",
                transform=ax.get_yaxis_transform(),
                color=rank_color, fontsize=10.5, fontweight='bold', fontfamily='DejaVu Sans Mono',
                va='center', ha='left', alpha=alpha, zorder=6, clip_on=False
            )

            # 6. Country Name
            ax.text(
                -0.165, smooth_y, country,
                transform=ax.get_yaxis_transform(),
                color='#fef3c7', fontsize=12.0, fontweight='bold', fontfamily='DejaVu Sans',
                va='center', ha='right', alpha=alpha, zorder=6, clip_on=False
            )

            # 7. Industrial Rectangular-Beveled Flag
            if country in flags:
                imagebox = OffsetImage(flags[country], zoom=0.44, alpha=alpha)
                ab = AnnotationBbox(
                    imagebox, (-0.078, smooth_y),
                    xycoords=('axes fraction', 'data'),
                    frameon=False,
                    box_alignment=(0.5, 0.5),
                    zorder=5,
                    annotation_clip=False
                )
                ax.add_artist(ab)

            # 8. Value Label in Mb/d
            if d_rate > 0.025:
                tag = " ▲"
                lbl_col = '#fde68a'
            elif d_rate < -0.015:
                tag = " ▼"
                lbl_col = '#fca5a5'
            else:
                tag = ""
                lbl_col = '#fcd34d'

            ax.text(
                vis_val + dx_3d + max_val * 0.018, smooth_y, f"{val:,.2f} Mb/d{tag}",
                color=lbl_col, fontsize=11.5, fontweight='bold', fontfamily='DejaVu Sans Mono',
                va='center', ha='left', alpha=alpha, zorder=6
            )

        ax.set_yticks([])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#d97706')
        ax.spines['left'].set_linewidth(1.6)
        ax.spines['bottom'].set_color('#44382c')
        ax.tick_params(axis='x', colors='#a8a29e', labelsize=9.5)
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f"{x:.0f}M"))

        # Industrial Beveled HUD Box in bottom-right corner
        hud_box = FancyBboxPatch(
            (0.48, 0.025), 0.48, 0.15,
            boxstyle="round,pad=0.015,rounding_size=0.016",
            transform=ax.transAxes,
            facecolor='#18130f', edgecolor='#d97706', linewidth=1.6, alpha=0.95, zorder=5
        )
        ax.add_patch(hud_box)

        ax.text(
            0.93, 0.125, f"{year_int}", transform=ax.transAxes,
            color='#fef3c7', fontsize=38, fontweight='bold', fontfamily='DejaVu Sans Mono',
            ha='right', va='center', zorder=6
        )
        ax.text(
            0.93, 0.075, f"{date_str}", transform=ax.transAxes,
            color='#f59e0b', fontsize=13.5, fontweight='bold', fontfamily='DejaVu Sans Mono',
            ha='right', va='center', zorder=6
        )
        total_mbd = float(vals_row.dropna().sum())
        ax.text(
            0.93, 0.043, f"GLOBAL OUTPUT: {total_mbd:,.1f} Mb/d", transform=ax.transAxes,
            color='#fcd34d', fontsize=8.8, fontweight='bold', fontfamily='DejaVu Sans Mono',
            ha='right', va='center', zorder=6
        )

        if frame_idx % 120 == 0 or frame_idx == TOTAL_FRAMES - 1:
            pct = int((frame_idx + 1) / TOTAL_FRAMES * 100)
            print(f"    Rendering progress: {pct}% ({frame_idx + 1}/{TOTAL_FRAMES} frames)")

    temp_video = os.path.join(TEMP_DIR, "silent_oil_video.mp4")
    writer = animation.FFMpegWriter(fps=FPS, codec='libx264', bitrate=5500, extra_args=['-pix_fmt', 'yuv420p'])
    anim = animation.FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=1000 / FPS, repeat=False)
    anim.save(temp_video, writer=writer)
    plt.close(fig)

    print(" -> Mixing audio track and encoding final MP4...")
    subprocess.check_call([
        ffmpeg_exe, "-y",
        "-i", temp_video,
        "-i", audio_path,
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        FINAL_OUTPUT
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f" -> SUCCESS! Final video saved as: {FINAL_OUTPUT}")


if __name__ == "__main__":
    if "--worker" in sys.argv:
        run_worker()
    else:
        run_bootstrap()
