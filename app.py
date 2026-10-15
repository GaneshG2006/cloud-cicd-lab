
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cloud CI/CD | DevOps Dashboard</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }

        :root {
            --bg: #080d18;
            --panel: #101827;
            --border: #253249;
            --text: #eef4ff;
            --muted: #93a4bd;
            --green: #45e6a0;
            --blue: #70a5ff;
            --purple: #bd9bff;
        }

        body {
            font-family: Inter, "Segoe UI", Arial, sans-serif;
            background:
                radial-gradient(ellipse at 15% 0%, #172b4d 0%, transparent 42%),
                radial-gradient(ellipse at 90% 15%, #24183e 0%, transparent 35%),
                var(--bg);
            color: var(--text);
            min-height: 100vh;
            line-height: 1.6;
        }

        .container { width: min(1080px, 92%); margin: auto; }

        nav {
            height: 76px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid var(--border);
        }

        .brand { font-weight: 800; font-size: 19px; letter-spacing: -.5px; }
        .brand span { color: var(--green); }
        .nav-tag {
            color: var(--muted);
            border: 1px solid var(--border);
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 12px;
        }

        .hero { padding: 66px 0 38px; }
        .eyebrow {
            color: var(--green);
            text-transform: uppercase;
            font-size: 12px;
            letter-spacing: 2px;
            font-weight: 800;
            margin-bottom: 15px;
        }

        h1 {
            font-size: clamp(36px, 6vw, 58px);
            line-height: 1.1;
            letter-spacing: -2px;
            max-width: 760px;
        }

        h1 span {
            background: linear-gradient(90deg, var(--green), var(--blue));
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }

        .intro {
            max-width: 650px;
            color: var(--muted);
            font-size: 17px;
            margin-top: 20px;
        }

        .success {
            display: flex;
            align-items: center;
            gap: 14px;
            background: #102a27;
            border: 1px solid #22694f;
            border-radius: 14px;
            padding: 18px 20px;
            margin: 12px 0 30px;
        }

        .check {
            display: grid;
            place-items: center;
            width: 38px;
            height: 38px;
            flex-shrink: 0;
            background: #174b3b;
            color: var(--green);
            border-radius: 50%;
            font-size: 20px;
        }

        .success strong { display: block; }
        .success p { color: #a5cdbd; font-size: 13px; }

        .section-title { font-size: 19px; margin: 28px 0 16px; }

        .pipeline {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 14px;
        }

        .stage {
            position: relative;
            background: linear-gradient(145deg, #141f31, #0e1624);
            border: 1px solid var(--border);
            border-radius: 15px;
            padding: 22px 17px;
            min-width: 0;
        }

        .stage-icon {
            display: grid;
            place-items: center;
            width: 45px;
            height: 45px;
            border-radius: 12px;
            background: #1c304a;
            font-size: 22px;
            margin-bottom: 17px;
        }

        .stage:nth-child(2) .stage-icon { background: #292343; }
        .stage:nth-child(3) .stage-icon { background: #173c32; }
        .stage:nth-child(4) .stage-icon { background: #3a2b20; }

        .stage h3 { font-size: 15px; margin-bottom: 5px; }
        .stage p { color: var(--muted); font-size: 12px; min-height: 39px; }

        .stage-status {
            display: inline-block;
            margin-top: 17px;
            color: var(--green);
            font-size: 11px;
            font-weight: 700;
        }

        .stage-status::before { content: "● "; }

        .details {
            display: grid;
            grid-template-columns: 1.3fr 1fr;
            gap: 16px;
            margin-top: 25px;
        }

        .card {
            background: rgba(16, 24, 39, .86);
            border: 1px solid var(--border);
            border-radius: 15px;
            padding: 23px;
        }

        .card h2 { font-size: 16px; margin-bottom: 17px; }

        .info-row {
            display: flex;
            justify-content: space-between;
            gap: 15px;
            padding: 12px 0;
            border-bottom: 1px solid #202c40;
            font-size: 13px;
        }

        .info-row:last-child { border-bottom: 0; }
        .info-row span { color: var(--muted); }
        .info-row strong { text-align: right; font-weight: 600; }

        .live { color: var(--green) !important; }

        .note {
            color: var(--muted);
            font-size: 13px;
            margin-top: 12px;
        }

        footer {
            margin-top: 44px;
            border-top: 1px solid var(--border);
            padding: 24px 0 30px;
            display: flex;
            justify-content: space-between;
            gap: 15px;
            flex-wrap: wrap;
            color: var(--muted);
            font-size: 12px;
        }

        @media (max-width: 720px) {
            .pipeline { grid-template-columns: repeat(2, 1fr); }
            .details { grid-template-columns: 1fr; }
            .hero { padding-top: 45px; }
            h1 { letter-spacing: -1px; }
        }

        @media (max-width: 380px) {
            .pipeline { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <nav class="container">
        <div class="brand">CLOUD<span> / </span>CI·CD</div>
        <div class="nav-tag">EXPERIMENT 05 · DEVOPS</div>
    </nav>

    <main class="container">
        <section class="hero">
            <div class="eyebrow">● &nbsp; Continuous integration & delivery</div>
            <h1>From every commit<br>to <span>successful deployment.</span></h1>
            <p class="intro">
                A Flask application delivered through an automated CI/CD
                workflow using GitHub, Jenkins and Docker.
            </p>
        </section>

        <section class="success">
            <div class="check">✓</div>
            <div>
                <strong>Application is running</strong>
                <p>Flask is serving this dashboard from the deployed container.</p>
            </div>
        </section>

        <h2 class="section-title">Deployment pipeline</h2>

        <section class="pipeline">
            <article class="stage">
                <div class="stage-icon">⌘</div>
                <h3>01 · GitHub</h3>
                <p>Source code and version control</p>
                <div class="stage-status">Source configured</div>
            </article>

            <article class="stage">
                <div class="stage-icon">⚙</div>
                <h3>02 · Jenkins</h3>
                <p>Automated pipeline orchestration</p>
                <div class="stage-status">Pipeline configured</div>
            </article>

            <article class="stage">
                <div class="stage-icon">▣</div>
                <h3>03 · Docker</h3>
                <p>Build and run a container image</p>
                <div class="stage-status">Container running</div>
            </article>

            <article class="stage">
                <div class="stage-icon">↗</div>
                <h3>04 · Deploy</h3>
                <p>Serve the application on a local port</p>
                <div class="stage-status">App available</div>
            </article>
        </section>

        <section class="details">
            <div class="card">
                <h2>Deployment overview</h2>
                <div class="info-row">
                    <span>Application</span>
                    <strong>Cloud CI/CD Flask App</strong>
                </div>
                <div class="info-row">
                    <span>Framework</span>
                    <strong>Python · Flask</strong>
                </div>
                <div class="info-row">
                    <span>Build automation</span>
                    <strong>Jenkins Pipeline</strong>
                </div>
                <div class="info-row">
                    <span>Container runtime</span>
                    <strong>Docker</strong>
                </div>
                <div class="info-row">
                    <span>Environment</span>
                    <strong>Local development</strong>
                </div>
            </div>

            <div class="card">
                <h2>Service health</h2>
                <div class="info-row">
                    <span>Flask application</span>
                    <strong class="live">● Online</strong>
                </div>
                <div class="info-row">
                    <span>Health endpoint</span>
                    <strong><a href="/health" style="color:#70a5ff">/health ↗</a></strong>
                </div>
                <div class="info-row">
                    <span>Delivery method</span>
                    <strong>CI/CD workflow</strong>
                </div>
                <p class="note">
                    This dashboard is served by the running Flask application.
                    The pipeline and container status can be verified in Jenkins
                    and Docker.
                </p>
            </div>
        </section>
    </main>

    <footer class="container">
        <span>Cloud Computing & DevOps · Experiment 5</span>
        <span>Built with Flask · Delivered with Docker</span>
    </footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
