create table todos (
  id         serial primary key,
  title      varchar(255),
  status     varchar(64),
  date       timestamp not null  
);