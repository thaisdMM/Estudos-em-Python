# 1. Liste os membros (full_name, city) que não são da cidade do Porto, em ordem alfabética pelo nome.

```sql
SELECT full_name, city FROM members WHERE city != 'Porto' ORDER BY full_name;
```

```
   full_name    |  city  
----------------+--------
 Bruno Silva    | Lisboa
 Diogo Antunes  | Braga
 Elena Costa    | Lisboa
 Filipe Moreira | Braga
(4 rows)
```

```sql
SELECT full_name, city FROM members WHERE city <> 'Porto' ORDER BY full_name;
```

```
   full_name    |  city  
----------------+--------
 Bruno Silva    | Lisboa
 Diogo Antunes  | Braga
 Elena Costa    | Lisboa
 Filipe Moreira | Braga
(4 rows)
```

```sql
SELECT full_name, city FROM members WHERE NOT (city = 'Porto') ORDER BY full_name;
```

```
   full_name    |  city  
----------------+--------
 Bruno Silva    | Lisboa
 Diogo Antunes  | Braga
 Elena Costa    | Lisboa
 Filipe Moreira | Braga
(4 rows)
```

```sql
SELECT full_name, city FROM members WHERE NOT city = 'Porto' ORDER BY full_name;
```

```
   full_name    |  city  
----------------+--------
 Bruno Silva    | Lisboa
 Diogo Antunes  | Braga
 Elena Costa    | Lisboa
 Filipe Moreira | Braga
(4 rows)
```

# 2. Qual foi o empréstimo devolvido mais recentemente? Mostre book_id e returned_on, e só ele.

```sql
SELECT book_id, returned_on FROM loans WHERE returned_on IS NOT NULL ORDER BY returned_on DESC LIMIT 1;
```

```
 book_id | returned_on 
---------+-------------
       8 | 2026-08-30
(1 row)
```

```sql
SELECT book_id, returned_on FROM loans ORDER BY returned_on DESC NULLS LAST LIMIT 1;
```

```
 book_id | returned_on 
---------+-------------
       8 | 2026-08-30
(1 row)
```

```sql
SELECT book_id, returned_on FROM loans ORDER BY returned_on DESC NULLS LAST FETCH FIRST 1 ROW ONLY;
```

```
 book_id | returned_on 
---------+-------------
       8 | 2026-08-30
(1 row)
```

# 3. Liste o nome do autor (authors.name), o título do livro (books.title) e a data do empréstimo (loans.loaned_on) de todos os empréstimos feitos a partir de 1º de julho de 2026, do mais recente para o mais antigo.

```sql
SELECT authors.name, books.title, loans.loaned_on FROM authors INNER JOIN books ON authors.id = books.author_id INNER JOIN loans ON books.id = loans.book_id WHERE loans.loaned_on >= '2026-07-01' ORDER BY loans.loaned_on DESC;
```

```
       name        |           title           | loaned_on  
-------------------+---------------------------+------------
 Han Kang          | The Vegetarian            | 2026-09-01
 Ursula K. Le Guin | The Left Hand of Darkness | 2026-08-27
 Chinua Achebe     | No Longer at Ease         | 2026-08-19
 Han Kang          | The Vegetarian            | 2026-08-14
 Italo Calvino     | Invisible Cities          | 2026-08-11
 Ursula K. Le Guin | A Wizard of Earthsea      | 2026-08-08
 Italo Calvino     | If on a Winter's Night    | 2026-08-03
 Chinua Achebe     | Things Fall Apart         | 2026-08-01
 Chinua Achebe     | Things Fall Apart         | 2026-07-22
 Chinua Achebe     | Things Fall Apart         | 2026-07-14
 Ursula K. Le Guin | The Left Hand of Darkness | 2026-07-05
(11 rows)
```

# 4. Quantos membros nunca pegaram nenhum livro emprestado? Quero só um número como resposta.

```sql
SELECT COUNT(DISTINCT members.id) AS members_never_loaned_on FROM members LEFT JOIN loans ON members.id = loans.member_id WHERE loans.loaned_on IS NULL;
```

```
 members_never_loaned_on 
-------------------------
                       1
(1 row)
```

# 5. Quantos membros diferentes têm pelo menos um empréstimo ainda em aberto (não devolvido) de um livro publicado depois de 1970? Quero só um número como resposta.

```sql
SELECT COUNT(DISTINCT loans.member_id) AS members_loans_not_returned_books_more_1970 FROM loans INNER JOIN books ON loans.book_id = books.id WHERE loans.returned_on IS NULL and books.published_year > 1970;
```

```
 members_loans_not_returned_books_more_1970 
--------------------------------------------
                                          2
(1 row)
```

# 6. Quantos empréstimos ainda estão em aberto (não devolvidos)? Conte usando member_id.

```sql
SELECT COUNT(member_id) FROM loans WHERE returned_on IS NULL;
```

```
 count 
-------
     6
(1 row)
```

```sql
SELECT DISTINCT COUNT(member_id) FROM loans WHERE returned_on IS NULL;
```

```
 count 
-------
     6
(1 row)
```

# 7. Quantos empréstimos existem no total? Conte usando book_id.

```sql
SELECT COUNT(book_id) FROM loans;
```

```
 count 
-------
    18
(1 row)
```

```sql
SELECT DISTINCT COUNT(book_id) FROM loans;
```

```
 count 
-------
    18
(1 row)
```

# 8. Quantos livros diferentes já foram emprestados?

```sql
SELECT COUNT(DISTINCT book_id) FROM loans;
```

```
 count 
-------
     8
(1 row)
```

# 9. Liste, sem repetição, o book_id de todos os livros que já foram emprestados.

```sql
SELECT DISTINCT book_id FROM loans;
```

```
 book_id 
---------
       3
       5
       4
       6
       2
       7
       1
       8
(8 rows)
```

# 10. Quantas cidades diferentes existem em members?

```sql
SELECT COUNT(DISTINCT city) FROM members;
```

```
 count 
-------
     3
(1 row)
```
