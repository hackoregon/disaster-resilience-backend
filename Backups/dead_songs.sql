
SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

DROP database if exists dead_songs;
drop role if exists sampleuser;

CREATE DATABASE dead_songs;

CREATE USER sampleuser WITH PASSWORD 'sit-down-c0mic';

ALTER ROLE sampleuser SET client_encoding TO 'utf8';
ALTER ROLE sampleuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE sampleuser SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE dead_songs TO sampleuser;

\connect dead_songs;

CREATE TABLE api_song (
    id SERIAL,
    release_date timestamp with time zone NOT NULL,
    title character varying(100) NOT NULL,
    album text NOT NULL,
    writer text NOT NULL
);

INSERT INTO api_song (release_date, title, album, writer)
    VALUES ('1970-11-01 00:00:00 PDT', 'Ripple', 'American Beauty', 'Garcia, Hunter');

INSERT INTO api_song (release_date, title, album, writer)
    VALUES ('1978-11-15 00:00:00 PDT', 'Shakedown Street', 'Shakedown Street', 'Garcia, Hunter');

INSERT INTO api_song (release_date, title, album, writer)
    VALUES ('1978-11-15 00:00:00 PDT', 'I Need a Miracle', 'Shakedown Street', 'Weir, Barlow');
