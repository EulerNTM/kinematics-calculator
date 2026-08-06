<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Kinematics Calculator</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {
      font-family: -apple-system, Segoe UI, Arial, sans-serif;
      max-width: 700px;
      margin: 60px auto;
      padding: 0 20px;
      line-height: 1.6;
      color: #222;
    }
    h1 { margin-bottom: 0.2em; }
    .subtitle { color: #666; margin-top: 0; }
    .download-btn {
      display: inline-block;
      background: #2563eb;
      color: white;
      padding: 12px 24px;
      border-radius: 6px;
      text-decoration: none;
      font-weight: 600;
      margin: 20px 0;
    }
    .download-btn:hover { background: #1d4ed8; }
    code {
      background: #f3f4f6;
      padding: 2px 6px;
      border-radius: 4px;
    }
    ul { padding-left: 20px; }
  </style>
</head>
<body>
  <h1>Kinematics Calculator</h1>
  <p class="subtitle">Solve any 1D kinematic (SUVAT) equation — enter what you know, get what you don't.</p>

  <a class="download-btn" href="https://github.com/yourusername/kinematics-calculator/releases/latest">
    Download for Windows (.exe)
  </a>

  <h2>What it does</h2>
  <p>
    Enter any combination of known values — initial velocity, final velocity,
    acceleration, time, or displacement — and the calculator solves for whatever's
    missing using symbolic algebra (via <a href="https://www.sympy.org/">sympy</a>),
    rather than hardcoded formulas for each case.
  </p>

  <h2>Features</h2>
  <ul>
    <li>Works with any valid combination of known variables</li>
    <li>Defaults to <code>v0 = 0</code> (starting from rest) if not specified</li>
    <li>Flags inconsistent or underdetermined inputs instead of failing silently</li>
    <li>No installation required — just run the .exe</li>
  </ul>

  <h2>Source code</h2>
  <p>
    Full source is available on
    <a href="https://github.com/yourusername/kinematics-calculator">GitHub</a>.
    Built with Python, Tkinter, and sympy.
  </p>
</body>
</html>
