---
name: paper-summary-version2
description: A skill to create concise, technical summaries of scientific papers based on the abstract; use it when users ask for a summary of a scientific paper's abstract, especially when they provide a URL or title.
---

## A Scientific Article Summarizer

This tool finds the paper based on the provided title or URL, summarize the main information
in the abstract, and output a short post to be published on LinkedIn

### Behavior

- Find the paper based on the provided link or by using Google search for the title

- If a paper appears in both preprint server (e.g., biorxiv) and in official publisher (e.g., nature.com), use the official publisher as the source

- Summarize the paper based on the Abstract of the paper only, unless instructed by the user to leverage main text too

- Make the post concise, ranging from 20 to 70 words, depending on complexity of the subject

- Use emojis when helpful

- At the end of the post, always add the link to the paper so that users can read more

- At the end of the post, also include 3 to 5 relevant hash tags

### Structure

- Starts the post with the problem, followed by methods (if relevant), and finally the key results or solutions

- Use bullet points for complex study

    + each point can be each key findings for discovery papers

    + each point can be key method, key dataset, and key results for methods papers

    + each point can be key points for review papers

### Guardrail


- Never use or infer information beyond the paper

- Validate the link to the paper before return the post

- Use the information from the Abstract only, unless asked otherwise
