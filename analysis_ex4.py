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

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4), dpi=150)
for mass in [8, 100]:

    df_summary = read_summary_for(mass, metallicity)

    # age / luminosity of neutrino losses
    ax1.plot(df_summary["age"], df_summary["luminosity of neutrino losses"], label=f"{mass} M☉")
    ax1.set_xlabel("age (years)")
    ax1.set_ylabel("luminosity of neutrino losses (L☉)")
    ax1.set_xscale("log")
    ax1.set_yscale("log")

    # step number / luminosity of neutrino losses
    ax2.plot(
        df_summary["step number"], df_summary["luminosity of neutrino losses"], label=f"{mass} M☉"
    )
    ax2.set_xlabel("step number")
    ax2.set_ylabel("luminosity of neutrino losses (L☉)")
    ax2.set_xscale("log")
    ax2.set_yscale("log")


for ax in [ax1, ax2]:
    ax.legend()
    ax.grid()
fig.tight_layout()

# %% - NOT USED

metallicity = 0.02

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 3.5), dpi=150)
for mass in [8, 100]:

    df_step = get_df_for_step(mass, metallicity, 100)

    # radius / electron pressure
    ax1.plot(df_step["radius coordinate"], df_step["total pressure"], label=f"{mass} M☉")
    ax1.set_xlabel("radius (R☉)")
    ax1.set_ylabel("total pressure (N m⁻²)")
    ax1.set_xscale("log")
    ax1.set_yscale("log")

    # radius / electron pressure
    ax2.plot(
        df_step["radius coordinate"],
        df_step["electron pressure"] / df_step["total pressure"],
        label=f"{mass} M☉",
    )
    ax2.set_xlabel("radius (R☉)")
    ax2.set_ylabel("ratio of electron pressure")
    ax2.set_xscale("log")
    ax2.set_ylim((0, 1))
    # ax2.set_yscale("log")

    # radius / radiation pressure
    ax3.plot(
        df_step["radius coordinate"],
        df_step["radiation pressure"] / df_step["total pressure"],
        label=f"{mass} M☉",
    )
    ax3.set_xlabel("radius (R☉)")
    ax3.set_ylabel("ratio of radiation pressure")
    ax3.set_xscale("log")
    ax3.set_ylim((0, 1))
    # ax3.set_yscale("log")


for ax in [ax1, ax2, ax3]:
    ax.legend()
    ax.grid()
fig.tight_layout()

# %% - NOT USED

metallicity = 0.02

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4), dpi=150)
for mass in [8, 100]:

    df_step = get_df_for_step(mass, metallicity, 100)

    ion_pressure_diff = (
        df_step["total pressure"] - df_step["electron pressure"] - df_step["radiation pressure"]
    )

    # radius / electron pressure
    ax1.plot(
        df_step["radius coordinate"],
        ion_pressure_diff,  # / df_step["total pressure"],
        label=f"{mass} M☉",
    )
    ax1.set_xlabel("radius (R☉)")
    ax1.set_ylabel(r"$P - P_\text{electron} - P_\text{radiation}$")
    ax1.set_xscale("log")
    # ax1.set_ylim((0, 1))
    ax1.set_yscale("log")

    ion_pressure_calculated = (
        df_step["density"]
        * 1.38e-23
        * df_step["temperature"]
        / (df_step["mean molecular weight"] * 1.66e-27)
    )

    # radius / electron pressure
    ax2.plot(
        df_step["radius coordinate"],
        ion_pressure_calculated,  # / df_step["total pressure"],
        label=f"{mass} M☉",
    )
    ax2.set_xlabel("radius (R☉)")
    ax2.set_ylabel(r"$P_\text{ion}$")
    ax2.set_xscale("log")
    # ax2.set_ylim((0, 1))
    ax2.set_yscale("log")


for ax in [ax1, ax2]:
    ax.legend()
    ax.grid()
fig.tight_layout()


# %%

metallicity = 0.02

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 3.5), dpi=150)


