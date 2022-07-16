create table tweets
( tweet_id SERIAL PRIMARY KEY,created_at varchar(1000), text varchar(3000),
source varchar(1000), name varchar(1000),
username varchar(1000), location varchar(100),is_verified varchar(100), description varchar(3000))