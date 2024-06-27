#!/bin/sh
python manage.py load_opinions_nfs data/opinions.csv
echo "Opinions loaded."
python manage.py load_genotox data/genotox_studies.csv
echo "Genotox loaded."
python manage.py load_adme data/adme.csv
echo "ADME loaded."
python manage.py load_endpoint_studies data/endpoint_studies.csv
echo "Endpoint studies loaded."
python manage.py load_chemical_identities data/chemical_identities.csv
echo "Chemical identities loaded."
python manage.py load_organism_identities data/organism_identities.csv
echo "Organism identities loaded."
python manage.py load_nf_variants data/use.csv
echo "NF variants loaded."
python manage.py load_processes data/processes.csv
echo "Processes loaded."
python manage.py load_composition data/composition.csv
echo "Composition loaded."