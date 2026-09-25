# 1. Liste todos os membros (full_name, city) em ordem alfabética pelo nome.

```sql
SELECT full_name, city FROM members ORDER BY full_name;
```

```
   full_name    |  city
----------------+--------
 Ana Ferreira   | Porto
 Bruno Silva    | Lisboa
 Carla Mendes   | Porto
 Diogo Antunes  | Braga
 Elena Costa    | Lisboa
 Filipe Moreira | Braga
(6 rows)
```

# 2. Liste os livros (title, published_year) do mais recente para o mais antigo.

```sql
SELECT title, published_year FROM books ORDER BY published_year DESC;
```

```
           title           | published_year
---------------------------+----------------
 The Vegetarian            |           2007
 If on a Winter's Night    |           1979
 The Dispossessed          |           1974
 Invisible Cities          |           1972
 The Left Hand of Darkness |           1969
 A Wizard of Earthsea      |           1968
 No Longer at Ease         |           1960
 Things Fall Apart         |           1958
(8 rows)
```

# 3. Liste os livros (title, author_id, published_year) agrupando por author_id e, dentro do mesmo autor, do mais antigo para o mais recente.

```sql
SELECT title, author_id, published_year FROM books ORDER BY author_id, published_year;
```

```
           title           | author_id | published_year
---------------------------+-----------+----------------
 A Wizard of Earthsea      |         1 |           1968
 The Left Hand of Darkness |         1 |           1969
 The Dispossessed          |         1 |           1974
 Invisible Cities          |         2 |           1972
 If on a Winter's Night    |         2 |           1979
 Things Fall Apart         |         3 |           1958
 No Longer at Ease         |         3 |           1960
 The Vegetarian            |         4 |           2007
(8 rows)
```

# 4. Liste os membros (full_name, city) por cidade em ordem alfabética e, dentro da mesma cidade, por joined_on do mais antigo para o mais recente — mesmo sem joined_on aparecer no SELECT.

```sql
SELECT full_name, city FROM members ORDER BY city, joined_on;
```

```
   full_name    |  city
----------------+--------
 Diogo Antunes  | Braga
 Filipe Moreira | Braga
 Bruno Silva    | Lisboa
 Elena Costa    | Lisboa
 Carla Mendes   | Porto
 Ana Ferreira   | Porto
(6 rows)
```

# 5. Liste os livros com mais de 2 cópias (title, copies), ordenados da menor quantidade de cópias para a maior.

```sql
SELECT title, copies FROM books WHERE copies > 2 ORDER BY copies;
```

```
        title         | copies
----------------------+--------
 A Wizard of Earthsea |      3
 Invisible Cities     |      4
 Things Fall Apart    |      5
(3 rows)
```

# 6. Liste os empréstimos (book_id, loaned_on, returned_on), ordenados por returned_on do mais recente para o mais antigo.

```sql
SELECT book_id, loaned_on, returned_on FROM loans ORDER BY returned_on DESC;
```

```
 book_id | loaned_on  | returned_on
---------+------------+-------------
       1 | 2026-08-08 |
       6 | 2026-08-01 |
       4 | 2026-08-11 |
       2 | 2026-08-27 |
       7 | 2026-08-19 |
       8 | 2026-09-01 |
       8 | 2026-08-14 | 2026-08-30
       5 | 2026-08-03 | 2026-08-25
       6 | 2026-07-22 | 2026-08-05
       6 | 2026-07-14 | 2026-07-28
       2 | 2026-07-05 | 2026-07-19
       4 | 2026-06-25 | 2026-07-10
       3 | 2026-06-09 | 2026-06-29
       1 | 2026-06-02 | 2026-06-20
       1 | 2026-05-18 | 2026-06-01
       4 | 2026-05-05 | 2026-05-21
       8 | 2026-04-12 | 2026-04-30
       2 | 2026-03-17 | 2026-04-02
(18 rows)
```

# 7. Liste os membros (full_name, joined_on) do que entrou por último para o que entrou primeiro.

```sql
SELECT full_name, joined_on FROM members ORDER BY joined_on DESC;
```

```
   full_name    | joined_on  
----------------+------------
 Filipe Moreira | 2026-01-09
 Elena Costa    | 2025-03-14
 Diogo Antunes  | 2025-01-20
 Bruno Silva    | 2024-06-30
 Ana Ferreira   | 2023-02-11
 Carla Mendes   | 2022-11-05
(6 rows)
```

# 8. Liste os livros (title, copies) da menor quantidade de cópias para a maior e, entre os que têm a mesma quantidade, em ordem alfabética pelo título.

```sql
SELECT title, copies FROM books ORDER BY copies, title;
```

```
           title           | copies 
---------------------------+--------
 No Longer at Ease         |      1
 The Dispossessed          |      1
 If on a Winter's Night    |      2
 The Left Hand of Darkness |      2
 The Vegetarian            |      2
 A Wizard of Earthsea      |      3
 Invisible Cities          |      4
 Things Fall Apart         |      5
(8 rows)
```
