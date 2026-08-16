import cv2

def generate_ascii_svg():
    img = cv2.imread("source-prepped.png", cv2.IMREAD_GRAYSCALE)
    if img is None:
        return print("Erro: source-prepped.png não encontrado.")
    img_resized = cv2.resize(img, (100, 53))
    RAMP = " .`:-=+*cs#%@"
    svg_width, svg_height = 650, 650
    line_height = 12
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">']
    svg.append('<style>')
    svg.append('  .ascii { font-family: "Courier New", monospace; font-size: 11px; fill: #c9d1d9; font-weight: bold; }')
    svg.append('</style>')
    svg.append(f'<rect width="{svg_width}" height="{svg_height}" fill="#0d1117" rx="8" />')
    svg.append('<defs>')
    begin_time = 0.5
    for i in range(53):
        svg.append(f'  <clipPath id="wipe-{i}">')
        svg.append(f'    <rect x="0" y="{i * line_height - 10}" width="0" height="{line_height + 5}">')
        svg.append(f'      <animate attributeName="width" from="0" to="{svg_width}" begin="{begin_time:.2f}s" dur="0.05s" fill="freeze" />')
        svg.append(f'    </rect>')
        svg.append(f'  </clipPath>')
        begin_time += 0.04
    svg.append('</defs>')
    svg.append('<g class="ascii" transform="translate(15, 20)">')
    for i, row in enumerate(img_resized):
        ascii_row = "".join([RAMP[int((255 - px) / 255.0 * (len(RAMP) - 1))] for px in row])
        escaped = ascii_row.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        svg.append(f'  <text y="{i * line_height}" clip-path="url(#wipe-{i})" xml:space="preserve">{escaped}</text>')
    svg.append('</g>\n</svg>')
    with open("guilherme-ascii.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print("Arte final gerada com sucesso: guilherme-ascii.svg")

if __name__ == "__main__":
    generate_ascii_svg()