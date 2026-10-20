"""Minimal end-to-end example of the Helios kit with placeholder content. Needs no image files.
Run: python3 example_helios_deck.py
Optional: Deck(banner, logo="official-lockup.png", photos_dir="photos") if the user supplies those files."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from helios_kit import Deck

d = Deck("Team Q4 Kickoff")
d.title("Team", "Q4 Kickoff", "One plain-language line about the quarter")
d.agenda([("01", "Q3 in review"), ("02", "Why this work"), ("03", "Q4 projects")])
d.section("01", "Q3 in review")
d.welcome("Welcome to the team", [("Pat Example", "Engineer", "Joined us this quarter", "pat"), ("Sam Example", "Designer", "Joined the team as our designer", "sam")])
d.cards("Q3: what we delivered", [("Project one", ["Thing built", "Thing shipped"]), ("Project two", ["Thing built"]), ("Project three", ["Thing built"])])
d.rows("Q3: platform and tooling", [("Area one", "Plain description of the outcome"), ("Area two", "Plain description of the outcome")])
d.scorecard("Q3 scorecard", [("Category", "00", "Plain label")] * 8)
d.shoutouts("Q3 shoutouts", [("Ada Example", "Release wrangler", "Automated releases"), ("Bo Example", "Query tuner", "Sped up a slow page")])
d.section("02", "Why this work")
d.cascade("Why this work", ["Company goal", "Priority", "Our Q4 work"], [("Goal one", "metric today", "Priority one", "why it matters", "Project A", "plain outcome")], ["Line one in accent", "Line two plain"])
d.statement([("Muted setup line.", "mute"), ("White punchline.", "fg"), ("Purple takeaway.", "acc")])
d.big("Project name", "Q4", "One-sentence description of the project.", ["Key fact in white", "Supporting fact in grey"])
d.notes("Speaker notes go to the sidecar markdown file by default.")
d.close("Thank you")
d.save("example-helios.pptx"); print("saved example-helios.pptx")
