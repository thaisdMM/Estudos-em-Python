# 1. Quais livros têm mais de 3 cópias?

```sql
SELECT title, copies FROM books WHERE copies > 3;
```

```
       title       | copies
-------------------+--------
 Invisible Cities  |      4
 Things Fall Apart |      5
(2 rows)
```

# 2. Quais membros são da cidade de Braga?

```sql
SELECT full_name, city FROM members WHERE city = 'Braga';
```

```
   full_name    | city
----------------+-------
 Diogo Antunes  | Braga
 Filipe Moreira | Braga
(2 rows)
```

# 3. Quais membros entraram depois de 1º de janeiro de 2025 (joined_on)?

```sql
SELECT full_name, joined_on FROM members WHERE joined_on > '2025-01-01';
```

```
   full_name    | joined_on
----------------+------------
 Diogo Antunes  | 2025-01-20
 Elena Costa    | 2025-03-14
 Filipe Moreira | 2026-01-09
(3 rows)
```

# 4. Quais autores não são dos EUA?

```sql
SELECT name, country FROM authors WHERE country != 'USA';
```

```
     name      |   country
---------------+-------------
 Italo Calvino | Italy
 Chinua Achebe | Nigeria
 Han Kang      | South Korea
(3 rows)
```

# 5. Quais livros foram publicados depois de 1970 e têm menos de 3 cópias?

```sql
SELECT title, published_year, copies FROM books WHERE published_year > 1970 and copies < 3;
```

```
         title          | published_year | copies
------------------------+----------------+--------
 The Dispossessed       |           1974 |      1
 If on a Winter's Night |           1979 |      2
 The Vegetarian         |           2007 |      2
(3 rows)
```

# 6. Quais empréstimos foram feitos entre 1º e 31 de agosto de 2026 (loaned_on)?

```sql
SELECT book_id, loaned_on FROM loans WHERE loaned_on >= '2026-08-01' and loaned_on <= '2026-08-31';
```

```
 book_id | loaned_on
---------+------------
       6 | 2026-08-01
       8 | 2026-08-14
       4 | 2026-08-11
       7 | 2026-08-19
       5 | 2026-08-03
       1 | 2026-08-08
       2 | 2026-08-27
(7 rows)
```

```sql
SELECT book_id, loaned_on FROM loans WHERE loaned_on BETWEEN '2026-08-01' AND '2026-08-31';
```

```
 book_id | loaned_on
---------+------------
       6 | 2026-08-01
       8 | 2026-08-14
       4 | 2026-08-11
       7 | 2026-08-19
       5 | 2026-08-03
       1 | 2026-08-08
       2 | 2026-08-27
(7 rows)
```
