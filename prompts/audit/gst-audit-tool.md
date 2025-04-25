--- 
title: ChatGPT Prompts for Building a GST Audit Tool 
category: Audit 
description: Leverage ChatGPT to create tailored prompts for automating GST audit processes, analyzing data, detecting revenue leakages, and streamlining reporting. These prompts are categorized for different aspects of the development process. 
--- 

## 🔧 Prompt

1. **Data Analysis**  
   > "Generate a Power Query script or Python script to extract and analyze GST purchase invoices. Identify revenue leakages by comparing taxable value, GST paid, and ITC claims with ledger data. Provide insights in a tabular format."

2. **Project Management**  
   > "Create a project plan for building an Excel-based GST audit tool, including feature development, testing, and deployment. Define budget, resources, and key milestones."

3. **Code Generation**  
   > "Generate a Python script using Pandas and OCR (Google ML Kit) to extract date, invoice number, taxable amount, and GST from PDFs and store them in an Excel file."

4. **Customer Experience (Reporting & UX)**  
   > "Provide best practices for designing a user-friendly GST audit report template, including summary insights, flagged errors, and recommended actions."

5. **Research Assistance**  
   > "Summarize the latest GST amendments related to ITC claims, e-invoicing, and tax compliance. Provide practical implications for auditors."

6. **Document Drafting**  
   > "Write a detailed audit report template covering GST discrepancies, tax risks, and recommendations for compliance improvement."

7. **Marketing Content Creation**  
   > "Suggest SEO strategies to promote a GST audit tool online, including keyword research and content marketing ideas."

8. **Business Presentation**  
   > "Design a professional PowerPoint presentation explaining the benefits of an AI-powered GST audit tool for businesses and tax consultants."

9. **Technical Documentation**  
   > "Create a user manual for a GST audit tool explaining how to extract, analyze, and interpret tax data."

10. **Streamlining Automation**  
    > "How can ChatGPT be used to automate GST audit processes, including invoice verification and tax compliance checks?"

--- 

## 🧩 Inputs

- `invoice_data`: Data from GST purchase invoices (e.g., taxable value, GST paid, ITC claims).
- `project_details`: Information related to project phases, features, budget, and milestones.
- `pdf_data`: PDF files containing invoice details to be processed with OCR.
- `audit_report`: Structured audit report detailing findings and recommendations.
- `marketing_goals`: Objectives for promoting the GST audit tool (e.g., keywords, content ideas).

---

## ⚙️ Constraints

- Scripts should be written in Python, Power Query, or Excel, with appropriate libraries and modules.
- Provide clear instructions for non-technical users where applicable (e.g., user manual).
- Include compliance checks for relevant GST laws and amendments in report generation.
- For presentations, ensure that visuals and slides are professional and concise.

---

## 📋 Output Format

```markdown
### Data Analysis
- Description: Extracts and analyzes GST purchase invoice data for discrepancies.
- Example:
```python
import pandas as pd

# Extract invoice data
data = pd.read_csv('gst_invoices.csv')

# Calculate mismatches
mismatches = data[data['ITC_claimed'] != data['GST_paid']]
