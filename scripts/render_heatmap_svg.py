import json

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]

def render_svg():
    with open("data/contributions.json", "r", encoding="utf-8") as f:
        days = json.load(f)
    box_size = 11
    gap = 4
    width = 53 * (box_size + gap) + 40 
    height = 7 * (box_size + gap) + 40
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">']
    svg.append('<style>')
    svg.append('  .day { opacity: 0; animation: slideDown 0.5s ease forwards; }')
    svg.append('  @keyframes slideDown {')
    svg.append('    0% { opacity: 0; transform: translateY(-10px); }')
    svg.append('    100% { opacity: 1; transform: translateY(0); }')
    svg.append('  }')
    svg.append('</style>')
    svg.append(f'<rect width="{width}" height="{height}" fill="#0d1117" rx="8" />')
    svg.append('<g transform="translate(20, 20)">')
    for i, day in enumerate(days):
        week = i // 7
        day_of_week = i % 7
        x = week * (box_size + gap)
        y = day_of_week * (box_size + gap)
        color = PALETTE[day["level"]]
        delay = (week * 0.02) + (day_of_week * 0.02)
        svg.append(f'  <rect class="day" x="{x}" y="{y}" width="{box_size}" height="{box_size}" rx="2" fill="{color}" style="animation-delay: {delay:.2f}s" />')
    svg.append('</g>\n</svg>')
    with open("contrib-heatmap.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print("Heatmap animado gerado em contrib-heatmap.svg")

if __name__ == "__main__":
    render_svg()