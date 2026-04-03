#!/bin/bash
#
# A lancer dans le répertoire du projet
#

# Génération des clés
echo "Lancer ce script dans le répertoire du projet :"
echo "Les fichiers de clé .pem pourront alors être stockés dans le sous-répertoire certs"
mkdir -p certs
mkcert -install
mkcert -key-file certs/key.pem -cert-file certs/cert.pem localhost 127.0.0.1 ::1

# Lancement de Django avec les bons paramètres dans le répertoir ci-dessous
echo "Certificats générés. Lancez Django avec :"
echo "python manage.py runsslserver --certificate certs/cert.pem --key certs/key.pem"

