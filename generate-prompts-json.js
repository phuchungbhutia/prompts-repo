// generate-prompts-json.js
const fs = require('fs');
const path = require('path');

const promptsDir = path.join(__dirname, 'prompts');

function extractMetadata(content) {
  const titleMatch = content.match(/^#\s+(.+)/m);
  const categoryMatch = content.match(/^##\s*Category\s*\n(.+)/m);
  const authorMatch = content.match(/^##\s*Author\s*\n(.+)/m);
  const dateMatch = content.match(/^##\s*Created\s*\n(.+)/m);

  return {
    title: titleMatch ? titleMatch[1].trim() : "Untitled",
    category: categoryMatch ? categoryMatch[1].trim() : "Uncategorized",
    author: authorMatch ? authorMatch[1].trim() : "Unknown",
    date: dateMatch ? new Date(dateMatch[1].trim()).toISOString().split('T')[0] : new Date().toISOString().split('T')[0]
  };
}

function createExcerpt(content) {
  const text = content
    .replace(/^#.*$/gm, '')
    .replace(/^##.*$/gm, '')
    .replace(/!\[.*\]\(.*\)/gm, '')
    .replace(/\[.*\]\(.*\)/gm, '')
    .replace(/[`*>\-\+]/gm, '')
    .replace(/\n/g, ' ')
    .trim();
  return text.length > 140 ? text.slice(0, 140) + '...' : text;
}

function main() {
  const files = fs.readdirSync(promptsDir).filter(f => f.endsWith('.md'));

  const prompts = files.map(file => {
    const filePath = path.join(promptsDir, file);
    const content = fs.readFileSync(filePath, 'utf-8');
    const meta = extractMetadata(content);

    return {
      title: meta.title,
      date: meta.date,
      author: meta.author,
      excerpt: createExcerpt(content),
      category: meta.category,
      file: `prompts/${file}`,
      views: 0
    };
  });

  fs.writeFileSync('prompts.json', JSON.stringify(prompts, null, 2));
  console.log('prompts.json generated successfully!');
}

main();
