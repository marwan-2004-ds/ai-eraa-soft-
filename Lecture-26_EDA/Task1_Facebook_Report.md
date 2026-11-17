# Task 1 Report: Facebook Metrics Analysis

**Data:** `dataset_Facebook.csv` contains 500 posts published in 2014 on the Facebook page of a cosmetics brand (Moro et al., 2016; UCI / Kaggle). The full code and charts are in `Task1_Facebook_Metrics_Analysis.ipynb`.

## Cleaning summary
- Only 5 values were missing:
  - 1 `like` and 4 `share` values were filled with 0. This is safe because `Total Interactions` equals comments + likes + shares on every row after filling.
  - 1 `Paid` flag was filled with the most common value (not paid).
- No duplicate rows were found.
- Column names were shortened. Category codes were mapped to names: 1 = Action (special offers), 2 = Product (ads), 3 = Inspiration.
- Rate metrics were added so that posts with different reach can be compared fairly:
  - engagement rate = engaged users ÷ reach
  - interaction rate = interactions ÷ reach
  - virality = shares ÷ interactions

## Key findings
1. **Skewed performance:** a typical post reaches 5,281 people (median) and gets 124 interactions. The means are much higher (13,903 reach and 212 interactions) because a few posts go viral. The best post reached 180,480 people and got 6,334 interactions.
2. **Content mix:** 85% of posts are photos, 9% statuses, 4% links and 1% videos.
3. **Post type:**

   | Post type | Median reach | Median interactions | Engagement rate |
   |---|---|---|---|
   | Video (7 posts) | 30,624 | 271 | 3.2% |
   | Status | 11,096 | 186 | 15.5% (highest) |
   | Photo | 4,675 | 122 | 12.3% |
   | Link | 7,422 | 53 | 2.3% |

   - **Videos** have the highest median reach and interactions, but only 7 videos were posted, so this result is uncertain.
   - **Status** posts give the best balance: high reach and the highest engagement rate.
   - **Photos** are the most used type but perform in the middle.
   - **Links** perform worst.
4. **Category:**
   - Inspiration posts (163 median interactions, highest virality at 16%) and Product posts (153 interactions, 14.3% engagement rate) do clearly better than Action/offer posts (87 interactions, 9.1% engagement rate).
   - Action is the most frequent category (215 posts), so the most-used category is the weakest.
5. **Paid promotion:**
   - Paid posts have about 46% more median reach than organic ones (7,132 vs 4,898) and more interactions (158 vs 117).
   - Their engagement rate is about the same (11.8% vs 12.3%). Paying buys more reach, but it does not make the content more engaging.
6. **Timing:**
   - Among hours with at least 10 posts, 13:00 (median 155 interactions), 10:00 and 03:00 perform best. 08:00 and 12:00 perform worst.
   - The differences between hours are moderate and based on small groups, so timing matters less than post type and category.
7. **Audience growth vs reach:**
   - Page likes grew 60% during 2014 (86,909 → 139,441).
   - Median reach per post did not grow, and October was the lowest month (2,955). More fans did not automatically bring more reach per post.
8. **Relationships between metrics:**
   - Likes make up 84% of all interactions, shares 13% and comments 3.5%.
   - Interactions are strongly linked to shares (Spearman 0.88) and comments (0.69), and moderately to reach (0.65).
   - Page size has almost no relationship with interactions (0.02).

## Recommendations for content planning
- Post more **status updates and videos** and fewer plain links. Test videos at larger volume to confirm their strong but small-sample results.
- Shift the mix from discount/offer posts towards **inspiration and product** content, which earns more engagement and shares.
- Use **paid promotion to extend reach** for posts that already perform well organically, because paying does not improve engagement rate.
- Schedule key posts around **10:00–13:00**, and keep testing timing because the effect is small.
- Track **engagement rate and shares**, not only page likes. Growing the fan base did not increase reach per post.

## Limitations
- The sample is 500 posts from one brand in one year (part of the original 790 posts).
- Some groups are very small (7 videos, 22 links).
- Weekday is only available as a code (1–7).
- All findings are correlations, not proof of cause.
