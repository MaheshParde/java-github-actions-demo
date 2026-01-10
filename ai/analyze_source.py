import os
from transformers import pipeline

print("🔍 AI SOURCE CODE ANALYSIS STARTED")

classifier = pipeline(
    "text-classification",
    model="distilbert-base-uncased"
)

issues = []

for root, _, files in os.walk("/workspace/src"):
    for file in files:
        if file.endswith(".java"):
            path = os.path.join(root, file)
            with open(path, "r", errors="ignore") as f:
                content = f.read()[:512]

            if "System.out.println" in content:
                issues.append(f"⚠ Debug print found in {path}")

            if "TODO" in content:
                issues.append(f"⚠ TODO comment found in {path}")

            result = classifier(content)[0]
            if result["label"] == "NEGATIVE":
                issues.append(f"⚠ Possible code smell in {path}")

print("\n===== AI CODE ANALYSIS REPORT =====")
if not issues:
    print("✅ No issues detected")
else:
    for issue in issues:
        print(issue)

print("===== ANALYSIS COMPLETED =====")

