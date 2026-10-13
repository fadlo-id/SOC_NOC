import sys
sys.path.insert(0, r"C:\Users\ppp\AppData\Local\Temp\claude\E--linkedin\a1f9fa53-d28c-4c4d-8c52-dfafdddf1b85\scratchpad")
from diagrams import *

W, H = 1900, 1040
img, d = new_canvas(W, H)
header(d, W, "Architecture générale du laboratoire SOC/NOC",
       "Maquette virtualisée, CHU Hassan II de Fès — deux phases distinctes, jamais exécutées comme une infrastructure unique")

panel_gap = 50
margin = 60
panel_w = (W - 2*margin - panel_gap) / 2
panel_y0 = 150
panel_y1 = H - 110

def panel(x0, title, subtitle, fill):
    x1 = x0 + panel_w
    rbox(d, [x0, panel_y0, x1, panel_y1], fill=fill, outline=GRAY_BORDER, width=2, radius=14)
    d.text((x0+24, panel_y0+18), title, font=F_H2, fill=INK)
    d.text((x0+24, panel_y0+48), subtitle, font=F_SMALL, fill=SUB)
    d.line([(x0+24, panel_y0+78), (x1-24, panel_y0+78)], fill=(203,213,225), width=1)
    return x0, x1

# ================= Phase 1 panel =================
p1x0, p1x1 = panel(margin, "PHASE 1 — Maquette initiale", "1er juillet 2026", (248, 250, 252))
cx = (p1x0 + p1x1) / 2
bw, bh = 230, 76

internet1 = (cx - bw/2, panel_y0+98, cx + bw/2, panel_y0+98+bh)
device_box(d, internet1, "cloud", "Internet", ["Accès autorisé ou bloqué"], WHITE, GRAY_BORDER, INK, SUB)

fw1 = (cx - bw/2, panel_y0+210, cx + bw/2, panel_y0+210+bh)
device_box(d, fw1, "firewall", "Palo Alto PA-VM", ["PAN-OS 11.1 — zones, NAT, URL"], RED_LIGHT, RED_BORDER, RED, RED)

host1 = (cx - bw/2, panel_y0+322, cx + bw/2, panel_y0+322+bh)
device_box(d, host1, "endpoint", "Hote Ubuntu 16.04", ["Agent Wazuh + Zabbix Agent 1"], GRAY_LIGHT, GRAY_BORDER, INK, SUB)

wazuh1 = (p1x0+40, panel_y0+460, p1x0+40+260, panel_y0+460+bh)
device_box(d, wazuh1, "shield", "Serveur Wazuh", ["SOC - manager/indexeur/dashboard"], BLUE_LIGHT, BLUE_BORDER, (30,58,138), (30,58,138))

zabbix1 = (p1x1-300, panel_y0+460, p1x1-300+260, panel_y0+460+bh)
device_box(d, zabbix1, "gauge", "Serveur Zabbix 7.0", ["NOC - conteneurise Docker"], GREEN_LIGHT, GREEN_BORDER, GREEN, GREEN)

cx_host = (host1[0]+host1[2])/2
elbow(d, [((internet1[0]+internet1[2])/2, internet1[3]), ((fw1[0]+fw1[2])/2, fw1[1])], color=INK, width=3)
elbow(d, [((fw1[0]+fw1[2])/2, fw1[3]), ((host1[0]+host1[2])/2, host1[1])], color=INK, width=3,
      label="trafic sortant", font_obj=F_TINY, label_at=0)

wz_x = (wazuh1[0]+wazuh1[2])/2
zb_x = (zabbix1[0]+zabbix1[2])/2
junc_y = panel_y0 + 420
elbow(d, [(cx_host, host1[3]), (cx_host, junc_y), (wz_x, junc_y), (wz_x, wazuh1[1])],
      color=(30,58,138), width=3, label="evenements securite", font_obj=F_TINY, label_fg=(30,58,138), label_at=0)
elbow(d, [(cx_host, host1[3]), (cx_host, junc_y+14), (zb_x, junc_y+14), (zb_x, zabbix1[1])],
      color=GREEN, width=3, label="metriques (CPU/RAM/disque)", font_obj=F_TINY, label_fg=GREEN, label_at=2)

# private admin network link
priv_y = (wazuh1[1]+wazuh1[3])/2
elbow(d, [(wazuh1[2], priv_y), (zabbix1[0], priv_y)], color=SUB, width=2, dashed=True)
d.text(((wazuh1[2]+zabbix1[0])/2 - 95, priv_y - 34), "reseau prive d'administration", font=F_TINY, fill=SUB)
d.text(((wazuh1[2]+zabbix1[0])/2 - 60, priv_y - 18), "(Tailscale 100.x)", font=F_TINY, fill=SUB)

# ================= Phase 2 panel =================
p2x0, p2x1 = panel(margin + panel_w + panel_gap, "PHASE 2 - Extension du laboratoire", "Sous-reseau dedie 192.168.65.0/24", (253, 250, 244))
cx2 = (p2x0 + p2x1) / 2

internet2 = (cx2 - bw/2, panel_y0+98, cx2 + bw/2, panel_y0+98+bh)
device_box(d, internet2, "cloud", "Internet", ["Test de sortie (ICMP)"], WHITE, GRAY_BORDER, INK, SUB)

