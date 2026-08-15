🚀 **Turn Your Local PDF Library into a Searchable Database!** 📚🔍

If you're a researcher or developer, you probably have a folder overflowing with research papers and PDFs. Finding that one specific paper can feel like searching for a needle in a haystack.

To solve this, I built **`pdf.db.builder`** — a lightweight tool that parses your local PDFs and spins up a fully searchable database with a Shiny web interface.

### How it works:
1️⃣ **GROBID Metadata Extraction**: It connects to a local GROBID service (run via Docker) to extract key bibliographic metadata: title, authors, year, abstract, journal, and DOI.
2️⃣ **SQLite + FTS5 Database**: The parsed metadata is ingested into a SQLite database with a full-text search (FTS5) index, allowing for lightning-fast keyword queries and ranking.
3️⃣ **Incremental Builds**: The ingest pipeline (powered by R and Python) skips unchanged PDFs, making subsequent updates extremely fast.
4️⃣ **Shiny App Interface**: A clean, responsive search application that lets you query metadata, select a paper, and open the original PDF in your system's default viewer.

⚠️ **Note & Disclaimer**:
This project is an **AI-assisted development**. While it's functional and ready to use, it is still in its early stages, not perfect, and has room for improvement (such as better error handling, more robust parsing edge cases, and expanded search features).

🤝 **Contributions welcome!**
If you'd like to help make this tool better, contributions via Pull Requests are highly welcome! Whether it's styling, performance, or additional features, feel free to dive in.

Check out the code, installation instructions, and documentation here:
👉 https://github.com/fortune9/pdf_db_builder

Happy researching! 💻✨

#RStats #Python #OpenSource #DataScience #ResearchTools #SQLite #ShinyApp #AIAssisted #Programming #DeveloperTools
