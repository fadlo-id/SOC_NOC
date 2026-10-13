import sys
sys.path.insert(0, r"C:\Users\ppp\AppData\Local\Temp\claude\E--linkedin\a1f9fa53-d28c-4c4d-8c52-dfafdddf1b85\scratchpad")
from diagrams import *

W, H = 1900, 980
img, d = new_canvas(W, H)
header(d, W, "Segmentation reseau et politiques de securite",
       "Zones de securite documentees par phase - adresses presentees au niveau sous-reseau (pas d'hotes individuels)")

margin = 60
panel_gap = 50
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

# ===================== Panel 1 : Palo Alto zones (phase 1) =====================
p1x0, p1x1 = panel(margin, "PHASE 1 - Zones Palo Alto (PAN-OS 11.1)", "Un reseau virtuel VMware distinct par zone de securite", (248,250,252))
cx = (p1x0+p1x1)/2

mgmt = (cx-140, panel_y0+100, cx+140, panel_y0+100+74)
device_box(d, mgmt, "server", "Management", ["192.168.67.0/24"], GRAY_LIGHT, GRAY_BORDER, INK, SUB)

fw = (cx-150, panel_y0+230, cx+150, panel_y0+230+90)
rbox(d, fw, fill=(15,23,42), outline=NAVY, width=3, radius=10)
d.text((fw[0]+20, fw[1]+16), "PA-VM", font=F_LABEL, fill=WHITE)
d.text((fw[0]+20, fw[1]+46), "politiques - NAT - filtrage URL", font=F_SMALL, fill=(203,213,225))

trust = (p1x0+30, panel_y0+230, p1x0+30+260, panel_y0+230+90)
device_box(d, trust, "endpoint", "Trust (LAN)", ["192.168.95.0/24 - hote supervise"], GREEN_LIGHT, GREEN_BORDER, GREEN, GREEN)

dmz = (cx-130, panel_y0+400, cx+130, panel_y0+400+74)
device_box(d, dmz, "server", "DMZ", ["192.168.9.0/24"], AMBER_LIGHT, AMBER_BORDER, (120,53,15), (120,53,15))

untrust = (p1x1-290, panel_y0+230, p1x1-290+260, panel_y0+230+90)
device_box(d, untrust, "cloud", "Untrust (WAN)", ["Sortie Internet (bridged)"], RED_LIGHT, RED_BORDER, RED, RED)

elbow(d, [((mgmt[0]+mgmt[2])/2, mgmt[3]), ((fw[0]+fw[2])/2, fw[1])], color=SUB, width=2, dashed=True, label="mgmt", font_obj=F_TINY, label_at=0)
elbow(d, [(trust[2], (trust[1]+trust[3])/2), (fw[0], (fw[1]+fw[3])/2)], color=GREEN, width=3)
elbow(d, [(fw[2], (fw[1]+fw[3])/2), (untrust[0], (untrust[1]+untrust[3])/2)], color=RED, width=3)
elbow(d, [((fw[0]+fw[2])/2, fw[3]), ((dmz[0]+dmz[2])/2, dmz[1])], color=(120,53,15), width=3)

rbox(d, [p1x0+24, panel_y0+500, p1x1-24, panel_y0+500+54], fill=GRAY_LIGHT, outline=GRAY_BORDER, width=1, radius=8)
d.text((p1x0+40, panel_y0+512), "Politique : Trust -> Untrust autorise (regle explicite) ; filtrage d'URL par",
       font=F_TINY, fill=SUB)
d.text((p1x0+40, panel_y0+530), "categorie personnalisee ; regle finale de rejet par defaut.",
       font=F_TINY, fill=SUB)

# ===================== Panel 2 : Sophos segmentation (phase 2) =====================
p2x0, p2x1 = panel(margin+panel_w+panel_gap, "PHASE 2 - Segmentation Sophos (laboratoire)", "Sous-reseau de laboratoire dedie 192.168.65.0/24", (253,250,244))
cx2 = (p2x0+p2x1)/2

wan = (cx2-150, panel_y0+100, cx2+150, panel_y0+100+74)
device_box(d, wan, "cloud", "WAN", ["Sortie Internet (test ICMP)"], RED_LIGHT, RED_BORDER, RED, RED)

fw2 = (cx2-150, panel_y0+220, cx2+150, panel_y0+220+90)
rbox(d, fw2, fill=(15,23,42), outline=NAVY, width=3, radius=10)
d.text((fw2[0]+20, fw2[1]+16), "Sophos XG", font=F_LABEL, fill=WHITE)
d.text((fw2[0]+20, fw2[1]+46), "5 regles, evaluees dans l'ordre", font=F_SMALL, fill=(203,213,225))

lan = (cx2-150, panel_y0+360, cx2+150, panel_y0+360+74)
device_box(d, lan, "switch", "LAN laboratoire", ["192.168.65.0/24"], GREEN_LIGHT, GREEN_BORDER, GREEN, GREEN)

elbow(d, [((wan[0]+wan[2])/2, wan[3]), ((fw2[0]+fw2[2])/2, fw2[1])], color=RED, width=3)
elbow(d, [((fw2[0]+fw2[2])/2, fw2[3]), ((lan[0]+lan[2])/2, lan[1])], color=GREEN, width=3)

hosts = (p2x0+30, panel_y0+480, p2x1-30, panel_y0+480+100)
rbox(d, hosts, fill=WHITE, outline=GRAY_BORDER, width=2, radius=10)
d.text((hosts[0]+20, hosts[1]+14), "Hotes du sous-reseau", font=F_LABEL, fill=INK)
d.text((hosts[0]+20, hosts[1]+44), "Wazuh - Zabbix - commutateur HP Aruba - clt_win11 - clt_linux", font=F_SMALL, fill=SUB)
d.text((hosts[0]+20, hosts[1]+66), "(adresses individuelles : voir docs/architecture.md)", font=F_TINY, fill=SUB)
elbow(d, [((lan[0]+lan[2])/2, lan[3]), ((hosts[0]+hosts[2])/2, hosts[1])], color=GREEN, width=2)

rbox(d, [p2x0+24, panel_y0+610, p2x1-24, panel_y0+610+54+30], fill=GRAY_LIGHT, outline=GRAY_BORDER, width=1, radius=8)
d.text((p2x0+40, panel_y0+622), "Regles (ordre d'evaluation) : 1) ping autorise vers 1.1.1.1 (test) 2) reste du trafic",
       font=F_TINY, fill=SUB)
d.text((p2x0+40, panel_y0+640), "Wazuh/Zabbix vers le WAN refuse 3) relais messagerie 4) LAN -> WAN autorise",
       font=F_TINY, fill=SUB)
d.text((p2x0+40, panel_y0+658), "5) rejet final par defaut (moindre privilege applique aux serveurs de supervision).",
       font=F_TINY, fill=SUB)

legend(d, (margin, H-72), [
    (GREEN_LIGHT, GREEN_BORDER, "Zone de confiance / LAN"),
    (RED_LIGHT, RED_BORDER, "Zone non fiable / WAN"),
    (AMBER_LIGHT, AMBER_BORDER, "DMZ"),
    (GRAY_LIGHT, GRAY_BORDER, "Management / hotes"),
])

footer(d, W, H, "Source : rapport de stage final, sections 4.5 et 5.4-5.5 (Figures 4.2, 5.10-5.13, 5.19) - maquette de laboratoire, CHU Hassan II de Fès. Adresses d'hotes individuelles omises pour cette version de diffusion.")

img.save(os.path.join(OUT, "03-segmentation-securite.png"))
print("saved 03")