sophos = (cx2 - bw/2, panel_y0+198, cx2 + bw/2, panel_y0+198+bh)
device_box(d, sophos, "firewall", "Pare-feu Sophos XG", ["VM - en coupure du laboratoire"], AMBER_LIGHT, AMBER_BORDER, (120,53,15), (120,53,15))

switch = (cx2 - bw/2, panel_y0+298, cx2 + bw/2, panel_y0+298+bh)
device_box(d, switch, "switch", "Commutateur HP Aruba", ["Modele 2530 - supervise SNMP"], GRAY_LIGHT, GRAY_BORDER, INK, SUB)

elbow(d, [((internet2[0]+internet2[2])/2, internet2[3]), ((sophos[0]+sophos[2])/2, sophos[1])], color=INK, width=3)
elbow(d, [((sophos[0]+sophos[2])/2, sophos[3]), ((switch[0]+switch[2])/2, switch[1])], color=INK, width=3)

win = (p2x0+30, panel_y0+420, p2x0+30+220, panel_y0+420+bh)
device_box(d, win, "endpoint", "Poste Windows 11", ["Agents Wazuh + Zabbix"], GRAY_LIGHT, GRAY_BORDER, INK, SUB)

lin = (p2x0+30, panel_y0+520, p2x0+30+220, panel_y0+520+bh)
device_box(d, lin, "endpoint", "Client Ubuntu 24.04", ["Agents Wazuh + Zabbix"], GRAY_LIGHT, GRAY_BORDER, INK, SUB)

elbow(d, [((win[0]+win[2])/2, switch[3]), ((win[0]+win[2])/2, win[1])], color=INK, width=2)
elbow(d, [((lin[0]+lin[2])/2, switch[3]), ((lin[0]+lin[2])/2, panel_y0+500), ((lin[0]+lin[2])/2, panel_y0+500), ((lin[0]+lin[2])/2, lin[1])], color=INK, width=2)

wazuh2 = (p2x1-250, panel_y0+420, p2x1-250+220, panel_y0+420+bh)
device_box(d, wazuh2, "shield", "Serveur Wazuh", ["SIEM/XDR"], BLUE_LIGHT, BLUE_BORDER, (30,58,138), (30,58,138))

zabbix2 = (p2x1-250, panel_y0+520, p2x1-250+220, panel_y0+520+bh)
device_box(d, zabbix2, "gauge", "Serveur Zabbix 7.4", ["Supervise 7 hotes"], GREEN_LIGHT, GREEN_BORDER, GREEN, GREEN)

# endpoints -> servers, orthogonal trunk (right side of endpoints, left side of servers)
trunk_x = (p2x0 + p2x1)/2 + 40
wz2_y = (wazuh2[1]+wazuh2[3])/2
zb2_y = (zabbix2[1]+zabbix2[3])/2
win_y = (win[1]+win[3])/2
lin_y = (lin[1]+lin[3])/2

elbow(d, [(win[2], win_y-14), (trunk_x, win_y-14), (trunk_x, wz2_y), (wazuh2[0], wz2_y)],
      color=(30,58,138), width=2, label="evenements", font_obj=F_TINY, label_fg=(30,58,138), label_at=0)
elbow(d, [(lin[2], lin_y-14), (trunk_x-14, lin_y-14), (trunk_x-14, wz2_y+16), (wazuh2[0], wz2_y+16)],
      color=(30,58,138), width=2)
elbow(d, [(win[2], win_y+14), (trunk_x-28, win_y+14), (trunk_x-28, zb2_y-16), (zabbix2[0], zb2_y-16)],
      color=GREEN, width=2)
elbow(d, [(lin[2], lin_y+14), (trunk_x, lin_y+14), (trunk_x, zb2_y), (zabbix2[0], zb2_y)],
      color=GREEN, width=2, label="metriques", font_obj=F_TINY, label_fg=GREEN, label_at=0)

# Sophos -> Wazuh (Syslog) and Switch -> Zabbix (SNMP), routed along the outer right margin
# (start from the bottom-right corner of each box, below the text, to avoid crossing labels)
out_x = p2x1 - 20
elbow(d, [(sophos[2], sophos[3]+10), (out_x, sophos[3]+10), (out_x, wz2_y-16), (wazuh2[2], wz2_y-16)],
      color=(120,53,15), width=2, dashed=True, label="Syslog", font_obj=F_TINY, label_fg=(120,53,15), label_at=1)
elbow(d, [(switch[2], switch[3]+10), (out_x+16, switch[3]+10), (out_x+16, zb2_y+16), (zabbix2[2], zb2_y+16)],
      color=GREEN, width=2, dashed=True, label="SNMP", font_obj=F_TINY, label_fg=GREEN, label_at=1)

legend(d, (margin, H-72), [
    (BLUE_LIGHT, BLUE_BORDER, "Collecte securite (SOC / Wazuh)"),
    (GREEN_LIGHT, GREEN_BORDER, "Supervision (NOC / Zabbix)"),
    (RED_LIGHT, RED_BORDER, "Pare-feu phase 1 (Palo Alto)"),
    (AMBER_LIGHT, AMBER_BORDER, "Pare-feu phase 2 (Sophos)"),
    (GRAY_LIGHT, GRAY_BORDER, "Endpoint / equipement reseau"),
])

footer(d, W, H, "Source : rapport de stage final, Figures 4.1 et 4.3 - maquette de laboratoire virtualisee, non connectee au reseau de production du CHU.")

img.save(os.path.join(OUT, "01-architecture-generale.png"))
print("saved 01")
