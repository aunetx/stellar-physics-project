# %%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%


def read_summary_for(mass, metallicity):
    return pd.read_csv(
        f"Data ex1/mass_{mass}_metallicity_{metallicity}_detailled/summary.txt",
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


def get_df_for_step(mass, metallicity, step):
    return pd.read_csv(
        f"Data ex1/mass_{mass}_metallicity_{metallicity}_detailled/structure_{step:05d}.txt",
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
            "power per unit mass from gravitational contraction",
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


# %%

metallicity = 0.02

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 7), dpi=150, sharex=True)
for mass in [8, 100]:

    df_summary = read_summary_for(mass, metallicity)
    relative_age = df_summary["age"] / df_summary["age"].iloc[-1]

    # age / surface temperature
    ax1.plot(relative_age, 10 ** df_summary["surface temperature"], label=f"{mass} M☉")
    ax1.set_ylabel("surface temperature (K)")
    ax1.set_yscale("log")

    # age / luminosity
    ax2.plot(relative_age, 10 ** df_summary["luminosity"], label=f"{mass} M☉")
    ax2.set_ylabel("luminosity (L☉)")
    ax2.set_yscale("log")

    # age / central density
    ax3.plot(relative_age, 10 ** df_summary["central density"], label=f"{mass} M☉")
    ax3.set_xlabel("relative age (age / maximum age)")
    ax3.set_ylabel("central density (kg/m³)")
    ax3.set_yscale("log")

    # age / central temperature
    ax4.plot(relative_age, 10 ** df_summary["central temperature"], label=f"{mass} M☉")
    ax4.set_xlabel("relative age (age / maximum age)")
    ax4.set_ylabel("central temperature (K)")
    ax4.set_yscale("log")

for ax in [ax1, ax2, ax3, ax4]:
    ax.legend()
    ax.grid()
fig.tight_layout()


# %%

metallicity = 0.02

fig, ax = plt.subplots(1, figsize=(4, 4), dpi=150)

for mass in [8, 100]:
    df_summary = read_summary_for(mass, metallicity)
    relative_age = df_summary["age"] / df_summary["age"].iloc[-1]

    # age / radius
    ax.plot(relative_age, 10 ** df_summary["radius"], label=f"{mass} M☉")
    ax.set_xlabel("relative age (age / maximum age)")
    ax.set_ylabel("radius (R☉)")
    ax.set_yscale("log")

ax.legend()
ax.grid()
fig.tight_layout()

# %%


metallicity = 0.02
for mass, steps in zip(
    [8, 100],
    [
        [
            50,  # main sequence
            700,  # red supergiant
            1150,  # supernovae
        ],
        [
            80,  # main sequence
            500,  # red supergiant
            760,  # supernovae
        ],
    ],
):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 5.5), dpi=150, sharex=True)

    for step in steps:
        age = read_summary_for(mass, 0.02)["age"].iloc[step]
        age_myr = np.round(age / 1e6, 2)

        df_step = get_df_for_step(mass, metallicity, step)
        radius = df_step["radius coordinate"]

        # radius / density
        ax1.plot(
            radius,
            df_step["density"],
            label=f"{age_myr} Myears",
        )
        ax1.set_ylabel("density (kg/m³)")
        ax1.set_xscale("log")
        ax1.set_yscale("log")

        # radius / temperature
        ax2.plot(
            radius,
            df_step["temperature"],
            label=f"{age_myr} Myears",
        )
        ax2.set_ylabel("temperature (K)")
        ax2.set_xscale("log")
        ax2.set_yscale("log")

        # radius / hydrogen mass fraction
        ax3.plot(
            radius,
            df_step["hydrogen mass fraction"],
            label=f"{age_myr} Myears",
        )
        ax3.set_xlabel("radius (R☉)")
        ax3.set_ylabel("hydrogen mass fraction")
        ax3.set_xscale("log")
        ax3.set_ylim((0, 1))

        # radius / luminosity
        ax4.plot(
            radius,
            df_step["luminosity"],
            label=f"{age_myr} Myears",
        )
        ax4.set_xlabel("radius (R☉)")
        ax4.set_ylabel("luminosity (L☉)")
        ax4.set_xscale("log")

    for ax in [ax1, ax2, ax3, ax4]:
        ax.legend()
        ax.grid()
    fig.tight_layout()
