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
    B --> CAT1[AI-Learning]
    B --> CAT2[AI-Techniques]
    B --> CAT3[AI-Tools]
    B --> CAT4[Audit]
    B --> CAT5[Business]
    B --> CAT6[Career]
    B --> CAT7[Content-Creation]
    B --> CAT8[Content-Generation]
    B --> CAT9[Content-generation]
    B --> CAT10[Creative]
    B --> CAT11[Data-Analysis]
    B --> CAT12[Design]
    B --> CAT13[Education]
    B --> CAT14[Excel]
    B --> CAT15[Fun]
    B --> CAT16[Learning]
    B --> CAT17[Marketing]
    B --> CAT18[Productivity]
    B --> CAT19[Programming]
    B --> CAT20[Prompting]
    B --> CAT21[SEO]
    B --> CAT22[Writing]
    B --> CAT23[academic-writing]
    B --> CAT24[content-generation]
    B --> CAT25[creative-writing]
    B --> CAT26[deepseek]
    B --> CAT27[health-nutrition]
    B --> CAT28[learning]
    CAT1[AI-Learning] --> F11[Comprehensive List of Prompt Types with Examples.md]
    CAT2[AI-Techniques] --> F21[Mastering the Art of AI Prompts - A Guide to Unlocking Creative Potential.md]
    CAT3[AI-Tools] --> F31[Boost Productivity with These Powerful ChatGPT Prompts.md]
    CAT3[AI-Tools] --> F32[Problem Solving Using Mental Models.md]
    CAT4[Audit] --> F41[Audit Observations.md]
    CAT4[Audit] --> F42[ChatGPT Prompts for Building a GST Audit Tool.md]
    CAT4[Audit] --> F43[GST Data Analysis for Audit.md]
    CAT5[Business] --> F51[9 ChatGPT Prompts to Find Profitable Market Opportunities.md]
    CAT6[Career] --> F61[Mastering Common Interview Questions with ChatGPT.md]
    CAT6[Career] --> F62[Practical and Versatile Prompts for Crafting Cover Letters.md]
    CAT6[Career] --> F63[Prompts for Specialized Tasks.md]
    CAT6[Career] --> F64[Resume Creation Prompts for Tailored Career Documents.md]
    CAT7[Content-Creation] --> F71[18 ChatGPT Prompts for Content Creation.md]
    CAT7[Content-Creation] --> F72[AI-Powered YouTube Video Script Generator.md]
    CAT8[Content-Generation] --> F81[Comprehensive Guide to Creating an eBook from Online Sources.md]
    CAT8[Content-Generation] --> F82[Enhanced Writing Prompts.md]
    CAT8[Content-Generation] --> F83[Podcast Creation Comprehensive Prompt.md]
    CAT9[Content-generation] --> F91[18 ChatGPT Prompts for User Experience.md]
    CAT10[Creative] --> F101[Comprehensive Brainstorming Prompts.md]
    CAT10[Creative] --> F102[Income-Generating AI Prompts Across Fields.md]
    CAT11[Data-Analysis] --> F111[Example Prompts for Data Analysis with ChatGPT.md]
    CAT11[Data-Analysis] --> F112[Prompts for Research Data Analysis.md]
    CAT12[Design] --> F121[Create a 3D Kawaii-Style Canvas with Chibi Stickers.md]
    CAT12[Design] --> F122[Trending Prompts for Stunning Image Generation.md]
    CAT13[Education] --> F131[ChatGPT Prompts for Learning and Development.md]
    CAT13[Education] --> F132[ChatGPT Prompts for Teaching.md]
    CAT13[Education] --> F133[Educator's Prompt Guide for Classroom Excellence.md]
    CAT14[Excel] --> F141[Master Excel with DeepSeek.md]
    CAT15[Fun] --> F151[Creative Prompts for Entertainment and Storytelling.md]
    CAT16[Learning] --> F161[10 Powerful AI-Based Learning Techniques for Mastering Any Topic.md]
    CAT16[Learning] --> F162[Comprehensive Prompt Guide for Strategic and Creative Tasks.md]
    CAT16[Learning] --> F163[Critical Thinking Prompt Template.md]
    CAT16[Learning] --> F164[Learn Anything 5x Faster with These 9 Proven Methods.md]
    CAT16[Learning] --> F165[Use AI to Learn Anything Faster.md]
    CAT17[Marketing] --> F171[18 ChatGPT Prompts for Advertising.md]
    CAT17[Marketing] --> F172[18 ChatGPT Prompts for Digital Marketing.md]
    CAT17[Marketing] --> F173[18 ChatGPT Prompts for Social Media Marketing.md]
    CAT17[Marketing] --> F174[Comprehensive Marketing and Content Prompt Guide.md]
    CAT17[Marketing] --> F175[Comprehensive Marketing Prompts.md]
    CAT18[Productivity] --> F181[5 Problem-Solving Method Prompts for Founders & CEOs.md]
    CAT18[Productivity] --> F182[Boosting Productivity with ChatGPT.md]
    CAT18[Productivity] --> F183[Boosting Productivity with ChatGPT.md]
    CAT18[Productivity] --> F184[Builder-to-Brand Gameplan - Brutal Focus Roadmap.md]
    CAT18[Productivity] --> F185[ChatGPT Prompt Frameworks for Effective Task Structuring.md]
    CAT18[Productivity] --> F186[Enhanced Productivity and Creativity Prompts with ChatGPT.md]
    CAT18[Productivity] --> F187[Formula for Crafting Effective ChatGPT Prompts.md]
    CAT18[Productivity] --> F188[Maximizing ChatGPT with Structured Prompts Across Applications.md]
    CAT18[Productivity] --> F189[Prompts for Enhancing Productivity Across Fields.md]
    CAT18[Productivity] --> F1810[Prompts for Professional Productivity.md]
    CAT18[Productivity] --> F1811[Prompts for Versatile Use Cases.md]
    CAT19[Programming] --> F191[10 Useful ChatGPT Prompts for Developers.md]
    CAT19[Programming] --> F192[50 Prompts for Extracting Text from PDF Tables Using Excel, Power Query, and Python.md]
    CAT19[Programming] --> F193[ChatGPT Prompts for Data Science.md]
    CAT19[Programming] --> F194[ChatGPT Prompts for Software Development.md]
    CAT19[Programming] --> F195[Cross-Platform Audit App Development Plan.md]
    CAT19[Programming] --> F196[Developer Prompts for Productivity and Clarity.md]
    CAT19[Programming] --> F197[Prompts for Coding and Project Generation.md]
    CAT19[Programming] --> F198[Ultimate Android Camera Text Scanner App – AI-Powered Document Scanner & OCR.md]
    CAT20[Prompting] --> F201[12 Must-Know ChatGPT Prompt Techniques.md]
    CAT20[Prompting] --> F202[ChatGPT Cheat Sheet - Crafting Effective Prompts.md]
    CAT20[Prompting] --> F203[ChatGPT for Marketing.md]
    CAT20[Prompting] --> F204[ChatGPT Prompt Cheatsheet for Various Use Cases.md]
    CAT20[Prompting] --> F205[ChatGPT Prompt Frameworks – Full Guide with Examples.md]
    CAT20[Prompting] --> F206[ChatGPT Prompt Guide.md]
    CAT20[Prompting] --> F207[ChatGPT Prompt Guide for Structured Usage.md]
    CAT20[Prompting] --> F208[ChatGPT Prompting Frameworks Explained.md]
    CAT20[Prompting] --> F209[Cheat Sheet for Crafting Effective ChatGPT Prompts.md]
    CAT20[Prompting] --> F2010[DeepSeek AI Prompt Hacks Cheat Sheet.md]
    CAT20[Prompting] --> F2011[DeepSeek Cheat Sheet - AI Prompts for Skill Building, Business & Productivity.md]
    CAT20[Prompting] --> F2012[Grok 3 Prompting Master Cheat Sheet.md]
    CAT20[Prompting] --> F2013[Prompt Engineering Guide for SaaS Product Development.md]
    CAT21[SEO] --> F211[18 ChatGPT Prompts for SEO.md]
    CAT21[SEO] --> F212[Advanced SEO Strategies and Content Optimization Prompts.md]
    CAT21[SEO] --> F213[Prompts for Crafting Human-Like SEO Content.md]
    CAT22[Writing] --> F221[ChatGPT Prompts for Producing Your Ebook Manuscript.md]
    CAT22[Writing] --> F222[ChatGPT Prompts for Writing a Book.md]
    CAT22[Writing] --> F223[ChatGPT Prompts for Writing an Ebook.md]
    CAT22[Writing] --> F224[Comprehensive Prompt Guide for Authors.md]
    CAT22[Writing] --> F225[eBook Writing Prompts That Sell.md]
    CAT22[Writing] --> F226[Effective ChatGPT Prompts for Creating User Manuals.md]
    CAT22[Writing] --> F227[Essential ChatGPT Prompts for Technical Documentation.md]
    CAT22[Writing] --> F228[Fictional Character Technical Advisor Prompt.md]
    CAT22[Writing] --> F229[Frequently Used Words in ChatGPT Conversations.md]
    CAT22[Writing] --> F2210[Prompts for Crafting Audit Manuals and Guidelines.md]
    CAT22[Writing] --> F2211[Prompts for Crafting Ebooks Focused on Manuals and Guidelines.md]
    CAT22[Writing] --> F2212[Prompts for Crafting Government Audit Manuals and Guidelines.md]
    CAT22[Writing] --> F2213[Prompts for Writing a Book.md]
    CAT22[Writing] --> F2214[Prompts to Write a Nonfiction Ebook.md]
    CAT22[Writing] --> F2215[Step-by-Step Book Writing Prompts.md]
    CAT22[Writing] --> F2216[Supercharge Your Creativity - Using AI to Brainstorm Like Never Before.md]
    CAT22[Writing] --> F2217[Trending Ebook Prompts for Your Next Writing Project.md]
    CAT23[academic-writing] --> F231[Comprehensive Thesis Chapter Prompts.md]
    CAT23[academic-writing] --> F232[Ethical AI Use in Academic Writing – Prompts & Guide.md]
    CAT23[academic-writing] --> F233[Generate Research Papers.md]
    CAT24[content-generation] --> F241[Blog Post Generator.md]
    CAT25[creative-writing] --> F251[Imaginative Creative Writing Prompts.md]
    CAT26[deepseek] --> F261[Deepseek prompts.md]
    CAT27[health-nutrition] --> F271[Create a Comprehensive Healthy Meal Plan Guide.md]
    CAT28[learning] --> F281[10 Powerful AI-Based Learning Techniques.md]
    C --> S[update_index.py]
    D --> W[update-index.yml]
    E --> I[indexing.png]
    A --> R[README.md]
    A --> T[categories.md]
```

## Prompt Categories

| Category     | Description                              | Example Prompt              |
|--------------|------------------------------------------|-----------------------------|
| AI-Learning | Prompts for AI Learning  | Comprehensive List of Prompt Types with Examples |
| AI-Techniques | Prompts for AI Techniques  | Mastering the Art of AI Prompts - A Guide to Unlocking Creative Potential |
| AI-Tools | Prompts for AI Tools  | Boost Productivity with These Powerful ChatGPT Prompts |
| Audit | Prompts for Audit  | Audit Observations |
| Business | Prompts for Business  | 9 ChatGPT Prompts to Find Profitable Market Opportunities |
| Career | Prompts for Career  | Mastering Common Interview Questions with ChatGPT |
| Content-Creation | Prompts for Content Creation  | 18 ChatGPT Prompts for Content Creation |
| Content-Generation | Prompts for Content Generation  | Comprehensive Guide to Creating an eBook from Online Sources |
| Content-generation | Prompts for Content generation  | 18 ChatGPT Prompts for User Experience |
| Creative | Prompts for Creative  | Comprehensive Brainstorming Prompts |
| Data-Analysis | Prompts for Data Analysis  | Example Prompts for Data Analysis with ChatGPT |
| Design | Prompts for Design  | Create a 3D Kawaii-Style Canvas with Chibi Stickers |
| Education | Prompts for Education  | ChatGPT Prompts for Learning and Development |
| Excel | Prompts for Excel  | Master Excel with DeepSeek |
| Fun | Prompts for Fun  | Creative Prompts for Entertainment and Storytelling |
| Learning | Prompts for Learning  | 10 Powerful AI-Based Learning Techniques for Mastering Any Topic |
| Marketing | Prompts for Marketing  | 18 ChatGPT Prompts for Advertising |
| Productivity | Prompts for Productivity  | 5 Problem-Solving Method Prompts for Founders & CEOs |
| Programming | Prompts for Programming  | 10 Useful ChatGPT Prompts for Developers |
| Prompting | Prompts for Prompting  | 12 Must-Know ChatGPT Prompt Techniques |
| SEO | Prompts for SEO  | 18 ChatGPT Prompts for SEO |
| Writing | Prompts for Writing  | ChatGPT Prompts for Producing Your Ebook Manuscript |
| academic-writing | Prompts for academic writing  | Comprehensive Thesis Chapter Prompts |
| content-generation | Prompts for content generation  | Blog Post Generator |
| creative-writing | Prompts for creative writing  | Imaginative Creative Writing Prompts |
| deepseek | Prompts for deepseek  | Deepseek prompts |
| health-nutrition | Prompts for health nutrition  | Create a Comprehensive Healthy Meal Plan Guide |
| learning | Prompts for learning  | 10 Powerful AI-Based Learning Techniques |

## Prompts

- [10 Powerful AI-Based Learning Techniques](prompts/learning/ai-based-learning.md) - Master any topic faster with these 10 optimized prompt templates designed to enhance understanding, retention, and motivation.
- [10 Powerful AI-Based Learning Techniques for Mastering Any Topic](prompts/learning/ai-learning.md) - This guide explains 10 AI-based learning techniques to make mastering any topic faster and easier. Each technique includes use cases, examples, prompt templates, and optimized prompts for direct implementation.
- [10 Useful ChatGPT Prompts for Developers](prompts/app-development/software-development2.md) - A detailed guide to 10 essential ChatGPT prompts designed to assist developers in various aspects of software development, including coding, debugging, API design, database management, and learning best practices.
- [12 Must-Know ChatGPT Prompt Techniques](prompts/AITools/chatgpt.md) - Learn how to use 12 powerful ChatGPT prompt techniques with 36 ready-to-use examples for better results in learning, creativity, productivity, and problem-solving.
- [18 ChatGPT Prompts for Advertising](prompts/Business/advertising.md) - A collection of prompts for crafting impactful advertising campaigns, scripts, and strategies tailored to any product or audience.
- [18 ChatGPT Prompts for Content Creation](prompts/content-generator/content-creation.md) - A versatile collection of ChatGPT prompts to help create compelling content for blogs, videos, emails, and more.
- [18 ChatGPT Prompts for Digital Marketing](prompts/Business/digital-marketing.md) - A curated collection of prompts to assist digital marketers in creating content for multiple platforms, from social media posts to email sequences.
- [18 ChatGPT Prompts for SEO](prompts/content-generator/seos.md) - A set of advanced prompts to streamline SEO tasks, from meta descriptions to content gap analysis and keyword research.
- [18 ChatGPT Prompts for Social Media Marketing](prompts/content-generator/social-media.md) - A collection of expert prompts for creating engaging social media content across platforms and formats.
- [18 ChatGPT Prompts for User Experience](prompts/content-generator/ux.md) - A curated set of prompts to enhance user experience design and research efforts for applications, websites, and platforms.
- [5 Problem-Solving Method Prompts for Founders & CEOs](prompts/AITools/5tools.md) - Practical ChatGPT prompts for applying five strategic problem-solving frameworks—Pre-Mortem, 5 Whys, Decision Tree, SWOT, and Impact vs Effort Matrix.
- [50 Prompts for Extracting Text from PDF Tables Using Excel, Power Query, and Python](prompts/app-development/data-extraction.md) - A comprehensive guide with 50 prompts to extract text from tables in multiple PDF files using Excel, Power Query, and Python. This includes formula-based, automated, and code-driven approaches for handling complex data structures.
- [9 ChatGPT Prompts to Find Profitable Market Opportunities](prompts/Business/Market.md) - Discover 9 powerful ChatGPT prompts to uncover hidden market opportunities, along with 3 real-world examples for each to help spark your next venture.
- [Advanced SEO Strategies and Content Optimization Prompts](prompts/content-generator/seo-prompt.md) - A collection of actionable SEO prompts to enhance content strategy, search rankings, and overall site performance.
- [AI-Powered YouTube Video Script Generator](prompts/content-generator/youtube-script.md) - This prompt is designed for content creators, marketers, and YouTubers who want to generate engaging and well-structured scripts for YouTube videos using AI.
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
- [Comprehensive Brainstorming Prompts](prompts/Academics/brainstorm.md) - Detailed prompts to utilize brainstorming frameworks and techniques for generating innovative ideas.
- [Comprehensive Guide to Creating an eBook from Online Sources](prompts/content-generator/ebook.md) - This document provides a clear process for creating an engaging eBook by extracting information from a specified web URL. It focuses on structuring content, targeting specific audiences, and implementing cohesive design elements to ensure a seamless reading experience.
- [Comprehensive List of Prompt Types with Examples](prompts/learning/prompts.md) - A categorized set of prompts to effectively guide conversations and outputs with AI across various contexts.
- [Comprehensive Marketing and Content Prompt Guide](prompts/Business/marketing.md) - A curated collection of 50 versatile prompts tailored for marketing campaigns and content creation, designed to enhance creativity and strategic execution.
- [Comprehensive Marketing Prompts](prompts/Business/marketing2.md) - A collection of versatile prompts for optimizing marketing efforts, from campaign planning to creative content generation.
- [Comprehensive Prompt Guide for Authors](prompts/content-generator/ebook-writer.md) - A versatile collection of prompts tailored for authors to enhance book outlining, character development, plot troubleshooting, and more.
- [Comprehensive Prompt Guide for Strategic and Creative Tasks](prompts/learning/creative.md) - A detailed collection of actionable prompts to support strategic analysis, marketing initiatives, project planning, content creation, and personal development.
- [Comprehensive Thesis Chapter Prompts](prompts/Academics/research-academics.md) - Detailed prompts for guiding the creation of each thesis chapter, from introduction to references.
- [Create a 3D Kawaii-Style Canvas with Chibi Stickers](prompts/content-generator/stickers.md) - A creative prompt to generate a 3D kawaii-style canvas in A4 size featuring chibi stickers with unique expressions and fun phrases.
- [Create a Comprehensive Healthy Meal Plan Guide](prompts/health-nutrition/nutrition-expert.md) - Acts as a nutrition expert to create a detailed, multi-diet meal planning guide with sample meals, tips, and substitutions.
- [Creative Prompts for Entertainment and Storytelling](prompts/learning/fun.md) - A diverse collection of prompts to inspire humor, storytelling, and imaginative activities across multiple themes.
- [Critical Thinking Prompt Template](prompts/learning/critical-thinking.md) - This template guides users in developing deeper understanding and applying higher-order thinking to analyze, evaluate, and create ideas based on specific topics. Organized into six distinct levels of thought, each section is designed to enhance learning and intellectual engagement.
- [Cross-Platform Audit App Development Plan](prompts/app-development/audit-app.md) - Prompt for generating a comprehensive development plan for a free, cross-platform mobile and web app for auditors using open-source tools and AI coding assistants.
- [DeepSeek AI Prompt Hacks Cheat Sheet](prompts/AITools/deepseek.md) - A comprehensive cheat sheet of DeepSeek AI prompt hacks with categorized examples to help you create powerful AI-generated content, resumes, code, educational material, and more.
- [DeepSeek Cheat Sheet - AI Prompts for Skill Building, Business & Productivity](prompts/AITools/deepseek2.md) - A detailed guide to using DeepSeek AI for skill development, business consulting, content creation, writing improvement, productivity, and more—featuring ready-to-use prompts and examples.
- [Deepseek prompts](prompts/deepseek/2025.04.18.md) - Collection of Deepseek prompts
- [Developer Prompts for Productivity and Clarity](prompts/app-development/software-development.md) - A set of detailed prompts to guide developers in specific scenarios, ensuring maximum efficiency and clear outcomes.
- [eBook Writing Prompts That Sell](prompts/content-generator/ebooks-that-sell.md) - A set of tailored prompts to create captivating eBook titles, effective structures, and engaging chapters that resonate with readers.
- [Educator's Prompt Guide for Classroom Excellence](prompts/Academics/education.md) - A comprehensive list of prompts designed to inspire and empower educators in classroom management, lesson planning, student engagement, and progress monitoring.
- [Effective ChatGPT Prompts for Creating User Manuals](prompts/content-generator/manuals.md) - A guide with prompts and strategies to leverage ChatGPT for creating clear, user-friendly technical manuals.
- [Enhanced Productivity and Creativity Prompts with ChatGPT](prompts/Productivity/creative.md) - A collection of practical and creative prompts tailored to boost productivity, streamline workflows, and unlock creativity using ChatGPT.
- [Enhanced Writing Prompts](prompts/content-generator/contents.md) - A detailed and comprehensive set of prompts to elevate writing projects across various domains.
- [Essential ChatGPT Prompts for Technical Documentation](prompts/content-generator/technical-documentation.md) - A curated collection of prompts for creating comprehensive, user-friendly technical documents with ChatGPT.
- [Ethical AI Use in Academic Writing – Prompts & Guide](prompts/Academics/academics.md) - A complete guide and prompt collection for using AI tools ethically in academic writing. Includes detailed steps, do’s and don’ts, and professional prompt templates.
- [Example Prompts for Data Analysis with ChatGPT](prompts/Data-analysis/chatgpt-data-analysis.md) - This document presents example prompts for utilizing ChatGPT to analyze research data effectively. Each prompt is tailored to specific data-related tasks, ensuring thorough and structured analysis.
- [Fictional Character Technical Advisor Prompt](prompts/content-generator/fiction.md) - A structured guide to assist fiction writers in crafting highly realistic and detailed technical achievements for their characters.
- [Formula for Crafting Effective ChatGPT Prompts](prompts/Productivity/chatgpt.md) - This document outlines a comprehensive formula for creating effective and precise ChatGPT prompts. By using structured components like roles, tasks, context, examples, and constraints, users can achieve highly relevant and actionable outputs.
- [Frequently Used Words in ChatGPT Conversations](prompts/Academics/chatgpt-words.md) - Categorized lists of commonly used words and phrases in ChatGPT interactions, with examples to illustrate their usage.
- [Generate Research Papers](prompts/Academics/research-papers.md) - A structured prompt for generating comprehensive research papers using provided content. Includes sections for literature review, findings, case studies, and recommendations—complete with citations and future exploration paths.
- [Grok 3 Prompting Master Cheat Sheet](prompts/AITools/grok.md) - Unlock Grok 3's full potential with this master cheat sheet of expert-level prompts. Learn the perfect prompt formula, roles, tasks, formats, and real-world use cases to save hours daily.
- [GST Data Analysis for Audit](prompts/audit/gst-data-anaylsis.md) - Analyzes GST data for audit compliance, focusing on turnover, ITC, and regulatory adherence
- [Imaginative Creative Writing Prompts](prompts/Academics/creative-writing.md) - A collection of 20 imaginative prompts to spark creativity, world-building, and futuristic storytelling.
- [Income-Generating AI Prompts Across Fields](prompts/Business/income-generator.md) - Comprehensive prompts leveraging AI to generate income across content creation, e-commerce, finance, healthcare, education, and more.
- [Learn Anything 5x Faster with These 9 Proven Methods](prompts/learning/learning-techniques.md) - A complete guide from beginner to expert on how to learn faster using 9 cognitive science-based frameworks. Includes explanations, use cases, and 27 actionable prompts.
- [Master Excel with DeepSeek](prompts/excel/excel-deepseek.md) - Discover 10 advanced Excel prompts designed to help you master dashboards, automation, data filtering, array formulas, Solver, and more. Ideal for professionals looking to boost productivity with Excel.
- [Mastering Common Interview Questions with ChatGPT](prompts/Career-Tips/Interview.md) - Learn how to master the most common interview questions using ChatGPT, with examples, prompts, pros, cons, and limitations for each. Perfect for job seekers who want to prepare smarter and faster.
- [Mastering the Art of AI Prompts - A Guide to Unlocking Creative Potential](prompts/Productivity/creativity3.md) - Explore a detailed guide to crafting tailored prompts for various domains—enhancing creativity, productivity, and problem-solving.
- [Maximizing ChatGPT with Structured Prompts Across Applications](prompts/Productivity/produtivity2.md) - A guide that categorizes and explains structured prompts for utilizing ChatGPT effectively. Includes examples and uses for business, content creation, learning, and personal development.
- [Podcast Creation Comprehensive Prompt](prompts/content-generator/podcast.md) - A structured guide for creating podcasts that blend human creativity with AI tools for efficiency and quality.
- [Practical and Versatile Prompts for Crafting Cover Letters](prompts/Career-Tips/coverletter.md) - A collection of six tailored prompts to create, polish, and customize cover letters for job seekers.
- [Problem Solving Using Mental Models](prompts/AITools/Problem-Solving.md) - Learn how to use ChatGPT more effectively by applying 9 powerful mental models for problem solving. Each framework includes 3 practical examples to guide your strategy, planning, and execution.
- [Prompt Engineering Guide for SaaS Product Development](prompts/content-generator/saas.md) - A detailed guide to crafting effective prompts for building a successful SaaS product, with focus on technical, business, and implementation aspects.
- [Prompts for Coding and Project Generation](prompts/Academics/projects.md) - A collection of creative prompts to inspire app development, website creation, and GitHub project setups.
- [Prompts for Crafting Audit Manuals and Guidelines](prompts/Academics/audit-manuals.md) - A collection of focused and detailed prompts to assist in creating audit-focused ebooks across industries.
- [Prompts for Crafting Ebooks Focused on Manuals and Guidelines](prompts/Academics/manuals.md) - A collection of structured prompts for creating official documents, including manuals and guidelines for various industries.
- [Prompts for Crafting Government Audit Manuals and Guidelines](prompts/Academics/documents.md) - A detailed set of prompts to create structured and informative ebooks focused on government audits using acts and regulations.
- [Prompts for Crafting Human-Like SEO Content](prompts/content-generator/seo.md) - A detailed prompt template guiding the creation of engaging, human-like SEO articles that balance technical precision and emotional relatability.
- [Prompts for Enhancing Productivity Across Fields](prompts/Academics/resume.md) - Practical prompts to streamline tasks and boost creativity in various fields like marketing, education, and technology.
- [Prompts for Professional Productivity](prompts/Productivity/professional.md) - A curated collection of practical prompts to optimize professional tasks and improve workflow efficiency.
- [Prompts for Research Data Analysis](prompts/Data-analysis/data-analysis-research.md) - This document provides example prompts for utilizing ChatGPT to analyze research data effectively. Each prompt is tailored to specific data-related tasks, ensuring thorough and structured analysis.
- [Prompts for Specialized Tasks](prompts/Productivity/tasks.md) - A collection of tailored prompts to streamline writing, analysis, problem-solving, and tool learning for specific tasks.
- [Prompts for Versatile Use Cases](prompts/Productivity/creativity.md) - A set of diverse ChatGPT prompts to enhance creativity, knowledge, and problem-solving across various tasks.
- [Prompts for Writing a Book](prompts/Academics/book.md) - A detailed framework for brainstorming, drafting, refining, and marketing books in various genres and styles.
- [Prompts to Write a Nonfiction Ebook](prompts/content-generator/non-fiction.md) - A collection of prompts to guide authors in every stage of nonfiction ebook creation, from ideation to marketing.
- [Resume Creation Prompts for Tailored Career Documents](prompts/Academics/resumes.md) - A set of focused prompts to craft personalized, impactful resumes and other career-related materials.
- [Step-by-Step Book Writing Prompts](prompts/Academics/books.md) - A detailed set of prompts to assist with brainstorming, writing, refining, and marketing your book project.
- [Supercharge Your Creativity - Using AI to Brainstorm Like Never Before](prompts/Productivity/creativity2.md) - A structured guide to maximizing brainstorming potential using AI techniques for innovative solutions and unique perspectives.
- [Trending Ebook Prompts for Your Next Writing Project](prompts/content-generator/writing.md) - A collection of detailed prompts to inspire creativity and craft engaging ebook stories or guides.
- [Trending Prompts for Stunning Image Generation](prompts/content-generator/image-generation.md) - A curated collection of prompts to inspire visually captivating AI-generated images across diverse themes.
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