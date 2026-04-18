---
name: linkedin-pitch-creator
description: Generates a LinkedIn pitch post and a matching high-resolution title image for blog posts or technical articles. Trigger this skill whenever the user wants to "pitch a post", "create a LinkedIn post for a blog", or "promote an article". It handles both the copy and the visual asset creation, adapting the style and background scene to the content.
---

# LinkedIn Pitch Creator

This skill automates the creation of professional LinkedIn promotional content. It produces a punchy, emoji-rich post and a custom-generated title image that is visually adapted to the content using dynamic scenes.

## Workflow

1.  **Analyze Content**: Read the target blog post to understand its core topic (e.g., Biology, AI, Coding, Networking).
2.  **Select Theme & Scene**: Choose the most relevant visual theme and accent color:
    *   `tech`: **Developer Scene**. Includes desks, monitors with code lines, and tech motifs. Color: `#00ff7f` (Spring Green). Use for coding, software, and web dev.
    *   `bio`: **Science Scene**. Includes DNA helices and organic motifs. Color: `#ff6b6b` (Coral). Use for biology, genetics, and life sciences.
    *   `network`: **Infrastructure Scene**. Includes nodes and graph motifs. Color: `#4dabf7` (Blue). Use for networking, cloud, and connectivity.
3.  **Generate Post**: Write a concise LinkedIn post (markdown format) focusing on the problem solved and a clear CTA.
4.  **Generate Dynamic Image**: Execute the bundled `generate_image.py` with the selected theme and color.
    *   Example: `python3 scripts/generate_image.py "Title" "Subtitle" "path.png" "tech" "#00ff7f"`
5.  **Organize Files**: Save the post as a `.md` file and the image as a `.png` in the structured `LinkedIn/` directories.

## Image Specifications
*   **Resolution**: 1800x1013 px (300 DPI, 16:9 ratio).
*   **Aesthetics**: Modern dark gradient background with complex background "scenes" that mimic the subject matter.
