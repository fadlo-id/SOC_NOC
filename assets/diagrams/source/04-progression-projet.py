import sys
sys.path.insert(0, r"C:\Users\ppp\AppData\Local\Temp\claude\E--linkedin\a1f9fa53-d28c-4c4d-8c52-dfafdddf1b85\scratchpad")
from diagrams import *

W, H = 1800, 540
img, d = new_canvas(W, H)
header(d, W, "Progression du projet SOC/NOC",
       "Étapes effectivement réalisées pendant le stage (CHU Hassan II de Fès, 1er juillet – 31 août 2026)")

steps = [
    ("1", "Préparation de\nl'environnement virtualisé", "VMware Workstation, machines\nUbuntu 16.04, réseaux privés"),
    ("2", "Architecture réseau\net règles de sécurité", "Zones Palo Alto, routage,\npolitiques, NAT, filtrage URL"),
    ("3", "Déploiement des outils\nde supervision", "Wazuh (SIEM), Zabbix\n(conteneurisé Docker)"),
    ("4", "Intégration des machines\net équipements (phase 2)", "Windows 11, Ubuntu 24.04,\ncommutateur HP Aruba, Sophos"),
    ("5", "Tests et validation", "Vulnérabilités, CIS Benchmarks,\nFIM, scénarios simulés"),
    ("6", "Analyse des limites et\npistes d'amélioration", "Matrice de validation,\nrecommandations priorisées"),
]

n = len(steps)
margin = 70
gap = 24
box_w = (W - 2 * margin - gap * (n - 1)) / n
box_h = 190
y0 = 170
line_y = y0 + 34

# connecting line
d.line([(margin + box_w/2, line_y), (W - margin - box_w/2, line_y)], fill=(203, 213, 225), width=4)

for i, (num, title, detail) in enumerate(steps):
    x0 = margin + i * (box_w + gap)
    x1 = x0 + box_w
    # circle node
    cx = x0 + box_w/2
    r = 26
    d.ellipse([cx-r, line_y-r, cx+r, line_y+r], fill=BLUE, outline=NAVY, width=2)
    bbox = d.textbbox((0,0), num, font=F_H2)
    d.text((cx-(bbox[2]-bbox[0])/2, line_y-(bbox[3]-bbox[1])/2-4), num, font=F_H2, fill=WHITE)

    by0 = line_y + 50
    by1 = by0 + box_h
    rbox(d, [x0, by0, x1, by1], fill=GRAY_LIGHT, outline=GRAY_BORDER, width=2, radius=10)
    ty = by0 + 20
    for ln in title.split("\n"):
        d.text((x0+16, ty), ln, font=F_LABEL, fill=INK)
        ty += 26
    ty += 10
    d.line([(x0+16, ty), (x1-16, ty)], fill=(203,213,225), width=1)
    ty += 16
    for ln in detail.split("\n"):
        d.text((x0+16, ty), ln, font=F_SMALL, fill=SUB)
        ty += 22

footer(d, W, H, "Source : rapport de stage final (démarche méthodologique, chapitres II et V) — réalisation personnelle, maquette de laboratoire, CHU Hassan II de Fès.")

img.save(os.path.join(OUT, "04-progression-projet.png"))
print("saved 04")
