# ESSS Solar Walk Map 🌌

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

An interactive, highly precise, physics-based 3D/2D scale model of the Solar System laid out as a walk over Addis Ababa, Ethiopia, and beyond. This project is developed under the **[Ethiopian Space Science and Society (ESSS)](https://ethiosss.org)** (ኢ.ስ.ሳ.ሶ).

**GitHub Repository:** [https://github.com/huwadev/SolarWalk](https://github.com/huwadev/SolarWalk)
---

## 🚀 Key Features

* **Universal Setup Wizard**: Drag the Sun to any point on the map (defaulting to the ESSS Office at AAU CTBE 5 Kilo) or search for cities/addresses globally. Select from various Sun diameter presets (from a 1.6 cm Marble to a 1 Meter Ball) or enter a custom size.
* **Physics-Based Keplerian Engine**: Planets and satellites orbit along true J2000.0 Keplerian paths derived from official NASA JPL Mean Orbital Elements and their centennial rates of change. Real-world planetary locations are calculated analytically relative to the J2000.0 epoch and synchronized dynamically to the actual calendar date (defaulting to today's date).
* **Interactive 3D Leaflet Markers**: Sun, planets, and the Moon render as live, rotating 3D models directly on the map. Features a fallback to 2D CSS spheres when loaded as a local file (`file://`) under browser CORS restrictions.
* **Bilingual Support (አማርኛ & English)**: Fully localized UI controls, labels, and text. Planet names in Amharic use traditional Ethiopic terminology (*አጣርድ, ዝሁራ, መሬት, መሪህ, መሽተሪ, ማኅፈድ, ኡራኑስ, ኔፕቱን, ፕሉቶ*).
* **Cosmic Belts & Clouds**: Interactive glassmorphic regions for the Asteroid Belt, Kuiper Belt, and Oort Cloud, dynamically synchronizing visibility and scale checks.
* **Scale-Independent Zooming**: Click "Inner planets" or individual planets to instantly center and zoom the viewport to their exact orbital bounding boxes.
* **Bespoke Simulation Controls**: A dynamic calendar display showing standard Gregorian dates in English mode and traditional Ethiopian dates (e.g., *4 ሰኔ 2018*) in Amharic mode. Includes custom speed levels (0.1 days/sec to 1,000 days/sec) and a "Today" button to instantly sync the simulation time back to the real-world date.
* **Global Navigation Inset Mini-Map**: Small, high-contrast visualizer displaying orbital positions, hover highlights, and drag-and-pan geographic shortcuts.

---

## 💻 Tech Stack

This project is built using modern, lightweight, client-side technologies to deliver a fluid, native-like experience without backend overhead:

* **Core Structure & Styling**: HTML5 & Vanilla CSS3 (featuring glassmorphism, responsive grid layouts, custom variable-based dark/light themes, and keyframe animations).
* **Application Logic**: Vanilla JavaScript (ES6+ modular design, local storage preference caching, custom state management).
* **Mapping Engine**: [Leaflet.js](https://leafletjs.com/) (handles geographic coordinate projections, custom interactive overlays, and zoom/pan bounding calculations).
* **3D Visualizations**: Google's [`<model-viewer>`](https://modelviewer.dev/) (WebXR-ready component utilizing WebGL to stream and render interactive, rotating GLTF/GLB models dynamically).
* **Physics & Mathematics**: High-precision Keplerian Orbit Engine utilizing NASA JPL J2000.0 Mean Orbital Elements and centennial rates. Projects positions by solving Kepler's Equation ($M = E - e \sin E$) in the 3D orbital plane and applying coordinate rotation matrices to project planets onto the 2D ecliptic plane.

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

> [!NOTE]
> **HTTPS Requirement for GPS**: Modern web browsers require a **Secure Context (HTTPS)** or `localhost` to enable GPS Geolocation (`navigator.geolocation`). Live deployment domains must be served over HTTPS (enabled by default on GitHub Pages, Vercel, Netlify, and Cloudflare Pages).

### 1. Static Web Hosting Providers (Recommended)
You can deploy this directory directly to any static hosting provider. The repository contains all required static assets (HTML, JS, and the 3D models directory `Planet model`).

* **GitHub Pages**:
  1. Go to your repository settings -> **Pages**.
  2. Under **Build and deployment** -> **Source**, select **Deploy from a branch**.
  3. Under **Branch**, select `main` and `/ (root)` -> Click **Save**.
  4. Your site will be live at: `https://<your-username>.github.io/SolarWalk/ESSS%20Solar%20Map.html`
  *(Note: GitHub Pages automatically serves `.glb` 3D model files with correct MIME types out of the box).*
* **Vercel / Netlify / Cloudflare Pages**:
  1. Connect your GitHub repository (`huwadev/SolarWalk`) to the platform.
  2. Leave the build command empty (or none), and set the output/publish directory to `./`.
  3. Deployments automatically support HTTPS and `.glb` static asset streaming.

### 2. cPanel (Shared Web Hosting)
* **File Upload**: 
  1. Login to your cPanel dashboard and open **File Manager**.
  2. Navigate to your domain's document root (typically `public_html` or a subdomain folder).
  3. Upload the entire project directory structure (`ESSS Solar Map.html`, `translations.js`, `Planet model/`, etc.).
* **MIME & SSL Configuration**:
  * Apache/cPanel servers might block or serve `.glb` files as plain text by default. To fix this, create a file named `.htaccess` in your site's root directory:
    ```apache
    AddType model/gltf-binary .glb
    ```
  * Ensure SSL (Let's Encrypt / AutoSSL) is enabled on your cPanel domain so GPS location requests function properly.

### 3. Microsoft Azure
* **Azure Static Web Apps (Recommended)**:
  1. Create a **Static Web App** resource in the Azure Portal.
  2. Connect it to your GitHub repository (`huwadev/SolarWalk`).
  3. Under the build options, choose **Custom**:
     * **App location**: `/`
     * **Api location**: *(leave empty)*
     * **Output location**: `/` *(or leave empty)*
  4. Azure automatically provisions a GitHub Actions workflow that builds and deploys your files on every commit.
* **Azure App Service (Windows / IIS)**:
  * Windows IIS web servers block unknown file extensions (like `.glb`) by default.
  * A pre-configured `web.config` file is included in the root directory to handle `.glb` MIME mapping automatically:
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

### 4. Custom Apache / Nginx Web Servers
* **Apache**: Add the MIME type inside your site configuration or `.htaccess`:
  ```apache
  AddType model/gltf-binary .glb
  ```
* **Nginx**: Add `.glb` to your `mime.types` file or server block:
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

## 👥 Credits & Acknowledgements

* **Kirubel M.**: Full project engineering & orbital mechanics.
* **Lealem K. Alula**: Handcrafted 3D models.
* **Hibreselam D.**: Initial codebase & layout.
* **[Solar System Scope](https://www.solarsystemscope.com/textures/)**: Planet texture maps, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
* **Livia Giacomini**: Inspiration from "Space Walk: Walking the Solar System in Your City".

---

## 📄 License

This project is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)**. 

[![CC BY-NC-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-nc-sa.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

To view a copy of this license, visit [https://creativecommons.org/licenses/by-nc-sa/4.0/](https://creativecommons.org/licenses/by-nc-sa/4.0/).
All maps, code, and configurations are Copyright (c) 2026 Ethiopian Space Science and Society (ESSS).
