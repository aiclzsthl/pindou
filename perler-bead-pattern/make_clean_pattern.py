#!/usr/bin/env python3
"""Hand-crafted clean perler-bead patterns for the birthday tabby cat."""

from __future__ import annotations

from collections import Counter, OrderedDict
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent
ART = Path("/opt/cursor/artifacts/perler")
OUT.mkdir(exist_ok=True)
ART.mkdir(parents=True, exist_ok=True)

C: OrderedDict[str, tuple[int, int, int] | None] = OrderedDict(
    [
        (".", None),
        ("K", (35, 35, 35)),  # 黑色
        ("D", (96, 58, 34)),  # 深棕描边/条纹
        ("B", (168, 112, 68)),  # 中棕毛色
        ("T", (210, 168, 118)),  # 浅棕高光
        ("W", (250, 250, 250)),  # 白色口鼻
        ("P", (255, 160, 180)),  # 粉色帽子/围嘴
        ("R", (220, 55, 70)),  # 红色爱心/绒球
        ("H", (235, 105, 130)),  # 深粉围嘴边
        ("Y", (255, 215, 70)),  # 黄色帽纹
        ("G", (140, 210, 165)),  # 薄荷绿帽纹
        ("U", (120, 195, 230)),  # 浅蓝帽纹
        ("A", (235, 165, 45)),  # 琥珀色眼睛
        ("N", (255, 150, 165)),  # 鼻粉
    ]
)

NAME = {
    "K": "黑色",
    "D": "深棕",
    "B": "中棕",
    "T": "浅棕",
    "W": "白色",
    "P": "粉色",
    "R": "红色",
    "H": "深粉",
    "Y": "黄色",
    "G": "薄荷绿",
    "U": "浅蓝",
    "A": "琥珀色",
    "N": "鼻粉",
}


def row(s: str, width: int) -> str:
    s = "".join(s.split())
    if len(s) != width:
        raise ValueError(f"row len {len(s)} != {width}: {s}")
    bad = [ch for ch in s if ch not in C]
    if bad:
        raise ValueError(f"bad colors {bad} in {s}")
    return s


# =====================================================================
# Recommended 29×36 — readable cat head + party hat + bib heart
# Columns: 12345678901234567890123456789
# =====================================================================
PATTERN_29 = [
    row(".............RR..............", 29),  # 01 pom
    row("............PPPP.............", 29),  # 02
    row("...........PPPPPP............", 29),  # 03
    row("..........PYYYYYYP...........", 29),  # 04 yellow
    row(".........PYYYYYYYYP..........", 29),  # 05
    row("........PGGGGGGGGGGP.........", 29),  # 06 mint
    row(".......PUUUUUUUUUUUUP........", 29),  # 07 blue
    row("......PPPPPPPPPPPPPPPP.......", 29),  # 08 brim
    row(".....DD.BBBBBBBBBBB.DD.......", 29),  # 09 pointed ear tips
    row("....DBPDBBBBBBBBBBBBDPBD.....", 29),  # 10 pink inner ears
    row("....DBBPBBBBBBDBBBBBPBBD.....", 29),  # 11
    row("....DBBBBBBBBDDDBBBBBBBD.....", 29),  # 12 tabby
    row("....DBBBBBBBDDDDDBBBBBBD.....", 29),  # 13 forehead M
    row("....DBBBBBBBDDDDDBBBBBBD.....", 29),  # 14
    row("....DBBBBBBBDBBBDBBBBBBD.....", 29),  # 15 brow
    row("....DBBBBBAABBBBBAABBBBD.....", 29),  # 16 amber eyes
    row("....DBBBBBKAKBBBBKAKBBBD.....", 29),  # 17 pupils
    row("....DBBBBBAABBBBBAABBBBD.....", 29),  # 18
    row("....DBBBBBBBBBNBBBBBBBBD.....", 29),  # 19 nose
    row("....DBBBBBBWWWWWWWBBBBBD.....", 29),  # 20 white muzzle
    row("....DBBBBBWWWWWWWWWBBBBD.....", 29),  # 21
    row("....DBBBBBBWWWKWWWBBBBBD.....", 29),  # 22 mouth
    row(".....DBBBBBBWWWWWBBBBBD......", 29),  # 23 chin
    row("......DBBBBBBBBBBBBBBD.......", 29),  # 24 jaw
    row("......DHHHHHHHHHHHHHHD.......", 29),  # 25 bib rim
    row(".......HPPPPPPPPPPPPH........", 29),  # 26
    row(".......HPPPPRRPRRPPPH........", 29),  # 27 heart lobes
    row(".......HPPPPRRRRRPPPH........", 29),  # 28
    row(".......HPPPPPRRRPPPPH........", 29),  # 29
    row(".......HPPPPPPRPPPPPH........", 29),  # 30 heart tip
    row(".......HPPPPPPPPPPPPH........", 29),  # 31
    row("........HHHHHHHHHHHH.........", 29),  # 32
    row(".........BBBBBBBBBB..........", 29),  # 33 chest
    row(".........BBB....BBB..........", 29),  # 34 paws
    row("..........BB....BB...........", 29),  # 35
]

