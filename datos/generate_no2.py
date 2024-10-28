import pandas as pd
from utils.synthetic_data_generator import load_data, calculate_statistics, generate_synthetic_data, save_data

#configuracion
file_path='data/data_no2.csv'
output_path = 'data_result/synthetic_data_no2.csv'
column_name = 'NO2'
u_synthetic_data = 600

# Cargar datos y calcular estadísticas
historical_data = load_data(file_path)
mean_co, std_co = calculate_statistics(historical_data, column_name)

# Generar datos sintéticos
synthetic_co = generate_synthetic_data(mean_co, std_co, u_synthetic_data)
synthetic_data = pd.DataFrame({column_name: synthetic_co})

# Guardar los datos sintéticos
save_data(synthetic_data, output_path)