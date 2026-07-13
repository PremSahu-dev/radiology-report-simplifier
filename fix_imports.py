from pathlib import Path

replacements = {
    "from preprocessing.": "from ai_model.preprocessing.",
    "from datasets.": "from ai_model.datasets.",
    "from models.": "from ai_model.models.",
    "from training.": "from ai_model.training.",
    "from explainability.": "from ai_model.explainability.",
    "from report_generator.": "from ai_model.report_generator.",
    "from config import": "from ai_model.config import",
}

root = Path("ai_model")

count = 0

for file in root.rglob("*.py"):
    print("Checking:", file)
    text = file.read_text(encoding="utf-8")

    original = text

    for old, new in replacements.items():
        text = text.replace(old, new)

    if text != original:
        file.write_text(text, encoding="utf-8")
        print("Fixed:", file)
        count += 1

print()
print("Finished.")
print("Files modified:", count)