import math
import tkinter as tk

import sympy as sp


def is_valid_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def calculate1d():
    v, v0, a, t, d = sp.symbols('v v0 a t d', real=True)
    SYMS = {'v0': v0, 'v': v, 'a': a, 't': t, 'd': d}
    subscripts = {v0: "v₀"}
    EQS = [
        sp.Eq(v, v0 + a * t),
        sp.Eq(d, v0 * t + 1/2 * a * t**2),
        sp.Eq(v**2, v0**2 + 2 * a * d),
        sp.Eq(d, (v0+v)/2 * t),
    ]
    UNITS = {v0: "m/s", v: "m/s", a: "m/s²", t: "s", d: "m"}
    raw_values = {"v": entry1.get(), "v0": entry2.get(), "a": entry3.get(), "t": entry4.get(), "d": entry5.get()}
    for y in raw_values.values():
        if not is_valid_float(y) and y != "":
            result_label.config(text="You did not give valid inputs.")
            return
    knowns = {SYMS[name]: sp.nsimplify(float(val)) for name, val in raw_values.items() if val != ""}
    unknowns = [sym for name, sym in SYMS.items() if sym not in knowns]
    if not unknowns:
        result_label.config(text="There are no unknown variables.")
        return
    neweqs = []
    for eq in EQS:
        if eq.subs(knowns) != sp.true:
            neweqs.append(eq.subs(knowns))
    
    solutions = sp.solve(neweqs, unknowns, dict=True)
    
    if not solutions:
        result_label.config(text="No solutions found.")
        return
    all_results = []    
    for item in solutions:
        parts = []
        
        for sym, val in item.items():
            if val.free_symbols:
                error_variables = ", ".join(str(k) for k in unknowns)
                result_label.config(text=f"There is not enough information to solve for {error_variables}.")
                return
            else:
                if val.is_real is False:
                    continue
                val = round(float(val), 4)
                if subscripts.get(sym) != None:
                    parts.append(f"{subscripts[sym]} = {val} {UNITS[sym]}")
                else:
                    parts.append(f"{sym} = {val} {UNITS[sym]}")
        result_text = ", ".join(parts)
        all_results.append(result_text)
    result_label.config(text="Result(s):\n" + "\n".join(all_results))
        
