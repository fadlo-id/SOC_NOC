import os, math
from PIL import Image, ImageDraw, ImageFont

OUT = "E:/linkedin/assets/soc-noc/diagrams"
os.makedirs(OUT, exist_ok=True)

# ---------- palette ----------
BG = (255, 255, 255)
GRID = (240, 242, 245)
INK = (30, 41, 59)        # dark slate text
SUB = (100, 116, 139)     # muted gray text
NAVY = (15, 23, 42)
BLUE = (37, 99, 235)
BLUE_LIGHT = (219, 234, 254)
BLUE_BORDER = (96, 165, 250)
GRAY_LIGHT = (241, 245, 249)
GRAY_BORDER = (148, 163, 184)
GREEN = (22, 101, 52)
GREEN_LIGHT = (220, 252, 231)
GREEN_BORDER = (74, 222, 128)
RED = (153, 27, 27)
RED_LIGHT = (254, 226, 226)
RED_BORDER = (248, 113, 113)
AMBER = (146, 64, 14)
AMBER_LIGHT = (254, 243, 199)
AMBER_BORDER = (251, 191, 36)
PURPLE = (88, 28, 135)
PURPLE_LIGHT = (243, 232, 255)
PURPLE_BORDER = (192, 132, 252)
WHITE = (255, 255, 255)

FONT_DIR = r"C:\Windows\Fonts"
def font(size, weight="regular"):
    paths = {
        "bold": ["segoeuib.ttf", "arialbd.ttf"],
        "semibold": ["seguisb.ttf", "segoeuib.ttf", "arialbd.ttf"],
        "regular": ["segoeui.ttf", "arial.ttf"],
    }
    for fn in paths.get(weight, paths["regular"]):
        p = os.path.join(FONT_DIR, fn)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

F_TITLE = font(34, "bold")
F_SUBTITLE = font(18, "regular")
F_H2 = font(22, "bold")
F_LABEL = font(18, "bold")
F_SMALL = font(15, "regular")
F_TINY = font(13, "regular")
F_MONO_TAG = font(13, "bold")

def new_canvas(w, h, grid=True, gap=40):
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    if grid:
        for x in range(0, w, gap):
            d.line([(x, 0), (x, h)], fill=GRID, width=1)
        for y in range(0, h, gap):
            d.line([(0, y), (w, y)], fill=GRID, width=1)
    return img, d

def header(d, w, title, subtitle, y=36):
    d.text((60, y), title, font=F_TITLE, fill=NAVY)
    d.text((60, y + 46), subtitle, font=F_SUBTITLE, fill=SUB)
    d.line([(60, y + 78), (w - 60, y + 78)], fill=(226, 232, 240), width=2)

def footer(d, w, h, text):
    d.line([(60, h - 56), (w - 60, h - 56)], fill=(226, 232, 240), width=2)
    d.text((60, h - 40), text, font=F_TINY, fill=SUB)

def rbox(d, xy, fill=WHITE, outline=GRAY_BORDER, width=2, radius=12):
    d.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)

def text_wrap(d, xy, text, font_obj, fill, max_width, line_h):
    x, y = xy
    words = text.split(" ")
    line = ""
    for wd in words:
        test = (line + " " + wd).strip()
        bbox = d.textbbox((0, 0), test, font=font_obj)
        if bbox[2] - bbox[0] > max_width and line:
            d.text((x, y), line, font=font_obj, fill=fill)
            y += line_h
            line = wd
        else:
            line = test
    if line:
        d.text((x, y), line, font=font_obj, fill=fill)
    return y + line_h

def device_box(d, xy, kind, title, subtitle_lines, fill, border, title_color, icon_color):
    x0, y0, x1, y1 = xy
    rbox(d, xy, fill=fill, outline=border, width=3, radius=10)
    icon(d, kind, (x0 + 20, y0 + 18), 34, icon_color)
    d.text((x0 + 68, y0 + 18), title, font=F_LABEL, fill=title_color)
    ty = y0 + 50
    for ln in subtitle_lines:
        d.text((x0 + 20, ty), ln, font=F_SMALL, fill=SUB)
        ty += 22

