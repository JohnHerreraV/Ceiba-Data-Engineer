📄 Decisiones Técnicas y Arquitectura - Caso FinTrust
Este documento detalla las justificaciones arquitectónicas y técnicas adoptadas para la resolución del caso práctico de ingeniería de datos.

1. Arquitectura de la Solución
Se ha optado por una arquitectura ELT (Extract, Load, Transform) sobre Snowflake, complementada con orquestación en Python.

Por qué ELT y no ETL: En un entorno moderno de Data Warehousing, es más eficiente cargar los datos con transformaciones mínimas (limpieza básica en Python) y aprovechar la potencia de cómputo elástica de Snowflake para el procesamiento pesado mediante SQL. Esto permite una mayor trazabilidad de los datos crudos y reduce la carga en los sistemas de origen.

Virtualización de Datos (Vistas): En lugar de crear múltiples tablas físicas que incrementen los costos de almacenamiento y la complejidad de los pipelines de actualización, se implementaron Vistas Analíticas. Esto garantiza que el área financiera consulte siempre datos en tiempo real (Real-time analytics) con una latencia de procesamiento cercana a cero.

2. Decisiones de Implementación
SQL (Snowflake)
Uso de CTEs (Common Table Expressions): Se priorizó la legibilidad y el mantenimiento. El uso de CTEs permite aislar las lógicas de agregación de pagos y cuotas antes de unirlas a la dimensión de créditos, facilitando el debugging técnico.

Lógica de Mora Dinámica: La mora no se extrae como un campo estático, sino que se calcula comparando el due_date contra el estado real de los pagos (payment_status). Esto evita inconsistencias si un pago se reversa o se confirma tarde.

Centralización de Reglas de Negocio: Al encapsular la lógica en la vista ANALYSIS_LOAN_PERFORMANCE, aseguramos que métricas como el "Outstanding Balance" sean consistentes en todos los tableros de BI (Single Source of Truth).

Python
Procesamiento y Exportación: Se utilizó Python para realizar la limpieza de los datos (manejo de nulos, consistencia de tipos y formatos de fecha). Una vez limpios, los DataFrames se exportaron a formato CSV.

Estrategia de Carga: Dado que la infraestructura de tablas ya había sido desplegada en Snowflake mediante scripts DDL, se optó por una carga semi-asistida utilizando la funcionalidad "Add Data" de Snowflake.

Justificación: Esta decisión se tomó para priorizar la velocidad de carga y asegurar la integridad de los datos procesados, garantizando que el esquema de destino (ya definido) 

3. Supuestos del Proyecto
Para el desarrollo de esta prueba, se asumieron las siguientes condiciones:

Estado "CONFIRMED": Solo los registros en la tabla de pagos con estado CONFIRMED afectan el saldo pendiente del crédito. Los pagos pendientes o fallidos se ignoran para el cálculo de recaudo real.

Snapshot de Datos: Los datos cargados representan el estado actual del negocio. En un entorno productivo, se asumiría una carga incremental diaria.

4. Riesgos Identificados y Mitigación
Integridad de Datos en Origen: Existe el riesgo de recibir pagos (payments) asociados a créditos (loans) inexistentes.

Mitigación: Se crearon scripts de Data Quality para detectar "pagos huérfanos" y asegurar que la integridad referencial se mantenga a nivel lógico.

Crecimiento del Volumen de Datos: El uso de vistas puede volverse lento si las tablas llegan a millones de registros.

Mitigación: Se diseñó la estructura para que sea fácilmente convertible a Tablas Dinámicas o Materialized Views en el futuro sin cambiar la lógica de negocio.

Seguridad: El manejo de credenciales en scripts de Python.

Mitigación: Se recomienda para producción el uso de Secret Managers o variables de entorno, evitando el hardcoding de contraseñas.

Notas de Autoría (Uso de IA)
Para este proyecto se utilizó asistencia de IA (Gemini) bajo una modalidad de Pair Programming. La IA apoyó en:

La optimización de las consultas SQL para mejorar el rendimiento.

La estructuración de la documentación técnica para asegurar claridad y profesionalismo.