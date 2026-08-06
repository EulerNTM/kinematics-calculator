import tkinter as tk

import sympy as sp


def is_valid_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def calculate():
    v, v0, a, t, d = sp.symbols('v v0 a t d', real=True)
    SYMS = {'v0': v0, 'v': v, 'a': a, 't': t, 'd': d}
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
                parts.append(f"{sym} = {val} {UNITS[sym]}")
        result_text = ", ".join(parts)
        result_label.config(text=f"Result: {result_text}")
                
root = tk.Tk()
root.title("Kinematics Calculator")
root.geometry("480x100")

tk.Label(root, text="v:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=(5, 0))
entry1 = tk.Entry(root, width=10)
entry1.grid(row=1, column=0, padx=(10,5), pady=(0, 5))

tk.Label(root, text="v0:", font=("Arial", 12)).grid(row=0, column=1, padx=5, pady=(5, 0))
entry2 = tk.Entry(root, width=10)
entry2.insert(0, "0")
entry2.grid(row=1, column=1, padx=5, pady=(0, 5))

tk.Label(root, text="a:", font=("Arial", 12)).grid(row=0, column=2, padx=5, pady=(5, 0))
entry3 = tk.Entry(root, width=10)
entry3.grid(row=1, column=2, padx=5, pady=(0, 5))

tk.Label(root, text="t:", font=("Arial", 12)).grid(row=0, column=3, padx=5, pady=(5, 0))
entry4 = tk.Entry(root, width=10)
entry4.grid(row=1, column=3, padx=5, pady=(0, 5))

tk.Label(root, text="d:", font=("Arial", 12)).grid(row=0, column=4, padx=5, pady=(5, 0))
entry5 = tk.Entry(root, width=10)
entry5.grid(row=1, column=4, padx=5, pady=(0, 5))

tk.Button(root, text="Calculate", width=10, command=lambda: calculate()).grid(row=1, column=5, padx=5, pady=(0,5))

result_label = tk.Label(root, text="Result: ", font=("Arial", 12), wraplength=480, anchor="w")
result_label.grid(row=2, column=0, columnspan=6, pady=(0,5), padx=(10,0), sticky="ew")

root.mainloop()             
    
