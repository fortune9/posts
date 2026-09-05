📄 **Tired of manually extracting paystub data? Automate ADP PDF parsing with AI Agent Skills!** 💼

Recently, while applying for unemployment benefits at EDD (which requires an 18-month payment history), I was faced with a daunting chore: opening dozens of ADP paystub PDFs one by one, hunting down pay dates and gross amounts, and tedious copy-pasting into forms.

Instead of spending hours on manual data entry, I built a reusable AI agent skill to handle it end-to-end: **`parse_adp_gross_pay`**! 🚀

---

🎯 **Why this skill works**:

1️⃣ **Structured CSV Output**: Automatically extracts key fields (`Period Beginning`, `Period Ending`, `Pay Date`, `Gross Pay`) across all your ADP paystubs into a clean, ready-to-use CSV table. And these fields are customizable.
2️⃣ **100% Verifiable**: Financial numbers must be accurate. The skill converts PDFs using layout-preserving text, records 1-indexed line numbers (`Beg Line`, `End Line`, `Gross Line`) in retained `.txt` files, and asks you to confirm values against exact lines. No hallucinated figures!
3️⃣ **Privacy-First & Token-Efficient**: Your paystubs contain sensitive personal financial data. Instead of dumping raw PDFs into LLM context tokens (costly and insecure), it uses a lightweight local extraction script (created first when you use the skill for the first time) + `pdftotext` locally on your machine.
4️⃣ **Cross-Agent Compatible**: Tested and verified on both **`antigravity-cli`** and **`qwen-code`**.
5️⃣ **Automated Dependency Setup**: Checks for `python3` and `pdftotext` (`poppler-utils`) and installs them automatically, with a clean human fallback if permissions require manual setup.

> *Note: This skill is specifically optimized for ADP paystub layouts (adp.com). It may need some adjustments for other payroll providers.*

---

📦 **How to Install & Use**:

Install directly into your favorite agent CLI in one command:

```bash
npx skills add fortune9/Agent_skills --skill parse_adp_gross_pay
```

Then simply prompt your agent:
> *"Extract gross pay and pay dates from all ADP PDFs in my `./paystubs` directory into a CSV file."*

---

🔗 **Explore the Skill & Code**:  
Check out the full implementation on GitHub:  
https://github.com/fortune9/Agent_skills/tree/main/job-transition/parse_adp_gross_pay

If you're dealing with a stack of ADP paystubs or navigating unemployment/mortgage applications, give it a try! Feedback and contributions are welcome.

What tedious administrative tasks have you automated with AI agents recently? Let's discuss below! 👇

#AIAgents #AgentSkills #Automation #OpenSource #Python #Productivity #DeveloperTools #Antigravity #QwenCode #JobTransition
