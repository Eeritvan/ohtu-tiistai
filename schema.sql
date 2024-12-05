--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4
-- Dumped by pg_dump version 15.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: sources; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.sources (
    id integer NOT NULL,
    citekey character varying(50) NOT NULL,
    ref_type character varying(50) NOT NULL,
    author character varying(255) NOT NULL,
    title character varying(255) NOT NULL,
    year integer NOT NULL,
    booktitle text,
    editor text,
    volume integer,
    number integer,
    series text,
    pages text,
    address text,
    month integer,
    organisation text,
    publisher text,
    journal text,
    note text
);


ALTER TABLE public.sources OWNER TO -;

--
-- Name: sources_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.sources_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sources_id_seq OWNER TO -;

--
-- Name: sources_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.sources_id_seq OWNED BY public.sources.id;


--
-- Name: sources id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.sources ALTER COLUMN id SET DEFAULT nextval('public.sources_id_seq'::regclass);


--
-- Data for Name: sources; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.sources (id, citekey, ref_type, author, title, year, booktitle, editor, volume, number, series, pages, address, month, organisation, publisher, journal, note) FROM stdin;
\.


--
-- Name: sources_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.sources_id_seq', 1, false);


--
-- Name: sources sources_citekey_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.sources
    ADD CONSTRAINT sources_citekey_key UNIQUE (citekey);


--
-- Name: sources sources_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.sources
    ADD CONSTRAINT sources_pkey PRIMARY KEY (id);


--
-- Name: sources sources_title_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.sources
    ADD CONSTRAINT sources_title_key UNIQUE (title);


--
-- PostgreSQL database dump complete
--

