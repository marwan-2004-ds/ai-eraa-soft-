# 200 SQL Practice Questions — Answers

All query examples use this sample schema (standard SQL; dialect notes where MySQL / SQL Server / PostgreSQL differ):

```sql
CREATE TABLE departments (
    dept_id    INT PRIMARY KEY,
    dept_name  VARCHAR(50) NOT NULL UNIQUE,
    location   VARCHAR(50)
);

CREATE TABLE employees (
    emp_id      INT PRIMARY KEY,
    first_name  VARCHAR(50) NOT NULL,
    last_name   VARCHAR(50) NOT NULL,
    email       VARCHAR(100) UNIQUE,
    salary      DECIMAL(10,2) CHECK (salary >= 0),
    hire_date   DATE,
    dept_id     INT REFERENCES departments(dept_id),
    manager_id  INT REFERENCES employees(emp_id)
);

CREATE TABLE projects (
    project_id   INT PRIMARY KEY,
    project_name VARCHAR(100),
    dept_id      INT REFERENCES departments(dept_id)
);

CREATE TABLE employee_projects (
    emp_id     INT REFERENCES employees(emp_id),
    project_id INT REFERENCES projects(project_id),
    PRIMARY KEY (emp_id, project_id)
);
```

---

## Basic SQL Questions (1–40)

**1. What is SQL and what is it used for?**
SQL (Structured Query Language) is the standard declarative language for relational databases. It is used to define structures (tables, indexes), manipulate data (insert, update, delete), query data, control access, and manage transactions.

**2. Difference between SQL and MySQL?**
SQL is a *language* (an ANSI/ISO standard). MySQL is a *relational database management system* (software) that implements SQL with its own extensions. Others: PostgreSQL, SQL Server, Oracle, SQLite.

