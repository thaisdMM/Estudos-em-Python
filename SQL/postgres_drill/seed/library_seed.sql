DROP TABLE IF EXISTS loans, books, authors, members;

CREATE TABLE members (
    id         serial PRIMARY KEY,
    full_name  text NOT NULL,
    city       text NOT NULL,
    joined_on  date NOT NULL
);

CREATE TABLE authors (
    id      serial PRIMARY KEY,
    name    text NOT NULL,
    country text NOT NULL
);

CREATE TABLE books (
    id             serial PRIMARY KEY,
    title          text NOT NULL,
    author_id      integer NOT NULL REFERENCES authors(id),
    published_year integer NOT NULL,
    copies         integer NOT NULL
);

CREATE TABLE loans (
    id          serial PRIMARY KEY,
    member_id   integer NOT NULL REFERENCES members(id),
    book_id     integer NOT NULL REFERENCES books(id),
    loaned_on   date NOT NULL,
    returned_on date
);

INSERT INTO members (full_name, city, joined_on) VALUES
  ('Ana Ferreira',    'Porto',   '2023-02-11'),
  ('Bruno Silva',     'Lisboa',  '2024-06-30'),
  ('Carla Mendes',    'Porto',   '2022-11-05'),
  ('Diogo Antunes',   'Braga',   '2025-01-20'),
  ('Elena Costa',     'Lisboa',  '2025-03-14'),
  ('Filipe Moreira',  'Braga',   '2026-01-09');

INSERT INTO authors (name, country) VALUES
  ('Ursula K. Le Guin', 'USA'),
  ('Italo Calvino',     'Italy'),
  ('Chinua Achebe',     'Nigeria'),
  ('Han Kang',          'South Korea');

INSERT INTO books (title, author_id, published_year, copies) VALUES
  ('A Wizard of Earthsea',        1, 1968, 3),
  ('The Left Hand of Darkness',   1, 1969, 2),
  ('The Dispossessed',            1, 1974, 1),
  ('Invisible Cities',            2, 1972, 4),
  ('If on a Winter''s Night',     2, 1979, 2),
  ('Things Fall Apart',           3, 1958, 5),
  ('No Longer at Ease',           3, 1960, 1),
  ('The Vegetarian',              4, 2007, 2);

INSERT INTO loans (member_id, book_id, loaned_on, returned_on) VALUES
  (1, 1, '2026-06-02', '2026-06-20'),
  (1, 4, '2026-06-25', '2026-07-10'),
  (1, 6, '2026-08-01', NULL),
  (1, 8, '2026-08-14', '2026-08-30'),
  (2, 2, '2026-07-05', '2026-07-19'),
  (2, 4, '2026-08-11', NULL),
  (3, 1, '2026-05-18', '2026-06-01'),
  (3, 3, '2026-06-09', '2026-06-29'),
  (3, 6, '2026-07-22', '2026-08-05'),
  (3, 7, '2026-08-19', NULL),
  (3, 8, '2026-09-01', NULL),
  (4, 5, '2026-08-03', '2026-08-25'),
  (5, 6, '2026-07-14', '2026-07-28'),
  (5, 1, '2026-08-08', NULL),
  (5, 2, '2026-08-27', NULL),
  (2, 8, '2026-04-12', '2026-04-30'),
  (4, 4, '2026-05-05', '2026-05-21'),
  (1, 2, '2026-03-17', '2026-04-02');
