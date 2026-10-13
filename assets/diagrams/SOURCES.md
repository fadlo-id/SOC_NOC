# Sources et format des schémas originaux

Schémas créés le 13/10/2026, en réponse à la demande explicite de visuels "d'ingénierie" (pas de style IA/marketing). Toutes les données techniques (noms de composants, protocoles, adresses de sous-réseau, résultats) proviennent du rapport de stage final — rien n'est inventé.

## Format source

**Choix : scripts Python (Pillow/PIL), pas draw.io ni Mermaid.** Justification :
- Un rendu draw.io nécessite un outil de rendu local (CLI drawio ou l'application desktop) dont la présence n'était pas confirmée dans cet environnement — je n'ai rien installé sans autorisation, conformément à la consigne.
- Mermaid produit une mise en page automatique (auto-layout) peu contrôlable au pixel près ; le rendu obtenu ne garantissait pas l'alignement sur grille et l'absence de croisements demandés explicitement.
- Python/Pillow, déjà installé et vérifié fonctionnel dans cet environnement, permet un contrôle précis de l'alignement, des couleurs et du routage des connecteurs (coudes à angle droit, sans croisement de texte) — le résultat a été vérifié visuellement avant validation (plusieurs itérations de correction effectuées).

Les scripts sources (modifiables) sont dans `source/` : `diagrams_lib.py` (bibliothèque de fonctions réutilisables — boîtes, icônes génériques, connecteurs orthogonaux, légende) et un script par schéma. Aucun logo officiel n'est utilisé : les icônes (pare-feu, serveur, commutateur, endpoint, bouclier, jauge) sont des glyphes géométriques simples dessinés par le script, pas des marques déposées.

## Schémas produits

| Fichier | Contenu | Source factuelle (rapport) |
|---|---|---|
| `01-architecture-generale.png` | Architecture des deux phases, côte à côte (Palo Alto et Sophos jamais mélangés dans un même schéma) | Figures 4.1 et 4.3, sections 4.2-4.6 |
| `02-flux-collecte-supervision.png` | Chaîne de collecte Wazuh (SOC) et chaîne de supervision Zabbix (NOC), séparées, avec note explicite sur l'absence de corrélation automatique | Sections 3.3-3.4, Figure 3.1, section 5.6 |
| `03-segmentation-securite.png` | Zones Palo Alto (phase 1) et segmentation Sophos (phase 2), adresses au niveau sous-réseau uniquement | Section 4.5, Figure 4.2, sections 5.4-5.5 |
| `04-progression-projet.png` | 6 étapes réellement réalisées (frise chronologique) | Section 2.8 (démarche méthodologique), chapitre V |
| `05-comparaison-phases.png` | Comparaison objectifs/pare-feu/composants/validation entre les deux phases | Tableau 5.4, section 5.5.10 |

## Décision de sanitisation (schéma 3)

Les adresses IP individuelles des hôtes (ex. 192.168.65.147, .148, .244, .245, .149, .150) **n'apparaissent pas** dans ce schéma destiné à la diffusion publique — seules les plages de sous-réseau (ex. 192.168.65.0/24) sont indiquées. Le détail complet par hôte reste disponible dans `docs/architecture.md` et `docs/installation.md` du dépôt, où le contexte technique complet justifie ce niveau de détail. Ces adresses restent des adresses privées de laboratoire, non routables sur Internet — ce choix est une précaution de bon sens, pas une exigence de confidentialité stricte du rapport original.
