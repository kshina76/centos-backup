create table posts (
  id         serial primary key,
  title      varchar(255),
  name       varchar(255),
  text       text,
  tag        varchar(64)[],
  category   varchar(64),
  created_at timestamp not null
);

create table sessions (
  id         serial primary key,
  uuid       varchar(64) not null unique,
  email      varchar(255),
  --user_id    integer references users(id),
  created_at timestamp not null
);

create table users (
  id         serial primary key,
  uuid       varchar(64) not null unique,
  name       varchar(255),
  email      varchar(255) not null unique,
  password   varchar(255) not null,
  created_at timestamp not null
);
