import pandas as pd
import numpy as np

# Carga de archivos
customers = pd.read_csv('C:\\Users\\Usuario\\Downloads\\IDE-001-fintrust\\Data\\clientes.csv',header=None)
loans = pd.read_csv('C:\\Users\\Usuario\\Downloads\\IDE-001-fintrust\\Data\\creditos.csv',header=None)
installments = pd.read_csv('C:\\Users\\Usuario\\Downloads\\IDE-001-fintrust\\Data\\cuotas_programadas.csv',header=None)
payments = pd.read_csv('C:\\Users\\Usuario\\Downloads\\IDE-001-fintrust\\Data\\pagos_recibidos.csv',header=None)

# Limpieza de datos customers
customers = customers.dropna(axis=1, how='all') # Se eliminan columnas vacías
customers.columns = ['customer_id', 'full_name', 'city', 'segment',
                     'monthly_income', 'date'] # se asignan nombres a las columnas
customers = customers.replace(r"[()';]", "", regex=True) # se eliminan caracteres no deseados

# Limpieza de datos loans
loans = loans.dropna(axis=1, how='all') # Se eliminan columnas vacías
loans.columns = ['loan_id' , 'customer_id', 'origination_date', 'principal_amount',
                 'annual_rate', 'term_months', 'loan_status', 'product_type'] # se asignan nombres a las columnas
loans = loans.replace(r"[()';]", "", regex=True) # se eliminan caracteres no deseados
# Se evidencia que una fila del dataset de loans está mal formateada, por lo que se corrige manualmente
raw_row = loans.iloc[44, 0]
clean_row = raw_row.split(',')
loans.loc[44] = clean_row

# Limpieza de datos installments
installments = installments.dropna(axis=1, how='all') # Se eliminan columnas vacías
installments.columns = ['installment_id', 'loan_id', 'installment_number',
                        'due_date','principal_due','interest_due','installment_status'] # se asignan nombres a las columnas
installments = installments.replace(r"[()';]", "", regex=True) # se eliminan caracteres no deseados

# Limpieza de datos payments
payments = payments.dropna(axis=1, how='all') # Se eliminan columnas vacías
payments.columns = ['payment_id', 'loan_id', 'installment_id', 'payment_date',
                    'payment_amount', 'payment_channel','payment_status','loaded_at'] # se asignan nombres a las columnas
payments = payments.replace(r"[()';]", "", regex=True) # se eliminan caracteres no deseados
payments = payments.drop(columns=['loaded_at']) # se elimina la columna 'loaded_at'
payments['payment_channel'] = payments['payment_channel'].fillna('NOT_SPECIFIED') # Si se evidencia que no existe una forma de pago definida se rellena con No especificado

# Reglas de validación de integridad referencial

# Verificar si hay loan_id en pagos que no existen en la tabla loans
orphans_payments = payments[~payments['loan_id'].isin(loans['loan_id'])]
print(f"Pagos huérfanos encontrados: {len(orphans_payments)}")

# Verificar si hay loan_id en cuotas que no existen en la tabla loans
orphans_installments = installments[~installments['loan_id'].isin(loans['loan_id'])]
print(f"Cuotas huérfanas encontradas: {len(orphans_installments)}")

# Reporte de valores nulos y tipos de datos
for name, df in {"clientes": customers, "creditos": loans, "cuotas": installments, "pagos": payments}.items():
    print(f"--- Calidad en {name} ---")
    print(df.isnull().sum())
    
# Validación de consistencia: Pagos sin canal definido
pagos_sin_canal = payments[payments['payment_channel'].isna()]
print(f"Pagos con canal nulo: {len(pagos_sin_canal)}")

# Descarga de archivos limpios guardados en formato CSV en carpeta Data_set_clean
customers.to_csv('C:\\Users\\Usuario\\Downloads\\IDE-001-fintrust\\Data_set_clean\\clientes_clean.csv', index=False)
loans.to_csv('C:\\Users\\Usuario\\Downloads\\IDE-001-fintrust\\Data_set_clean\\creditos_clean.csv', index=False)
installments.to_csv('C:\\Users\\Usuario\\Downloads\\IDE-001-fintrust\\Data_set_clean\\cuotas_clean.csv', index=False)
payments.to_csv('C:\\Users\\Usuario\\Downloads\\IDE-001-fintrust\\Data_set_clean\\pagos_clean.csv', index=False)