def calculate2d():
    v, v0, θ, vx, v0x, ax, t, dx = sp.symbols('v v0 θ vx v0x ax t dx', real=True)
    vy, v0y, ay, dy = sp.symbols('vy v0y ay dy', real = True)
    SYMS = {'v': v, 'θ': θ, 'v0x': v0x, 'vx': vx, 'ax': ax, 't': t, 'dx': dx, 'vy': vy, 'v0y': v0y, 'ay': ay, 'dy': dy}
    subscripts = {v0x: "v₀ₓ", v0y: "v₀ᵧ", vx: "vₓ", vy: "vᵧ", ax: "aₓ", ay: "aᵧ", dx: "dₓ", dy: "dᵧ"}
    EQS = [
        sp.Eq(vx, v0x + ax * t),
        sp.Eq(dx, v0x * t + 1/2 * ax * t**2),
        sp.Eq(vx**2, v0x**2 + 2 * ax * dx),
        sp.Eq(dx, (v0x+vx)/2 * t),
        sp.Eq(vy, v0y + ay * t),
        sp.Eq(dy, v0y * t + 1/2 * ay * t**2),
        sp.Eq(vy**2, v0y**2 + 2 * ay * dy),
        sp.Eq(dy, (v0y+vy)/2 * t),
        sp.Eq(v, sp.sqrt(vx**2+vy**2)),
        sp.Eq(v0, sp.sqrt(v0x**2+v0y**2)),
        sp.Eq(θ, sp.atan2(vy, vx)),
    ]
    UNITS = {v: "m/s", θ: "°", v0x: "m/s", vx: "m/s", ax: "m/s²", t: "s", dx: "m", v0y: "m/s", vy: "m/s", ay: "m/s²", dy: "m"}
    raw_values = {"v": entry_v.get(), "θ": entry_theta.get(), "vx": entry_vx.get(), "v0x": entry_v0x.get(), "ax": entry_ax.get(), "t": entry_t.get(), "dx": entry_dx.get(), "v0y": entry_v0y.get(), "vy": entry_vy.get(), "ay": entry_ay.get(), "dy": entry_dy.get()}
    for z in raw_values.values():
        if not is_valid_float(z) and z != "":
            result_label_b.config(text="You did not give valid inputs.")
            return
    knowns = {}
    for name, val in raw_values.items():
        if val == "":
            continue
        num = float(val)
        if name == "θ":
            num = math.radians(num)
        knowns[SYMS[name]] = sp.nsimplify(num)
    unknowns = [sym for name, sym in SYMS.items() if sym not in knowns]
    if not unknowns:
        result_label_b.config(text="There are no unknown variables.")
        return
    neweqs = []
    for eq in EQS:
        if eq.subs(knowns) != sp.true:
            neweqs.append(eq.subs(knowns))
    
    solutions = sp.solve(neweqs, unknowns, dict=True)
    
    if not solutions:
        result_label_b.config(text="No solutions found.")
        return
    
    all_results = []
    for item in solutions:
        parts = []
        for sym, val in item.items():
            if val.free_symbols:
                error_variables = ", ".join(str(k) for k in unknowns)
                result_label_b.config(text=f"There is not enough information to solve for {error_variables}.")
                return
            else:
                if val.is_real is False:
                    continue
                val = float(val)
                if sym == θ:
                    val = math.degrees(val)
                val = round(val, 4)
                if subscripts.get(sym) != None:
                    parts.append(f"{subscripts[sym]} = {val} {UNITS[sym]}")
                else:
                    parts.append(f"{sym} = {val} {UNITS[sym]}")
        result_text = ", ".join(parts)
        all_results.append(result_text)
    result_label_b.config(text="Result(s):\n" + "\n".join(all_results))
                
root = tk.Tk()
root.title("Kinematics Calculator")

## Frame A

frame_a = tk.Frame(root)

