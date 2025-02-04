# %%

import pandas as pd
import matplotlib.pyplot as plt

# %%

df = pd.read_csv(
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

for feature in ["surface temperature", "luminosity", "central density", "central temperature"]:
    plt.figure(figsize=(8, 5), dpi=150)
    plt.plot(df.age, df[feature])
    plt.xlabel("age")
    plt.ylabel(feature)
    plt.show()
