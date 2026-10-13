# Installation et configuration

Ce document résume les grandes étapes de mise en place de la maquette, telles que documentées dans le rapport de stage original. **Aucun fichier de configuration exporté, script d'automatisation ni identifiant n'est fourni dans ce dépôt** — conformément au principe de confidentialité appliqué dans le rapport original, seules les grandes lignes sont reproduites ici.

## Prérequis

- VMware Workstation (virtualisation des machines du laboratoire).
- Images/paquets officiels : Wazuh 4.14 (manager + indexeur + agents), Zabbix 7.0/7.4 (serveur + agents), Palo Alto PA-VM (PAN-OS 11.1), pare-feu Sophos XG (VM), image Kali Linux (hébergement Docker pour Zabbix en phase 1).
- Systèmes cibles : Ubuntu 16.04 LTS / 24.04 LTS, Windows 11 Enterprise LTSC 2024.

## Grandes étapes (phase 1)

1. **Déploiement du serveur Wazuh** (manager, indexeur, tableau de bord) et installation de l'agent sur l'hôte Ubuntu.
2. **Déploiement conteneurisé de Zabbix 7.0** via Docker sur une machine Kali Linux dédiée (isolation des rôles : interface Web, base de données, serveur).
3. **Configuration du pare-feu Palo Alto** : interfaces de niveau 3, zones de sécurité (Management, Trust, DMZ, Untrust), routeur virtuel, règle de sécurité trust → untrust, règle NAT de sortie, catégorie de filtrage d'URL personnalisée.
4. **Vérification croisée** : interface Web et ligne de commande (`show interface all`, `ip route`) pour confirmer la cohérence du routage et des zones.

## Grandes étapes (phase 2 — extension)

1. **Déploiement des agents Wazuh et Zabbix Agent 2** sur un poste Windows 11 et un client Ubuntu 24.04, via l'assistant d'enrôlement intégré au tableau de bord Wazuh.
2. **Intégration du pare-feu Sophos** : configuration réseau (interface LAN/WAN), politique de pare-feu à cinq règles évaluées dans l'ordre (principe du moindre privilège), raccordement SNMP (vers Zabbix) et Syslog (vers Wazuh).
3. **Supervision SNMP du commutateur HP Aruba 2530** par Zabbix (modèle « HP Enterprise Switch by SNMP »).
4. **Activation des modules avancés Wazuh** sur les deux endpoints : détection de vulnérabilités, Security Configuration Assessment (CIS Benchmarks), File Integrity Monitoring, cartographie MITRE ATT&CK.

## Non couvert par ce dépôt

- Fichiers de configuration complets (`ossec.conf`, règles de pare-feu détaillées, etc.) — non partagés, conformément à l'Annexe A du rapport original.
- Scripts d'automatisation du déploiement — la maquette a été construite manuellement, étape par étape, à but pédagogique.
- Toute adresse ou information permettant un accès réel à un composant — seules des adresses privées de laboratoire (non routables) apparaissent dans la documentation.
