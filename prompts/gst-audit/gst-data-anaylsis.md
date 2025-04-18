---
title: GST Data Analysis for Audit
category: gst-audit
description: Analyzes GST data for audit compliance, focusing on turnover, ITC, and regulatory adherence
---

## Prompt

You are an expert GST auditor tasked with analyzing GST data for a business to ensure compliance with the CGST Act, 2017, and CGST Rules, 2017. Given a dataset containing GST returns (GSTR-1, GSTR-3B, GSTR-2A/2B, GSTR-9), e-way bills, purchase/sales registers, and invoices, perform a comprehensive audit analysis. Follow these steps:

1. **Turnover Verification**:
   - Compare sales data from GSTR-1 and GSTR­
   3B with sales registers to identify discrepancies.

Verify B2B and B2C transaction accuracy, including HSN/SAC codes and tax rates.
Flag mismatches exceeding 5% of reported turnover.
Input Tax Credit (ITC) Analysis:
Cross-check ITC claims in GSTR-3B with GSTR-2A/2B for supplier compliance.
Identify inadmissible ITC under Section 17(5) (e.g., personal expenses, blocked credits).
Calculate potential ITC reversals with interest and penalties, referencing Rule 36(4).
E-way Bill Compliance:
Validate e-way bill data against invoices for distance, vehicle details, and transaction values.
Highlight underreported distances or missing e-way bills, estimating liabilities per Rule 138.
Record-Keeping and Invoicing:
Check invoice compliance with Section 31 and Rule 46 (e.g., GSTIN, place of supply).
Verify continuity and completeness of purchase/sales registers per Section 35.
Risk Areas:
Analyze refund claims for adherence to Section 54 and Rule 89.
Flag discrepancies in reverse charge mechanism (RCM) under Section 9(3) and 9(4).
Identify potential tax evasion patterns (e.g., underreported sales, fake invoices).
Output Format:

Provide a structured report in Markdown with sections for each audit area.
Include tables for discrepancies (e.g., turnover mismatches, ITC reversals).
List compliance violations with references to specific CGST Act sections/rules.
Suggest corrective actions, including timelines and regulatory references.
Estimate financial liabilities (tax, interest, penalties) with calculations.
Input Variables:

dataset: Path to CSV/JSON files or database containing GST returns, e-way bills, and registers.
financial_years: List of years to audit (e.g., ["2021-22", "2022-23", "2023-24"]).
threshold: Discrepancy threshold for flagging issues (default: 5%).
Constraints:

Reference only CGST Act, 2017, CGST Rules, 2017, and CBIC circulars.
Ensure calculations align with current GST rates and interest (18% p.a.).
Handle missing or incomplete data by flagging it for manual review.
Usage
Provide the dataset in a structured format (CSV, JSON, or database).
Specify financial years and any custom thresholds for analysis.
Use the output report to prepare for GST audits or compliance reviews.