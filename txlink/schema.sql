DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS product;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

create table customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    company_addr varchar(20),
    site_addr varchar(20),
    Email varchar(50),
    Note varchar(100),
    user_id int
    ,foreign key (user_id) references user(id) on delete cascade
);

create table product (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  prod_name TEXT UNIQUE NOT NULL,
  user_id int
  ,foreign key (user_id) references user(id) on delete cascade
);