"""Practicing for ...in ... loops."""

pets: list[str] = ["Louie", "Bo", "Bear"]
for animal in pets:
    print(f"Good boy, {animal}!")

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, 3):
    print(f"{idx}: {names[idx]}")