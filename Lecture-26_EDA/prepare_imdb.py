"""Stream-merge the two IMDb files (both sorted by tconst) with constant memory.

Outputs (in data/):
- imdb_rated_movies.csv : every rated feature film (titleType == 'movie') with its rating and votes
- imdb_type_summary.csv : per title type, total titles and titles that have a rating

The full title.basics file has 11M+ rows, too large to load at once on a machine with little free memory.
"""
import csv, gzip, sys
from collections import Counter

csv.field_size_limit(10_000_000)
DATA = 'data/'

def rows(path):
    with gzip.open(path, 'rt', encoding='utf-8', newline='') as f:
        r = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
        header = next(r)
        for row in r:
            yield dict(zip(header, row))

ratings = rows(DATA + 'title.ratings.tsv.gz')
cur = next(ratings, None)
total, rated = Counter(), Counter()
prev_b = prev_r = ''
kept = 0
with open(DATA + 'imdb_rated_movies.csv', 'w', encoding='utf-8', newline='') as out:
    w = csv.writer(out)
    w.writerow(['tconst', 'primaryTitle', 'isAdult', 'startYear', 'runtimeMinutes', 'genres', 'averageRating', 'numVotes'])
    for b in rows(DATA + 'title.basics.tsv.gz'):
        t = b['tconst']
        assert t > prev_b, 'basics not sorted'
        prev_b = t
        total[b['titleType']] += 1
        while cur is not None and cur['tconst'] < t:
            assert cur['tconst'] > prev_r or prev_r == '', 'ratings not sorted'
            prev_r = cur['tconst']
            cur = next(ratings, None)
        if cur is not None and cur['tconst'] == t:
            rated[b['titleType']] += 1
            if b['titleType'] == 'movie':
                w.writerow([t, b['primaryTitle'], b['isAdult'], b['startYear'], b['runtimeMinutes'],
                            b['genres'], cur['averageRating'], cur['numVotes']])
                kept += 1

with open(DATA + 'imdb_type_summary.csv', 'w', encoding='utf-8', newline='') as out:
    w = csv.writer(out)
    w.writerow(['titleType', 'titles', 'rated_titles'])
    for k, v in total.most_common():
        w.writerow([k, v, rated.get(k, 0)])

print('titles:', sum(total.values()), '| rated movies written:', kept)
