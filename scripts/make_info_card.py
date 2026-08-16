import os

def generate_info_card():
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" width="490" height="380">
<style>
    .text { font-family: 'Courier New', Courier, monospace; font-size: 14px; fill: #c9d1d9; }
    .title { font-weight: bold; font-size: 16px; fill: #58a6ff; }
    .key { font-weight: bold; }
    .line { opacity: 0; animation: fadeIn 0.5s ease forwards; }
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateX(-10px); }
        100% { opacity: 1; transform: translateX(0); }
    }
</style>
<rect width="490" height="380" fill="#0d1117" rx="8" />
<g class="text" transform="translate(20, 30)">
    <text class="title line" style="animation-delay: 0.1s" y="0">guilherme@github</text>
    <text class="line" style="animation-delay: 0.2s" y="20">-----------------------------------------------</text>
'''
    lines = [
        ("Role", "Software Engineering Student @ FIAP", "#58a6ff", 100),
        ("Location", "Guarulhos, SP, Brazil", "#3fb950", 100),
        ("Stack", "Full Stack, Python, Flask, Jinja, JS, SQL", "#d2a8ff", 100),
        ("Interests", "Machine Learning, AI, Data Architecture", "#f0883e", 100),
        ("Projects", "", "#ff7b72", 100),
        (" ├─", "PassaBola (Web App)", "#79c0ff", 40),
        (" ├─", "SkillSync (GenAI Platform)", "#79c0ff", 40),
        (" ├─", "Análise de Desempenho", "#79c0ff", 40),
        (" └─", "Stock Flow (CS50 Final Project)", "#79c0ff", 40),
        ("Hobbies", "Weightlifting, F1, Rick & Morty, Anime", "#ffa657", 100)
    ]
    y_offset = 50
    delay = 0.3
    for key, val, color, x_offset in lines:
        suffix = ":" if key not in [" ├─", " └─", "Projects"] else ""
        if key == "Projects":
            suffix = ":"
        svg_content += f'    <text class="line" style="animation-delay: {delay:.2f}s" y="{y_offset}">\n'
        svg_content += f'        <tspan class="key" fill="{color}">{key}{suffix}</tspan>\n'
        svg_content += f'        <tspan x="{x_offset}">{val}</tspan>\n'
        svg_content += f'    </text>\n'
        y_offset += 25
        delay += 0.15
    svg_content += '</g>\n</svg>'
    output_path = os.path.join(os.getcwd(), "info-card.svg")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Info card gerado com sucesso em: {output_path}")

if __name__ == "__main__":
    generate_info_card()