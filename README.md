# 🛢️ Black Gold: Global Crude Oil Production (1950 – Oct 2026) | Beveled 3D Bar Chart Race
# 🛢️ Черное золото: Добыча нефти по странам (1950 – Окт 2026) | 3D-генератор видео (Bar Chart Race)

![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Format 9:16 MP4](https://img.shields.io/badge/Output-1080x1920%20MP4%20(30%20FPS)-d97706.svg)
![Audio CC0](https://img.shields.io/badge/Audio-CC0%201.0%20Public%20Domain-success.svg)

**[English](#english)** | **[Русский](#русский)**

---

<a name="english"></a>
## 🇬🇧 English

### Overview
An automated, self-contained Python pipeline that renders a **40-second vertical HD (9:16, 1080x1920, 30 FPS) MP4 video** with an industrial sub-bass soundtrack. It visualizes the historical evolution of **Crude Oil Production by Country (in Million Barrels per Day, Mb/d)** from **1950 to October 2026** based on U.S. Energy Information Administration (EIA) and Energy Institute Statistical Review data.

### Key Features
* **Black Gold & Burnished Bronze Palette (Restrained Gradient):** Deep petroleum-obsidian background (`#090807` / `#120f0d`) paired with solid, industrial copper-amber and dark bronze bars (`#78350f` -> `#b45309` -> `#d97706`) featuring a restrained, realistic metallic sheen.
* **Chamfered Rectangular 3D Blocks:** Every bar is constructed as a chiseled, semi-rectangular 3D ingot (`ry = 0.12`) with three distinct horizontal 3D facets (bright top bevel, flat-lit brushed front face, and dark bottom bevel), a sharp specular ridge line, and a 3D bottom-right extruded metallic block base.
* **Viscous Oil & Industrial Pressure Animations:**
  * **Rising Crude Droplets:** Translucent amber-gold oil droplets slowly rise and expand in the background.
  * **Viscous Flow & Extraction Indicators (`▲` / `▼`):** A slow pressure wave flows through each 3D block, while active production booms (`▲`) or sharp output cuts (`▼`) are highlighted in real time.
* **Royalty-Free Soundtrack (`CC0 1.0`):** Automatically synthesizes a 40-second stereo track (*"Black Gold Industrial Bass"* — heavy pumping oil-rig sub-bass, dark brassy drone pad, and mechanical derrick percussion ticks) and generates a `MUSIC_LICENSE_CC0.txt` certificate for safe monetization on YouTube Shorts, Instagram Reels, and TikTok.
* **Zero System Clutter (Auto-Venv & Self-Cleanup):** `run.py` automatically creates a temporary `.venv_oil_race` virtual environment, installs all required packages (including a portable `FFmpeg` binary via `imageio-ffmpeg`), renders the final `.mp4`, and completely removes the virtual environment and temporary files upon completion.

### Quick Start
1. Ensure **Python 3.8+** is installed on your machine.
2. Clone this repository or extract the project archive.
3. Run the generator with a single command:
   ```bash
   python run.py
   ```
   *(On macOS/Linux, you may use `python3 run.py`)*.

### Output Files
* `global_oil_production_1950_2026_shorts.mp4` — Final 40-second 1080x1920 vertical video with audio.
* `MUSIC_LICENSE_CC0.txt` — Public Domain (CC0 1.0) license certificate for the audio track.
* `YOUTUBE_DESCRIPTION.txt` — Ready-to-use title, description, data sources, and tags for social media publishing.

---

<a name="русский"></a>
## 🇷🇺 Русский

### Описание проекта
Полностью автономный генератор на Python, создающий **40-секундный вертикальный видеоролик высокой четкости (9:16, 1080x1920, 30 FPS) в формате `.mp4`** с индустриальным басовым саундтреком. Видео наглядно демонстрирует динамику **мировой добычи нефти по странам (в миллионах баррелей в сутки, Mb/d)** с **1950 по октябрь 2026 года** на основе исторических данных U.S. EIA и Energy Institute Statistical Review of World Energy.

### Ключевые особенности
* **Палитра «Черное золото и темная бронза» со сдержанным градиентом:** Глубокий нефтяной обсидианово-асфальтовый фон (`#090807` / `#120f0d`) в сочетании с массивными полосками цвета темного янтаря, меди и вороненой бронзы со сдержанным металлическим переходом.
* **Граненая прямоугольная 3D-геометрия (бруски со снятой фаской):** Вместо круглых капсул каждая полоска выполнена в виде массивного 3D-бруска с легким скосом углов (`ry = 0.12`), тремя продольными гранями освещения (светлая верхняя фаска, матовая центральная грань и темная нижняя фаска), четким ребром жесткости и выступающей 3D-подложкой справа-снизу.
* **Анимация нефтяного потока и давления:**
  * **Всплывающие капли нефти:** На заднем плане медленно поднимаются и плавно пульсируют полупрозрачные янтарные капли.
  * **Волна давления и индикаторы добычи (`▲` / `▼`):** Внутри каждого 3D-бруска движется плавная волна потока, а периоды резкого наращивания добычи (`▲`) или обвала на фоне войн/санкций (`▼`) подсвечиваются в реальном времени.
* **Лицензионно чистая музыка (`CC0 1.0`):** Скрипт процедурно синтезирует 40-секундную стереодорожку (*«Black Gold Industrial Bass»* — тяжелый пульсирующий саб-бас в ритме насосной качалки, темный индустриальный дрон-пэд и механический металлический бит) и создает сертификат `MUSIC_LICENSE_CC0.txt`.
* **Полная самоочистка (Auto-Venv & Cleanup):** При запуске `run.py` сам создает изолированную виртуальную среду `.venv_oil_race`, скачивает внутрь все библиотеки и портативный видеокодек `FFmpeg` (`imageio-ffmpeg`), собирает готовый `.mp4` и автоматически удаляет виртуальную среду и временные файлы после завершения.

### Быстрый запуск
1. Убедитесь, что у вас установлен **Python 3.8+**.
2. Склонируйте репозиторий или распакуйте архив проекта.
3. Запустите генерацию одной командой в терминале (PowerShell / Bash):
   ```bash
   python run.py
   ```
   *(На macOS / Linux может использоваться команда `python3 run.py`)*.

### Итоговые файлы после запуска
* `global_oil_production_1950_2026_shorts.mp4` — готовый 40-секундный вертикальный видеоролик со звуком.
* `MUSIC_LICENSE_CC0.txt` — сертификат свободной лицензии (CC0 1.0 Public Domain) на музыкальную дорожку.
* `YOUTUBE_DESCRIPTION.txt` — готовые заголовки, описание, источники и теги для загрузки на YouTube / Reels / TikTok.