# Mini 23×29
PATTERN_23 = [
    row("..........RR...........", 23),
    row(".........PPPP..........", 23),
    row("........PYYYYP.........", 23),
    row(".......PGGGGGGP........", 23),
    row("......PUUUUUUUUP.......", 23),
    row(".....PPPPPPPPPPPP......", 23),
    row("....DD.BBBBBBB.DD......", 23),
    row("...DBPDBBBBBBBBDPBD....", 23),
    row("...DBBPBBBBBDBBPBBD....", 23),
    row("...DBBBBBBDDDBBBBBD....", 23),
    row("...DBBBBBDDDDDBBBBD....", 23),
    row("...DBBBBAABBBBAABBD....", 23),
    row("...DBBBBKAKBBBKAKBD....", 23),
    row("...DBBBBBBBNBBBBBBD....", 23),
    row("...DBBBBWWWWWWWBBBD....", 23),
    row("...DBBBWWWWWWWWWBBD....", 23),
    row("...DBBBBWWWKWWWBBBD....", 23),
    row("....DBBBBWWWWWBBBD.....", 23),
    row(".....DBBBBBBBBBBD......", 23),
    row(".....DHHHHHHHHHHD......", 23),
    row("......HPPPPPPPPH.......", 23),
    row("......HPPPRRPRPPH......", 23),
    row("......HPPPRRRRPPH......", 23),
    row("......HPPPPRRPPPH......", 23),
    row("......HPPPPPRPPPH......", 23),
    row("......HPPPPPPPPH.......", 23),
    row(".......HHHHHHHH........", 23),
    row("........BBBBBB.........", 23),
    row("........BB..BB.........", 23),
]


def load_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    path = (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    )
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


