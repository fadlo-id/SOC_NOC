import sys
sys.path.insert(0, r"C:\Users\ppp\AppData\Local\Temp\claude\E--linkedin\a1f9fa53-d28c-4c4d-8c52-dfafdddf1b85\scratchpad")
from diagrams import *

W, H = 1900, 1010
img, d = new_canvas(W, H)
header(d, W, "Flux de collecte et de supervision",
       "Deux chaines paralleles - Wazuh (securite) et Zabbix (disponibilite) - sans correlation automatique entre elles")

margin = 60
lane1_y0 = 210
bw, bh = 290, 110
gap = 55

def lane_label(y, text, color, bg):
    rbox(d, [margin, y, margin+230, y+40], fill=bg, outline=color, width=2, radius=8)
    d.text((margin+14, y+9), text, font=F_LABEL, fill=color)

# ---------------- Lane 1 : Wazuh / SOC ----------------
lane_label(lane1_y0-54, "SOC - Wazuh", (30,58,138), BLUE_LIGHT)

x = margin
y = lane1_y0
boxes1 = [
    ("endpoint", "Endpoint surveille", ["Fichiers, journaux Windows/Linux"], GRAY_LIGHT, GRAY_BORDER),
    ("server", "Agent Wazuh", ["Logcollector + Agentd"], BLUE_LIGHT, BLUE_BORDER),
    ("server", "Serveur Wazuh", ["Remoted -> Analysisd (decode + regles)"], BLUE_LIGHT, BLUE_BORDER),
    ("doc", "Indexeur", ["archives.json / alerts.json"], BLUE_LIGHT, BLUE_BORDER),
    ("shield", "Tableau de bord", ["Alertes par severite"], BLUE_LIGHT, BLUE_BORDER),
]
coords1 = []
for i, (kind, title, sub, fill, border) in enumerate(boxes1):
    bx0 = x + i*(bw+gap)
    box = (bx0, y, bx0+bw, y+bh)
    coords1.append(box)
    device_box(d, box, kind, title, sub, fill, border, (30,58,138), (30,58,138))
    if i > 0:
        px0, py0, px1, py1 = coords1[i-1]
        elbow(d, [(px1, (py0+py1)/2), (bx0, (py0+py1)/2)], color=(30,58,138), width=2)

# equipment without agent -> Serveur Wazuh (Syslog), routed in the gutter below the row, entering from the bottom edge
gutter1_y = lane1_y0 + bh + 70
eq1 = (margin, gutter1_y + 30, margin+230, gutter1_y + 30 + 70)
device_box(d, eq1, "firewall", "Equipement sans agent", ["Pare-feu (Syslog)"], GRAY_LIGHT, GRAY_BORDER, SUB, SUB)
rem_box = coords1[2]
rem_cx = (rem_box[0]+rem_box[2])/2
eq1_cx = (eq1[0]+eq1[2])/2
elbow(d, [(eq1_cx, eq1[1]), (eq1_cx, gutter1_y), (rem_cx, gutter1_y), (rem_cx, rem_box[3])],
      color=(120,53,15), width=2, dashed=True, label="Syslog", font_obj=F_TINY, label_fg=(120,53,15), label_at=2)

# ---------------- Lane 2 : Zabbix / NOC ----------------
lane2_y0 = eq1[3] + 100
lane_label(lane2_y0-54, "NOC - Zabbix", GREEN, GREEN_LIGHT)
y2 = lane2_y0
boxes2 = [
    ("endpoint", "Endpoint supervise", ["Agent Zabbix (passif ou actif)"], GRAY_LIGHT, GRAY_BORDER),
    ("server", "Serveur Zabbix", ["Collecte + traitement"], GREEN_LIGHT, GREEN_BORDER),
    ("doc", "Base de donnees", ["Historique des metriques"], GREEN_LIGHT, GREEN_BORDER),
    ("gauge", "Tableaux de bord", ["CPU, RAM, disque, reseau"], GREEN_LIGHT, GREEN_BORDER),
]
coords2 = []
bw2 = 350
for i, (kind, title, sub, fill, border) in enumerate(boxes2):
    bx0 = x + i*(bw2+gap)
    box = (bx0, y2, bx0+bw2, y2+bh)
    coords2.append(box)
    device_box(d, box, kind, title, sub, fill, border, GREEN, GREEN)
    if i > 0:
        px0, py0, px1, py1 = coords2[i-1]
        elbow(d, [(px1, (py0+py1)/2), (bx0, (py0+py1)/2)], color=GREEN, width=2)

gutter2_y = lane2_y0 + bh + 70
eq2 = (margin, gutter2_y + 30, margin+230, gutter2_y + 30 + 70)
device_box(d, eq2, "switch", "Equipement sans agent", ["Commutateur / pare-feu (SNMP)"], GRAY_LIGHT, GRAY_BORDER, SUB, SUB)
srv_box = coords2[1]
srv_cx = (srv_box[0]+srv_box[2])/2
eq2_cx = (eq2[0]+eq2[2])/2
elbow(d, [(eq2_cx, eq2[1]), (eq2_cx, gutter2_y), (srv_cx, gutter2_y), (srv_cx, srv_box[3])],
      color=GREEN, width=2, dashed=True, label="SNMP", font_obj=F_TINY, label_fg=GREEN, label_at=2)

# divider note between the two lanes (placed in the lane-1 gutter area, to the right of eq1)
note_x0 = eq1[2] + 50
rbox(d, [note_x0, gutter1_y-26, W-margin, gutter1_y+36], fill=(254,242,242), outline=(252,165,165), width=2, radius=8)
d.text((note_x0+20, gutter1_y-14), "Wazuh et Zabbix restent deux consoles separees : aucune correlation automatique n'existe entre",
       font=F_SMALL, fill=(153,27,27))
d.text((note_x0+20, gutter1_y+8), "les evenements de securite et les metriques de disponibilite - le rapprochement reste manuel.",
       font=F_SMALL, fill=(153,27,27))

footer(d, W, H, "Source : rapport de stage final, section 3.3 (Wazuh) et 3.4 (Zabbix), Figure 3.1 - maquette de laboratoire, CHU Hassan II de Fès.")

img.save(os.path.join(OUT, "02-flux-collecte-supervision.png"))
print("saved 02", "H needed:", eq2[3]+90)
