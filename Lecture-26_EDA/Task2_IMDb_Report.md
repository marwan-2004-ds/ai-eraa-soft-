# Task 2 Report: IMDb Dataset Analysis

**Data:** IMDb non-commercial datasets `title.basics` and `title.ratings`, the same files as the Kaggle *ashirwadsangwan/imdb-dataset*, downloaded in their current version.

- `title.basics` has 12.97 million titles and `title.ratings` has 1.73 million ratings.
- `prepare_imdb.py` merges the two files line by line, because both are sorted by ID and the computer had very little free memory.
- The analysis uses 347,160 rated, non-adult feature films.
- Full code and charts are in `Task2_IMDb_Dataset_Analysis.ipynb`.

## Cleaning summary
- IMDb's `\N` markers were read as missing values. There are no duplicate IDs and no duplicate rows.
- Missing values among rated movies:
  - runtime: 8.4%
  - genre: 3.3%, labelled "Unknown"
  - year: 33 films, dropped
- 153 implausible runtimes (under 40 or over 600 minutes) were treated as errors and set to missing.
- Adult titles were excluded.
- Because vote counts are extremely skewed, rating comparisons use **popular films with 1,000 or more votes** (49,528 films, 14% of rated films, holding 97% of all movie votes). The top list uses a weighted (Bayesian) rating.

## Key findings
1. **Title types:**
   - IMDb is mostly TV episodes (77% of all titles), followed by shorts (9%) and feature films (5.9%).
   - Only 13% of titles have a rating. Feature films are the most often rated type (46%), and TV episodes the least (9%).
2. **Genres:**
   - Drama is by far the most common movie genre (158,502 rated films), followed by Comedy (83,229) and Documentary (58,036).
   - Over time, Documentary grew from about 2% of films in the 1950s to about 26% in the 2010s.
   - Horror and Thriller also grew, while Drama, Romance and Crime shrank as a share.
3. **Release years:**
   - 62% of rated films were released in 2000 or later.
   - The peak year is 2023, with 11,968 rated films.
4. **Runtime:**
   - The median feature film runs 91 minutes.
   - Median runtime grew from 70 minutes in the 1920s to about 90–94 minutes from the 1950s onwards, and has stayed stable since.
5. **Ratings and votes:**
   - The average rating is 6.15 (median 6.3), and the distribution is slightly skewed towards high ratings.
   - Votes are extremely uneven: the median film has only 66 votes, but the top 1% have more than 75,000.
   - Films with very few votes (5–10) average 6.62 and vary widely (std 1.50), which shows that small samples are unreliable.
   - Among films with 1,000+ votes, the most-voted films are rated higher: 100k+ votes average 6.99, against 6.11 for 1k–10k votes.
6. **Highly rated titles:** the weighted top list is led by *The Shawshank Redemption* (9.3 from 3.27M votes), *The Godfather* (9.2), *The Dark Knight* (9.1) and *The Return of the King* (9.0). The most-voted films overlap strongly with the top-rated list.
7. **Genres: quality vs popularity** (films with 1,000+ votes):
   - **Highest rated:** Documentary (7.19), Biography (6.90), Film-Noir (6.85), History (6.82) and War (6.77).
   - **Lowest rated:** Horror (5.25), Sci-Fi (5.43), Thriller (5.82) and Action (5.93).
   - **Most total votes:** Drama, Action, Comedy and Adventure.
   - Popularity and rating differ: Action and Sci-Fi draw huge audiences but have lower average ratings.
8. **Relationships** (Spearman correlation, popular films):
   - Rating vs runtime: +0.28. Longer films are rated higher, rising from 5.77 for 80–90 minutes to 6.82 for 150+ minutes.
   - Rating vs votes: +0.20.
   - Rating vs year: −0.16. Mean rating fell from about 6.8 for 1930s–40s films to about 6.1 for the 2010s–2020s.
   - All of these correlations are weak to moderate.
9. **The age effect is likely survivorship:** older films that still collect 1,000+ votes today tend to be the well-remembered classics. Newer films include many more average releases.

## Insights about audience preferences
- Audiences give the highest ratings to factual and serious genres (documentary, biography, history, war). Entertainment genres (action, comedy, adventure) attract the most votes, so the most-watched content is not necessarily the best-rated.
- Horror is the lowest-rated genre even though its share of production keeps growing. Producers keep making it because of audience demand, not critical approval.
- Longer, more ambitious films are associated with higher ratings, but this does not show that adding minutes improves a film.
- A rating based on few votes should not be trusted. Ranking needs a vote threshold or a weighted rating.

## Limitations
- The data is a current snapshot, so recent films have had less time to collect votes.
- One film can carry up to three genres.
- Ratings come from self-selected IMDb users.
- All relationships are correlations, not causes.
