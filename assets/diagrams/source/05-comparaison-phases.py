import sys
sys.path.insert(0, r"C:\Users\ppp\AppData\Local\Temp\claude\E--linkedin\a1f9fa53-d28c-4c4d-8c52-dfafdddf1b85\scratchpad")
from diagrams import *

W, H = 1700, 870
img, d = new_canvas(W, H)
header(d, W, "Comparaison des deux phases du laboratoire",
       "Les deux phases ne forment pas une infrastructure unique simultanée — périmètres et pare-feu distincts")

col_gap = 40
margin = 60
col_w = (W - 2*margin - col_gap) / 2
y0 = 150

def phase_col(x0, title_kind, title, subtitle, fill, border, title_color, rows):
    x1 = x0 + col_w
    rbox(d, [x0, y0, x1, y0+70], fill=fill, outline=border, width=3, radius=10)
    icon(d, title_kind, (x0+20, y0+16), 36, title_color)
    d.text((x0+68, y0+12), title, font=F_H2, fill=title_color)
    d.text((x0+68, y0+40), subtitle, font=F_SMALL, fill=SUB)

    ry = y0 + 90
    for label, value in rows:
        rbox(d, [x0, ry, x1, ry+104], fill=WHITE, outline=GRAY_BORDER, width=2, radius=8)
        d.text((x0+20, ry+14), label, font=F_LABEL, fill=INK)
        d.line([(x0+20, ry+42), (x1-20, ry+42)], fill=(226,232,240), width=1)
        yy = ry + 52
        for ln in value:
            d.text((x0+20, yy), ln, font=F_SMALL, fill=SUB)
            yy += 21
        ry += 118

rows1 = [
    ("Objectif", ["Établir une maquette minimale mais", "complète autour d'un hôte unique"]),
    ("Pare-feu", ["Palo Alto PA-VM (PAN-OS 11.1)", "zones, NAT, filtrage d'URL"]),
    ("Composants", ["1 hôte Ubuntu 16.04, 1 serveur Wazuh,", "1 serveur Zabbix (Docker)"]),
    ("Validation", ["Agent actif, alertes consultables,", "tests de navigation autorisée/bloquée"]),
]

rows2 = [
    ("Objectif", ["Étendre à un environnement multi-", "systèmes proche d'un parc réel"]),
    ("Pare-feu", ["Sophos XG (VM), placé en coupure", "du laboratoire — remplace Palo Alto"]),
    ("Composants", ["+ Windows 11, Ubuntu 24.04,", "commutateur HP Aruba 2530 (SNMP)"]),
    ("Validation", ["118/4164 vulnérabilités détectées, CIS", "28%/38%, 2 scénarios d'auth. simulés"]),
]

phase_col(margin, "firewall", "Phase 1 — Maquette initiale", "Hôte Ubuntu 16.04 + Palo Alto",
          BLUE_LIGHT, BLUE_BORDER, (30,58,138), rows1)
phase_col(margin + col_w + col_gap, "firewall", "Phase 2 — Extension du laboratoire", "Multi-systèmes + Sophos",
          AMBER_LIGHT, AMBER_BORDER, (120,53,15), rows2)

# bottom note
note_y = y0 + 90 + 4*118 + 14
rbox(d, [margin, note_y, W-margin, note_y+70], fill=GRAY_LIGHT, outline=GRAY_BORDER, width=2, radius=8)
d.text((margin+20, note_y+12), "ATTENTION — Les deux phases sont présentées séparément à dessein : Palo Alto (phase 1) et Sophos (phase 2)",
       font=F_SMALL, fill=INK)
d.text((margin+20, note_y+36), "n'ont jamais coexisté dans une même architecture simultanée. Chaque phase a son propre périmètre validé.",
       font=F_SMALL, fill=INK)

footer(d, W, H, "Source : rapport de stage final, tableau 5.4 (évolution des indicateurs) — maquette de laboratoire, CHU Hassan II de Fès.")

img.save(os.path.join(OUT, "05-comparaison-phases.png"))
print("saved 05")
