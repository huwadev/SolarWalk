# ESSS Solar Walk Map 🌌

An interactive, highly precise, physics-based 3D/2D scale model of the Solar System laid out as a walk over Addis Ababa, Ethiopia, and beyond. This project is developed under the **Ethiopian Space Science and Society (ESSS)** (ኢ.ስ.ሳ.ሶ).

---

## 🚀 Key Features

* **Universal Setup Wizard**: Drag the Sun to any point on the map (defaulting to the ESSS Office at AAU CTBE 5 Kilo) or search for cities/addresses globally. Select from various Sun diameter presets (from a 1.6 cm Marble to a 1 Meter Ball) or enter a custom size.
* **Physics-Based Keplerian Engine**: Planets and satellites orbit along true elliptical paths derived from their orbital periods and eccentricities, solving Kepler's equation in real-time.
* **Interactive 3D Leaflet Markers**: Sun, planets, and the Moon render as live, rotating 3D models directly on the map. Features a fallback to 2D CSS spheres when loaded as a local file (`file://`) under browser CORS restrictions.
* **Bilingual Support (አማርኛ & English)**: Fully localized UI controls, labels, and text. Planet names in Amharic use traditional Ethiopic terminology (*አጣርድ, ዝሁራ, መሬት, መሪህ, መሽተሪ, ማኅፈድ, ኡራኑስ, ኔፕቱን, ፕሉቶ*).
* **Cosmic Belts & Clouds**: Interactive glassmorphic regions for the Asteroid Belt, Kuiper Belt, and Oort Cloud, dynamically synchronizing visibility and scale checks.
* **Scale-Independent Zooming**: Click "Inner planets" or individual planets to instantly center and zoom the viewport to their exact orbital bounding boxes.
* **Bespoke Simulation Controls**: Time elapsed calendars tracking years, months, and days, with custom speed levels (e.g. 1 day/sec to 1 year/sec).
* **Global Navigation Inset Mini-Map**: Small, high-contrast visualizer displaying orbital positions, hover highlights, and drag-and-pan geographic shortcuts.

---

## 🛠️ How to Run Locally

Because the application uses WebGL/gltf models via Google's `<model-viewer>`, modern web browsers prevent loading files from local filesystems (`file://`) due to CORS security policies. 

To experience the full interactive 3D rendering, run a local HTTP web server in the project directory:

### Using Python (Easiest)
Run this command in your terminal/powershell:
```bash
python -m http.server 8000
```
Then open your browser and navigate to:
[http://localhost:8000/ESSS%20Solar%20Map.html](http://localhost:8000/ESSS%20Solar%20Map.html)

### Using Node.js / npm
```bash
npx serve
```

---

## 💡 Keyboard Shortcuts

* `[Space]` — Play / Pause orbital simulation
* `[R]` — Reset views (main and mini-map) centered on the Sun
* `[F]` — Frame all active orbits on the viewport
* `[0]` — Fly to the Sun
* `[1]` - `[9]` — Fly to Mercury (1) through Pluto (9) and open details popup
* `[Escape]` — Dismiss open popups, panels, or wizard

---

## 📄 License

This project is licensed under the **Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)**. 

To view a copy of this license, visit [https://creativecommons.org/licenses/by-sa/4.0/](https://creativecommons.org/licenses/by-sa/4.0/).
All maps, code, and configurations are Copyright (c) 2026 Ethiopian Space Science and Society (ESSS).
