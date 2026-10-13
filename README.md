# Plateforme SOC/NOC — Maquette de laboratoire

> ⚠️ **Avertissement obligatoire** : ce dépôt documente une **maquette de laboratoire virtualisé**, réalisée dans le cadre d'un stage académique. Elle n'a **jamais été déployée en production** et n'est **pas connectée** au réseau réel du Centre Hospitalier Universitaire (CHU) Hassan II de Fès. Les résultats présentés (alertes, vulnérabilités, scores de conformité) concernent exclusivement les machines de test du laboratoire — ils ne décrivent en aucun cas une faille réelle du CHU.

## Présentation du projet

Stage de 2ème année du cycle ingénieur (filière Systèmes Communicants et Cybersécurité, ENSA Fès), réalisé au sein de la Division des Systèmes d'Information du CHU Hassan II de Fès, du 1er juillet au 31 août 2026.

**Sujet officiel du stage :** *Mise en place d'une plateforme SOC/NOC pour la supervision et la sécurisation du réseau.*

**Encadrement :** Pr. Hakim El Fadili (ENSA Fès) · M. Aziz Abdelghani (CHU Hassan II, DSI)

### Objectifs pédagogiques

Construire, à l'échelle d'un laboratoire, une plateforme associant trois fonctions complémentaires :
- un volet **SOC** (Security Operations Center) avec **Wazuh** pour la collecte et l'analyse des événements de sécurité ;
- un volet **NOC** (Network Operations Center) avec **Zabbix** pour la supervision des ressources système et réseau ;
- un point de **contrôle périmétrique** avec un pare-feu nouvelle génération **Palo Alto** pour le contrôle du trafic sortant.

### Périmètre exact et limites

- **Phase 1** : un hôte Ubuntu 16.04 LTS supervisé simultanément par un agent Wazuh et un agent Zabbix, dont le trafic Internet traverse un pare-feu Palo Alto (zones, NAT, filtrage d'URL).
- **Phase 2 (extension du laboratoire)** : élargissement à un environnement multi-systèmes (poste Windows 11, client Ubuntu 24.04, commutateur HP Aruba supervisé par SNMP, pare-feu Sophos placé en coupure), exploitation des modules avancés de Wazuh (détection de vulnérabilités, audit de conformité CIS Benchmarks, contrôle d'intégrité des fichiers, cartographie MITRE ATT&CK) et détection de scénarios d'authentification simulés (tests volontaires, pas des incidents réels).
- Toutes les adresses IP utilisées sont des adresses **privées de laboratoire** (réseaux VMware host-only / plage Tailscale 100.x pour l'administration) — aucune n'est routable sur Internet, aucune ne correspond au réseau de production du CHU.

Voir `docs/security-and-limitations.md` pour le détail des limites identifiées et `report/synthese-publique.md` pour une synthèse complète du rapport de stage original (non publié intégralement — voir ci-dessous).

## Architecture

![Architecture générale du laboratoire SOC/NOC](assets/diagrams/01-architecture-generale.png)

Détail complet, avec les schémas de segmentation réseau et de flux de collecte/supervision, dans `docs/architecture.md`. Schémas originaux sourcés dans `assets/diagrams/SOURCES.md` (fichiers Python modifiables dans `assets/diagrams/source/`).

## Technologies utilisées

| Catégorie | Outils |
|---|---|
| SIEM / XDR | Wazuh 4.14 |
| Supervision (NOC) | Zabbix 7.0 (phase 1, conteneurisé Docker) / Zabbix 7.4 (phase 2) |
| Pare-feu nouvelle génération | Palo Alto PA-VM, PAN-OS 11.1 |
| Pare-feu (phase 2) | Sophos XG (VM) |
| Commutateur | HP Aruba 2530 (supervision SNMP) |
| Systèmes | Ubuntu 16.04 / 24.04 LTS, Windows 11 Enterprise LTSC 2024 |
| Virtualisation | VMware Workstation |
| Référentiels de sécurité | MITRE ATT&CK, CIS Benchmarks |

## Installation et configuration

Voir `docs/installation.md` — la reproduction du laboratoire nécessite VMware Workstation et les paquets officiels Wazuh/Zabbix/PAN-OS/Sophos. Ce dépôt ne fournit pas de fichiers de configuration exportés (aucune configuration complète n'est partagée, conformément au rapport de stage original).

## Scénarios de validation et résultats

Voir `docs/validation.md` pour la matrice de validation complète (ce qui a été vérifié, ce qui reste à confirmer, ce qui est recommandé).

## Limites, difficultés et pistes d'amélioration

Voir `docs/security-and-limitations.md`.

## À propos du rapport de stage original

Le rapport de stage complet contient des éléments institutionnels du CHU Hassan II (organigramme, architecture réseau de production) qui ne sont **pas la propriété du stagiaire** et ne sont donc **pas publiés dans ce dépôt**. Une synthèse publique expurgée, couvrant uniquement la maquette personnelle, est disponible dans `report/synthese-publique.md`.

## Auteur

Fadlollah Idrissi — élève ingénieur en dernière année, filière Systèmes Communicants et Cybersécurité, ENSA Fès. Recherche un stage de fin d'études (PFE) de 6 mois à partir de janvier 2027, en priorité en cybersécurité / SOC / Blue Team.
