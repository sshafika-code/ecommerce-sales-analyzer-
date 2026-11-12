<div align="center">

# E-Commerce Sales & Profit Analytics Engine

**Turning Raw E-Commerce Transactions into Executive-Ready Financial Intelligence**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Engineering-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Excel](https://img.shields.io/badge/Excel-Dynamic%20Dashboards-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)](https://www.microsoft.com/en-in/microsoft-365/excel)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-success?style=for-the-badge)]()

</div>

---

## 1. Project Details: What This Project Is

The **E-Commerce Sales & Profit Analytics Engine** is a Python-based data pipeline and automated business intelligence reporting tool. Instead of manually cleaning spreadsheets and building static graphs every month, this application processes multi-category sales transactions, computes unit-level profit and loss margins, and automatically exports a **self-updating Excel dashboard** complete with live formulas and embedded visual charts.

---

## 2. Why I Created This Project (The Vision)

In real-world retail and e-commerce, **high revenue does not always equal high profit**. Looking at a raw table of product prices and quantities makes it nearly impossible to spot which items are quietly losing money or which categories actually drive sustainable growth.

I built this project to solve two practical problems:
1. **Bridge the gap between raw code and business decisions:** Stakeholders rarely read Python terminal logs—they make decisions using clean, interactive Excel workbooks.
2. **Eliminate manual reporting bottlenecks:** By programmatically injecting live Excel formulas (`SUM`, `AVERAGE`) and native charts directly from Python, the final report stays dynamic even after it leaves the codebase.

---

## 3. What I Built & Engineered

- **Scaled Multi-Category Dataset Architecture:** Designed and structured a **120-row transactional dataset** tracking **20 distinct products** across **3 core retail categories** (*Electronics*, *Accessories*, and *Clothing*) over a **6-month sales cycle**.
- **Financial & Profit/Loss (P&L) Modeling:** Engineered financial metrics beyond gross sales (`Price_INR × Quantity_Sold`) by integrating unit cost structures to calculate exact net **Profit and Loss** per transaction.
- **Automated Excel Report Engine (`main.py`):** Built an end-to-end export script that formats raw transaction logs and category summaries into a multi-sheet `.xlsx` workbook.
- **Live Formula & Chart Injection:** Programmed native Excel formulas directly into summary cells alongside two embedded charts:
  - **Monthly Sales Trend Chart:** Visualizes revenue and profit momentum across the 6-month period.
  - **Profit-by-Category Chart:** Compares net profitability across *Electronics*, *Accessories*, and *Clothing*.

---

## 4. The Results & Business Insights

Running the pipeline transforms raw numbers into immediate, actionable takeaways:

### Console Analytics Snapshot
```text
--- E-Commerce Sales Table ---

Rows: 120  |  Products: 20

--- By Category ---
              Revenue  Total_Cost   Profit
Category                                 
Accessories  1904100      987800   916300
Clothing     1272400      798300   474100
Electronics  8067800     6547700  1520100

--- Monthly ---
        Revenue  Profit
Month                 
Jan    1890150  497880
Feb    1805650  472290
Mar    1911600  494060
Apr    1860150  473380
May    1763450  464100
Jun    2013300  508790

Most profitable: Smartphone 490000
Biggest loss: Dress -24600

---
Built by Shafika S — 2nd year BSc Computer Science student, learning data science one projct at a time.
