# Task 3 Report: Telco Customer Churn Analysis

**Data:** `Telco-Customer-Churn.csv` (IBM / Kaggle *blastchar*), 7,043 customers and 21 columns. Full code and charts are in `Task3_Telco_Customer_Churn_Analysis.ipynb`.

## Cleaning summary
- `TotalCharges` was stored as text and contained 11 blank values. All 11 belong to customers with tenure = 0 who have not been billed yet, so the blanks were set to 0 and the column was converted to a number.
- There are no other missing values, no duplicate rows and no duplicate customer IDs.
- `SeniorCitizen` was recoded from 0/1 to No/Yes.
- Three columns were added: a numeric churn flag, tenure groups (0–12, 13–24, 25–48, 49–60 and 61–72 months), and a count of add-on services (0–6).
- "No internet service" and "No phone service" were kept as their own categories, because these customers cannot buy the add-ons.

## Key findings
1. **Overall churn:** 26.5% of customers left (1,869 of 7,043). They account for $139,131 of monthly charges, which is **30.5% of monthly recurring revenue**. Churners therefore pay more than average.
2. **Contract type is the strongest factor:**
   - Month-to-month customers churn at 42.7%.
   - One-year contracts churn at 11.3%, and two-year contracts at only 2.8%.
   - Month-to-month contract has the highest correlation with churn of any feature (+0.41).
3. **Tenure:**
   - Churn is 47.4% in the first year and falls steadily to 6.6% after five years.
   - Churners have a median tenure of 10 months, against 38 months for customers who stayed.
4. **Charges:**
   - Churners pay more per month (median $79.6 vs $64.4).
   - The lowest charge quartile churns at 11.2%, while the $70–90 band churns at 37.5%.
5. **Internet service:**
   - Fiber-optic customers churn at 41.9%, compared with 19.0% for DSL and 7.4% for customers without internet.
   - Fiber is also much more expensive (median $91.7 vs $56.2 for DSL).
6. **Protective add-ons:** customers without Online Security (41.8%) or Tech Support (41.6%) churn about three times as often as those who have them (14.6% and 15.2%). Among fiber customers, adding Tech Support cuts churn from 49.4% to 22.6%.
7. **Number of add-ons:**
   - Churn peaks at 45.8% for customers with exactly one add-on and falls to 5.3% for customers with all six.
   - Customers with zero add-ons churn at only 21.4%, because most of them have no internet service.
8. **Payment and billing:**
   - Electronic check users churn at 45.3%. The other payment methods range from 15% to 19%.
   - Paperless billing customers churn at 33.6%, against 16.3% for paper billing.
9. **Demographics:**
   - Gender makes no difference (26.9% vs 26.2%).
   - Senior citizens churn at 41.7%.
   - Customers without a partner (33.0%) or without dependents (31.3%) churn more than those with a partner or dependents.

## High-churn segments
| Segment | Customers | Churn rate |
|---|---|---|
| Month-to-month + Fiber + Electronic check | 1,307 | **60.4%** (789 churners) |
| Month-to-month + Fiber + Mailed check | 201 | 50.7% |
| Month-to-month + Fiber + Bank transfer | 327 | 45.6% |
| Month-to-month + Fiber + **first 12 months** | 916 (13% of base) | **70.2%**, 34% of all churners |

## Retention strategies
- **Move customers to longer contracts.** Offer a discount or free upgrade for switching from month-to-month to a 1- or 2-year plan, especially during the first year.
- **Focus on onboarding in the first 12 months.** Run welcome calls and check-ins, and give extra attention to new fiber customers.
- **Bundle protective services.** Include Online Security and Tech Support free or at a discount for fiber customers, since these customers churn far less.
- **Review fiber pricing and quality.** High fiber churn at high prices suggests a value-for-money or service problem that needs investigation through surveys and network data.
- **Encourage automatic payment.** Give a small incentive to move from electronic check to card or bank auto-pay.
- **Target seniors and single-person households** with tailored plans and support.

## Limitations
- The data is a snapshot, so we only see whether a customer left in the last month.
- The findings are correlations. For example, fiber itself may not cause churn; price or service quality could.
- Features overlap with each other (for example, short tenure and month-to-month contracts), so a predictive model would be needed to measure each factor's separate effect.
