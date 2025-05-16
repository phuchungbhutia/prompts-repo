// generate-prompts-json.js
const fs = require('fs');
const path = require('path');

const promptsDir = path.join(__dirname, 'prompts');

function readFilesRecursively(dir) {
  let results = [];
  const list = fs.readdirSync(dir, { withFileTypes: true });

  list.forEach(dirent => {
    const fullPath = path.join(dir, dirent.name);
    if (dirent.isDirectory()) {
      results = results.concat(readFilesRecursively(fullPath));
    } else if (dirent.isFile() && dirent.name.endsWith('.md')) {
      results.push(fullPath);
    }
  });

  return results;
}

function extractMetadata(content) {
  // Use regex to capture metadata lines (title, category, description)
  // Assumes metadata lines are at the top of the file, e.g.:
  // title: Prompt Title
  // category: Category Name
  // description: Short description here

  const titleMatch = content.match(/^title:\s*(.+)$/im);
  const categoryMatch = content.match(/^category:\s*(.+)$/im);
  const descriptionMatch = content.match(/^description:\s*(.+)$/im);

  return {
    title: titleMatch ? titleMatch[1].trim() : 'Untitled',
    category: categoryMatch ? categoryMatch[1].trim() : 'Uncategorized',
    excerpt: descriptionMatch ? descriptionMatch[1].trim() : '',
  };
}

function createExcerptFromContent(content) {
  // Fallback excerpt if description is missing - first 140 chars of content without metadata lines
  const noMeta = content
    .replace(/^title:.*$/gim, '')
    .replace(/^category:.*$/gim, '')
    .replace(/^description:.*$/gim, '')
    .replace(/^\s*$/gm, '') // remove empty lines
    .trim();

  return noMeta.length > 140 ? noMeta.slice(0, 140) + '...' : noMeta;
}

function main() {
  const files = readFilesRecursively(promptsDir);

  const prompts = files.map(filePath => {
    const content = fs.readFileSync(filePath, 'utf-8');
    const meta = extractMetadata(content);
    const excerpt = meta.excerpt || createExcerptFromContent(content);
    const stats = fs.statSync(filePath);
    const date = stats.mtime.toISOString().split('T')[0]; // use last modified date

    return {
      title: meta.title,
      category: meta.category,
      excerpt: excerpt,
      file: path.relative(__dirname, filePath).replace(/\\/g, '/'), // for Windows fix
      date: date,
      author: "Unknown",  // Optional: you can add author metadata if you want
      views: 0
    };
  });

  fs.writeFileSync('prompts.json', JSON.stringify(prompts, null, 2));
  console.log('prompts.json generated successfully!');
}

main();
