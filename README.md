
<p align="center">
  <h1>Service room</h1>

  <p align="center">
    Projet du module de formation architecture microservices
</p>


<details open="open">
  <summary>Table des matières</summary>
  <ol>
    <li><a href="#a-propos">A propos</a></li>
    <li><a href="#fabriqué-avec">Fabriqué avec</a></li>
    <li><a href="#getting-started">Contexte</a></li>
    <li><a href="#auteurs">Auteurs</a></li>
    <li><a href="#github">GitHub</a></li>
  </ol>
</details>



## A propos 


Ce service est un service de room d'un jeu vidéo de boxe. Il permet d'instancier une room qui permet a deux clients (joueurs) de jouer à distance à ce jeu. Le projet est composer de deux parties distincts : la partie technique du jeu et la partie protocole réseau. EN effet ce jeu est en relation avec un serveur de jeu auquel nous communions via MQTT.

C'est pourquoi :
* mqttClient est la classe qui permet la connexion, les publish et les subscribe au serveur MQTT
* player est la classe qui définit les attrubuts et méthode des joueurs
* combat est la classe qui détermine les modalités d'une partie de jeu tels.
* room.py est le fichier de lancement, il est composé de la classe Room et de la fonction main. La classe room instancie une room d'une partie qui communique avec différents services. La fonction main permet de se connecter au serveur mqtt, d'instancier la classe room et d'écouter les topics définit. 
* Le main permet de tester le jeu indépendamment du reste. Test tel que les déplacements, l'attaque, la garde, la collision


## Fabriqué avec

* [MQTT](https://mqtt.org/) - protocole de communication
* [Raspberry Pi](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) - serveur de jeu
* [Python](https://www.python.org/) - lanquage de programmation

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


## Contexte

Ce projet rentre dans l'évaluation du module d'architecture microservices. La demande était de réaliser un projet en suivant les principes de l'architecture en microservice. À la suite d'un brainstorming, il a été défini que le projet allait prendre la forme d'un jeu de boxe contenant des pronostics de pari. Le plus gros enjeu est la mise en place de la communication entre les différents services :

* Le service Client : le visuel du jeu, la partie joueurs
* Le service Room : le côté technique d'une partie de jeu
* Le service Joueur : modèle d'un joueur avec base de données virtualité sous docker
* Le service IA : mise en place d'un paterne d'analyse des données des joueurs et des parties pour réaliser des pronostics de match


## Auteurs

* Groupe B3 informatique | Ynov Lyon Campus - Spécialité Ingénierie Logicielle


## GitHub

Ce projet est disponible sur GitHub

* [Dépot](https://github.com/ebbane/microservices-room)




