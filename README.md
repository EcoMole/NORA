# Novel Foods Risk Assessment Data Modelling and Extraction (NORA) Project

## For Developers

### Local development

1. `mkdir Nora && cd Nora`
2. `git clone git@github.com:EcoMole/NORA.git`
3. `cd NORA`
4. create virtual environment `python -m venv venv`
5. Activate the virtual environment `source venv/bin/activate`
6. Install [poetry](https://python-poetry.org/docs/#installation)
7. Run `poetry install` to install dependencies
8. Create a `.env` file in the root directory and add variables from `.env.example`
9. Create PostgreSQL database
   ```shell
   psql -d postgres
   CREATE ROLE nora_user WITH LOGIN PASSWORD 'noraheslo' CREATEDB SUPERUSER;
   CREATE DATABASE nora_db WITH ENCODING='UTF8' OWNER=nora_user CONNECTION LIMIT=30;
   GRANT ALL PRIVILEGES ON DATABASE nora_db TO nora_user;
   \q
   ```
10. Run `python manage.py migrate` to apply migrations
11. Run `python manage.py createsuperuser` to create a superuser
12. Run `python manage.py runserver` to start the development server
13. Open `http://127.0.0.1:<port>/something-criptic/` in your browser to view the admin

## Introduction

The European Food Safety Authority (EFSA) awarded Ecomole, s.r.o. the contract titled "Novel foods Risk Assessment Data Modelling and Extraction" (Contract No: NP/EFSA/NIF/2023/03). This project aims to aid EFSA in enhancing risk analysis capabilities by improving the quality, interoperability, and usability of data related to novel foods (NF).

## Background

**Contractor**: EcoMole s.r.o.
**Awarding Body**: EFSA (European Food Safety Authority)

## Project Overview

The NORA project focuses on three primary objectives:

1. **Data Modelling**: Develop a comprehensive data model for the risk assessment of NF dossiers.
2. **Data Extraction**: Extract relevant data from existing EFSA opinions on novel food applications.
3. **Guideline for Data Entry**: Create guidelines for consistent future data entry, ensuring data quality and usability.

## Data and Methodologies

### Data Sources

The project utilizes publicly available novel food opinions published by EFSA, including safety assessments of various food sources such as mung bean protein, nicotinamide riboside chloride, and oil from Schizochytrium limacinum.

### Methodology

The project comprises several phases:

- **Data Modelling**: Developing a structured data model using existing frameworks like OpenFoodTox 2.0, IUCLID, and OECD Harmonised Templates.
- **Data Extraction**: Implementing methodologies for efficient data extraction from NF opinions.
- **Guideline Development**: Formulating comprehensive guidelines for data entry based on the developed data model.

### Tools and Technologies

- **Django & Django REST Framework**: For backend API development and database management.
- **Django Admin Interface**: This project includes a Django-admin interface to add, edit, and manage data within the database. The interface provides extensive searching, filtering, and ordering capabilities, making data management and exploration efficient.
- **Vue.js 3 & Vite**: Employed for efficient frontend development.
- **Vuetify**: Utilized for UI components in Vue.js applications.
- **Axios**: For making HTTP requests from the frontend.
- **JWT (JSON Web Tokens)**: For secure authentication mechanisms.
- **GraphQL**: Used for querying the database. The custom frontend interface built with Vue.js 3 enables flexible data querying using GraphQL, allowing users to apply filters based on any field in the database. Users can also fetch and structure the data from all fields in a format of their choosing, adding flexibility and customization to the data retrieval process.

## Results and Impact

Preliminary results demonstrate the effective translation of the OFT 2.0 design into the new NORA data model, aligning with the unique requirements of novel food assessments. This project is expected to significantly enhance the efficiency and accuracy of risk assessments for novel foods within EFSA.

## Documentation

Further documentation, including the Entity Relationship Diagram (ERD) and detailed project methodologies, is provided in the appendices.

- **Appendix A**: Initial ERD Draft

## License

This project is developed under the guidance of EFSA and adheres to its regulatory framework.
