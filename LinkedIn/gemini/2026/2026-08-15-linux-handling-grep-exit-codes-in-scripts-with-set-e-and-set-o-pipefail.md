The Grep Spell 🤯

Ever had a Bash script silently crash without printing any error message, leaving you scratching your head? 🤯

If you write strict Bash scripts with `set -e` and `set -o pipefail`, `grep` might be the culprit silently killing your execution!

### 🚨 The Core Issue & Consequences

Unix tools usually return `0` for success and non-zero for errors. But `grep` uses exit status for search outcome:
- **`0`**: Matching lines found.
- **`1`**: **No matching lines found** (a completely normal search outcome!).
- **`2` (+ higher)**: Real syntax or file access error.

💥 **The Consequences:**
1. **With `set -e`**: If `grep` finds no matches, it exits with `1`. Bash interprets `1` as a command failure and **aborts the script instantly** before subsequent lines run!
2. **With `set -o pipefail`**: In a pipeline (e.g., `cat app.log | grep "CRITICAL" | wc -l`), `grep`'s exit code `1` propagates as the pipeline exit status—causing `set -e` to kill the script before assigning output variables.

---

### 💡 4 Practical Solutions Briefly Explained

1️⃣ **`grep ... || true`**: Appending `|| true` turns non-zero exits into `0` so `set -e` won't abort *(Quick fix, but masks code 2 real errors)*.

2️⃣ **Conditional Testing (`if` / `$?`)**: Wrapping in `if grep ...` or checking `$?` prevents triggering `set -e` and lets you cleanly handle code `1` vs code `2`.

3️⃣ **`awk` Pipeline Filtering**: Replace `grep` with `awk '/pattern/'`. `awk` returns `0` even when 0 lines match, keeping `set -o pipefail` happy while still failing on syntax/file errors.

4️⃣ **Temporary Flag Toggling**: Toggle `set +e` / `set +o pipefail` around `grep` blocks and re-enable strict mode right after.

---

📖 **Read the full article for code examples and a detailed solution comparison table:**  
👉 https://fortune9.netlify.app/2026/08/15/linux-handling-grep-exit-codes-in-scripts-with-set-e-and-set-o-pipefail/

#Linux #Bash #ShellScripting #DevOps #SystemAdministration #SoftwareEngineering #Automation #Programming
