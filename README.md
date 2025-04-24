# GPT Prompt Templates

[![GitHub stars](https://img.shields.io/github/stars/phuchungbhutia/prompts-repo)](https://github.com/phuchungbhutia/prompts-repo/stargazers) [![License](https://img.shields.io/github/license/phuchungbhutia/prompts-repo)](https://github.com/phuchungbhutia/prompts-repo/blob/main/LICENSE) [![Workflow Status](https://img.shields.io/github/workflow/status/phuchungbhutia/prompts-repo/Update%20Prompt%20Indexes)](https://github.com/phuchungbhutia/prompts-repo/actions) [![Contributors](https://img.shields.io/github/contributors/phuchungbhutia/prompts-repo)](https://github.com/phuchungbhutia/prompts-repo/graphs/contributors) [![Last Updated](https://img.shields.io/github/last-commit/phuchungbhutia/prompts-repo/main?label=Last%20Updated)](https://github.com/phuchungbhutia/prompts-repo/commits/main)

This repository contains a collection of GPT prompt templates organized by category, with automated indexing via GitHub Actions.

## Repository Stats

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=phuchungbhutia&show_icons=true&theme=radical)

## Repository Structure

```mermaid
graph TD
    A[prompts-repo] --> B[prompts]
    A --> C[scripts]
    A --> D[.github/workflows]
    A --> E[docs/images]
    B --> CAT1[AI Prompt Engineering]
    B --> CAT2[AI Tools]
    B --> CAT3[Academic Writing]
    B --> CAT4[Android App Development, OCR, AI Tools]
    B --> CAT5[App Development]
    B --> CAT6[Audit]
    B --> CAT7[Business]
    B --> CAT8[Career Tips]
    B --> CAT9[Learning Techniques]
    B --> CAT10[Learning with AI]
    B --> CAT11[Prompt Engineering]
    B --> CAT12[Strategy & Productivity]
    B --> CAT13[content generation]
    B --> CAT14[deepseek]
    B --> CAT15[health-nutrition]
    B --> CAT16[learning]
    CAT1[AI Prompt Engineering] --> F11[ChatGPT Prompting Frameworks Explained.md]
    CAT1[AI Prompt Engineering] --> F12[Grok 3 Prompting Master Cheat Sheet.md]
    CAT2[AI Tools] --> F21[12 Must-Know ChatGPT Prompt Techniques.md]
    CAT2[AI Tools] --> F22[Boost Productivity with These Powerful ChatGPT Prompts.md]
    CAT2[AI Tools] --> F23[DeepSeek Cheat Sheet - AI Prompts for Skill Building, Business & Productivity.md]
    CAT2[AI Tools] --> F24[Problem Solving Using Mental Models.md]
    CAT3[Academic Writing] --> F31[Ethical AI Use in Academic Writing – Prompts & Guide.md]
    CAT4[Android App Development, OCR, AI Tools] --> F41[Ultimate Android Camera Text Scanner App – AI-Powered Document Scanner & OCR.md]
    CAT5[App Development] --> F51[Cross-Platform Audit App Development Plan.md]
    CAT6[Audit] --> F61[Audit Observations.md]
    CAT6[Audit] --> F62[GST Data Analysis for Audit.md]
    CAT7[Business] --> F71[9 ChatGPT Prompts to Find Profitable Market Opportunities.md]
    CAT8[Career Tips] --> F81[Mastering Common Interview Questions with ChatGPT.md]
    CAT9[Learning Techniques] --> F91[Learn Anything 5x Faster with These 9 Proven Methods.md]
    CAT10[Learning with AI] --> F101[Use AI to Learn Anything Faster.md]
    CAT11[Prompt Engineering] --> F111[DeepSeek AI Prompt Hacks Cheat Sheet.md]
    CAT12[Strategy & Productivity] --> F121[5 Problem-Solving Method Prompts for Founders & CEOs.md]
    CAT13[content generation] --> F131[Blog Post Generator.md]
    CAT14[deepseek] --> F141[2025.04.18.md]
    CAT15[health-nutrition] --> F151[Create a Comprehensive Healthy Meal Plan Guide.md]
    CAT16[learning] --> F161[10 Powerful AI-Based Learning Techniques.md]
    C --> S[update_index.py]
    D --> W[update-index.yml]
    E --> I[indexing.png]
    A --> R[README.md]
    A --> T[categories.md]
```

## Prompt Categories

| Category     | Description                              | Example Prompt              |
|--------------|------------------------------------------|-----------------------------|
| AI Prompt Engineering | Prompts for AI Prompt Engineering  | ChatGPT Prompting Frameworks Explained |
| AI Tools | Prompts for AI Tools  | 12 Must-Know ChatGPT Prompt Techniques |
| Academic Writing | Prompts for Academic Writing  | Ethical AI Use in Academic Writing – Prompts & Guide |
| Android App Development, OCR, AI Tools | Prompts for Android App Development, OCR, AI Tools  | Ultimate Android Camera Text Scanner App – AI-Powered Document Scanner & OCR |
| App Development | Prompts for App Development  | Cross-Platform Audit App Development Plan |
| Audit | Prompts for Audit  | Audit Observations |
| Business | Prompts for Business  | 9 ChatGPT Prompts to Find Profitable Market Opportunities |
| Career Tips | Prompts for Career Tips  | Mastering Common Interview Questions with ChatGPT |
| Learning Techniques | Prompts for Learning Techniques  | Learn Anything 5x Faster with These 9 Proven Methods |
| Learning with AI | Prompts for Learning with AI  | Use AI to Learn Anything Faster |
| Prompt Engineering | Prompts for Prompt Engineering  | DeepSeek AI Prompt Hacks Cheat Sheet |
| Strategy & Productivity | Prompts for Strategy & Productivity  | 5 Problem-Solving Method Prompts for Founders & CEOs |
| content generation | Prompts for content generation  | Blog Post Generator |
| deepseek | Prompts for deepseek  | 2025.04.18 |
| health-nutrition | Prompts for health nutrition  | Create a Comprehensive Healthy Meal Plan Guide |
| learning | Prompts for learning  | 10 Powerful AI-Based Learning Techniques |

## Prompts

- [10 Powerful AI-Based Learning Techniques](prompts/learning/ai-based-learning.md) - Master any topic faster with these 10 optimized prompt templates designed to enhance understanding, retention, and motivation.
- [12 Must-Know ChatGPT Prompt Techniques](prompts/AITools/chatgpt.md) - Learn how to use 12 powerful ChatGPT prompt techniques with 36 ready-to-use examples for better results in learning, creativity, productivity, and problem-solving.
- [2025.04.18](prompts/deepseek/2025.04.18.md) - Collection of Deepseek prompts
- [5 Problem-Solving Method Prompts for Founders & CEOs](prompts/AITools/5tools.md) - Practical ChatGPT prompts tailored for five essential problem-solving methods used by founders and CEOs—Pre-Mortem, 5 Whys, Decision Tree, SWOT, and Impact vs Effort Matrix.
- [9 ChatGPT Prompts to Find Profitable Market Opportunities](prompts/Business/Market.md) - Discover 9 powerful ChatGPT prompts to uncover hidden market opportunities, along with 3 real-world examples for each to help spark your next venture.
- [Audit Observations](prompts/audit/observations.md) - Prompt for Writing Audit Observations
- [Blog Post Generator](prompts/content-generator/blog-post-generator.md) - Generates outlines and content for blog posts based on given topics
- [Boost Productivity with These Powerful ChatGPT Prompts](prompts/AITools/productivity.md) - Learn how to maximize your productivity in 2025 using ChatGPT prompts. This blog breaks down the structure, examples, and best practices to make ChatGPT your ultimate task partner.
- [ChatGPT Prompting Frameworks Explained](prompts/AITools/frameworks.md) - Learn how to unlock the full potential of ChatGPT using four powerful prompting frameworks—RTF, BAB, CAR, and TARG. Includes examples, use cases, pros, cons, and limitations.
- [Create a Comprehensive Healthy Meal Plan Guide](prompts/health-nutrition/nutrition-expert.md) - Acts as a nutrition expert to create a detailed, multi-diet meal planning guide with sample meals, tips, and substitutions.
- [Cross-Platform Audit App Development Plan](prompts/app-development/audit-app.md) - Prompt for generating a comprehensive development plan for a free, cross-platform mobile and web app for auditors using open-source tools and AI coding assistants.
- [DeepSeek AI Prompt Hacks Cheat Sheet](prompts/AITools/deepseek.md) - A comprehensive cheat sheet of DeepSeek AI prompt hacks with categorized examples to help you create powerful AI-generated content, resumes, code, educational material, and more.
- [DeepSeek Cheat Sheet - AI Prompts for Skill Building, Business & Productivity](prompts/AITools/deepseek2.md) - A detailed guide to using DeepSeek AI for skill development, business consulting, content creation, writing improvement, productivity, and more—featuring ready-to-use prompts and examples.
- [Ethical AI Use in Academic Writing – Prompts & Guide](prompts/Academics/academics.md) - A complete guide and prompt collection for using AI tools ethically in academic writing. Includes detailed steps, do’s and don’ts, and professional prompt templates.
- [Grok 3 Prompting Master Cheat Sheet](prompts/AITools/grok.md) - Unlock Grok 3's full potential with this master cheat sheet of expert-level prompts. Learn the perfect prompt formula, roles, tasks, formats, and real-world use cases to save hours daily.
- [GST Data Analysis for Audit](prompts/audit/gst-data-anaylsis.md) - Analyzes GST data for audit compliance, focusing on turnover, ITC, and regulatory adherence
- [Learn Anything 5x Faster with These 9 Proven Methods](prompts/learning/learning-techniques.md) - A complete guide from beginner to expert on how to learn faster using 9 cognitive science-based frameworks. Includes explanations, use cases, and 27 actionable prompts.
- [Mastering Common Interview Questions with ChatGPT](prompts/Career-Tips/Interview.md) - Learn how to master the most common interview questions using ChatGPT, with examples, prompts, pros, cons, and limitations for each. Perfect for job seekers who want to prepare smarter and faster.
- [Problem Solving Using Mental Models](prompts/AITools/Problem-Solving.md) - Learn how to use ChatGPT more effectively by applying 9 powerful mental models for problem solving. Each framework includes 3 practical examples to guide your strategy, planning, and execution.
- [Ultimate Android Camera Text Scanner App – AI-Powered Document Scanner & OCR](prompts/app-development/camscanner-app.md) - Build an advanced Android camera document scanning app with smart features, OCR, AI-enhanced image processing, and optimized performance.
- [Use AI to Learn Anything Faster](prompts/AITools/learn-faster.md) - A practical guide on how to leverage AI tools like ChatGPT to supercharge your learning using proven techniques like simplification, analogies, quizzes, mind maps, and more.

## Installation

Clone the repository:
```bash
git clone https://github.com/phuchungbhutia/prompts-repo.git
cd prompts-repo
```

Run the indexing script:
```python
python scripts/update_index.py
```

### 💡 Tip: Run the indexing script from Local Drive C in Windows:

```powershell
cd C:/Projects/prompts-repo
python scripts/update_index.py
```
### 💡 Tip: To Update Files
```
python scripts/update_index.py
git add .
git commit -m [Update]
git push
```

## Contributing

1. Add a new prompt in `/prompts/category_name/` using the [template](prompts/template.md).
2. Run `python scripts/update_index.py` to update indexes.
3. Submit a pull request.

To add yourself as a contributor, use the all-contributors bot:
```bash
npm run contributors:add <your-username> code
```

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START -->
<!-- This section is automatically generated by all-contributors -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

## License

MIT License. See [LICENSE](LICENSE) for details.

## Indexing in Action

![Indexing Script](docs/images/indexing.png)

(https://www.flaticon.com/free-icons/layout)