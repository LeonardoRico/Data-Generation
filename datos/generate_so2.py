import pandas as pd
import numpy as np
from utils.synthetic_data_generator import load_data, calculate_statistics, generate_synthetic_data, save_data

#configuracion
file_path='data/data_so2.csv'
output_path = 'data_result/synthetic_data_so2.csv'
column_name = 'SO2'
u_synthetic_data = 600

# Cargar datos y calcular estadísticas
historical_data = load_data(file_path)
mean_co, std_co = calculate_statistics(historical_data, column_name)

#Se encuentran los valores más altos y bajos
low = historical_data['SO2'].min()
high = historical_data['SO2'].max()

# Generar datos sintéticos. Se usa un método diferente, 
# dado que no se tienen que limpiar los datos
synthetic_so2 = np.random.uniform(low, high, size=u_synthetic_data)
synthetic_data = pd.DataFrame({column_name: synthetic_so2})

# Guardar los datos sintéticos
save_data(synthetic_data, output_path)