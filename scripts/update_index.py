import os
import yaml
from pathlib import Path

def parse_front_matter(file_path):
    """Extract front matter from a markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.startswith('---'):
                front_matter = content.split('---')[1].strip()
                return yaml.safe_load(front_matter) or {}
    except Exception as e:
        print(f"Error parsing front matter in {file_path}: {e}")
    return {}

def collect_prompts(prompts_dir):
    """Collect all prompts and their metadata."""
    prompts = []
    repo_root = Path(__file__).parent.parent  # Repository root (prompts-repo/)
    prompts_path = repo_root / prompts_dir

    if not prompts_path.exists():
        print(f"Prompts directory {prompts_path} does not exist.")
        return prompts

    for category_dir in prompts_path.iterdir():
        if category_dir.is_dir():
            category = category_dir.name
            for file in category_dir.glob('*.md'):
                try:
                    # Compute relative path from repo root
                    relative_path = file.relative_to(repo_root).as_posix()
                    front_matter = parse_front_matter(file)
                    if front_matter:
                        prompts.append({
                            'title': front_matter.get('title', file.stem),
                            'category': front_matter.get('category', category),
                            'description': front_matter.get('description', ''),
                            'path': relative_path
                        })
                except Exception as e:
                    print(f"Error processing {file}: {e}")
    return sorted(prompts, key=lambda x: x['title'].lower())

def generate_mermaid_diagram(categories):
    """Generate a dynamic Mermaid diagram including all categories."""
    lines = [
        "```mermaid",
        "graph TD",
        "    A[prompts-repo] --> B[prompts]",
        "    A --> C[scripts]",
        "    A --> D[.github/workflows]",
        "    A --> E[docs/images]"
    ]
    category_nodes = []
    file_nodes = []
    for i, category in enumerate(sorted(categories)):
        cat_node = f"CAT{i+1}[{category}]"
        category_nodes.append(f"    B --> {cat_node}")
        for j, prompt in enumerate(categories[category]):
            file_node = f"F{i+1}{j+1}[{prompt['title']}.md]"
            file_nodes.append(f"    {cat_node} --> {file_node}")
    
    lines.extend(category_nodes)
    lines.extend(file_nodes)
    lines.extend([
        "    C --> S[update_index.py]",
        "    D --> W[update-index.yml]",
        "    E --> I[indexing.png]",
        "    A --> R[README.md]",
        "    A --> T[categories.md]"
    ])
    lines.append("```")
    return lines

def update_readme(prompts):
    """Update README.md with enhanced content."""
    categories = {}
    for prompt in prompts:
        cat = prompt['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(prompt)
    
    content = [
        "# GPT Prompt Templates",
        "",
        "[![GitHub stars](https://img.shields.io/github/stars/phuchungbhutia/prompts-repo)](https://github.com/phuchungbhutia/prompts-repo/stargazers) "
        "[![License](https://img.shields.io/github/license/phuchungbhutia/prompts-repo)](https://github.com/phuchungbhutia/prompts-repo/blob/main/LICENSE) "
        "[![Workflow Status](https://img.shields.io/github/workflow/status/phuchungbhutia/prompts-repo/Update%20Prompt%20Indexes)](https://github.com/phuchungbhutia/prompts-repo/actions) "
        "[![Contributors](https://img.shields.io/github/contributors/phuchungbhutia/prompts-repo)](https://github.com/phuchungbhutia/prompts-repo/graphs/contributors) "
        "[![Last Updated](https://img.shields.io/github/last-commit/phuchungbhutia/prompts-repo/main?label=Last%20Updated)](https://github.com/phuchungbhutia/prompts-repo/commits/main)",
        "",
        "This repository contains a collection of GPT prompt templates organized by category, with automated indexing via GitHub Actions.",
        "",
        "## Repository Stats",
        "",
        "![GitHub Stats](https://github-readme-stats.vercel.app/api?username=phuchungbhutia&show_icons=true&theme=radical)",
        "",
        "## Repository Structure",
        ""
    ]
    content.extend(generate_mermaid_diagram(categories))
    content.extend([
        "",
        "## Prompt Categories",
        "",
        "| Category     | Description                              | Example Prompt              |",
        "|--------------|------------------------------------------|-----------------------------|"
    ])
    
    for category in sorted(categories.keys()):
        example = categories[category][0]['title']
        content.append(f"| {category} | Prompts for {category.replace('-', ' ')}  | {example} |")
    
    content.extend([
        "",
        "## Prompts",
        ""
    ])
    for prompt in prompts:
        content.append(f"- [{prompt['title']}]({prompt['path']}) - {prompt['description']}")
    
    content.extend([
        "",
        "## Installation",
        "",
        "Clone the repository:",
        "```bash",
        "git clone https://github.com/phuchungbhutia/prompts-repo.git",
        "cd prompts-repo",
        "```",
        "",
        "Run the indexing script:",
        "```python",
        "python scripts/update_index.py",
        "```",
        "",
         "### 💡 Tip: If You Update Files Later",
        "",
        "```",
        "git add .",
        "git commit -m [Update]",
        "git push",
        "```",
        "",
        "## Contributing",
        "",
        "1. Add a new prompt in `/prompts/category_name/` using the [template](prompts/template.md).",
        "2. Run `python scripts/update_index.py` to update indexes.",
        "3. Submit a pull request.",
        "",
        "To add yourself as a contributor, use the all-contributors bot:",
        "```bash",
        "npm run contributors:add <your-username> code",
        "```",
        "",
        "## Contributors",
        "",
        "<!-- ALL-CONTRIBUTORS-LIST:START -->",
        "<!-- This section is automatically generated by all-contributors -->",
        "<!-- ALL-CONTRIBUTORS-LIST:END -->",
        "",
        "## License",
        "",
        "MIT License. See [LICENSE](LICENSE) for details.",
        "",
        "## Indexing in Action",
        "",
        "![Indexing Script](docs/images/indexing.png)",
        "",
        "(https://www.flaticon.com/free-icons/layout)"
    ])
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))

def update_categories(prompts):
    """Update categories.md with prompts grouped by category."""
    content = [
        "# Prompt Categories",
        "",
        "Prompts are grouped by category below.",
        "",
        "## Category Summary",
        "",
        "| Category | Description | Example Prompt |",
        "|----------|-------------|---------------|"
    ]
    categories = {}
    for prompt in prompts:
        cat = prompt['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(prompt)
    
    for category in sorted(categories.keys()):
        example = categories[category][0]['title']
        content.append(f"| {category} | Prompts for {category.replace('-', ' ')}  | {example} |")
    
    content.append("")
    for category, cat_prompts in sorted(categories.items()):
        content.append(f"## {category}")
        content.append("")
        for prompt in sorted(cat_prompts, key=lambda x: x['title'].lower()):
            content.append(f"- [{prompt['title']}]({prompt['path']}) - {prompt['description']}")
        content.append("")
    
    with open('categories.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))

def main():
    prompts_dir = 'prompts'
    prompts = collect_prompts(prompts_dir)
    update_readme(prompts)
    update_categories(prompts)
    print("Index files updated successfully.")

if __name__ == "__main__":
    main()