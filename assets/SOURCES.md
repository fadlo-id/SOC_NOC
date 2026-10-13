# Sources des images — projet SOC/NOC (CHU Hassan II de Fès)

Bibliothèque constituée le 13/10/2026 à partir du rapport de stage final (`Rapport_Stage_SOC_NOC_Fadlollah_Idrissi_FINAL (5) (1).pdf`), après lecture intégrale du document (52 pages + annexes).

## rapport/ — images extraites du rapport de stage

Toutes les images ci-dessous sont des **réalisations personnelles de Fadlollah** (schémas) ou des **captures d'écran de la maquette de laboratoire** (consoles Wazuh/Zabbix), explicitement distinctes de l'infrastructure réelle du CHU. Extraites en résolution native via `pdfimages` (pas de recompression, pas de retouche).

| Fichier | Figure source | Nature | Statut |
|---|---|---|---|
| `architecture-phase1.png` | Figure 4.1 | Schéma — architecture logique phase 1 | ✅ Réalisation personnelle (rapport, p.19) — sûr pour diffusion publique |
| `topologie-paloalto-zones.png` | Figure 4.2 | Schéma — zones de sécurité Palo Alto | ✅ Réalisation personnelle (rapport, p.21) — sûr pour diffusion publique |
| `architecture-phase2-laboratoire.png` | Figure 4.3 | Schéma — architecture phase 2 (laboratoire multi-systèmes) | ✅ Réalisation personnelle (rapport, p.22) — sûr pour diffusion publique, image la plus représentative du projet |
| `wazuh-dashboard-overview.png` | Figure 5.2 | Capture — vue d'ensemble du tableau de bord Wazuh | ✅ Capture de la maquette (rapport, p.24) — aucune donnée sensible, compteurs d'alertes du laboratoire uniquement |
| `zabbix-dashboard-global.png` | Figure 5.6b | Capture — vue globale Zabbix | ✅ Capture de la maquette (rapport, p.26) — aucune donnée sensible |

**Vérification effectuée avant sélection :** lecture intégrale des 52 pages du rapport (texte + images) pour confirmer le contenu de chaque figure avant de l'extraire. Aucune image ne contient de mot de passe, jeton, clé ou identifiant réel (conforme à l'Annexe A du rapport, qui confirme explicitement l'absence de tels éléments).

## Images explicitement exclues (ne pas publier)

| Figures | Raison de l'exclusion |
|---|---|
| Figures 1.1 à 1.6 (p.3-7) | Organigramme et architecture réseau **institutionnels du CHU Hassan II** (bâtiment, organigramme de direction, architecture du "local nodal principal", segmentation VLAN par service hospitalier) — sourcés du document de présentation interne du CHU, donc **propriété de l'établissement, pas du stagiaire**. Décrivent une infrastructure de production réelle (modèles d'équipements : commutateur HP Aruba 5400zl, routeur Cisco, pare-feu Sophos du CHU). **Jamais publiées, ni sur GitHub ni sur LinkedIn**, sans autorisation explicite du CHU. |
| Figures 5.9, 5.17-5.29 (captures détaillées phase 2) | Captures d'écran montrant des chiffres de vulnérabilités, scores CIS, ou détails de configuration (ex. Figure 5.27 : tentatives d'authentification échouées). Utilisables en contexte GitHub avec légende complète (voir `docs/validation.md`), **mais exclues des posts LinkedIn** pour respecter la consigne de ne jamais citer de chiffres de vulnérabilité dans une publication courte, où le contexte complet ne peut pas être garanti. |

## internet/ — images externes

**Aucune image externe n'a été téléchargée.** Les logos officiels Wazuh, Zabbix, Palo Alto Networks et Sophos sont des marques déposées ; leur réutilisation sur un dépôt public sans autorisation explicite présente un risque de droits d'image non vérifiable dans cette session. Recommandation : citer les outils par leur nom (texte), pas par leur logo. Si Fadlollah souhaite malgré tout des logos officiels, il peut les télécharger lui-même depuis les kits presse officiels de chaque éditeur.

## creations/ — schémas originaux

Aucun schéma supplémentaire n'a été nécessaire pour le projet SOC/NOC : les Figures 4.1 à 4.3 du rapport (déjà des réalisations personnelles) couvrent entièrement le besoin d'illustration de l'architecture.
