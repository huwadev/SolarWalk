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

## 💻 Tech Stack

This project is built using modern, lightweight, client-side technologies to deliver a fluid, native-like experience without backend overhead:

* **Core Structure & Styling**: HTML5 & Vanilla CSS3 (featuring glassmorphism, responsive grid layouts, custom variable-based dark/light themes, and keyframe animations).
* **Application Logic**: Vanilla JavaScript (ES6+ modular design, local storage preference caching, custom state management).
* **Mapping Engine**: [Leaflet.js](https://leafletjs.com/) (handles geographic coordinate projections, custom interactive overlays, and zoom/pan bounding calculations).
* **3D Visualizations**: Google's [`<model-viewer>`](https://modelviewer.dev/) (WebXR-ready component utilizing WebGL to stream and render interactive, rotating GLTF/GLB models dynamically).
* **Physics & Mathematics**: Live Keplerian Orbit Engine solving Kepler's Equation ($M = E - e \sin E$) in real-time to project high-precision planet positions along elliptical paths.

---

## 📋 Environment & Prerequisites

Since the ESSS Solar Walk Map is a **serverless, fully static client-side application**, it does not require database instances, environment variable secrets (`.env`), or server-side compilers.

### What you need:
1. **A Web Browser**: Any modern browser with WebGL enabled (Google Chrome, Mozilla Firefox, Microsoft Edge, or Apple Safari).
2. **A Local HTTP Server (For 3D Models)**: 
   > [!IMPORTANT]
   > Web browsers block loading 3D asset files (`.glb`) under direct filesystem URLs (`file://`) due to CORS security restrictions. You **must** run a lightweight local HTTP server or host it on a web server to see the interactive 3D rotating planet models. Otherwise, the app automatically falls back to 2D CSS planetary indicators.

---

## 🛠️ Step-by-Step Guide to Run Locally

Follow these steps to run the application on your computer:

### Step 1: Download the Codebase
Download or clone the files from this GitHub repository:
```bash
git clone https://github.com/huwadev/SolarWalk.git
cd SolarWalk
```

### Step 2: Launch a Local Server
Choose **one** of the methods below to serve the files locally:

#### Method A: Using Python (Recommended)
If you have Python installed, run this command in your project directory:
```bash
python -m http.server 8000
```

#### Method B: Using Node.js (npm)
If you have Node.js installed, run:
```bash
npx serve
```

#### Method C: Using Visual Studio Code
If you use VS Code, install the **Live Server** extension. Then, open the project folder in VS Code, right-click `ESSS Solar Map.html`, and select **Open with Live Server**.

### Step 3: Open in Browser
Once your server is running, open your web browser and navigate to:
* For Python/Node.js: [http://localhost:8000/ESSS%20Solar%20Map.html](http://localhost:8000/ESSS%20Solar%20Map.html)
* For Live Server: It will open automatically (usually on port 5500).

---

## 🌐 Hosting on a Live Website

Since this is a client-side static web application (HTML, CSS, JavaScript), hosting it on a live website is straightforward. 

### 1. Static Web Hosting Providers
You can deploy this directory to any static hosting provider. The folder contains all required static assets (HTML, JS, and the 3D models directory `Planet model`).
* **GitHub Pages**: Go to your repository settings -> **Pages** -> Under Build and deployment, choose the **main** branch -> Save. Your site will be live at `https://<your-username>.github.io/SolarWalk/ESSS%20Solar%20Map.html`.
* **Vercel / Netlify / Cloudflare Pages**: Connect your GitHub repository to these platforms, leave the build command empty (or none), and set the publish directory to `./`.

### 2. cPanel (Shared Web Hosting)
* **File Upload**: 
  1. Login to your cPanel dashboard and open **File Manager**.
  2. Navigate to your domain's document root (typically `public_html` or a subdomain folder).
  3. Upload the entire project directory structure (`ESSS Solar Map.html`, `translations.js`, and the `Planet model` folder).
* **MIME Configuration**:
  * By default, many cPanel/Apache setups serve `.glb` files as plain text or block them. To fix this, create a file named `.htaccess` in the same directory and add:
    ```apache
    AddType model/gltf-binary .glb
    ```
  * Alternatively, search for the **MIME Types** tool in cPanel, and add a new user-defined MIME type with `model/gltf-binary` as the Type and `glb` as the Extension.

### 3. Microsoft Azure
* **Azure Static Web Apps (Recommended)**:
  1. Create a **Static Web App** resource in the Azure Portal.
  2. Connect it to your GitHub repository (`huwadev/SolarWalk`).
  3. Under the build options, choose **Custom**:
     * **App location**: `/`
     * **Api location**: (leave empty)
     * **Output location**: `/` (or leave empty)
  4. Azure will automatically provision a GitHub Actions workflow that builds and deploys your files on every push.
* **Azure App Service (Windows/IIS)**:
  * When hosting on a Windows-based Azure App Service, the IIS web server blocks files with unconfigured extensions (like `.glb`) by default.
  * To fix this, a custom configuration file named `web.config` is included in the project root containing:
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <configuration>
      <system.webServer>
        <staticContent>
          <remove fileExtension=".glb" />
          <mimeMap fileExtension=".glb" mimeType="model/gltf-binary" />
        </staticContent>
      </system.webServer>
    </configuration>
    ```

### 4. Other Standard Web Servers
* **Apache**: Enable the mime module and configure `.glb` types inside your server configuration or a local `.htaccess` file:
  ```apache
  AddType model/gltf-binary .glb
  ```
* **Nginx**: Define the MIME type inside your `mime.types` file or local block:
  ```nginx
  types {
      model/gltf-binary glb;
  }
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

## 👥 Credits & Acknowledgement

We would like to express our gratitude to the contributors of this project:
* **Lealem K. Alula**: Handcrafted and configured the beautiful 3D planetary models (`.glb` assets).
* **Hibreselam D.**: Created the initial 2D project codebase and conceptual layout.
* **Kirubel M.**: Engineered the entire physics engine, bilingual system, orbital mechanics, interface systems, and integration.

---

## 📄 License

This project is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)**. 

[![CC BY-NC-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-nc-sa.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

To view a copy of this license, visit [https://creativecommons.org/licenses/by-nc-sa/4.0/](https://creativecommons.org/licenses/by-nc-sa/4.0/).
All maps, code, and configurations are Copyright (c) 2026 Ethiopian Space Science and Society (ESSS).
