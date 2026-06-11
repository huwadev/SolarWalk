# ESSS Solar Walk Map 🌌

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

An interactive, highly precise, physics-based 3D/2D scale model of the Solar System laid out as a walk over Addis Ababa, Ethiopia, and beyond. This project is developed under the **[Ethiopian Space Science and Society (ESSS)](https://ethiosss.org)** (ኢ.ስ.ሳ.ሶ).

**GitHub Repository:** [https://github.com/huwadev/SolarWalk](https://github.com/huwadev/SolarWalk)
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

## 🌐 Hosting on a Live Website

Since this is a client-side static web application (HTML, CSS, JavaScript), hosting it on a live website is straightforward. 

### 1. Static Web Hosting Providers
You can deploy this directory to any static hosting provider. The folder contains all required static assets (HTML, JS, and the 3D models directory `Planet model`).
* **GitHub Pages**: Go to your repository settings -> **Pages** -> Under Build and deployment, choose the **main** branch -> Save. Your site will be live at `https://<your-username>.github.io/SolarWalk/ESSS%20Solar%20Map.html`.
* **Vercel / Netlify / Cloudflare Pages**: Connect your GitHub repository to these platforms, leave the build command empty (or none), and set the publish directory to `./`.

### 2. Standard Web Servers (Apache, Nginx, IIS)
Upload the entire project folder (including `ESSS Solar Map.html`, `translations.js`, and the `Planet model` folder) to your web server's public root directory (e.g., `public_html` or `/var/www/html/`).

### 3. Handling 3D Model MIME Types (.glb)
Because the app loads 3D planet models dynamically using `<model-viewer>`, some web servers (like Microsoft IIS or custom Apache/Nginx configurations) might fail to serve the `.glb` files if they do not recognize their MIME type, causing the planets to render in 2D fallback mode.

Ensure your server is configured with the correct MIME type for `.glb` files:
* **MIME Type**: `model/gltf-binary`
* **File Extension**: `.glb`

#### Config Snippets:

* **Apache (.htaccess)**
  ```apache
  AddType model/gltf-binary .glb
  ```

* **Nginx (mime.types)**
  ```nginx
  types {
      model/gltf-binary glb;
  }
  ```

* **IIS (web.config)**
  ```xml
  <configuration>
    <system.webServer>
      <staticContent>
        <mimeMap fileExtension=".glb" mimeType="model/gltf-binary" />
      </staticContent>
    </system.webServer>
  </configuration>
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

This project is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)**. 

[![CC BY-NC-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-nc-sa.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

To view a copy of this license, visit [https://creativecommons.org/licenses/by-nc-sa/4.0/](https://creativecommons.org/licenses/by-nc-sa/4.0/).
All maps, code, and configurations are Copyright (c) 2026 Ethiopian Space Science and Society (ESSS).
