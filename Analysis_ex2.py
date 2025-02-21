import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def readsummary(foldername):
    return pd.read_csv(
            f"{foldername}/summary.txt",
            header=None,
            sep=r"\s+",
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


def plot_features(variable_list, variable_names, xvalues, constant_value = 0.02, xaxis='mass',together_on_one_figure="False"):
    if xaxis == 'mass':
        xlabel = r"mass [$M_\mathrm{Sun}$]"
        print(f"Generating plots for constant metallicity {constant_value}")
    elif xaxis == 'metallicity':
        xlabel = "metallicity"
        print(f"Generating plots for constant mass {constant_value}")
    elif xaxis == 'age':
        xlabel = 'age [Mljn yrs?]'
    else:
        print("wdymmm")

    if together_on_one_figure == "True":
        for k,feature in enumerate(variable_list):
            #plt.figure(figsize=(8, 5), dpi=150)
            plt.plot(xvalues, feature,label=variable_names[k])
            plt.xlabel(xlabel)
            plt.ylabel(variable_names[k])
        #plt.xscale("log")
        plt.yscale("log")
        plt.legend()
        plt.show()
    else:
        for k,feature in enumerate(variable_list):
            #plt.figure(figsize=(8, 5), dpi=150)
            plt.scatter(xvalues, feature,label=variable_names[k])
            plt.xlabel(xlabel)
            plt.ylabel(variable_names[k])
            plt.legend()
            plt.show()



def get_summary_data(variable_names, foldername,iteration=1):
    variables = np.zeros(len(variable_names))
    df = readsummary(foldername)
    return [df[variable][iteration] for variable in variable_names]


def get_data_for_more_folders(variable_names, foldernames, iteration=1, xaxis="mass",plot='True'): #mass must always be the last of the variable names
    
    data = np.zeros((len(foldernames),len(variable_names)))
    
    for k,foldername in enumerate(foldernames):
        variables = get_summary_data(variable_names,f"Data ex2/{foldername}",iteration)
        data[k] = variables
    
    if xaxis == "mass":
        xvalues = data[:,-1]
        constant_value=0.02 #metallicity

    elif xaxis == "metallicity":
        xvalues = np.array([0.0001,0.0003,0.001,0.004,0.01,0.02,0.03]) #metallicities
        constant_value = data[1,-1,]

    if plot == 'True':
        plot_features(data[:,:-1].T,variable_names[:-1],xvalues,constant_value,xaxis)
        return data

    else:
        return data