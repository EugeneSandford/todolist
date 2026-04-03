# Todolist

# objectifs du projet
- Créer une application de gestion des taches
- Les taches sont liées aux utilisateurs


## Configuration HTTPS locale
Utilisation de mkcert sans django-sslserver.
Les raisons : 
- Une expérience de développement plus proche de la production.
- Éviter les avertissements de certificat dans le navigateur.
- Tester pleinement les fonctionnalités dépendantes de HTTPS (ex : redirections, cookies sécurisés).

### Utilisation de mkcert
L'utilisation des certificats et clés privées permet d'ajouter une couche HTTPS.
Ce sont des clés qui sont liées à la machine et donc ne doivent pas
être partagées ni avec d'autres machines ni avec quiconque.

#### Installation de mkcert
Pour chaque machine, il sera nécessaire d'installer puis de lancer les commandes suivantes, soit :
1. Installer [mkcert](https://github.com/FiloSottile/mkcert).
Sous Linux Mint :
- Installez les dépendances :
>
sudo apt update
>
sudo apt install libnss3-tools wget
	
- Télécharger et installer mkcert
> wget https://github.com/FiloSottile/mkcert/releases/download/v1.4.4/mkcert-v1.4.4-linux-amd64

>chmod +x mkcert-v1.4.4-linux-amd64

> sudo mv mkcert-v1.4.4-linux-amd64 /usr/local/bin/mkcert

#### Utilisation de mkcert
2. Créer une autorité de certification locale  dans le système
   > mkcert -install
   
   > mkcert 127.0.0.1 localhost ::1
   
3. Générer un certificat pour localhost

 Naviguez dans le répertoire de votre projet Django :
> cd /chemin/vers/votre_projet

Créez un dossier pour les certificats :
> mkdir certs

Générez le certificat :
> mkcert -key-file certs/key.pem -cert-file certs/cert.pem localhost 127.0.0.1 ::1

Cela crée deux fichiers dans le répertoire certs
> certs/key.pem (clé privée)

> certs/cert.pem (certificat public)

#### La structure du projet sécurisée par HTTPS est donc :
Les fichiers pem seront seront donc copiés dans le répertoire ''certs'' à la rachine du projet Django.
En outre, les fichiers pem seront donc ignorés du commit sur le projet global
> mon_projet/

> ├── .gitignore          # Ignore certs/*.key et certs/*.pem

> ├── README.md           # Documente la génération des certificats

> ├── setup_ssl.sh        # Script pour générer les certificats

> └── certs/              # Dossier ignoré par Git

>	├──── cert.pem        # Certificat public (optionnel à commiter)
 
 > 	└──── key.pem         # Clé privée (JAMAIS committée)

### Configuration manuelle (sans django-sslserver)


