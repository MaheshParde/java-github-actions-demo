import os
import re

print("🔍 AI SOURCE CODE ANALYSIS STARTED\n")

issues = []
suggestions = []

SRC_DIR = "/workspace/src/main/java"
TEST_DIR = "/workspace/src/test/java"

# ---------- Helper checks ----------

def has_unit_test(class_name):
    if not os.path.exists(TEST_DIR):
        return False
    for root, _, files in os.walk(TEST_DIR):
        for f in files:
            if class_name in f:
                return True
    return False

# ---------- Source code analysis ----------

for root, _, files in os.walk(SRC_DIR):
    for file in files:
        if file.endswith(".java"):
            path = os.path.join(root, file)
            class_name = file.replace(".java", "")

            with open(path, "r", errors="ignore") as f:
                lines = f.readlines()
                content = "".join(lines)

            # 1️⃣ Missing unit test detection
            if not has_unit_test(class_name):
                issues.append(f"❌ Missing unit test for class: {class_name}")
                suggestions.append(
                    f"➕ Add {class_name}Test.java with tests for public methods"
                )

            # 2️⃣ System.out.println usage
            if "System.out.println" in content:
                issues.append(f"⚠ Debug print found in {file}")
                suggestions.append(
                    f"🔧 Replace System.out.println with a logger (SLF4J)"
                )

            # 3️⃣ TODO / FIXME comments
            if re.search(r"TODO|FIXME", content):
                issues.append(f"⚠ TODO/FIXME found in {file}")
                suggestions.append(
                    f"📝 Remove TODOs or convert them into Jira tickets"
                )

            # 4️⃣ Bad indentation (tabs)
            for i, line in enumerate(lines, start=1):
                if "\t" in line:
                    issues.append(f"⚠ Tab indentation at {file}:{i}")
                    suggestions.append(
                        f"🎨 Use spaces instead of tabs (4 spaces recommended)"
                    )

            # 5️⃣ Unused commented code
            if re.search(r"//\s*(int|String|if|for|while)", content):
                issues.append(f"⚠ Commented-out code found in {file}")
                suggestions.append(
                    f"🧹 Remove commented code; use Git history instead"
                )

            # 6️⃣ Empty catch blocks
            if re.search(r"catch\s*\(.*\)\s*\{\s*\}", content):
                issues.append(f"⚠ Empty catch block in {file}")
                suggestions.append(
                    f"🚨 Handle exceptions properly or log the error"
                )

# ---------- Final Report ----------

print("===== AI CODE ANALYSIS REPORT =====")

if not issues:
    print("✅ No critical issues detected")
else:
    for issue in sorted(set(issues)):
        print(issue)

print("\n===== SUGGESTED IMPROVEMENTS =====")
if not suggestions:
    print("✅ No suggestions")
else:
    for suggestion in sorted(set(suggestions)):
        print(suggestion)

print("\n===== ANALYSIS COMPLETED =====")

