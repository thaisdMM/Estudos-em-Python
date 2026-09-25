# 1. Quais os 3 livros com mais cópias? (title, copies)

```sql
SELECT title, copies FROM books ORDER BY copies DESC LIMIT 3;
```

```
        title         | copies 
----------------------+--------
 Things Fall Apart    |      5
 Invisible Cities     |      4
 A Wizard of Earthsea |      3
(3 rows)
```

# 2. Quais os 2 membros que entraram por último (mais recentes)? (full_name, joined_on)

```sql
SELECT full_name, joined_on FROM members ORDER BY joined_on DESC LIMIT 2;
```

```
   full_name    | joined_on  
----------------+------------
 Filipe Moreira | 2026-01-09
 Elena Costa    | 2025-03-14
(2 rows)
```

# 3. Qual o livro mais antigo do acervo? Traga só ele. (title, published_year)

```sql
SELECT title, published_year FROM books ORDER BY published_year LIMIT 1;
```

```
       title       | published_year 
-------------------+----------------
 Things Fall Apart |           1958
(1 row)
```

# 4. Ignorando os 2 primeiros livros em ordem alfabética por título, quais são os 3 seguintes? (title)

```sql
SELECT title FROM books ORDER BY title LIMIT 3 OFFSET 2;
```

```
       title       
-------------------
 Invisible Cities
 No Longer at Ease
 The Dispossessed
(3 rows)
```

# 5. Quais os 3 empréstimos com loaned_on mais recente? (book_id, loaned_on)

```sql
SELECT book_id, loaned_on FROM loans ORDER BY loaned_on DESC LIMIT 3;
```

```
 book_id | loaned_on  
---------+------------
       8 | 2026-09-01
       2 | 2026-08-27
       7 | 2026-08-19
(3 rows)
```
