import pandas as pd
import numpy as np
def load_data(file_path):
    #Se carga el archivo con los datos historicos
    return pd.read_csv(file_path)

def calculate_statistics(data, column):
    #Se calcula de media y la desviacion estandar
    mean = data[column].mean()
    std = data[column].std()
    return mean, std

def generate_synthetic_data(mean, std, size):
    #Generar datos sintéticos usando una distribución uniforme
    low = mean - std
    high = mean + std
    return np.random.uniform(low, high, size=size)

def save_data(data, file_path, decimals=2):
    #Guardar el dataframe en unarchivo csv
    data.to_csv(file_path, index=False, float_format=f'%.{decimals}f')
    print(f"Datos sintéticos guardados en {file_path}")