**3. Types of SQL commands?**
- **DDL** (Data Definition): `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, `RENAME`
- **DML** (Data Manipulation): `INSERT`, `UPDATE`, `DELETE`, `MERGE`
- **DQL** (Data Query): `SELECT`
- **DCL** (Data Control): `GRANT`, `REVOKE`
- **TCL** (Transaction Control): `COMMIT`, `ROLLBACK`, `SAVEPOINT`

**4. What is a database?**
An organized, persistent collection of related data, managed by a DBMS that handles storage, querying, concurrency, security and recovery.

**5. What is a table?**
A named set of rows that share the same columns — the basic storage structure in a relational database (a "relation").

**6. What is a row?**
One record in a table (a "tuple"): one value per column, describing a single entity, e.g. one employee.

**7. What is a column?**
A named attribute of a table with a data type and optional constraints, e.g. `salary DECIMAL(10,2)`.

**8. Primary key?**
A column (or set) that uniquely identifies each row. It must be unique and NOT NULL; a table has only one primary key.

**9. Foreign key?**
A column that references the primary (or unique) key of another table, enforcing that the referenced row exists (referential integrity). Example: `employees.dept_id → departments.dept_id`.

**10. Unique key?**
A constraint guaranteeing that no two rows share the same value in a column (set). Unlike a primary key, a table can have several, and most DBMSs allow NULLs in them.

**11. Composite key?**
A key made of two or more columns whose combination is unique, e.g. `PRIMARY KEY (emp_id, project_id)`.

**12. Candidate key?**
Any minimal set of columns that could uniquely identify rows. One candidate key is chosen as the primary key; the others become alternate (unique) keys. E.g. `emp_id` and `email`.

**13. Normalization?**
Organizing tables to reduce redundancy and update anomalies by splitting data into related tables based on functional dependencies.

**14. Normal forms?**
- **1NF**: atomic values, no repeating groups.
- **2NF**: 1NF + no partial dependency of non-key columns on part of a composite key.
- **3NF**: 2NF + no transitive dependency (non-key → non-key).
- **BCNF**: every determinant is a candidate key.
- **4NF**: no multi-valued dependencies. **5NF**: no join dependencies.

**15. Denormalization?**
Deliberately adding redundancy (duplicated columns, pre-joined or summary tables) to speed up reads, at the cost of extra storage and harder updates. Common in data warehouses.

**16. DELETE vs DROP vs TRUNCATE?**

| | DELETE | TRUNCATE | DROP |
|---|---|---|---|
| Type | DML | DDL | DDL |
| Removes | chosen rows (`WHERE`) | all rows | whole table (structure + data) |
| Rollback | yes | often not (DBMS-dependent) | often not |
| Triggers fire | yes | no | no |
| Speed | slow (row by row, logged) | fast | fast |

**17. WHERE vs HAVING?**
`WHERE` filters rows *before* grouping and cannot use aggregates. `HAVING` filters groups *after* `GROUP BY` and can use aggregates.

**18. CHAR vs VARCHAR?**
`CHAR(n)` is fixed-length (padded with spaces) — good for fixed codes like country codes. `VARCHAR(n)` is variable-length and stores only the actual characters plus a length byte.

**19. NULL vs 0?**
`0` is a known numeric value. `NULL` means unknown/missing. Comparisons with NULL return UNKNOWN (`NULL = NULL` is not true), so use `IS NULL`. Aggregates ignore NULLs.

**20. SELECT?** Retrieves data from one or more tables/views.
**21. INSERT?** Adds new rows to a table.
**22. UPDATE?** Modifies values in existing rows.
**23. DELETE?** Removes rows from a table.
**24. CREATE?** Creates database objects: databases, tables, views, indexes, procedures, etc.
**25. ALTER?** Changes an existing object's structure: add/drop/rename columns, change types, add constraints.
**26. DROP?** Permanently removes an object (and its data).
**27. DISTINCT?** Removes duplicate rows from the result.
**28. ORDER BY?** Sorts the result by one or more columns, `ASC` (default) or `DESC`.
**29. GROUP BY?** Groups rows sharing the same values so aggregates are computed per group.
**30. LIMIT?** Restricts the number of returned rows (MySQL/PostgreSQL; SQL Server uses `TOP` or `FETCH FIRST n ROWS ONLY`).
**31. OFFSET?** Skips the first *n* rows; used with LIMIT for pagination: `LIMIT 10 OFFSET 20` = rows 21–30.
**32. BETWEEN?** Inclusive range test: `salary BETWEEN 4000 AND 6000` ≡ `salary >= 4000 AND salary <= 6000`.
**33. IN?** Tests membership in a list or subquery: `dept_id IN (1, 2, 3)`.
**34. LIKE?** Pattern matching: `%` = any sequence, `_` = one character.
**35. IS NULL?** Tests for missing values (`= NULL` does not work).
**36. EXISTS?** True if a subquery returns at least one row; stops at the first match.
**37. ANY?** True if the comparison holds for *at least one* subquery value: `salary > ANY (...)` = greater than the minimum.
**38. ALL?** True if the comparison holds for *every* subquery value: `salary > ALL (...)` = greater than the maximum.
**39. UNION?** Combines results of two SELECTs (same number/compatible types of columns) and removes duplicates.
**40. UNION vs UNION ALL?** `UNION` removes duplicates (requires a sort/hash, slower); `UNION ALL` keeps all rows and is faster.

---

## SQL Query Writing Questions (41–70)

```sql
-- 41. All records
SELECT * FROM employees;

-- 42. Specific columns
SELECT first_name, last_name, salary FROM employees;

-- 43. WHERE
SELECT * FROM employees WHERE dept_id = 2 AND salary > 5000;

-- 44. Ascending
SELECT * FROM employees ORDER BY salary ASC;

-- 45. Descending
SELECT * FROM employees ORDER BY salary DESC;

-- 46. Unique values
SELECT DISTINCT dept_id FROM employees;

-- 47. LIKE (names starting with 'A')
SELECT * FROM employees WHERE first_name LIKE 'A%';

-- 48. BETWEEN
SELECT * FROM employees WHERE hire_date BETWEEN '2020-01-01' AND '2022-12-31';

-- 49. IN
SELECT * FROM employees WHERE dept_id IN (1, 3, 5);

-- 50. NULL values
SELECT * FROM employees WHERE manager_id IS NULL;

-- 51. Count rows
SELECT COUNT(*) AS total_employees FROM employees;

-- 52. Max salary
SELECT MAX(salary) AS max_salary FROM employees;

-- 53. Min salary
SELECT MIN(salary) AS min_salary FROM employees;

