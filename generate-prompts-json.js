// generate-prompts-json.js
const fs = require('fs');
const path = require('path');

const promptsDir = path.join(__dirname, 'prompts');
const outputFile = path.join(__dirname, 'prompts.json');

function generatePromptsJson() {
  const promptFiles = [];

  function walk(dir) {
    const files = fs.readdirSync(dir);

    files.forEach(file => {
      const fullPath = path.join(dir, file);
      const stat = fs.statSync(fullPath);

      if (stat.isDirectory()) {
        walk(fullPath);
      } else if (file.endsWith('.md')) {
        const content = fs.readFileSync(fullPath, 'utf-8');

        // Extract metadata using regex
        const titleMatch = content.match(/^title:\s*(.*)$/m);
        const categoryMatch = content.match(/^category:\s*(.*)$/m);
        const descriptionMatch = content.match(/^description:\s*(.*)$/m);

        if (titleMatch && categoryMatch && descriptionMatch) {
          // Create relative path with './' prefix and convert Windows backslash to slash
          const relativeFilePath = './' + path.relative(__dirname, fullPath).replace(/\\/g, '/');

          promptFiles.push({
            title: titleMatch[1].trim(),
            category: categoryMatch[1].trim(),
            description: descriptionMatch[1].trim(),
            file: relativeFilePath
          });
        } else {
          console.warn(`Skipping file ${fullPath} - missing required metadata.`);
        }
      }
    });
  }

  walk(promptsDir);

  fs.writeFileSync(outputFile, JSON.stringify(promptFiles, null, 2), 'utf-8');
  console.log(`prompts.json generated successfully with ${promptFiles.length} prompts.`);
}

generatePromptsJson();
