1. Resumen de la Solución
Este proyecto automatiza la ingesta, limpieza y transformación de datos para la Fintech FinTrust. La solución transforma datos crudos de originación, pagos y cuotas en un Data Mart Analítico listo para el consumo de negocio (BI), eliminando el procesamiento manual y reduciendo la latencia de los indicadores clave (Originación, Recaudo y Mora).

2. Arquitectura de Datos
Se implementó una estrategia ELT (Extract, Load, Transform) utilizando:

Visual Code (Python): Orquestación inicial y limpieza de datos (Data Wrangling).

Snowflake: Data Warehouse principal. Se eligió Snowflake por su capacidad de escalabilidad elástica y separación de cómputo/almacenamiento, permitiendo un procesamiento eficiente de reglas de negocio financieras.

Modelado: Se optó por una estructura de Vistas Analíticas (Virtualización de Datos) para garantizar que los reportes siempre reflejen el dato más reciente sin incurrir en costos de almacenamiento redundante.

3. Componentes del Proyecto
/python_scripts: Limpieza de datos.

/sql_scripts: DDLs para la creación de tablas y DMLs para las vistas de negocio.

/data_quality: Consultas de validación de integridad referencial y coherencia financiera.

4. Lógica de Negocio Implementada
Se desarrolló integración: Consolidación de Loans, Customers, Installments y Payments.

Cálculo de Mora: Lógica avanzada en SQL para identificar cuotas vencidas comparando due_date vs payment_status en tiempo real.

Data Marts: * Originación por Cohorte: Análisis temporal de colocación de crédito.

Calidad de Cartera: Estado de recuperación y balance pendiente por segmento.

5. Decisiones Técnicas y Justificación
¿Por qué Snowflake en lugar de BigQuery? Para demostrar versatilidad tecnológica. Snowflake permite un manejo de tipos de datos NUMBER y TIMESTAMP altamente preciso, crítico para aplicaciones fintech.

Validaciones de Calidad (DQ): Se incluyeron checks de "pagos huérfanos" y "unicidad de créditos" para asegurar que los KPIs de negocio no presenten duplicidad.

Uso de IA: Se utilizó asistencia de LLM (Gemini) para optimizar la estructura de las consultas SQL (uso de CTEs) y refinar la documentación técnica, aumentando la productividad del desarrollo.

6. Instrucciones de Ejecución
Ejecutar el script SQL de creación de tablas en Snowflake.

Correr el script de Python para cargar los archivos CSV limpios.

Consultar la vista ANALYSIS_LOAN_PERFORMANCE para verificar los resultados.