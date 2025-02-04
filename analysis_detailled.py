# %%

import pandas as pd
import matplotlib.pyplot as plt

# %%

df_summary = pd.read_csv(
    "mass_8_metallicity_0.02_detailled/summary.txt",
    header=None,
    sep="\s+",
    names=[
        "step number",
        "age",
        "mass",
        "luminosity",
        "radius",
        "surface temperature",
        "central temperature",
        "central density",
        "central pressure",
        "central electron degeneracy parameter",
        "central hydrogen mass fraction",
        "central helium mass fraction",
        "central carbon mass fraction",
        "central nitrogen mass fraction",
        "central oxygen mass fraction",
        "dynamical timescale",
        "kelvin-helmholtz timescale",
        "nuclear timescale",
        "luminosity from PP chain",
        "luminosity from CNO cycle",
        "luminosity from triple-alpha reactions",
        "luminosity from metal burning",
        "luminosity of neutrino losses",
        "mass of helium core",
        "mass of carbon core",
        "mass of oxygen core",
        "radius of helium core",
        "radius of carbon core",
        "radius of oxygen core",
    ],
)

# %%

df_steps = []
for i in df_summary["step number"]:
    fname = f"structure_{i:05d}.txt"
    df_step = pd.read_csv(
        f"mass_8_metallicity_0.02_detailled/{fname}",
        header=None,
        sep="\s+",
        names=[
            "lagrangian mass coordinate",
            "radius coordinate",
            "luminosity",
            "total pressure",
            "density",
            "temperature",
            "specific internal energy",
            "specific entropy",
            "specific heat at constant pressure",
            "first adiabatic exponent",
            "adiabatic temperature gradient",
            "mean molecular weight",
            "electron number density",
            "electron pressure",
            "radiation pressure",
            "radiative temperature gradient",
            "material temperature gradient",
            "convective velocity",
            "rosseland mean opacity",
            "power per unit mass from all nuclear reactions, excluding neutrino losses",
            "power per unit mass from PP chain",
            "power per unit mass from CNO cycle",
            "power per unit mass from triple-alpha reaction",
            "power loss per unit mass in nuclear neutrinos",
            "power loss per unit mass in nuclear non-neutrinos",
            "power per unit mass from gravitational contraction" "hydrogen mass fraction",
            "hydrogen mass fraction",
            "molecular hydrogen mass fraction",
            "singly-ionized hydrogen mass fraction",
            "helium mass fraction",
            "singly-ionized helium mass fraction",
            "doubly-ionized helium mass fraction",
            "carbon mass fraction",
            "nitrogen mass fraction",
            "oxygen mass fraction",
            "electron degeneracy parameter",
        ],
    )
    df_steps.append(df_step)

# %%

step_number = 500
df_step = df_steps[step_number]
radius = df_step["radius coordinate"]
density = df_step["temperature"]

plt.figure(figsize=(8, 5), dpi=150)
plt.plot(radius, density)
plt.xlabel("radius")
plt.ylabel("temperature")
plt.xscale("log")
# plt.yscale("log")
plt.show()
