"""Generates src/guydai-islands.theme.json from src/guydai.theme.json.

Run after editing the classic theme so both stay in sync:  python make_islands.py
"""
import json
from pathlib import Path

SRC = Path(__file__).parent / "src"

ISLAND = "#030507"  # islands surface = default editor background (GuydAI Pure Black)
GAP = "#1a2236"     # main-window gaps; JetBrains asks for >=1.2:1 contrast vs islands on dark themes
CLEAR = GAP + "00"

theme = json.loads((SRC / "guydai.theme.json").read_text(encoding="utf-8"))

theme["name"] = "GuydAI Islands"
theme["parentTheme"] = "Islands Dark"
theme["colors"]["chrome"] = ISLAND
theme["colors"]["black"] = GAP
theme["colors"]["island"] = ISLAND
theme["colors"]["gap"] = GAP

ui = theme["ui"]
ui["Islands"] = 1
ui["Island.borderColor"] = ISLAND
ui["Island.arc"] = 20
ui["Island.arc.compact"] = 16
ui["Island.borderWidth"] = 5
ui["Island.borderWidth.compact"] = 4
ui["Island.inactiveAlpha"] = 0.44
ui["MainWindow.background"] = GAP

ui["ToolWindow"]["background"] = ISLAND
ui["ToolWindow"]["Header"].update(background=ISLAND, inactiveBackground=ISLAND, borderColor=ISLAND + "00")
ui["ToolWindow.Stripe.borderColor"] = CLEAR
ui["MainToolbar"]["borderColor"] = CLEAR
ui["StatusBar"].update(background=GAP, borderColor=CLEAR)
ui["NavBar"].update(background=GAP, borderColor=CLEAR)

ui["EditorTabs"].update(
    background=ISLAND,
    underlinedTabBackground=ISLAND,
    inactiveUnderlinedTabBackground=ISLAND,
    underlinedBorderColor="blue",
    inactiveUnderlinedTabBorderColor="border",
    borderColor=ISLAND + "00",
)

ordered = {k: theme[k] for k in ("name", "dark", "author", "editorScheme", "parentTheme")}
ordered.update({k: v for k, v in theme.items() if k not in ordered})

out = SRC / "guydai-islands.theme.json"
out.write_text(json.dumps(ordered, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Wrote {out}")
