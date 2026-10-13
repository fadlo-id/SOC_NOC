# Sécurité, limites et recommandations

## Rappel du périmètre

Cette plateforme est une **maquette académique de laboratoire**, construite à but pédagogique dans le cadre d'un stage de 2ème année du cycle ingénieur. Elle n'a jamais été déployée en production et n'est pas connectée au réseau réel du CHU Hassan II de Fès. Les familles d'équipements utilisées (Wazuh, Zabbix, Palo Alto, Sophos, commutateurs HP Aruba) sont comparables à celles employées en production, mais la maquette elle-même reste strictement isolée.

## Limites identifiées (issues du rapport de stage)

- **Échelle réduite** : quelques endpoints, un commutateur et un pare-feu par phase — le comportement de la plateforme avec un volume réel d'agents et de flux n'a pas été évalué.
- **Observations ponctuelles** : les captures établissent un état à un instant donné (agents actifs, hôtes disponibles), pas une disponibilité continue.
- **Supervision encore informative** : les seuils, canaux de notification et procédures d'escalade ne sont pas formalisés ; certains modèles Zabbix produisent vraisemblablement des faux positifs.
- **Volume et bruit des journaux réseau** : les événements de niveau 3 du pare-feu représentent l'essentiel des alertes classées « faibles ». Sans filtrage ni agrégation des événements répétitifs, ce volume peut masquer les signaux utiles.
- **Paramètres de supervision non vérifiés en détail** : la configuration effective des vérifications actives de l'agent Windows n'est pas entièrement visible, de même que le chiffrement des échanges agent-serveur (SNMP et Syslog compris).
- **Absence de corrélation automatique entre consoles** : les journaux du pare-feu Sophos sont centralisés dans Wazuh, mais Wazuh et Zabbix restent deux consoles séparées — le rapprochement entre événements de sécurité et indicateurs de disponibilité reste manuel.
- **Configurations non divulguées** : conformément aux règles de confidentialité appliquées dans le rapport original, ce dépôt ne publie ni mot de passe, ni clé, ni règle de pare-feu non affichée, ni politique de rétention des journaux.

## Recommandations (priorisées dans le rapport original, non appliquées pendant le stage)

| Priorité | Domaine | Action recommandée |
|---|---|---|
| 1 | Correctifs | Mettre à jour le client Ubuntu 24.04 (suppression de l'ancien noyau) et les logiciels vulnérables identifiés (Wireshark, 7-Zip) sur le poste Windows. |
| 1 | Plateforme | Vérifier puis activer le chiffrement PSK entre les agents Zabbix et le serveur ; corriger les paramètres de vérification active si ce mode est utilisé. |
| 1 | Plateforme | Installer un certificat de confiance pour la console Wazuh, servir Zabbix en HTTPS, restreindre l'accès aux consoles au réseau d'administration. |
| 2 | SOC | Filtrer et agréger les événements de faible sévérité issus du pare-feu afin de réduire le bruit. |
| 2 | SOC | Optimiser les règles de détection (seuils de fréquence sur les refus répétés, attaques DoS, signatures IPS). |
| 2 | Durcissement | Relever progressivement les scores de conformité CIS (inchangés entre les deux relevés de la maquette). |
| 3 | Visualisation | Étudier l'ajout de Grafana pour une visualisation unifiée des indicateurs SOC/NOC. |
| 3 | Intégration | Étudier une corrélation plus poussée entre Wazuh et Zabbix pour rapprocher événements de sécurité et problèmes de disponibilité. |

## Ce que ce projet n'est pas

- ❌ Un audit de sécurité du réseau réel du CHU Hassan II de Fès.
- ❌ Une plateforme déployée en production.
- ❌ Une preuve d'incident de sécurité réel (les scénarios d'authentification échouée sont des tests volontaires).
- ❌ Une démonstration de création de règles de détection Wazuh personnalisées (le projet documente l'usage des modules et décodeurs existants, pas l'écriture de règles sur mesure).

## Ce que ce projet est

- ✅ Une maquette pédagogique démontrant l'intégration cohérente d'un SIEM (Wazuh), d'un outil de supervision (Zabbix) et d'un contrôle périmétrique (pare-feu nouvelle génération), avec preuves à l'appui (captures datées, matrice de validation).
- ✅ Une base d'apprentissage sur la complémentarité — et les limites — de plusieurs outils de sécurité et de supervision observés ensemble sur les mêmes hôtes.
