create table posts (
  id         serial primary key,
  title      varchar(255),
  name       varchar(255),
  text       text,
  tag        varchar(64)[],
  category   varchar(64),
  created_at timestamp not null
);