tk.Label(frame_a, text="v:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=(5, 0))
entry1 = tk.Entry(frame_a, width=10)
entry1.grid(row=1, column=0, padx=(10, 5), pady=(0, 5))

tk.Label(frame_a, text="v₀:", font=("Arial", 12)).grid(row=0, column=1, padx=5, pady=(5, 0))
entry2 = tk.Entry(frame_a, width=10)
entry2.insert(0, "0")
entry2.grid(row=1, column=1, padx=5, pady=(0, 5))

tk.Label(frame_a, text="a:", font=("Arial", 12)).grid(row=0, column=2, padx=5, pady=(5, 0))
entry3 = tk.Entry(frame_a, width=10)
entry3.grid(row=1, column=2, padx=5, pady=(0, 5))

tk.Label(frame_a, text="t:", font=("Arial", 12)).grid(row=0, column=3, padx=5, pady=(5, 0))
entry4 = tk.Entry(frame_a, width=10)
entry4.grid(row=1, column=3, padx=5, pady=(0, 5))

tk.Label(frame_a, text="d:", font=("Arial", 12)).grid(row=0, column=4, padx=5, pady=(5, 0))
entry5 = tk.Entry(frame_a, width=10)
entry5.grid(row=1, column=4, padx=5, pady=(0, 5))

tk.Button(frame_a, text="Calculate", width=10, command=lambda: calculate1d()).grid(row=1, column=5, padx=5, pady=(0, 5))

result_label = tk.Label(frame_a, text="Result(s): ", font=("Arial", 12), wraplength=480)
result_label.grid(row=2, column=0, columnspan=6, pady=(0, 15), padx=(10, 0))


## Frame B

frame_b = tk.Frame(root)

# --- v and θ fields (row 0: labels, row 1: entries) ---
tk.Label(frame_b, text="v:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=(5, 0))
entry_v = tk.Entry(frame_b, width=10)
entry_v.grid(row=1, column=0, padx=(10, 5), pady=(0, 5))

tk.Label(frame_b, text="θ:", font=("Arial", 12)).grid(row=0, column=1, padx=5, pady=(5, 0))
entry_theta = tk.Entry(frame_b, width=10)
entry_theta.grid(row=1, column=1, padx=5, pady=(0, 5))

# --- x-axis fields (row 2: labels, row 3: entries) ---
tk.Label(frame_b, text="vₓ:", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=(5, 0))
entry_vx = tk.Entry(frame_b, width=10)
entry_vx.grid(row=3, column=0, padx=(10, 5), pady=(0, 5))

tk.Label(frame_b, text="v₀ₓ:", font=("Arial", 12)).grid(row=2, column=1, padx=5, pady=(5, 0))
entry_v0x = tk.Entry(frame_b, width=10)
entry_v0x.insert(0, "0")
entry_v0x.grid(row=3, column=1, padx=5, pady=(0, 5))

tk.Label(frame_b, text="aₓ:", font=("Arial", 12)).grid(row=2, column=2, padx=5, pady=(5, 0))
entry_ax = tk.Entry(frame_b, width=10)
entry_ax.grid(row=3, column=2, padx=5, pady=(0, 5))

tk.Label(frame_b, text="t:", font=("Arial", 12)).grid(row=2, column=3, padx=5, pady=(5, 0))
entry_t = tk.Entry(frame_b, width=10)
entry_t.grid(row=3, column=3, padx=5, pady=(0, 5))

tk.Label(frame_b, text="dₓ:", font=("Arial", 12)).grid(row=2, column=4, padx=5, pady=(5, 0))
entry_dx = tk.Entry(frame_b, width=10)
entry_dx.grid(row=3, column=4, padx=5, pady=(0, 5))

# --- y-axis fields (row 4: labels, row 5: entries) ---
tk.Label(frame_b, text="vᵧ:", font=("Arial", 12)).grid(row=4, column=0, padx=5, pady=(5, 0))
entry_vy = tk.Entry(frame_b, width=10)
entry_vy.grid(row=5, column=0, padx=(10, 5), pady=(0, 5))

tk.Label(frame_b, text="v₀ᵧ:", font=("Arial", 12)).grid(row=4, column=1, padx=5, pady=(5, 0))
entry_v0y = tk.Entry(frame_b, width=10)
entry_v0y.insert(0, "0")
entry_v0y.grid(row=5, column=1, padx=5, pady=(0, 5))

tk.Label(frame_b, text="aᵧ:", font=("Arial", 12)).grid(row=4, column=2, padx=5, pady=(5, 0))
entry_ay = tk.Entry(frame_b, width=10)
entry_ay.grid(row=5, column=2, padx=5, pady=(0, 5))

tk.Label(frame_b, text="dᵧ:", font=("Arial", 12)).grid(row=4, column=3, padx=5, pady=(5, 0))
entry_dy = tk.Entry(frame_b, width=10)
entry_dy.grid(row=5, column=3, padx=5, pady=(0, 5))

# --- Button (row 5, same row as the y-axis entries) ---
tk.Button(frame_b, text="Calculate", width=10, command=lambda: calculate2d()).grid(row=5, column=4, padx=5, pady=(0, 5))

# --- Result (row 6) ---
result_label_b = tk.Label(frame_b, text="Result(s): ", font=("Arial", 12), wraplength=480)
result_label_b.grid(row=6, column=0, columnspan=6, pady=(0, 15), padx=(10, 0))

def switch_frame(value):
    frame_a.pack_forget()
    frame_b.pack_forget()
    
    if value == "1D calculator":
        frame_a.pack()
    else:
        frame_b.pack()
        
    root.update_idletasks()
    root.geometry("")
        
selected = tk.StringVar(root)
selected.set("1D calculator")

dropdown = tk.OptionMenu(root, selected, "1D calculator", "2D calculator", command=switch_frame)
dropdown.pack(pady=10)

frame_a.pack()

root.mainloop()             
    
