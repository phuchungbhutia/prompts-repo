---
title: Ethical AI Use in Academic Writing – Prompts & Guide  
category: Writing  
description: A complete guide and prompt collection for using AI tools ethically in academic writing. Includes detailed steps, do’s and don’ts, and professional prompt templates.

---

## 🔧 Prompt

Use this structured guide and set of prompts to ethically leverage AI tools like ChatGPT for academic writing. Follow these steps:

1. Start with your own thesis, arguments, and outline.
2. Write a full draft in your voice before using AI.
3. Use editing prompts to improve grammar, clarity, and academic tone—without changing your core content.
4. Work in small sections and review all AI suggestions.
5. Maintain your voice and acknowledge AI use where required.

### Recommended Prompts:

- **Editing Clarity & Tone (Main Prompt)**  
  ```txt
  You are a professional academic editor. Your job is to improve the clarity, coherence, and style of my writing without changing any of the original ideas or introducing new content. Focus on grammar, sentence structure, flow, and academic tone. Do not remove or reframe my arguments—just help me express them more effectively.
  ```

- **Grammar & Flow Only**  
  ```txt
  Act as a grammar and style assistant. Improve sentence clarity and flow without altering the meaning or introducing new ideas. Do not rephrase any arguments—only correct grammar and enhance structure.
  ```

- **Passive to Active Voice**  
  ```txt
  Convert this academic text from passive to active voice where appropriate. Do not change meaning or add any new content.
  ```

- **Polishing Academic Tone**  
  ```txt
  Polish the following text to meet academic standards in tone and formality. Maintain original arguments and structure.
  ```

---

## 🧩 Inputs

- `draft_text`: The academic text written by the user, in 2–3 paragraph chunks  
- `prompt_type`: Select the relevant editing goal (e.g., clarity, grammar, tone, passive-to-active)
- `disclosure_required`: Yes/No — whether AI use should be acknowledged in submission

---

## ⚙️ Constraints

- Do not allow AI to generate full essays or write content from scratch
- Do not change the user’s arguments, tone, or structure without review
- Break edits into small sections for better control
- Always preserve academic integrity and originality
- Disclose AI assistance if institutional policies require it

---

## 📋 Output Format

```markdown
### Original Text:
<Your submitted text>

### Edited Text:
<AI-edited version, with improved clarity, grammar, and tone, but no changes to ideas>

### Comments (Optional):
- <Suggestions, grammar notes, or alternatives to consider>
- <Mention if passive voice was changed, or tone adjusted>

---
