# Synthèse publique du rapport de stage

Ce document résume le rapport de stage original (*« Mise en place d'une plateforme SOC/NOC pour la supervision et la sécurisation du réseau »*, CHU Hassan II de Fès, 1er juillet – 31 août 2026). **Le rapport complet n'est pas publié dans ce dépôt** : il contient des éléments institutionnels appartenant au CHU (présentation de l'établissement, organigramme, architecture réseau de production) qui ne sont pas la propriété du stagiaire. Cette synthèse ne couvre que la maquette personnelle réalisée pendant le stage.

## Contexte

Stage de 2ème année du cycle ingénieur (ENSA Fès, filière Systèmes Communicants et Cybersécurité), réalisé au sein de la Division des Systèmes d'Information (Service des Infrastructures, Systèmes et Réseaux) du CHU Hassan II de Fès. Encadrement : Pr. Hakim El Fadili (ENSA Fès) et M. Aziz Abdelghani (CHU Hassan II).

## Problématique

*Comment mettre en place une plateforme cohérente permettant de superviser un hôte, de centraliser ses événements de sécurité, de suivre ses indicateurs de performance et de contrôler son accès à Internet à travers un pare-feu de nouvelle génération ?*

## Démarche

Le projet a été conduit en deux phases incrémentales :

1. **Phase 1** — maquette minimale mais complète : un hôte Ubuntu 16.04 supervisé simultanément par Wazuh (SOC) et Zabbix Agent 1 (NOC), dont le trafic Internet traverse un pare-feu Palo Alto.
2. **Phase 2** — extension du laboratoire à un environnement multi-systèmes (Windows 11, Ubuntu 24.04, commutateur HP Aruba, pare-feu Sophos), avec exploitation des modules avancés de Wazuh et intégration des journaux du pare-feu dans le SOC.

Détail technique complet : voir `../docs/architecture.md`, `../docs/installation.md` et `../docs/validation.md`.

## Résultats clés (maquette uniquement)

- Les trois briques de l'architecture Wazuh (gestionnaire, indexeur, tableau de bord) ont été vérifiées opérationnelles, avec un agent actif sur l'hôte supervisé.
- Le déploiement conteneurisé de Zabbix (Docker) a été vérifié, avec visualisation des métriques système, stockage, disque et réseau de l'hôte.
- Le pare-feu Palo Alto a été configuré avec des zones de sécurité (trust/untrust), une règle NAT et un filtrage d'URL, validés par des tests de navigation autorisée et bloquée.
- En phase 2, les modules avancés de Wazuh ont permis de détecter des vulnérabilités, d'évaluer la conformité CIS Benchmarks et de cartographier les alertes selon MITRE ATT&CK sur deux endpoints (Windows 11, Ubuntu 24.04).
- Deux scénarios d'authentification échouée ont été **simulés volontairement** pour valider la chaîne de détection (règles de corrélation Wazuh, technique MITRE ATT&CK T1110 — Brute Force). Ce ne sont pas des incidents réels.
- Le pare-feu Sophos a été intégré aux deux consoles de supervision (SNMP vers Zabbix, Syslog vers Wazuh).

## Limites assumées

- Échelle réduite (quelques hôtes), observations ponctuelles plutôt que supervision continue, absence de corrélation automatique entre Wazuh et Zabbix, et plusieurs paramètres de sécurité (chiffrement des échanges, vérifications actives) restant à confirmer. Détail complet : `../docs/security-and-limitations.md`.

## Ce que cette synthèse ne couvre pas (volontairement)

- La présentation institutionnelle du CHU Hassan II de Fès (organigramme, architecture réseau de production, équipements réels de l'établissement) — propriété du CHU, non reproduite ici.
- Les configurations complètes, mots de passe, clés ou identifiants — aucun n'est divulgué, conformément aux règles de confidentialité du rapport original.

## Apports du stage

- **Techniques** : déploiement et exploitation d'un SIEM/XDR (Wazuh), supervision par agent et par SNMP (Zabbix), intégration Syslog d'un pare-feu, configuration d'un pare-feu de nouvelle génération (zones, NAT, filtrage d'URL), gestion des vulnérabilités et durcissement selon les référentiels CIS.
- **Méthodologiques** : conduite d'un projet incrémental en deux phases, validation fondée sur des preuves, lecture critique des alertes et des tableaux de bord, priorisation des recommandations selon l'impact et l'effort.
- **Professionnels** : découverte du fonctionnement d'une DSI hospitalière, prise en compte des contraintes de continuité de service et de confidentialité, rédaction d'une documentation technique structurée.
