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
    B --> CAT1[AI-Tools]
    B --> CAT2[Audit]
    B --> CAT3[Business]
    B --> CAT4[Career-Tips]
    B --> CAT5[Content-Creation]
    B --> CAT6[Content-Generation]
    B --> CAT7[Content-generation]
    B --> CAT8[Data-Analysis]
    B --> CAT9[Education]
    B --> CAT10[Excel]
    B --> CAT11[Fun]
    B --> CAT12[Learning]
    B --> CAT13[Marketing]
    B --> CAT14[Productivity]
    B --> CAT15[Programming]
    B --> CAT16[Prompting]
    B --> CAT17[Writing]
    B --> CAT18[academic-writing]
    B --> CAT19[content-generation]
    B --> CAT20[content-generator]
    B --> CAT21[creative-writing]
    B --> CAT22[deepseek]
    B --> CAT23[health-nutrition]
    B --> CAT24[learning]
    CAT1[AI-Tools] --> F11[Boost Productivity with These Powerful ChatGPT Prompts.md]
    CAT1[AI-Tools] --> F12[Problem Solving Using Mental Models.md]
    CAT2[Audit] --> F21[Audit Observations.md]
    CAT2[Audit] --> F22[ChatGPT Prompts for Building a GST Audit Tool.md]
    CAT2[Audit] --> F23[GST Data Analysis for Audit.md]
    CAT3[Business] --> F31[9 ChatGPT Prompts to Find Profitable Market Opportunities.md]
    CAT4[Career-Tips] --> F41[Mastering Common Interview Questions with ChatGPT.md]
    CAT5[Content-Creation] --> F51[18 ChatGPT Prompts for Content Creation.md]
    CAT5[Content-Creation] --> F52[Prompts for Crafting Human-Like SEO Content.md]
    CAT6[Content-Generation] --> F61[Comprehensive Guide to Creating an eBook from Online Sources.md]
    CAT7[Content-generation] --> F71[18 ChatGPT Prompts for User Experience.md]
    CAT8[Data-Analysis] --> F81[Example Prompts for Data Analysis with ChatGPT.md]
    CAT8[Data-Analysis] --> F82[Prompts for Research Data Analysis.md]
    CAT9[Education] --> F91[ChatGPT Prompts for Learning and Development.md]
    CAT9[Education] --> F92[ChatGPT Prompts for Teaching.md]
    CAT9[Education] --> F93[Educator's Prompt Guide for Classroom Excellence.md]
    CAT10[Excel] --> F101[Master Excel with DeepSeek.md]
    CAT11[Fun] --> F111[Creative Prompts for Entertainment and Storytelling.md]
    CAT12[Learning] --> F121[10 Powerful AI-Based Learning Techniques for Mastering Any Topic.md]
    CAT12[Learning] --> F122[Comprehensive Prompt Guide for Strategic and Creative Tasks.md]
    CAT12[Learning] --> F123[Critical Thinking Prompt Template.md]
    CAT12[Learning] --> F124[Learn Anything 5x Faster with These 9 Proven Methods.md]
    CAT12[Learning] --> F125[Use AI to Learn Anything Faster.md]
    CAT13[Marketing] --> F131[18 ChatGPT Prompts for Advertising.md]
    CAT13[Marketing] --> F132[18 ChatGPT Prompts for Digital Marketing.md]
    CAT13[Marketing] --> F133[18 ChatGPT Prompts for Social Media Marketing.md]
    CAT13[Marketing] --> F134[Comprehensive Marketing and Content Prompt Guide.md]
    CAT14[Productivity] --> F141[5 Problem-Solving Method Prompts for Founders & CEOs.md]
    CAT14[Productivity] --> F142[Boosting Productivity with ChatGPT.md]
    CAT14[Productivity] --> F143[Boosting Productivity with ChatGPT.md]
    CAT14[Productivity] --> F144[Builder-to-Brand Gameplan - Brutal Focus Roadmap.md]
    CAT14[Productivity] --> F145[ChatGPT Prompt Frameworks for Effective Task Structuring.md]
    CAT14[Productivity] --> F146[Enhanced Productivity and Creativity Prompts with ChatGPT.md]
    CAT14[Productivity] --> F147[Formula for Crafting Effective ChatGPT Prompts.md]
    CAT14[Productivity] --> F148[Maximizing ChatGPT with Structured Prompts Across Applications.md]
    CAT15[Programming] --> F151[10 Useful ChatGPT Prompts for Developers.md]
    CAT15[Programming] --> F152[15 Must-Have ChatGPT Prompts for Developers.md]
    CAT15[Programming] --> F153[50 Prompts for Extracting Text from PDF Tables Using Excel, Power Query, and Python.md]
    CAT15[Programming] --> F154[ChatGPT Prompts for Data Science.md]
    CAT15[Programming] --> F155[ChatGPT Prompts for Software Development.md]
    CAT15[Programming] --> F156[Cross-Platform Audit App Development Plan.md]
    CAT15[Programming] --> F157[Ultimate Android Camera Text Scanner App – AI-Powered Document Scanner & OCR.md]
    CAT16[Prompting] --> F161[12 Must-Know ChatGPT Prompt Techniques.md]
    CAT16[Prompting] --> F162[ChatGPT Cheat Sheet - Crafting Effective Prompts.md]
    CAT16[Prompting] --> F163[ChatGPT for Marketing.md]
    CAT16[Prompting] --> F164[ChatGPT Prompt Cheatsheet for Various Use Cases.md]
    CAT16[Prompting] --> F165[ChatGPT Prompt Frameworks – Full Guide with Examples.md]
    CAT16[Prompting] --> F166[ChatGPT Prompt Guide.md]
    CAT16[Prompting] --> F167[ChatGPT Prompt Guide for Structured Usage.md]
    CAT16[Prompting] --> F168[ChatGPT Prompting Frameworks Explained.md]
    CAT16[Prompting] --> F169[Cheat Sheet for Crafting Effective ChatGPT Prompts.md]
    CAT16[Prompting] --> F1610[DeepSeek AI Prompt Hacks Cheat Sheet.md]
    CAT16[Prompting] --> F1611[DeepSeek Cheat Sheet - AI Prompts for Skill Building, Business & Productivity.md]
    CAT16[Prompting] --> F1612[Grok 3 Prompting Master Cheat Sheet.md]
    CAT16[Prompting] --> F1613[Prompt Engineering Guide for SaaS Product Development.md]
    CAT17[Writing] --> F171[18 ChatGPT Prompts for SEO.md]
    CAT17[Writing] --> F172[ChatGPT Prompts for Producing Your Ebook Manuscript.md]
    CAT17[Writing] --> F173[ChatGPT Prompts for Writing a Book.md]
    CAT17[Writing] --> F174[ChatGPT Prompts for Writing an Ebook.md]
    CAT17[Writing] --> F175[Comprehensive Prompt Guide for Authors.md]
    CAT17[Writing] --> F176[eBook Writing Prompts That Sell.md]
    CAT17[Writing] --> F177[Effective ChatGPT Prompts for Creating User Manuals.md]
    CAT17[Writing] --> F178[Essential ChatGPT Prompts for Technical Documentation.md]
    CAT17[Writing] --> F179[Fictional Character Technical Advisor Prompt.md]
    CAT17[Writing] --> F1710[Prompts to Write a Nonfiction Ebook.md]
    CAT18[academic-writing] --> F181[Ethical AI Use in Academic Writing – Prompts & Guide.md]
    CAT18[academic-writing] --> F182[Generate Research Papers.md]
    CAT18[academic-writing] --> F183[Thesis Outline – 7 Chapters with Detailed Elements.md]
    CAT19[content-generation] --> F191[Blog Post Generator.md]
    CAT20[content-generator] --> F201[youtube-script.md]
    CAT21[creative-writing] --> F211[Imaginative Creative Writing Prompts.md]
    CAT22[deepseek] --> F221[2025.04.18.md]
    CAT23[health-nutrition] --> F231[Create a Comprehensive Healthy Meal Plan Guide.md]
    CAT24[learning] --> F241[10 Powerful AI-Based Learning Techniques.md]
    C --> S[update_index.py]
    D --> W[update-index.yml]
    E --> I[indexing.png]
    A --> R[README.md]
    A --> T[categories.md]
```

## Prompt Categories

| Category     | Description                              | Example Prompt              |
|--------------|------------------------------------------|-----------------------------|
| AI-Tools | Prompts for AI Tools  | Boost Productivity with These Powerful ChatGPT Prompts |
| Audit | Prompts for Audit  | Audit Observations |
| Business | Prompts for Business  | 9 ChatGPT Prompts to Find Profitable Market Opportunities |
| Career-Tips | Prompts for Career Tips  | Mastering Common Interview Questions with ChatGPT |
| Content-Creation | Prompts for Content Creation  | 18 ChatGPT Prompts for Content Creation |
| Content-Generation | Prompts for Content Generation  | Comprehensive Guide to Creating an eBook from Online Sources |
| Content-generation | Prompts for Content generation  | 18 ChatGPT Prompts for User Experience |
| Data-Analysis | Prompts for Data Analysis  | Example Prompts for Data Analysis with ChatGPT |
| Education | Prompts for Education  | ChatGPT Prompts for Learning and Development |
| Excel | Prompts for Excel  | Master Excel with DeepSeek |
| Fun | Prompts for Fun  | Creative Prompts for Entertainment and Storytelling |
| Learning | Prompts for Learning  | 10 Powerful AI-Based Learning Techniques for Mastering Any Topic |
| Marketing | Prompts for Marketing  | 18 ChatGPT Prompts for Advertising |
| Productivity | Prompts for Productivity  | 5 Problem-Solving Method Prompts for Founders & CEOs |
| Programming | Prompts for Programming  | 10 Useful ChatGPT Prompts for Developers |
| Prompting | Prompts for Prompting  | 12 Must-Know ChatGPT Prompt Techniques |
| Writing | Prompts for Writing  | 18 ChatGPT Prompts for SEO |
| academic-writing | Prompts for academic writing  | Ethical AI Use in Academic Writing – Prompts & Guide |
| content-generation | Prompts for content generation  | Blog Post Generator |
| content-generator | Prompts for content generator  | youtube-script |
| creative-writing | Prompts for creative writing  | Imaginative Creative Writing Prompts |
| deepseek | Prompts for deepseek  | 2025.04.18 |
| health-nutrition | Prompts for health nutrition  | Create a Comprehensive Healthy Meal Plan Guide |
| learning | Prompts for learning  | 10 Powerful AI-Based Learning Techniques |

## Prompts

- [10 Powerful AI-Based Learning Techniques](prompts/learning/ai-based-learning.md) - Master any topic faster with these 10 optimized prompt templates designed to enhance understanding, retention, and motivation.
- [10 Powerful AI-Based Learning Techniques for Mastering Any Topic](prompts/learning/ai-learning.md) - This guide explains 10 AI-based learning techniques to make mastering any topic faster and easier. Each technique includes use cases, examples, prompt templates, and optimized prompts for direct implementation.
- [10 Useful ChatGPT Prompts for Developers](prompts/app-development/software-development2.md) - A detailed guide to 10 essential ChatGPT prompts designed to assist developers in various aspects of software development, including coding, debugging, API design, database management, and learning best practices.
- [12 Must-Know ChatGPT Prompt Techniques](prompts/AITools/chatgpt.md) - Learn how to use 12 powerful ChatGPT prompt techniques with 36 ready-to-use examples for better results in learning, creativity, productivity, and problem-solving.
- [15 Must-Have ChatGPT Prompts for Developers](prompts/app-development/software-development.md) - A collection of essential ChatGPT prompts to improve developer efficiency and productivity.
- [18 ChatGPT Prompts for Advertising](prompts/Business/advertising.md) - A collection of prompts for crafting impactful advertising campaigns, scripts, and strategies tailored to any product or audience.
- [18 ChatGPT Prompts for Content Creation](prompts/content-generator/content-creation.md) - A versatile collection of ChatGPT prompts to help create compelling content for blogs, videos, emails, and more.
- [18 ChatGPT Prompts for Digital Marketing](prompts/Business/digital-marketing.md) - A curated collection of prompts to assist digital marketers in creating content for multiple platforms, from social media posts to email sequences.
- [18 ChatGPT Prompts for SEO](prompts/content-generator/seos.md) - A set of advanced prompts to streamline SEO tasks, from meta descriptions to content gap analysis and keyword research.
- [18 ChatGPT Prompts for Social Media Marketing](prompts/content-generator/social-media.md) - A collection of expert prompts for creating engaging social media content across platforms and formats.
- [18 ChatGPT Prompts for User Experience](prompts/content-generator/ux.md) - A curated set of prompts to enhance user experience design and research efforts for applications, websites, and platforms.
- [2025.04.18](prompts/deepseek/2025.04.18.md) - Collection of Deepseek prompts
- [5 Problem-Solving Method Prompts for Founders & CEOs](prompts/AITools/5tools.md) - Practical ChatGPT prompts for applying five strategic problem-solving frameworks—Pre-Mortem, 5 Whys, Decision Tree, SWOT, and Impact vs Effort Matrix.
- [50 Prompts for Extracting Text from PDF Tables Using Excel, Power Query, and Python](prompts/app-development/data-extraction.md) - A comprehensive guide with 50 prompts to extract text from tables in multiple PDF files using Excel, Power Query, and Python. This includes formula-based, automated, and code-driven approaches for handling complex data structures.
- [9 ChatGPT Prompts to Find Profitable Market Opportunities](prompts/Business/Market.md) - Discover 9 powerful ChatGPT prompts to uncover hidden market opportunities, along with 3 real-world examples for each to help spark your next venture.
- [Audit Observations](prompts/audit/observations.md) - Prompt for Writing Audit Observations
- [Blog Post Generator](prompts/content-generator/blog-post-generator.md) - Generates outlines and content for blog posts based on given topics
- [Boost Productivity with These Powerful ChatGPT Prompts](prompts/AITools/productivity.md) - Learn how to maximize your productivity in 2025 using ChatGPT prompts. This blog breaks down the structure, examples, and best practices to make ChatGPT your ultimate task partner.
- [Boosting Productivity with ChatGPT](prompts/Productivity/booster.md) - A curated collection of prompts and strategies to optimize productivity using ChatGPT for professionals, students, and entrepreneurs.
- [Boosting Productivity with ChatGPT](prompts/Productivity/productivity-chatgpt.md) - A curated collection of prompts and strategies to optimize productivity using ChatGPT for professionals, students, and entrepreneurs.
- [Builder-to-Brand Gameplan - Brutal Focus Roadmap](prompts/Productivity/productivity.md) - A comprehensive 4-stage roadmap designed to align your multi-talented brain with ruthless execution, helping you transition from a "Builder" to a memorable "Brand." This plan ensures clarity, focus, and scalable growth.
- [ChatGPT Cheat Sheet - Crafting Effective Prompts](prompts/AITools/chatgpt-cheatsheet.md) - A detailed guide on using structured prompts to maximize ChatGPT’s potential across various domains, including content creation, coding, sales, marketing, and personal career development.
- [ChatGPT for Marketing](prompts/AITools/marketing.md) - A comprehensive guide to using ChatGPT for 10 powerful marketing tasks—from campaign planning to SEO content ideas—complete with optimized prompts, use cases, and real-world examples.
- [ChatGPT Prompt Cheatsheet for Various Use Cases](prompts/AITools/chagpt2.md) - This cheatsheet provides beginner-friendly ChatGPT prompts to explain, learn, brainstorm, and solve problems across multiple use cases.
- [ChatGPT Prompt Frameworks for Effective Task Structuring](prompts/Productivity/prompt-framework.md) - This document outlines five structured frameworks to craft ChatGPT prompts for effective task execution. Each framework is explained with its structure, purpose, and practical examples for various use cases like business, content creation, education, and personal growth.
- [ChatGPT Prompt Frameworks – Full Guide with Examples](prompts/AITools/chatgpt-frameworks.md) - Learn to master ChatGPT using 5 powerful prompt frameworks—R-T-F, T-A-G, B-A-B, C-A-R-E, and R-I-S-E. Each structure includes explanations, ideal use cases, and real-world prompt examples for getting actionable, relevant outputs from ChatGPT.
- [ChatGPT Prompt Guide](prompts/content-generator/prompts.md) - A comprehensive guide to crafting effective ChatGPT prompts for optimal outputs, including foundational strategies and advanced techniques.
- [ChatGPT Prompt Guide for Structured Usage](prompts/AITools/chatgpt3.md) - This guide provides a comprehensive explanation and examples of structured prompts to use ChatGPT effectively. It covers various roles, techniques, and use cases to help users optimize their interactions and generate precise responses.
- [ChatGPT Prompting Frameworks Explained](prompts/AITools/frameworks.md) - Learn how to unlock the full potential of ChatGPT using four powerful prompting frameworks—RTF, BAB, CAR, and TARG. Includes examples, use cases, pros, cons, and limitations.
- [ChatGPT Prompts for Building a GST Audit Tool](prompts/audit/gst-audit-tool.md) - Leverage ChatGPT to create tailored prompts for automating GST audit processes, analyzing data, detecting revenue leakages, and streamlining reporting. These prompts are categorized for different aspects of the development process.
- [ChatGPT Prompts for Data Science](prompts/app-development/data-science.md) - A versatile set of prompts to tackle tasks in data science, including modeling, visualization, and cleaning.
- [ChatGPT Prompts for Learning and Development](prompts/learning/learn-develop.md) - A versatile collection of prompts to enhance learning and development initiatives through creative instructional design, assessments, and engagement strategies.
- [ChatGPT Prompts for Producing Your Ebook Manuscript](prompts/content-generator/manuscript.md) - A comprehensive guide to using ChatGPT for crafting an engaging and market-ready ebook, covering everything from back cover descriptions to manuscript creation and graphics.
- [ChatGPT Prompts for Software Development](prompts/app-development/sw-develop.md) - A versatile collection of prompts to assist with software development, from architecture and testing to documentation and code improvement.
- [ChatGPT Prompts for Teaching](prompts/Academics/teaching.md) - A comprehensive collection of prompts to assist educators in lesson planning, classroom management, and student engagement.
- [ChatGPT Prompts for Writing a Book](prompts/content-generator/book-writer.md) - A detailed collection of ChatGPT prompts to assist authors in various stages of book writing, from outlining to character development and marketing strategies.
- [ChatGPT Prompts for Writing an Ebook](prompts/content-generator/ebooks.md) - A versatile collection of prompts that guide authors through the ebook writing process, from ideation to proofreading and marketing.
- [Cheat Sheet for Crafting Effective ChatGPT Prompts](prompts/AITools/chatgpt4.md) - This cheat sheet provides a structured approach to writing effective ChatGPT prompts using roles, tasks, formats, linked prompting, and prompt priming techniques. Enhance precision, clarity, and actionable responses through these frameworks.
- [Comprehensive Guide to Creating an eBook from Online Sources](prompts/content-generator/ebook.md) - This document provides a clear process for creating an engaging eBook by extracting information from a specified web URL. It focuses on structuring content, targeting specific audiences, and implementing cohesive design elements to ensure a seamless reading experience.
- [Comprehensive Marketing and Content Prompt Guide](prompts/Business/marketing.md) - A curated collection of 50 versatile prompts tailored for marketing campaigns and content creation, designed to enhance creativity and strategic execution.
- [Comprehensive Prompt Guide for Authors](prompts/content-generator/ebook-writer.md) - A versatile collection of prompts tailored for authors to enhance book outlining, character development, plot troubleshooting, and more.
- [Comprehensive Prompt Guide for Strategic and Creative Tasks](prompts/learning/creative.md) - A detailed collection of actionable prompts to support strategic analysis, marketing initiatives, project planning, content creation, and personal development.
- [Create a Comprehensive Healthy Meal Plan Guide](prompts/health-nutrition/nutrition-expert.md) - Acts as a nutrition expert to create a detailed, multi-diet meal planning guide with sample meals, tips, and substitutions.
- [Creative Prompts for Entertainment and Storytelling](prompts/learning/fun.md) - A diverse collection of prompts to inspire humor, storytelling, and imaginative activities across multiple themes.
- [Critical Thinking Prompt Template](prompts/learning/critical-thinking.md) - This template guides users in developing deeper understanding and applying higher-order thinking to analyze, evaluate, and create ideas based on specific topics. Organized into six distinct levels of thought, each section is designed to enhance learning and intellectual engagement.
- [Cross-Platform Audit App Development Plan](prompts/app-development/audit-app.md) - Prompt for generating a comprehensive development plan for a free, cross-platform mobile and web app for auditors using open-source tools and AI coding assistants.
- [DeepSeek AI Prompt Hacks Cheat Sheet](prompts/AITools/deepseek.md) - A comprehensive cheat sheet of DeepSeek AI prompt hacks with categorized examples to help you create powerful AI-generated content, resumes, code, educational material, and more.
- [DeepSeek Cheat Sheet - AI Prompts for Skill Building, Business & Productivity](prompts/AITools/deepseek2.md) - A detailed guide to using DeepSeek AI for skill development, business consulting, content creation, writing improvement, productivity, and more—featuring ready-to-use prompts and examples.
- [eBook Writing Prompts That Sell](prompts/content-generator/ebooks-that-sell.md) - A set of tailored prompts to create captivating eBook titles, effective structures, and engaging chapters that resonate with readers.
- [Educator's Prompt Guide for Classroom Excellence](prompts/Academics/education.md) - A comprehensive list of prompts designed to inspire and empower educators in classroom management, lesson planning, student engagement, and progress monitoring.
- [Effective ChatGPT Prompts for Creating User Manuals](prompts/content-generator/manuals.md) - A guide with prompts and strategies to leverage ChatGPT for creating clear, user-friendly technical manuals.
- [Enhanced Productivity and Creativity Prompts with ChatGPT](prompts/Productivity/creative.md) - A collection of practical and creative prompts tailored to boost productivity, streamline workflows, and unlock creativity using ChatGPT.
- [Essential ChatGPT Prompts for Technical Documentation](prompts/content-generator/technical-documentation.md) - A curated collection of prompts for creating comprehensive, user-friendly technical documents with ChatGPT.
- [Ethical AI Use in Academic Writing – Prompts & Guide](prompts/Academics/academics.md) - A complete guide and prompt collection for using AI tools ethically in academic writing. Includes detailed steps, do’s and don’ts, and professional prompt templates.
- [Example Prompts for Data Analysis with ChatGPT](prompts/Data-analysis/chatgpt-data-analysis.md) - This document presents example prompts for utilizing ChatGPT to analyze research data effectively. Each prompt is tailored to specific data-related tasks, ensuring thorough and structured analysis.
- [Fictional Character Technical Advisor Prompt](prompts/content-generator/fiction.md) - A structured guide to assist fiction writers in crafting highly realistic and detailed technical achievements for their characters.
- [Formula for Crafting Effective ChatGPT Prompts](prompts/Productivity/chatgpt.md) - This document outlines a comprehensive formula for creating effective and precise ChatGPT prompts. By using structured components like roles, tasks, context, examples, and constraints, users can achieve highly relevant and actionable outputs.
- [Generate Research Papers](prompts/Academics/research-papers.md) - A structured prompt for generating comprehensive research papers using provided content. Includes sections for literature review, findings, case studies, and recommendations—complete with citations and future exploration paths.
- [Grok 3 Prompting Master Cheat Sheet](prompts/AITools/grok.md) - Unlock Grok 3's full potential with this master cheat sheet of expert-level prompts. Learn the perfect prompt formula, roles, tasks, formats, and real-world use cases to save hours daily.
- [GST Data Analysis for Audit](prompts/audit/gst-data-anaylsis.md) - Analyzes GST data for audit compliance, focusing on turnover, ITC, and regulatory adherence
- [Imaginative Creative Writing Prompts](prompts/Academics/creative-writing.md) - A collection of 20 imaginative prompts to spark creativity, world-building, and futuristic storytelling.
- [Learn Anything 5x Faster with These 9 Proven Methods](prompts/learning/learning-techniques.md) - A complete guide from beginner to expert on how to learn faster using 9 cognitive science-based frameworks. Includes explanations, use cases, and 27 actionable prompts.
- [Master Excel with DeepSeek](prompts/excel/excel-deepseek.md) - Discover 10 advanced Excel prompts designed to help you master dashboards, automation, data filtering, array formulas, Solver, and more. Ideal for professionals looking to boost productivity with Excel.
- [Mastering Common Interview Questions with ChatGPT](prompts/Career-Tips/Interview.md) - Learn how to master the most common interview questions using ChatGPT, with examples, prompts, pros, cons, and limitations for each. Perfect for job seekers who want to prepare smarter and faster.
- [Maximizing ChatGPT with Structured Prompts Across Applications](prompts/Productivity/produtivity2.md) - A guide that categorizes and explains structured prompts for utilizing ChatGPT effectively. Includes examples and uses for business, content creation, learning, and personal development.
- [Problem Solving Using Mental Models](prompts/AITools/Problem-Solving.md) - Learn how to use ChatGPT more effectively by applying 9 powerful mental models for problem solving. Each framework includes 3 practical examples to guide your strategy, planning, and execution.
- [Prompt Engineering Guide for SaaS Product Development](prompts/content-generator/saas.md) - A detailed guide to crafting effective prompts for building a successful SaaS product, with focus on technical, business, and implementation aspects.
- [Prompts for Crafting Human-Like SEO Content](prompts/content-generator/seo.md) - A detailed prompt template guiding the creation of engaging, human-like SEO articles that balance technical precision and emotional relatability.
- [Prompts for Research Data Analysis](prompts/Data-analysis/data-analysis-research.md) - This document provides example prompts for utilizing ChatGPT to analyze research data effectively. Each prompt is tailored to specific data-related tasks, ensuring thorough and structured analysis.
- [Prompts to Write a Nonfiction Ebook](prompts/content-generator/non-fiction.md) - A collection of prompts to guide authors in every stage of nonfiction ebook creation, from ideation to marketing.
- [Thesis Outline – 7 Chapters with Detailed Elements](prompts/Academics/research-academics.md) - This guide breaks down a typical thesis structure into 7 chapters with detailed sub-elements, examples, purposes, and practical uses. Ideal for students planning and writing academic theses.
- [Ultimate Android Camera Text Scanner App – AI-Powered Document Scanner & OCR](prompts/app-development/camscanner-app.md) - Build an advanced Android camera document scanning app with smart features, OCR, AI-enhanced image processing, and optimized performance.
- [Use AI to Learn Anything Faster](prompts/AITools/learn-faster.md) - A practical guide on how to leverage AI tools like ChatGPT to supercharge your learning using proven techniques like simplification, analogies, quizzes, mind maps, and more.
- [youtube-script](prompts/content-generator/youtube-script.md) - 

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