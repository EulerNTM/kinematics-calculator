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
