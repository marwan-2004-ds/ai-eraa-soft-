# Task 1 Report: PS4 Video Game Sales Analysis

**Data:** `PS4_GamesSales.csv`, 1,034 rows, 1,031 titles after cleaning. Sales are in **millions of units**, not revenue, so "profitable" here means "high unit sales". Full code and charts are in `Task1_Video_Game_Sales_Analysis.ipynb`.

**Scope limit:** the file covers one platform only (PS4), so platforms could not be compared.

## Cleaning summary
- `Year` converted to integer; 209 titles have no year (about 0.04% of sales) and are left out of year analysis only.
- 209 missing publishers filled with "Unknown"; a stray hidden character removed from names.
- 152 publisher spellings merged to 139 (e.g. *EA Sports* into *Electronic Arts*, *Sony Computer Entertainment* into *Sony Interactive Entertainment*).
- 3 duplicate titles (all zero sales) removed; no exact duplicate rows; no negative values; `Global` equals the sum of regions (max rounding difference 0.02).
- 322 titles show 0.00 sales (under about 10k units); these are real, so they were kept.

## Key findings
1. **Total volume:** 595.6M units across 1,031 titles.
2. **Best sellers:** Grand Theft Auto V (19.39M), Call of Duty: Black Ops 3 (15.09M), Red Dead Redemption 2 (13.94M), Call of Duty: WWII (13.40M), FIFA 18 (11.80M).
3. **Hit-driven market:** the top 10 games make up 20.2% of sales, the top 50 make up 52.2% and the top 100 make up 71.1%. 143 titles (13.9% of the catalogue) generate 80% of sales. The median game sells 0.06M units against a mean of 0.58M (skewness 5.7), and 31% of titles sell effectively nothing.
4. **Genres:**
   - Action leads total sales (136.9M, 23.0%) but only because it has 258 titles; it averages 0.53M per game.
   - Shooter is almost level on total (135.0M) from just 89 titles (1.52M per game).
   - Action-Adventure has the best average (1.55M) from 40 titles, followed by Shooter and Sports (1.31M, 92.9M total).
   - Adventure, Misc, Strategy and Puzzle titles are numerous or niche but sell little per title.
5. **Publishers:** after merging name variants, Electronic Arts (102.5M, 40 titles) and Sony Interactive Entertainment (97.1M, 72 titles) lead, followed by Activision (72.4M from only 30 titles) and Ubisoft (59.2M). Using raw labels, Activision would wrongly appear first. Rockstar Games sold 33.9M from just 3 titles.
6. **Regions:** Europe 43.2%, North America 35.5%, Rest of World 15.5%, Japan 5.8%. Western regions move together (correlation 0.82 to 0.95); Japan behaves differently (about 0.4). Japan's share is highest for Visual Novels (41%), Strategy (26%) and Role-Playing (15%), and is near zero for Shooters (3%) and Sports (2%).
7. **Release years:**
   - Sales rose from 28.8M (2013 releases) to a plateau of about 130 to 136M a year over 2015 to 2017, peaking at 135.7M in 2016.
   - Releases kept growing, from 98 in 2014 to 254 in 2017, so average sales per game fell from 1.44M (2013) to 0.52M (2017).
   - 2018 shows 50.2M from 39 titles (largely Red Dead Redemption 2 and Spider-Man), but this year is likely incomplete.

## Conclusions
- Success on PS4 depends on a few blockbuster franchises (GTA, Call of Duty, FIFA, Sony first-party titles), while most releases earn very little.
- Shooter, Sports and Action-Adventure give the best return per title; Action wins on volume only through quantity.
- Europe is the largest market, ahead of North America; Japan is small and prefers different genres, so regional strategy should differ.
- The market got more crowded each year without growing proportionally, which makes new releases harder to sell.

## Limitations
Single platform, units rather than revenue (no price or cost data), 20% of titles lacking a year, and a snapshot that likely makes 2018 and later years incomplete.