-- 54. Average salary
SELECT AVG(salary) AS avg_salary FROM employees;

-- 55. Total salary
SELECT SUM(salary) AS total_salary FROM employees;

-- 56. GROUP BY
SELECT dept_id, COUNT(*) AS emp_count
FROM employees
GROUP BY dept_id;

-- 57. HAVING
SELECT dept_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY dept_id
HAVING AVG(salary) > 6000;

-- 58. Aliases
SELECT e.first_name AS "First Name", e.salary * 12 AS annual_salary
FROM employees AS e;

-- 59. Nested conditions
SELECT * FROM employees
WHERE (dept_id = 1 OR dept_id = 2)
  AND (salary > 5000 AND hire_date >= '2021-01-01');

-- 60. CASE
SELECT first_name, salary,
       CASE WHEN salary >= 10000 THEN 'High'
            WHEN salary >= 5000  THEN 'Medium'
            ELSE 'Low' END AS salary_band
FROM employees;

-- 61. Update salaries (10% raise for dept 2)
UPDATE employees SET salary = salary * 1.10 WHERE dept_id = 2;

-- 62. Delete duplicates (keep lowest emp_id per email)
DELETE FROM employees
WHERE emp_id NOT IN (
    SELECT keep_id FROM (SELECT MIN(emp_id) AS keep_id FROM employees GROUP BY email) t
);

-- 63. Insert multiple rows
INSERT INTO departments (dept_id, dept_name, location) VALUES
    (1, 'HR', 'Cairo'),
    (2, 'IT', 'Giza'),
    (3, 'Sales', 'Alexandria');

-- 64. Create table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    city        VARCHAR(50),
    created_at  DATE DEFAULT CURRENT_DATE
);

-- 65. Add column
ALTER TABLE employees ADD phone VARCHAR(20);

-- 66. Rename column (MySQL 8 / PostgreSQL; SQL Server: EXEC sp_rename 'employees.phone','phone_number','COLUMN')
ALTER TABLE employees RENAME COLUMN phone TO phone_number;

-- 67. Drop column
ALTER TABLE employees DROP COLUMN phone_number;

-- 68. Primary key
ALTER TABLE customers ADD CONSTRAINT pk_customers PRIMARY KEY (customer_id);

-- 69. Foreign key
ALTER TABLE projects
ADD CONSTRAINT fk_projects_dept FOREIGN KEY (dept_id) REFERENCES departments(dept_id);

-- 70. Unique constraint
ALTER TABLE employees ADD CONSTRAINT uq_employees_email UNIQUE (email);
```

---

## Joins Questions (71–90)

**71. JOIN?** Combines rows from two or more tables based on a related column.
**72. INNER JOIN?** Returns only rows that have a match in both tables.
**73. LEFT JOIN?** All rows from the left table plus matches from the right; NULLs where no match.
**74. RIGHT JOIN?** All rows from the right table plus matches from the left; NULLs where no match.
**75. FULL OUTER JOIN?** All rows from both tables, matched where possible, NULLs elsewhere (MySQL lacks it — emulate with LEFT JOIN UNION RIGHT JOIN).
**76. CROSS JOIN?** Cartesian product: every row of A with every row of B (|A| × |B| rows).
**77. SELF JOIN?** A table joined to itself using aliases, e.g. employees to their managers.
**78. INNER vs LEFT JOIN?** INNER drops left rows without a match; LEFT keeps them with NULLs for right-side columns.
**79. LEFT vs RIGHT JOIN?** Mirror images: LEFT keeps all rows of the first table, RIGHT keeps all rows of the second. `A LEFT JOIN B` ≡ `B RIGHT JOIN A`.

```sql
-- 80. INNER JOIN
SELECT e.first_name, d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;

-- 81. LEFT JOIN (employees even without a department)
SELECT e.first_name, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;

-- 82. RIGHT JOIN (departments even without employees)
SELECT e.first_name, d.dept_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.dept_id;

-- 83. FULL OUTER JOIN
SELECT e.first_name, d.dept_name
FROM employees e
FULL OUTER JOIN departments d ON e.dept_id = d.dept_id;

-- 84. CROSS JOIN
SELECT e.first_name, p.project_name
FROM employees e
CROSS JOIN projects p;

