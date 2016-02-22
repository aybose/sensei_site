drop table if exists SocialProximity;
create table SocialProximity (
  id integer primary key autoincrement,
  school text not null,
  date text not null,
  primary_student text not null,
  secondary_student text not null,
  rsval integer not null
);