def render(pattern: list[str], cell: int, title: str):
    h = len(pattern)
    w = len(pattern[0])
    pix = Image.new("RGB", (w, h), (255, 255, 255))
    px = pix.load()
    counts: Counter[str] = Counter()
    for y, r in enumerate(pattern):
        for x, ch in enumerate(r):
            if ch == "." or C[ch] is None:
                px[x, y] = (255, 255, 255)
            else:
                px[x, y] = C[ch]  # type: ignore[assignment]
                counts[ch] += 1

    scale = 18
    preview = pix.resize((w * scale, h * scale), Image.Resampling.NEAREST)
    pd = ImageDraw.Draw(preview)
    for x in range(0, w * scale + 1, scale):
        pd.line([(x, 0), (x, h * scale)], fill=(225, 225, 225), width=1)
    for y in range(0, h * scale + 1, scale):
        pd.line([(0, y), (w * scale, y)], fill=(225, 225, 225), width=1)

    grid = pix.resize((w * cell, h * cell), Image.Resampling.NEAREST)
    draw = ImageDraw.Draw(grid)
    for x in range(0, w * cell + 1, cell):
        draw.line([(x, 0), (x, h * cell)], fill=(150, 150, 150), width=1)
    for y in range(0, h * cell + 1, cell):
        draw.line([(0, y), (w * cell, y)], fill=(150, 150, 150), width=1)

    # letter overlay on grid for easy following
    font_cell = load_font(max(9, cell // 2 - 2))
    for y, r in enumerate(pattern):
        for x, ch in enumerate(r):
            if ch == ".":
                continue
            # pick contrasting text color
            rgb = C[ch]
            assert rgb is not None
            lum = 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]
            fill = (255, 255, 255) if lum < 140 else (40, 40, 40)
            tx, ty = x * cell + cell // 3 - 1, y * cell + cell // 4 - 1
            draw.text((tx, ty), ch, fill=fill, font=font_cell)

    axis = 34
    chart = Image.new("RGB", (w * cell + axis, h * cell + axis), (255, 255, 255))
    chart.paste(grid, (axis, axis))
    cd = ImageDraw.Draw(chart)
    font = load_font(11)
    font_b = load_font(18, bold=True)
    font_m = load_font(15)
    for x in range(w):
        if x % 5 == 0:
            cd.text((axis + x * cell + 4, 8), str(x + 1), fill=(80, 80, 80), font=font)
    for y in range(h):
        if y % 5 == 0:
            cd.text((4, axis + y * cell + 5), str(y + 1), fill=(80, 80, 80), font=font)

    used = [(ch, counts[ch]) for ch in C if ch in counts]
    used.sort(key=lambda t: -t[1])
    legend_h = 96 + 32 * len(used)
    legend_w = max(560, chart.size[0])
    legend = Image.new("RGB", (legend_w, legend_h), (255, 255, 255))
    ld = ImageDraw.Draw(legend)
    total = sum(counts.values())
    ld.text((16, 14), f"{title}  ·  {w}×{h}", fill=(20, 20, 20), font=font_b)
    ld.text(
        (16, 44),
        f"总豆数: {total}    颜色数: {len(used)}    “.” = 留空不拼",
        fill=(90, 90, 90),
        font=font_m,
    )
    y0 = 78
    for ch, cnt in used:
        rgb = C[ch]
        assert rgb is not None
        ld.rectangle([16, y0, 42, y0 + 24], fill=rgb, outline=(0, 0, 0))
        ld.text(
            (54, y0 + 2),
            f"{ch}  {NAME[ch]}  RGB{rgb}  × {cnt}",
            fill=(20, 20, 20),
            font=font_m,
        )
        y0 += 32

    sheet = Image.new(
        "RGB",
        (max(chart.size[0], legend_w), chart.size[1] + legend_h + 16),
        (255, 255, 255),
    )
    sheet.paste(chart, ((sheet.size[0] - chart.size[0]) // 2, 0))
    sheet.paste(legend, ((sheet.size[0] - legend_w) // 2, chart.size[1] + 8))

    lines = [
        f"# {title}",
        f"尺寸: {w}x{h}",
        f"总豆数: {total}",
        "",
        "色号统计:",
    ]
    for ch, cnt in used:
        lines.append(f"  {ch} {NAME[ch]} RGB{C[ch]} × {cnt}")
    lines += ["", "字母网格（. = 留空）:", ""]
    lines.append("   " + "".join(str((i + 1) % 10) for i in range(w)))
    for i, r in enumerate(pattern, 1):
        lines.append(f"{i:02d} {r}")
    return preview, grid, sheet, "\n".join(lines), total, used, w, h


def save_set(pattern: list[str], cell: int, title: str, tag: str) -> None:
    preview, grid, sheet, text, total, used, w, h = render(pattern, cell, title)
    stem = f"{w}x{h}"
    preview.save(OUT / f"10-{tag}-preview-{stem}.png")
    grid.save(OUT / f"11-{tag}-grid-{stem}.png")
    sheet.save(OUT / f"12-{tag}-sheet-{stem}.png")
    (OUT / f"13-{tag}-guide-{stem}.txt").write_text(text, encoding="utf-8")
    preview.save(ART / f"{tag}-preview-{stem}.png")
    sheet.save(ART / f"{tag}-sheet-{stem}.png")
    grid.save(ART / f"{tag}-grid-{stem}.png")
    print(f"{tag} {stem}: {total} beads, {len(used)} colors")


def main() -> None:
    save_set(PATTERN_29, cell=20, title="生日猫拼豆图纸（推荐）", tag="clean")
    save_set(PATTERN_23, cell=22, title="生日猫拼豆图纸（迷你）", tag="mini")
    src = Path("/opt/cursor/artifacts/assets/cat-birthday-optimized.png")
    if src.exists():
        Image.open(src).save(ART / "00-optimized-illustration.png")
        Image.open(src).save(OUT / "00-optimized-source.png")

    # README for the pack
    readme = """# 生日猫拼豆图纸

根据原照片做了两步优化：

1. **简化构图**：只保留猫脸 + 彩虹生日帽 + 粉色围嘴爱心（去掉蛋糕、盘子、烛光、复杂毛发与文字）。
2. **像素图纸**：按拼豆友好色盘手绘网格，附色号与数量。

## 推荐使用

| 文件 | 说明 |
|------|------|
| `00-optimized-source.png` | 简化后的插画参考 |
| `10-clean-preview-29x35.png` | 推荐版效果预览 |
| `11-clean-grid-29x35.png` | 推荐版格子+色号图 |
| `12-clean-sheet-29x35.png` | 推荐版完整图纸（含统计） |
| `13-clean-guide-29x35.txt` | 字母网格与豆数清单 |
| `10-mini-preview-23x29.png` | 迷你版效果预览 |
| `12-mini-sheet-23x29.png` | 迷你版完整图纸 |

> 实际文件名以生成结果中的宽高为准。

## 拼豆建议

- 推荐版约 **29×35**，适合大方板或两块板拼接。
- 迷你版约 **23×29**，可放进常见 29 孔方板。
- 背景白格（`.`）留空不拼。
- 颜色可按家中现有豆色就近替换同色系。
"""
    (OUT / "README.md").write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    main()