def icon(d, kind, origin, size, color):
    """Simple geometric glyphs (no vendor logos)."""
    x, y = origin
    s = size
    lw = max(2, s // 14)
    if kind == "server":
        d.rounded_rectangle([x, y, x + s, y + s], radius=4, outline=color, width=lw)
        for i in range(3):
            yy = y + 6 + i * (s - 12) // 3
            d.line([(x + 6, yy), (x + s - 6, yy)], fill=color, width=lw)
            d.ellipse([x + s - 12, yy - 2, x + s - 8, yy + 2], fill=color)
    elif kind == "firewall":
        rows, cols = 2, 3
        bw, bh = s / cols, s / rows
        for r in range(rows):
            offset = (bw / 2) if r % 2 else 0
            for c in range(-1, cols + 1):
                bx0 = x + c * bw + offset
                by0 = y + r * bh
                bx1, by1 = bx0 + bw - 4, by0 + bh - 4
                if bx1 < x or bx0 > x + s:
                    continue
                d.rectangle([max(bx0, x), by0, min(bx1, x + s), by1], outline=color, width=lw)
    elif kind == "switch":
        d.rounded_rectangle([x, y + s * 0.3, x + s, y + s * 0.7], radius=3, outline=color, width=lw)
        for i in range(5):
            px = x + 6 + i * (s - 12) / 4
            d.line([(px, y + s * 0.7), (px, y + s * 0.85)], fill=color, width=lw)
    elif kind == "endpoint":
        d.rectangle([x, y, x + s, y + s * 0.68], outline=color, width=lw)
        d.line([(x + s * 0.5, y + s * 0.68), (x + s * 0.5, y + s * 0.85)], fill=color, width=lw)
        d.line([(x + s * 0.25, y + s * 0.92), (x + s * 0.75, y + s * 0.92)], fill=color, width=lw)
    elif kind == "shield":
        pts = [(x + s * 0.5, y), (x + s, y + s * 0.22), (x + s, y + s * 0.55),
               (x + s * 0.5, y + s), (x, y + s * 0.55), (x, y + s * 0.22)]
        d.polygon(pts, outline=color, width=lw)
        d.line([(x + s * 0.28, y + s * 0.5), (x + s * 0.45, y + s * 0.68)], fill=color, width=lw + 1)
        d.line([(x + s * 0.45, y + s * 0.68), (x + s * 0.75, y + s * 0.32)], fill=color, width=lw + 1)
    elif kind == "gauge":
        d.ellipse([x, y, x + s, y + s], outline=color, width=lw)
        cx, cy = x + s / 2, y + s / 2
        d.line([(cx, cy), (cx + s * 0.3, cy - s * 0.2)], fill=color, width=lw)
        d.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=color)
    elif kind == "cloud":
        d.ellipse([x, y + s * 0.3, x + s * 0.5, y + s * 0.8], outline=color, width=lw)
        d.ellipse([x + s * 0.3, y, x + s * 0.9, y + s * 0.7], outline=color, width=lw)
        d.ellipse([x + s * 0.55, y + s * 0.35, x + s, y + s * 0.85], outline=color, width=lw)
    elif kind == "doc":
        d.rectangle([x + s * 0.15, y, x + s * 0.85, y + s], outline=color, width=lw)
        for i in range(3):
            yy = y + s * 0.25 + i * s * 0.2
            d.line([(x + s * 0.28, yy), (x + s * 0.72, yy)], fill=color, width=lw)

def arrow(d, p1, p2, color=INK, width=3, dashed=False, label=None, font_obj=None, label_bg=WHITE, label_fg=None, perp_offset=0):
    x0, y0 = p1
    x1, y1 = p2
    if dashed:
        dist = math.hypot(x1 - x0, y1 - y0)
        n = max(1, int(dist // 10))
        for i in range(n):
            t0 = i / n
            t1 = t0 + 0.5 / n
            if t1 > 1:
                t1 = 1
            sx = x0 + (x1 - x0) * t0
            sy = y0 + (y1 - y0) * t0
            ex = x0 + (x1 - x0) * t1
            ey = y0 + (y1 - y0) * t1
            d.line([(sx, sy), (ex, ey)], fill=color, width=width)
    else:
        d.line([(x0, y0), (x1, y1)], fill=color, width=width)
    ang = math.atan2(y1 - y0, x1 - x0)
    L = 12
    a1 = (x1 - L * math.cos(ang - 0.4), y1 - L * math.sin(ang - 0.4))
    a2 = (x1 - L * math.cos(ang + 0.4), y1 - L * math.sin(ang + 0.4))
    d.polygon([p2, a1, a2], fill=color)
    if label:
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        my += perp_offset
        bbox = d.textbbox((0, 0), label, font=font_obj)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        pad = 5
        d.rectangle([mx - tw / 2 - pad, my - th / 2 - pad, mx + tw / 2 + pad, my + th / 2 + pad], fill=label_bg)
        d.text((mx - tw / 2, my - th / 2), label, font=font_obj, fill=(label_fg or color))

def elbow(d, points, color=INK, width=3, dashed=False, label=None, font_obj=None, label_bg=WHITE, label_fg=None, label_at=-1):
    """Draw an orthogonal multi-segment connector through `points` (list of (x,y)), arrowhead at the end."""
    for i in range(len(points) - 1):
        p1, p2 = points[i], points[i + 1]
        if dashed:
            x0, y0 = p1
            x1, y1 = p2
            dist = math.hypot(x1 - x0, y1 - y0)
            n = max(1, int(dist // 10))
            for k in range(n):
                t0 = k / n
                t1 = min(1, t0 + 0.5 / n)
                sx, sy = x0 + (x1 - x0) * t0, y0 + (y1 - y0) * t0
                ex, ey = x0 + (x1 - x0) * t1, y0 + (y1 - y0) * t1
                d.line([(sx, sy), (ex, ey)], fill=color, width=width)
        else:
            d.line([p1, p2], fill=color, width=width)
    # arrowhead on last segment
    x0, y0 = points[-2]
    x1, y1 = points[-1]
    ang = math.atan2(y1 - y0, x1 - x0)
    L = 12
    a1 = (x1 - L * math.cos(ang - 0.4), y1 - L * math.sin(ang - 0.4))
    a2 = (x1 - L * math.cos(ang + 0.4), y1 - L * math.sin(ang + 0.4))
    d.polygon([points[-1], a1, a2], fill=color)
    if label:
        p1, p2 = points[label_at - 1], points[label_at]
        mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
        bbox = d.textbbox((0, 0), label, font=font_obj)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        pad = 5
        d.rectangle([mx - tw / 2 - pad, my - th / 2 - pad, mx + tw / 2 + pad, my + th / 2 + pad], fill=label_bg)
        d.text((mx - tw / 2, my - th / 2), label, font=font_obj, fill=(label_fg or color))

def legend(d, xy, items):
    x, y = xy
    for fill, border, label in items:
        d.rounded_rectangle([x, y, x + 22, y + 16], radius=3, fill=fill, outline=border, width=2)
        d.text((x + 30, y - 2), label, font=F_SMALL, fill=INK)
        bbox = d.textbbox((0, 0), label, font=F_SMALL)
        x += 30 + (bbox[2] - bbox[0]) + 28

print("lib loaded")
