# 🚀 FinTrust: Data Engineering Case Study

[![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white)](https://www.snowflake.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQL](https://img.shields.io/badge/SQL-Advanced-orange?style=for-the-badge)](https://en.wikipedia.org/wiki/SQL)

## 📋 1. Resumen de la Solución
Este proyecto automatiza la ingesta, limpieza y transformación de datos para la Fintech **FinTrust**. La solución convierte datos crudos de originación, pagos y cuotas en un **Data Mart Analítico** de alto rendimiento, optimizando la toma de decisiones sobre indicadores clave: **Originación, Recaudo y Mora**.

---

## 🏗️ 2. Arquitectura de Datos
Se implementó una estrategia **ELT (Extract, Load, Transform)** diseñada para escalabilidad:

* **🐍 Python (VS Code):** Orquestación y limpieza de datos (*Data Wrangling*) para asegurar la calidad en el origen.
* **❄️ Snowflake:** Data Warehouse principal. Elegido por su arquitectura de separación de cómputo y almacenamiento, ideal para cargas de trabajo financieras variables.
* **📊 Modelado:** Uso de **Vistas Analíticas (Virtualización)** para garantizar reportes en tiempo real y eficiencia en costos de almacenamiento.

---

## 📂 3. Estructura del Proyecto
```bash
├── 📁 python_scripts    # Scripts de limpieza y normalización de datos.
├── 📁 sql_scripts       # DDLs de tablas y DMLs para lógica de negocio.
└── 📁 data_quality      # Validaciones de integridad y coherencia financiera.
