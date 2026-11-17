# Task 2 Report: Netflix Shows Analysis

**Data:** `netflix_titles.csv`, 7,787 titles (Kaggle *shivamb/netflix-shows*, 2021 release; titles added up to 16 January 2021). Full code and charts are in `Task2_Netflix_Shows_Analysis.ipynb`.

## Cleaning summary
- Missing values: `director` 30.7%, `cast` 9.2%, `country` 6.5% were filled with "Unknown" (text fields used only for counting). `rating` (7 rows) was filled with "Not Rated". `date_added` (10 rows) was left missing and excluded only from time analysis.
- No duplicate rows, no duplicate `show_id`, and no repeated title + type + year.
- `date_added` converted from text to datetime. `duration` split into a number and a unit (minutes for movies, seasons for TV shows).
- New column `age_when_added` = year added − release year. 12 titles show a negative value (added before their official release year) and were excluded from that analysis.

## Key findings
1. **Library mix:** 5,377 movies (69.1%) and 2,410 TV shows (30.9%).
2. **Genres:**
   - International Movies (2,437), Dramas (2,106) and Comedies (1,471) lead.
   - On the TV side: International TV Shows (1,199), TV Dramas (704) and TV Comedies (525).
   - "International" is the top label for both movies and shows, so non-US content is central to the catalogue.
3. **Countries:**
   - The United States leads (3,297 titles), followed by India (990), the United Kingdom (723), Canada (412) and France (349).
   - Countries specialise differently: India is 92% movies, while South Korea (74%) and Japan (64%) are mostly TV shows (K-dramas and anime).
4. **People:** with director missing for 31% of titles, director counts are incomplete. The top cast list is dominated by Indian actors, which matches India's strong movie catalogue.
5. **Growth over time:**
   - Titles added per year rose from 25 (2014) to 443 (2016), 1,225 (2017) and a peak of 2,153 (2019).
   - 2020 dipped slightly to 2,009 (−6.7%). 2021 holds only two weeks of data.
   - TV-show additions kept rising in 2020 (656 → 697) while movie additions fell (1,497 → 1,312).
6. **Freshness:** 70% of titles were released in 2015 or later. Half of the movies were added within 1 year of release, and half of the TV shows in the same year as release.
7. **Ratings and audience:** about 45% of titles are adult-rated (TV-MA, R, NC-17) and 30% are for teens (TV-14, PG-13). Content for young children (TV-Y, TV-G, G) is only about 7%.
8. **Duration:**
   - The median movie runs 98 minutes, and runtimes have been getting shorter: the median was 112 minutes for 1970s releases and 96 minutes for 2010s releases.
   - Kids' content is much shorter (TV-Y median 44 minutes).
   - Two-thirds of TV shows (66.7%) have only one season.

## Conclusions (content strategy)
- Netflix grew its library fast between 2016 and 2019 and then slowed, which is consistent with a shift from adding volume to focusing on selected content.
- The strategy is clearly global: international movies and shows are the largest genre labels, with Indian movies and Korean/Japanese series as distinct regional strengths.
- The catalogue targets adults and teens. Family and kids' content is a relatively small share, which could be an opportunity.
- Many one-season shows suggest Netflix tests many series and renews few.

## Limitations
- This is a snapshot from January 2021, so it does not show later years.
- Director and cast are missing for a large share of titles.
- Genres are Netflix's own tags, and one title can carry several.
- The patterns above are associations in the catalogue and do not show what caused them.
