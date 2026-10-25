---
name: linkedin-pitch-creator
description: Create LinkedIn posts and matching illustrated title images for blog posts, technical articles, or personal reflections. Use when asked to pitch a post, promote an article, or explicitly use linkedin-pitch-creator.
---

# LinkedIn Pitch Creator

Create a concise, emoji-rich LinkedIn post and a matching image that communicates its meaning through recognizable scenes, objects, or visual comparisons. Preserve the user's voice and any approved wording.

## Workflow

1.  **Analyze Content**: Read the article or supplied thoughts. Identify the title, date, slug, central message, and concepts the image should convey. For an original post without a publication date, use the current date.
2.  **Plan Meaningful Visuals**: Translate the key concepts into recognizable objects or human scenes. Choose a single scene, a comparison, or several illustrated panels according to the content. Use color to support the topic rather than choosing generic imagery solely because the post mentions technology, science, or networking. See the visual guidance below.
3.  **Determine Target Paths**:
    *   Target base: `LinkedIn/<agent-dir>/<YYYY>/` (e.g., `LinkedIn/gemini/2026/`)
    *   Post path: `LinkedIn/<agent-dir>/<YYYY>/YYYY-MM-DD-<slug>.md`
    *   Image path: `LinkedIn/<agent-dir>/<YYYY>/images/YYYY-MM-DD-<slug>.png`
4.  **Generate Post**: Write a concise LinkedIn post (markdown format) focusing on the problem solved and a clear CTA. Save to `LinkedIn/<agent-dir>/<YYYY>/YYYY-MM-DD-<slug>.md`.
5.  **Generate and Inspect Image**: Use the built-in image generation tool by default, following the available imagegen skill. Supply the visual concept, exact headline and labels, intended layout, and palette. For edits, inspect the existing image first and provide it as the edit target. Inspect the output for clear meaning, readable text, correct spelling, and cropping; make a targeted revision if needed. Save the selected output to the workspace image path. Save revisions as separate versions, such as `-v2.png`, unless replacement is requested. Report links to the saved post and image.

The bundled `scripts/generate_image.py` makes a basic text-and-background card. Retain it for explicitly requested simple cards; use AI image generation for illustrated images. If built-in image generation is unavailable, explain the limitation and offer alternatives rather than silently substituting a generic card.

## Intuitive Visual Guidance

The image should help a reader understand the post before reading its caption. Illustrate the key concepts with recognizable objects, human scenes, or visual comparisons. Give illustrations enough space to be recognizable at LinkedIn feed size. Avoid title-only cards with decorative shapes.

When several ideas benefit from separate illustrations, use labeled panels. Choose the number of panels to fit the content. For example, a job-search reflection can show:

* **Reflect**: someone looking thoughtfully into a mirror.
* **Learn**: someone studying with books, a notebook, and a laptop.
* **Reconnect**: former colleagues talking over coffee.
* **Purpose**: someone holding a compass on a path toward a warm horizon.

For technical posts, show a relevant workflow, relationship, or comparison that illustrates the main finding. Keep scientific representations accurate and avoid invented data or visuals that imply unsupported results. Decorative DNA helices, code monitors, or network nodes alone rarely explain the message.

Use a cohesive illustration style, clear visual hierarchy, and brief readable labels. Keep the headline prominent without crowding the scenes. Let the content and the user's requested style guide the palette and mood.

## Image Specifications
*   **Resolution**: 1800x1013 px (300 DPI, 16:9 ratio).
*   **Aesthetics**: Polished, content-specific illustrations with legible text and balanced composition. A dark gradient can support the layout when appropriate; recognizable scenes and objects should carry the message.
