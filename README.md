# ecommerce-sales-analyzer-
Pandas project analyzing e-commerce sales by category
# E-Commerce Sales Data Analyzer

A small Python + Pandas project that turns raw sales data into answers:
which products sell best, and which category actually drives the revenue.

## What it does

- Builds a sample e-commerce sales dataset (product, category, price, quantity sold)
- Calculates **Total Revenue** per product (`Price × Quantity`)
- Groups and sums revenue by **Category** to find the top performer

## Sample Output

```
--- Our E-Commerce Sales Table ---
   Product_ID Product_Name     Category  Price_INR  Quantity_Sold  Total_Revenue
0         101       Laptop  Electronics      60000              5         300000
1         102   Smartphone  Electronics      45000             12         540000
2         103   Headphones  Accessories       3000             40         120000
3         104      Monitor  Electronics      15000              8         120000
4         105     Keyboard  Accessories       2500             25          62500

--- Total Revenue by Category ---
Category
Accessories    182500
Electronics    960000
Name: Total_Revenue, dtype: int64
```

**Takeaway:** Electronics drives most of the revenue overall, but on a
per-unit basis, Accessories sell in much higher volume — a pattern that's
easy to miss just by scanning the raw table.

## Tools Used

- Python
- Pandas

## What I Learned

Real data is never as clean as tutorial data. Even with a tiny, made-up
dataset like this, the actual work isn't the math — it's structuring the
data so the math means something. Grouping by category instead of just
listing products was the difference between a table and an actual insight.

## Next Steps

- Add a bar chart visualization (Matplotlib/Seaborn) of revenue by category
- Swap in a real, larger dataset (e.g. from Kaggle) to test the same logic at scale
- Add average order value and top single-product performer

---
Built by [Shafika S](https://www.linkedin.com/in/shafika-sdatascientist) — 2nd year BSc Computer Science student, learning data science one project at a time.

