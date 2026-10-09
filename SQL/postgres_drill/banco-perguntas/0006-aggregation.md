# 1. Quantos livros (books) têm mais de 2 cópias?

```sql
SELECT COUNT(*) AS books_with_more_than_2_copies FROM books WHERE copies > 2;
```

```
 books_with_more_than_2_copies 
--------------------------------
                              3
(1 row)
```

# 2. Qual é a média de cópias (copies) entre os livros publicados antes de 1970?

```sql
SELECT AVG(copies) AS avg_copies_under_1970 FROM books WHERE published_year < 1970;
```

```
 avg_copies_under_1970 
------------------------
    2.7500000000000000
(1 row)
```

# 3. Quantos autores diferentes (authors) tiveram algum livro emprestado pelo menos uma vez?

```sql
SELECT COUNT(DISTINCT books.author_id) AS loaned_author FROM books INNER JOIN loans ON books.id = loans.book_id;
```

```
 loaned_author 
---------------
             4
(1 row)
```

# 4. Qual é a data do empréstimo mais antigo (loans.loaned_on) entre os livros de autores dos EUA (authors.country)?

```sql
SELECT MIN(loans.loaned_on) AS usa_min_loaned_on FROM loans INNER JOIN books ON loans.book_id = books.id INNER JOIN authors ON authors.id = books.author_id WHERE authors.country = 'USA';
```

```
 usa_min_loaned_on 
-------------------
 2026-03-17
(1 row)
```