-- 85. SELF JOIN
SELECT e.first_name AS employee, m.first_name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.emp_id;

-- 86. Three tables
SELECT e.first_name, p.project_name, d.dept_name
FROM employees e
JOIN employee_projects ep ON e.emp_id = ep.emp_id
JOIN projects p           ON ep.project_id = p.project_id
JOIN departments d        ON p.dept_id = d.dept_id;

-- 87. Unmatched records (departments with no employees)
SELECT d.*
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
WHERE e.emp_id IS NULL;

-- 88. Common records (employees who are also on a project)
SELECT DISTINCT e.emp_id, e.first_name
FROM employees e
INNER JOIN employee_projects ep ON e.emp_id = ep.emp_id;
-- or: SELECT emp_id FROM employees INTERSECT SELECT emp_id FROM employee_projects;

-- 89. Multiple JOIN conditions (projects in the employee's own department)
SELECT e.first_name, p.project_name
FROM employees e
JOIN employee_projects ep ON e.emp_id = ep.emp_id
JOIN projects p ON ep.project_id = p.project_id
               AND p.dept_id = e.dept_id;

-- 90. Aliases with JOINs
SELECT emp.first_name AS name, dep.dept_name AS department
FROM employees AS emp
JOIN departments AS dep ON emp.dept_id = dep.dept_id;
```

---

## Aggregate Functions Questions (91–110)

**91. Aggregate functions?** Functions that compute one value from a set of rows: `COUNT`, `SUM`, `AVG`, `MAX`, `MIN` (plus `STRING_AGG`, `STDDEV`, …). Usually combined with `GROUP BY`.
**92. COUNT()?** Counts rows. `COUNT(*)` counts all rows; `COUNT(col)` counts non-NULL values; `COUNT(DISTINCT col)` counts distinct non-NULL values.
**93. SUM()?** Total of numeric values (ignores NULLs).
**94. AVG()?** Arithmetic mean of non-NULL values.
**95. MAX()?** Largest value (works on numbers, dates, strings).
**96. MIN()?** Smallest value.

```sql
-- 97. COUNT
SELECT COUNT(*) FROM employees WHERE dept_id = 2;

-- 98. SUM
SELECT SUM(salary) AS payroll FROM employees;

-- 99. AVG
SELECT AVG(salary) AS avg_it_salary FROM employees WHERE dept_id = 2;

-- 100. MAX
SELECT MAX(hire_date) AS latest_hire FROM employees;

-- 101. MIN
SELECT MIN(salary) AS lowest_salary FROM employees;

-- 102. GROUP BY + COUNT
SELECT dept_id, COUNT(*) AS employees FROM employees GROUP BY dept_id;

-- 103. GROUP BY + SUM
SELECT dept_id, SUM(salary) AS dept_payroll FROM employees GROUP BY dept_id;

-- 104. GROUP BY + AVG
SELECT dept_id, ROUND(AVG(salary), 2) AS avg_salary FROM employees GROUP BY dept_id;

-- 105. HAVING with aggregates
SELECT dept_id, SUM(salary) AS payroll
FROM employees
GROUP BY dept_id
HAVING SUM(salary) > 100000;

-- 106. Duplicate values
SELECT email, COUNT(*) AS occurrences
FROM employees
GROUP BY email
HAVING COUNT(*) > 1;

-- 107. Second highest salary
SELECT MAX(salary) AS second_highest
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- 108. Nth highest salary (N = 3)
SELECT DISTINCT salary
FROM (SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk FROM employees) t
WHERE rnk = 3;

-- 109. Departments with more than 5 employees
SELECT d.dept_name, COUNT(*) AS emp_count
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name
HAVING COUNT(*) > 5;

-- 110. Employees earning above average
SELECT * FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

---

## Subqueries and Nested Queries (111–130)

**111. Subquery?** A query nested inside another statement (in `SELECT`, `FROM`, `WHERE`, `HAVING`), whose result is used by the outer query.
**112. Correlated subquery?** A subquery that references columns of the outer query, so it is evaluated once per outer row.
**113. Correlated vs non-correlated?** A non-correlated subquery is independent and runs once; a correlated one depends on the outer row and runs (logically) for each row — usually slower, but often rewritable as a JOIN or window function.

```sql
-- 114. Subquery in WHERE
SELECT * FROM employees
WHERE dept_id = (SELECT dept_id FROM departments WHERE dept_name = 'IT');

-- 115. Subquery in FROM (derived table)
SELECT dept_id, avg_salary
FROM (SELECT dept_id, AVG(salary) AS avg_salary FROM employees GROUP BY dept_id) AS dept_avg
WHERE avg_salary > 5000;

-- 116. Subquery in SELECT
SELECT e.first_name, e.salary,
       (SELECT AVG(salary) FROM employees) AS company_avg
FROM employees e;

-- 117. EXISTS (departments that have employees)
SELECT d.dept_name FROM departments d
WHERE EXISTS (SELECT 1 FROM employees e WHERE e.dept_id = d.dept_id);

-- 118. NOT EXISTS (employees on no project)
SELECT e.first_name FROM employees e
WHERE NOT EXISTS (SELECT 1 FROM employee_projects ep WHERE ep.emp_id = e.emp_id);

-- 119. IN with subquery
SELECT * FROM employees
WHERE dept_id IN (SELECT dept_id FROM departments WHERE location = 'Cairo');

-- 120. ANY with subquery (earns more than at least one IT employee)
SELECT * FROM employees
WHERE salary > ANY (SELECT salary FROM employees WHERE dept_id = 2);

-- 121. ALL with subquery (earns more than every IT employee)
SELECT * FROM employees
WHERE salary > ALL (SELECT salary FROM employees WHERE dept_id = 2);

-- 122. Highest salary in each department (correlated)
SELECT e.* FROM employees e
WHERE e.salary = (SELECT MAX(salary) FROM employees x WHERE x.dept_id = e.dept_id);

-- 123. Duplicate rows using a subquery
SELECT * FROM employees
WHERE email IN (SELECT email FROM employees GROUP BY email HAVING COUNT(*) > 1)
ORDER BY email;

-- 124. Delete duplicate rows using a subquery (keep first occurrence)
DELETE FROM employees e
WHERE emp_id > (SELECT MIN(x.emp_id) FROM employees x WHERE x.email = e.email);
-- MySQL: wrap the inner query in a derived table, as in Q62.

-- 125. Alternate rows (every 2nd row by emp_id)
SELECT * FROM (SELECT e.*, ROW_NUMBER() OVER (ORDER BY emp_id) AS rn FROM employees e) t
WHERE rn % 2 = 0;

-- 126. Odd-numbered rows
SELECT * FROM (SELECT e.*, ROW_NUMBER() OVER (ORDER BY emp_id) AS rn FROM employees e) t
WHERE rn % 2 = 1;

-- 127. Even-numbered rows
SELECT * FROM (SELECT e.*, ROW_NUMBER() OVER (ORDER BY emp_id) AS rn FROM employees e) t
WHERE rn % 2 = 0;

-- 128. Hired after the average hire date (PostgreSQL)
SELECT * FROM employees
WHERE hire_date > (SELECT TO_TIMESTAMP(AVG(EXTRACT(EPOCH FROM hire_date)))::date FROM employees);
-- MySQL: WHERE hire_date > (SELECT FROM_UNIXTIME(AVG(UNIX_TIMESTAMP(hire_date))) FROM employees)

-- 129. Compare row values (salary vs department average)
SELECT e.first_name, e.salary,
       e.salary - (SELECT AVG(x.salary) FROM employees x WHERE x.dept_id = e.dept_id) AS diff_from_dept_avg
FROM employees e;

-- 130. Nested aggregates (average of department payrolls)
SELECT AVG(dept_total) AS avg_dept_payroll
FROM (SELECT dept_id, SUM(salary) AS dept_total FROM employees GROUP BY dept_id) t;
```

---

## Advanced SQL Questions (131–160)

**131. View?** A stored, named query that behaves like a virtual table. Used to simplify complex queries, hide columns (security), and give a stable interface.
**132. Index?** A data structure (usually a B-tree) that speeds up lookups, joins and sorting on columns, at the cost of extra storage and slower writes.
**133. Clustered vs non-clustered index?** A clustered index defines the physical order of the table's rows (only one per table, often the PK). A non-clustered index is a separate structure with keys and pointers to rows (many allowed).
**134. Stored procedure?** Precompiled, named SQL code stored in the database, which can take parameters, contain logic, and be called with `CALL`/`EXEC`. Benefits: reuse, security, fewer round trips.
**135. Trigger?** Code that runs automatically on `INSERT`/`UPDATE`/`DELETE` (BEFORE/AFTER) on a table — e.g. audit logging or enforcing rules.
**136. Cursor?** A database object for processing a query result row by row. Useful for procedural logic but slow; set-based SQL is preferred.
**137. Transaction?** A sequence of operations executed as one logical unit: either all succeed (COMMIT) or none take effect (ROLLBACK).
**138. ACID?**
- **Atomicity**: all or nothing.
- **Consistency**: the database moves from one valid state to another (constraints hold).
- **Isolation**: concurrent transactions don't see each other's intermediate states.
- **Durability**: committed changes survive crashes.

**139. Savepoint?** A named point inside a transaction that you can roll back to without undoing the whole transaction: `SAVEPOINT sp1; … ROLLBACK TO sp1;`.
**140. Rollback?** Undoes all uncommitted changes of the current transaction (or back to a savepoint).
**141. Commit?** Makes all changes of the current transaction permanent and visible to others.
**142. Deadlock?** Two (or more) transactions each hold a lock the other needs, so neither can proceed. The DBMS detects it and aborts one (the "victim").
**143. Database locking?** The mechanism that controls concurrent access: shared (read) locks and exclusive (write) locks, at row, page or table level.
**144. Isolation level?** How much a transaction is isolated from others' changes. Standard levels: **Read Uncommitted** (dirty reads possible), **Read Committed**, **Repeatable Read**, **Serializable** (strictest). Higher isolation = fewer anomalies but less concurrency.
**145. Sequence?** A database object that generates ordered unique numbers, e.g. `CREATE SEQUENCE emp_seq START 1; SELECT nextval('emp_seq');`.
**146. Auto increment?** A column property that assigns the next number automatically on insert: `AUTO_INCREMENT` (MySQL), `IDENTITY` (SQL Server), `SERIAL`/`GENERATED AS IDENTITY` (PostgreSQL).
**147. Materialized view?** A view whose result is physically stored and refreshed periodically. Faster reads than a normal view, but data can be stale.
**148. CTE?** A Common Table Expression: a named temporary result defined with `WITH` and used in the following statement. Improves readability and enables recursion.
**149. Recursion in SQL?** A recursive CTE refers to itself to walk hierarchies or generate series (e.g. an org chart).
**150. Window function?** A function computed over a set of rows related to the current row (a "window", defined with `OVER (PARTITION BY … ORDER BY …)`) without collapsing rows as `GROUP BY` does.
**151. ROW_NUMBER()?** Assigns a unique sequential number to each row in its partition (ties get different numbers).
**152. RANK()?** Ranks rows; ties get the same rank and the next rank is skipped (1, 2, 2, 4).
**153. DENSE_RANK()?** Like RANK but without gaps (1, 2, 2, 3).
**154. NTILE(n)?** Splits the ordered rows into *n* roughly equal buckets and returns the bucket number (e.g. quartiles with NTILE(4)).
**155. LEAD()?** Returns a value from a following row (default: next row) in the window.
**156. LAG()?** Returns a value from a preceding row (default: previous row).

```sql
-- 148/149 example: recursive CTE for the reporting chain
WITH RECURSIVE chain AS (
    SELECT emp_id, first_name, manager_id, 1 AS level
    FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.emp_id, e.first_name, e.manager_id, c.level + 1
    FROM employees e JOIN chain c ON e.manager_id = c.emp_id
)
SELECT * FROM chain ORDER BY level;

-- 157. ROW_NUMBER
SELECT first_name, dept_id, salary,
       ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS row_num
FROM employees;

-- 158. RANK
SELECT first_name, salary, RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM employees;

-- 159. DENSE_RANK
SELECT first_name, salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank
FROM employees;

-- 160. Window functions (running total, dept average, previous hire's salary)
SELECT first_name, dept_id, hire_date, salary,
       SUM(salary) OVER (ORDER BY hire_date)                        AS running_payroll,
       AVG(salary) OVER (PARTITION BY dept_id)                      AS dept_avg,
       LAG(salary) OVER (PARTITION BY dept_id ORDER BY hire_date)   AS prev_hire_salary,
       NTILE(4)    OVER (ORDER BY salary)                           AS salary_quartile
FROM employees;
```

---

## Database Design Questions (161–180)

**161. Entity relationship modeling?** A conceptual design technique that describes the data as entities (things), their attributes, and the relationships between them, before building tables.
**162. ER diagram?** A visual representation of an ER model: entities as boxes, attributes, and relationship lines with cardinality notation (e.g. crow's foot).
**163. Cardinality?** The number of instances of one entity that can relate to instances of another (1:1, 1:N, M:N). In a column context it also means the number of distinct values.
**164. One-to-one?** Each row in A relates to at most one row in B and vice versa (e.g. employee ↔ passport). Implemented with a FK that is also UNIQUE.
**165. One-to-many?** One row in A relates to many in B (department → employees). Implemented with a FK on the "many" side.
**166. Many-to-many?** Many rows in A relate to many in B (employees ↔ projects). Implemented with a junction table (`employee_projects`) holding two FKs.
**167. Referential integrity?** The guarantee that every foreign key value points to an existing referenced row, enforced by FK constraints and `ON DELETE/UPDATE` rules (CASCADE, SET NULL, RESTRICT).
**168. Surrogate key?** An artificial key with no business meaning (auto-increment ID, UUID) used as the PK.
**169. Natural key?** A key taken from real-world data that is already unique (national ID, ISBN, email).
**170. Database constraints?** Rules enforced by the DBMS to keep data valid: PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, CHECK, DEFAULT.
**171. NOT NULL?** The column must always have a value.
**172. CHECK?** The value must satisfy a condition, e.g. `CHECK (salary >= 0)`.
**173. DEFAULT?** Provides a value when none is given on insert, e.g. `DEFAULT CURRENT_DATE`.
**174. Purpose of indexing?** Faster searches, joins, sorting and uniqueness enforcement, avoiding full table scans.
**175. How normalization improves design?** It removes redundancy, prevents insert/update/delete anomalies, keeps data consistent, and makes the schema easier to maintain.
**176. Disadvantages of normalization?** More tables and joins, so read queries are more complex and can be slower; reporting workloads often need denormalized structures.
**177. Schema design?** Planning the logical structure of a database: tables, columns, data types, keys, constraints, relationships and indexes, based on requirements and query patterns.
**178. Star schema?** A data-warehouse design with one central **fact** table (measures, e.g. sales amount) joined directly to denormalized **dimension** tables (date, product, customer, store).
**179. Snowflake schema?** A star schema where dimensions are normalized into sub-dimensions (product → category → department). Less redundancy, more joins.
**180. Data warehousing?** Collecting and integrating data from many sources (via ETL/ELT) into a central, historical, analysis-optimized store (OLAP) for reporting and BI, separate from operational (OLTP) systems.

---

## SQL Interview and Real-World Questions (181–200)

**181. Optimizing a slow query?**
1. Read the execution plan (`EXPLAIN` / `EXPLAIN ANALYZE`).
2. Add or fix indexes on filter, join and sort columns.
3. Select only the columns needed; avoid `SELECT *`.
4. Keep `WHERE` conditions sargable (no functions on indexed columns, e.g. use `hire_date >= '2024-01-01'` instead of `YEAR(hire_date) = 2024`).
5. Replace correlated subqueries with JOINs or window functions.
6. Filter early, paginate, and update table statistics.

**182. Identifying duplicates?** `GROUP BY` the identifying columns with `HAVING COUNT(*) > 1` (Q106), or `ROW_NUMBER() OVER (PARTITION BY … ORDER BY …)` and keep rows where `rn > 1`.

**183. Improving database performance?** Proper indexing, query tuning, normalization (or selective denormalization), partitioning large tables, caching, connection pooling, adequate hardware/memory configuration, archiving old data, and regular maintenance (statistics, index rebuilds, vacuum).

**184. Handling large datasets?** Partitioning, appropriate indexes, batch processing (process in chunks), bulk-load tools, summary/materialized tables, columnar storage for analytics, avoiding full scans, and scaling out with replication or sharding.

**185. Best practices for SQL queries?** Explicit column lists, consistent formatting and meaningful aliases, explicit `JOIN … ON` syntax, parameterized queries, sargable filters, comments for complex logic, `EXISTS` for existence checks, careful NULL handling, and transactions for multi-step changes.

**186. Query optimization?** The process — by both the DBMS optimizer and the developer — of choosing the most efficient way to execute a query (access paths, join order, join algorithms) to minimize time and resources.

**187. Execution plan?** The step-by-step strategy the optimizer chooses for a query (scans vs index seeks, join methods, sort operations, estimated costs/rows). Viewed with `EXPLAIN` (MySQL/PostgreSQL) or "Display Execution Plan" (SQL Server).

**188. Indexing strategy?** Deciding which indexes to create based on workload: index PKs/FKs and frequent filter/join/sort columns, use composite indexes with the most selective/equality columns first, use covering indexes for hot queries, avoid over-indexing write-heavy tables, and drop unused indexes.

**189. Securing a database?** Least-privilege roles (`GRANT`/`REVOKE`), strong authentication, encryption in transit (TLS) and at rest, parameterized queries against injection, auditing and monitoring, patching, network restrictions/firewalls, and protected backups.

**190. Backup and restore?** Full, differential and transaction-log (incremental) backups on a schedule using tools such as `mysqldump`, `pg_dump`/`pg_restore`, or `BACKUP DATABASE` / `RESTORE DATABASE` in SQL Server. Store copies offsite and regularly test restores; point-in-time recovery uses log backups.

**191. Preventing SQL injection?** Use parameterized queries/prepared statements or an ORM, validate and whitelist input, never concatenate user input into SQL, give the application account least privilege, and escape identifiers where dynamic SQL is unavoidable.

**192. Parameterized query?** A query where user values are passed as separate parameters, not concatenated into the SQL text, so they are always treated as data:
```python
cursor.execute("SELECT * FROM employees WHERE email = %s", (user_email,))
```

**193. Partitioning?** Splitting one large table into smaller pieces (by range, list or hash — e.g. by year) within the same database. Queries touch only relevant partitions (partition pruning), and maintenance is easier.

**194. Sharding?** Horizontal partitioning across multiple database servers, each holding a subset of rows (e.g. by customer ID), to scale writes and storage beyond one machine.

**195. Replication?** Copying data from a primary server to one or more replicas (synchronously or asynchronously) for high availability, failover, and read scaling.

**196. Database migration?** Moving or changing a database in a controlled way: schema changes via versioned migration scripts (Flyway, Liquibase, Alembic), or moving data to another server/platform, with testing and rollback plans.

**197. Monitoring SQL performance?** Slow-query logs, execution plans, DMVs (SQL Server) / `pg_stat_statements` (PostgreSQL) / Performance Schema (MySQL), and metrics such as CPU, I/O, locks, wait events, connections and cache hit ratio, with dashboards and alerts.

**198. A challenging SQL project (example answer).**
In the EraaSoft course I analysed a sales dataset in SQL. The challenge was a monthly report that took minutes because of correlated subqueries on a large orders table. I rewrote them with CTEs and window functions (`SUM() OVER (PARTITION BY month)`), added a composite index on `(order_date, product_id)`, and checked the plan with `EXPLAIN`. The report ran in seconds and the logic was easier to maintain.

**199. Common SQL mistakes?** Using `= NULL` instead of `IS NULL`; forgetting `WHERE` in `UPDATE`/`DELETE`; selecting non-aggregated columns not in `GROUP BY`; accidental Cartesian products from missing join conditions; `SELECT *` in production; functions on indexed columns; string concatenation (SQL injection); ignoring transactions; and confusing `WHERE` with `HAVING`.

**200. Designing a scalable database system?** Start from requirements and access patterns; build a normalized core schema with proper keys and indexes; separate OLTP and analytics (warehouse); add read replicas and caching (e.g. Redis); partition big tables and shard when one node is not enough; use connection pooling, monitoring, automated backups and high availability; and evolve the schema with versioned migrations.