for mass in [8, 100]:
    age = []
    total_pressure = []
    electron_pressure = []
    radiation_pressure = []

    df_summary = read_summary_for(mass, metallicity)
    for step in range(df_summary["step number"].iloc[-1]):
        df_step = get_df_for_step(mass, metallicity, step)
        age.append(df_summary["age"].iloc[step])
        total_pressure.append(df_step["total pressure"].iloc[-1])
        electron_pressure.append(df_step["electron pressure"].iloc[-1])
        radiation_pressure.append(df_step["radiation pressure"].iloc[-1])

    age = np.array(age) / 1e6
    total_pressure = np.array(total_pressure)
    electron_pressure = np.array(electron_pressure)
    radiation_pressure = np.array(radiation_pressure)

    # radius / electron pressure
    ax1.plot(age, total_pressure, label=f"{mass} M☉")
    ax1.set_xlabel("age (Myears)")
    ax1.set_ylabel("total pressure (N m⁻²)")
    ax1.set_xscale("log")
    ax1.set_yscale("log")

    # radius / electron pressure
    ax2.plot(
        age,
        electron_pressure / total_pressure,
        label=f"{mass} M☉",
    )
    ax2.set_xlabel("age (Myears)")
    ax2.set_ylabel("ratio of electron pressure")
    ax2.set_xscale("log")
    ax2.set_ylim((0, 1))
    # ax2.set_yscale("log")

    # radius / radiation pressure
    ax3.plot(
        age,
        radiation_pressure / total_pressure,
        label=f"{mass} M☉",
    )
    ax3.set_xlabel("age (Myears)")
    ax3.set_ylabel("ratio of radiation pressure")
    ax3.set_xscale("log")
    ax3.set_ylim((0, 1))
    # ax3.set_yscale("log")


for ax in [ax1, ax2, ax3]:
    ax.legend()
    ax.grid()
fig.tight_layout()

# %%

metallicity = 0.02

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.5), dpi=150)
for mass, ax in zip([8, 100], [ax1, ax2]):

    age = []
    total_pressure = []
    electron_pressure = []
    radiation_pressure = []
    density = []
    temperature = []
    molecular_weight = []

    df_summary = read_summary_for(mass, metallicity)
    for step in range(df_summary["step number"].iloc[-1]):
        df_step = get_df_for_step(mass, metallicity, step)
        age.append(df_summary["age"].iloc[step])
        total_pressure.append(df_step["total pressure"].iloc[-1])
        electron_pressure.append(df_step["electron pressure"].iloc[-1])
        radiation_pressure.append(df_step["radiation pressure"].iloc[-1])
        density.append(df_step["density"].iloc[-1])
        temperature.append(df_step["temperature"].iloc[-1])
        molecular_weight.append(df_step["mean molecular weight"].iloc[-1])

    age = np.array(age) / 1e6
    total_pressure = np.array(total_pressure)
    electron_pressure = np.array(electron_pressure)
    radiation_pressure = np.array(radiation_pressure)
    density = np.array(density)
    temperature = np.array(temperature)
    molecular_weight = np.array(molecular_weight)

    ion_pressure_diff = total_pressure - electron_pressure - radiation_pressure

    # radius / electron pressure
    ax.plot(
        age,
        ion_pressure_diff,  # / df_step["total pressure"],
        label=r"$P - P_\text{electron} - P_\text{radiation}$",
    )

    ion_pressure_calculated = density * 1.38e-23 * temperature / (molecular_weight * 1.66e-27)

    # radius / electron pressure
    ax.plot(
        age,
        ion_pressure_calculated,  # / df_step["total pressure"],
        label=r"$P_\text{ion}$",
    )
    ax.set_xlabel("age (Myears)")
    ax.set_ylabel(f"{mass} M☉")
    # ax.set_xscale("log")
    ax.set_yscale("log")


for ax in [ax1, ax2]:
    ax.legend()
    ax.grid()
fig.tight_layout()
