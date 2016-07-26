--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.3
-- Dumped by pg_dump version 9.5.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE auth_group OWNER TO "user";

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_id_seq OWNER TO "user";

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_group_permissions OWNER TO "user";

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_permissions_id_seq OWNER TO "user";

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE auth_permission OWNER TO "user";

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_permission_id_seq OWNER TO "user";

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    password character varying(128) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    is_superuser boolean NOT NULL,
    last_login timestamp with time zone NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE auth_user OWNER TO "user";

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE auth_user_groups OWNER TO "user";

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_groups_id_seq OWNER TO "user";

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_id_seq OWNER TO "user";

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_user_user_permissions OWNER TO "user";

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_user_permissions_id_seq OWNER TO "user";

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    content_type_id integer,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE django_admin_log OWNER TO "user";

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_admin_log_id_seq OWNER TO "user";

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE django_content_type OWNER TO "user";

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_content_type_id_seq OWNER TO "user";

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE django_session OWNER TO "user";

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE django_site OWNER TO "user";

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE django_site_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_site_id_seq OWNER TO "user";

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE django_site_id_seq OWNED BY django_site.id;


--
-- Name: testapp_author; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE testapp_author (
    id integer NOT NULL,
    salutation character varying(10) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(40) NOT NULL,
    email character varying(75) NOT NULL,
    headshot character varying(100) NOT NULL
);


ALTER TABLE testapp_author OWNER TO "user";

--
-- Name: testapp_author_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE testapp_author_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE testapp_author_id_seq OWNER TO "user";

--
-- Name: testapp_author_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE testapp_author_id_seq OWNED BY testapp_author.id;


--
-- Name: testapp_book; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE testapp_book (
    id integer NOT NULL,
    title character varying(100) NOT NULL,
    publisher_id integer NOT NULL,
    publication_date date NOT NULL
);


ALTER TABLE testapp_book OWNER TO "user";

--
-- Name: testapp_book_authors; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE testapp_book_authors (
    id integer NOT NULL,
    book_id integer NOT NULL,
    author_id integer NOT NULL
);


ALTER TABLE testapp_book_authors OWNER TO "user";

--
-- Name: testapp_book_authors_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE testapp_book_authors_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE testapp_book_authors_id_seq OWNER TO "user";

--
-- Name: testapp_book_authors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE testapp_book_authors_id_seq OWNED BY testapp_book_authors.id;


--
-- Name: testapp_book_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE testapp_book_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE testapp_book_id_seq OWNER TO "user";

--
-- Name: testapp_book_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE testapp_book_id_seq OWNED BY testapp_book.id;


--
-- Name: testapp_categories; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE testapp_categories (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    parent_id integer,
    slug character varying(50) NOT NULL,
    default_image_id integer
);


ALTER TABLE testapp_categories OWNER TO "user";

--
-- Name: testapp_categories_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE testapp_categories_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE testapp_categories_id_seq OWNER TO "user";

--
-- Name: testapp_categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE testapp_categories_id_seq OWNED BY testapp_categories.id;


--
-- Name: testapp_images; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE testapp_images (
    id integer NOT NULL,
    image character varying(100) NOT NULL
);


ALTER TABLE testapp_images OWNER TO "user";

--
-- Name: testapp_images_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE testapp_images_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE testapp_images_id_seq OWNER TO "user";

--
-- Name: testapp_images_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE testapp_images_id_seq OWNED BY testapp_images.id;


--
-- Name: testapp_product; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE testapp_product (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    category_id integer,
    count integer NOT NULL,
    price integer NOT NULL,
    image_id integer
);


ALTER TABLE testapp_product OWNER TO "user";

--
-- Name: testapp_product_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE testapp_product_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE testapp_product_id_seq OWNER TO "user";

--
-- Name: testapp_product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE testapp_product_id_seq OWNED BY testapp_product.id;


--
-- Name: testapp_publisher; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE testapp_publisher (
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    address character varying(50) NOT NULL,
    city character varying(60) NOT NULL,
    state_province character varying(30) NOT NULL,
    country character varying(50) NOT NULL,
    website character varying(200) NOT NULL
);


ALTER TABLE testapp_publisher OWNER TO "user";

--
-- Name: testapp_publisher_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE testapp_publisher_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE testapp_publisher_id_seq OWNER TO "user";

--
-- Name: testapp_publisher_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE testapp_publisher_id_seq OWNED BY testapp_publisher.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY django_site ALTER COLUMN id SET DEFAULT nextval('django_site_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY testapp_author ALTER COLUMN id SET DEFAULT nextval('testapp_author_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY testapp_book ALTER COLUMN id SET DEFAULT nextval('testapp_book_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY testapp_book_authors ALTER COLUMN id SET DEFAULT nextval('testapp_book_authors_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY testapp_categories ALTER COLUMN id SET DEFAULT nextval('testapp_categories_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY testapp_images ALTER COLUMN id SET DEFAULT nextval('testapp_images_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY testapp_product ALTER COLUMN id SET DEFAULT nextval('testapp_product_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY testapp_publisher ALTER COLUMN id SET DEFAULT nextval('testapp_publisher_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: user
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: user
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: user
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add permission	1	add_permission
2	Can change permission	1	change_permission
3	Can delete permission	1	delete_permission
4	Can add group	2	add_group
5	Can change group	2	change_group
6	Can delete group	2	delete_group
7	Can add user	3	add_user
8	Can change user	3	change_user
9	Can delete user	3	delete_user
10	Can add content type	4	add_contenttype
11	Can change content type	4	change_contenttype
12	Can delete content type	4	delete_contenttype
13	Can add session	5	add_session
14	Can change session	5	change_session
15	Can delete session	5	delete_session
16	Can add site	6	add_site
17	Can change site	6	change_site
18	Can delete site	6	delete_site
28	Can add categories	10	add_categories
29	Can change categories	10	change_categories
30	Can delete categories	10	delete_categories
31	Can add log entry	11	add_logentry
32	Can change log entry	11	change_logentry
33	Can delete log entry	11	delete_logentry
34	Can add images	12	add_images
35	Can change images	12	change_images
36	Can delete images	12	delete_images
37	Can add product	13	add_product
38	Can change product	13	change_product
39	Can delete product	13	delete_product
40	Can add test	14	add_test
41	Can change test	14	change_test
42	Can delete test	14	delete_test
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('auth_permission_id_seq', 42, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: user
--

COPY auth_user (id, username, first_name, last_name, email, password, is_staff, is_active, is_superuser, last_login, date_joined) FROM stdin;
1	root			serafinn@mail.ru	pbkdf2_sha256$10000$kuhLdSfCkIkc$voJK0Xrn2UWj88rCkrDkJwSXln51hbZS09TLBN8I3xw=	t	t	t	2016-07-22 15:21:15.89576+07	2016-07-22 15:18:35.272258+07
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: user
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('auth_user_id_seq', 1, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: user
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: user
--

COPY django_admin_log (id, action_time, user_id, content_type_id, object_id, object_repr, action_flag, change_message) FROM stdin;
1	2016-07-22 15:44:48.800516+07	1	12	1	Images object	1	
2	2016-07-22 15:45:00.046696+07	1	12	2	Images object	1	
3	2016-07-22 15:46:11.105678+07	1	13	1	19' монитро номер раз\n	1	
4	2016-07-22 15:46:46.856267+07	1	13	2	21" номер раз\n	1	
5	2016-07-22 15:47:34.966522+07	1	13	3	оооочень мощьный проц от интел\n	1	
6	2016-07-22 15:47:53.854615+07	1	13	4	замена печки\n	1	
7	2016-07-22 15:48:37.642922+07	1	13	5	процессор для ноутбука\n	1	
8	2016-07-22 17:13:07.764913+07	1	13	6	процессор для ноутбука 2\n	1	
9	2016-07-25 09:11:41.788988+07	1	10	1	Мониторы | /monitors/ | 1	1	
10	2016-07-25 09:11:51.541493+07	1	10	2	21 | /monitors/21/ | 2	1	
11	2016-07-25 09:12:07.216665+07	1	10	3	19 | /monitors/19/ | 2	1	
12	2016-07-25 09:12:37.936634+07	1	10	4	27 | /monitors/27/ | 2	1	
13	2016-07-25 09:32:35.209106+07	1	10	5	TFT | /monitors/19/tft/ | 3	1	
14	2016-07-25 09:33:03.463487+07	1	10	6	lcd | /monitors/19/lcd/ | 3	1	
15	2016-07-25 09:33:35.365077+07	1	10	7	tft | /monitors/21/tft/ | 3	1	
16	2016-07-25 09:34:06.224743+07	1	10	8	Процессоры | /cpu/ | 1	1	
17	2016-07-25 09:34:49.105394+07	1	10	9	intel | /cpu/intel/ | 2	1	
18	2016-07-25 10:15:25.19557+07	1	12	3	Images object	1	
19	2016-07-25 10:15:39.484016+07	1	10	1	Монитры | /monitors/ | 1	1	
20	2016-07-25 10:15:52.773197+07	1	10	2	19 | /monitors/19/ | 2	1	
21	2016-07-25 10:16:41.653559+07	1	13	1	Product object	1	
22	2016-07-25 10:21:51.943229+07	1	10	3	21 | /monitors/21/ | 2	1	
23	2016-07-25 10:21:58.801428+07	1	13	2	21" монитор	1	
24	2016-07-25 10:35:44.02325+07	1	13	3	19' монитор asus	1	
25	2016-07-25 10:46:26.622151+07	1	10	5	Процессоры | /cpu/ | 1	1	
26	2016-07-25 10:46:58.32601+07	1	10	6	Intel | /cpu/intel/ | 2	1	
27	2016-07-25 10:48:35.900614+07	1	10	7	Intel notebook | /cpu/intel/notebook/ | 3	1	
28	2016-07-25 10:49:41.815799+07	1	13	4	Intel i7	1	
29	2016-07-25 10:50:05.711201+07	1	13	5	intel i3 notebook	1	
30	2016-07-25 11:44:26.937585+07	1	10	1	Процессоры | /cpu/ | 1	1	
31	2016-07-25 11:47:38.080134+07	1	10	2	Мониторы | /monitors/ | 1	1	
32	2016-07-25 11:49:12.639443+07	1	10	2	Мониторы | /monitors/ | 1	3	
33	2016-07-25 11:49:12.649267+07	1	10	1	Процессоры | /cpu/ | 1	3	
34	2016-07-25 11:49:29.450496+07	1	10	3	Мониторы | /monitors/ | 1	1	
35	2016-07-25 11:49:46.281964+07	1	10	4	Процессоры | /cpu/ | 1	1	
36	2016-07-25 11:50:17.639691+07	1	10	5	19 | /monitors/19/ | 2	1	
37	2016-07-25 11:50:28.106895+07	1	10	6	21 | /monitors/21/ | 2	1	
38	2016-07-25 11:51:02.566179+07	1	10	7	intel | /cpu/intel/ | 2	1	
39	2016-07-25 11:51:18.660215+07	1	10	8	amd | /cpu/amd/ | 2	1	
40	2016-07-25 11:51:39.346065+07	1	10	9	notebook | /cpu/intel/notebooks/ | 3	1	
41	2016-07-25 11:52:01.068932+07	1	10	10	notebook | /cpu/amd/notebooks/ | 3	1	
42	2016-07-25 11:53:37.710547+07	1	13	1	19' монитор	1	
43	2016-07-25 11:53:59.375385+07	1	13	2	21" монитор	1	
44	2016-07-25 11:54:22.216387+07	1	13	3	intel i3 notebook	1	
45	2016-07-25 11:54:40.811752+07	1	13	4	amd cpu	1	
46	2016-07-25 11:55:01.864947+07	1	13	5	amd notebook	1	
47	2016-07-25 14:11:45.499607+07	1	13	6	19' монитор asusa	1	
48	2016-07-25 14:12:13.632434+07	1	13	7	21" монитор benq	1	
49	2016-07-25 14:30:07.834286+07	1	13	8	19' монитор noname	1	
50	2016-07-25 14:32:19.271568+07	1	13	9	21" монитор noname	1	
51	2016-07-25 14:43:58.510748+07	1	13	10	21" монитор noname	1	
52	2016-07-25 14:44:38.611014+07	1	13	11	19' монитор noname 3	1	
53	2016-07-25 14:45:05.642425+07	1	13	12	19' монитор noname 4	1	
54	2016-07-25 14:45:18.412094+07	1	13	13	21" монитор benq 3	1	
55	2016-07-25 14:45:30.153506+07	1	13	14	21" монитор benq 2	1	
56	2016-07-25 14:45:57.532399+07	1	13	15	19' монитор asusaki	1	
57	2016-07-25 14:46:18.179815+07	1	13	16	19' монитор noname 4	1	
58	2016-07-25 15:24:34.210033+07	1	10	11	27 | /monitors/27/ | 2	1	
59	2016-07-25 16:45:59.361497+07	1	10	2	Мониторы | /monitors/ | 1	1	
60	2016-07-25 16:51:55.114766+07	1	10	3	19 | /monitors/19/ | 2	1	
61	2016-07-25 16:52:16.431293+07	1	10	4	intel | /monitors/intel/ | 2	1	
62	2016-07-25 16:52:27.804044+07	1	10	5	Процессоры | /cpu/ | 1	1	
63	2016-07-25 16:52:37.26604+07	1	10	4	intel | /cpu/intel/ | 2	2	Changed parent.
64	2016-07-25 16:53:04.805162+07	1	10	6	amd | /cpu/amd/ | 2	1	
65	2016-07-25 16:53:32.190695+07	1	10	7	21 | /monitors/21/ | 2	1	
66	2016-07-25 16:55:39.521445+07	1	10	8	Intel notebook | /cpu/amd/notebook/ | 3	1	
67	2016-07-25 16:55:48.888369+07	1	10	8	Intel notebook | /cpu/intel/notebook/ | 3	2	Changed parent.
68	2016-07-25 16:56:01.100004+07	1	10	8	Intel notebook | /cpu/amd/notebook/ | 3	2	Changed parent.
69	2016-07-25 16:56:08.251564+07	1	10	8	Intel notebook | /cpu/intel/notebook/ | 3	2	Changed parent.
70	2016-07-25 16:57:12.886232+07	1	13	1	19	1	
71	2016-07-25 16:57:21.508168+07	1	13	1	19' монитор	2	Changed name.
72	2016-07-25 16:57:49.366376+07	1	13	2	21" монитор	1	
73	2016-07-25 16:58:06.385382+07	1	13	3	19' монитор noname 3	1	
74	2016-07-26 09:44:55.527655+07	1	13	4	19' монитор noname 3	1	
75	2016-07-26 09:45:07.322839+07	1	13	5	19' монитор noname 4	1	
76	2016-07-26 09:49:32.970052+07	1	13	6	19' монитор noname 31	1	
77	2016-07-26 09:49:47.394423+07	1	13	7	19' монитор 1	1	
78	2016-07-26 09:49:58.289216+07	1	13	8	21" монитор benq	1	
79	2016-07-26 09:50:08.888819+07	1	13	9	19' монитор asus	1	
80	2016-07-26 09:50:52.120419+07	1	13	10	19' монитор asus 1	1	
81	2016-07-26 09:51:01.5479+07	1	13	11	21" монитор noname	1	
82	2016-07-26 10:06:32.964167+07	1	13	12	21" монитор noname 123	1	
83	2016-07-26 10:06:41.924896+07	1	13	13	21" монитор benq	1	
84	2016-07-26 12:42:37.895692+07	1	14	1	Test object	1	
85	2016-07-26 12:44:27.176899+07	1	14	2	1-12-312-3	1	
86	2016-07-26 12:45:08.486897+07	1	14	3	1	1	
87	2016-07-26 12:46:12.986759+07	1	14	4	as-das-d	1	
88	2016-07-26 12:46:18.183895+07	1	14	4	as-das-d	2	Changed slug.
89	2016-07-26 12:46:23.038185+07	1	14	4	123	2	Changed slug.
90	2016-07-26 12:48:14.494144+07	1	14	5	21-noname	1	
91	2016-07-26 12:48:30.96737+07	1	14	6	21	1	
92	2016-07-26 13:03:42.40909+07	1	14	7		1	
93	2016-07-26 13:06:12.948063+07	1	12	1	Images object	1	
94	2016-07-26 13:13:18.238676+07	1	10	5	Процессоры | cpu | 0	1	
95	2016-07-26 13:13:36.889761+07	1	10	6	intel |  | 0	1	
96	2016-07-26 13:14:27.536109+07	1	10	5	Процессоры | cpu | 0	2	Changed slug.
97	2016-07-26 13:14:46.856022+07	1	10	6	intel | intel | 1	2	No fields changed.
98	2016-07-26 13:15:49.027189+07	1	10	7	Intel notebook | intel-notebook | 1	1	
99	2016-07-26 13:40:21.656059+07	1	10	8	13312312 123  | 13312312-123 | 2 | cpu/13312312-123/	1	
100	2016-07-26 13:40:27.951395+07	1	10	8	13312312 123  | 13312312-123 | 2 | cpu/13312312-123/	3	
101	2016-07-26 13:42:54.984621+07	1	10	9	процессоры | cpu1 | 1 | cpu1/	1	
102	2016-07-26 14:54:15.754338+07	1	10	9	процессоры | cpu1 | 1 | cpu1/	3	
103	2016-07-26 14:54:15.764507+07	1	10	7	Intel notebook | intel-notebook | 3 | cpu/intel/intel-notebook/	3	
104	2016-07-26 14:54:29.498629+07	1	10	10	AMD | amd | 2 | cpu/amd/	1	
105	2016-07-26 15:13:55.824211+07	1	13	1	intel i7	1	
106	2016-07-26 15:14:14.377241+07	1	13	2	AMD Cpu	1	
107	2016-07-26 16:47:39.756983+07	1	10	11	11 | notebook | notebook | 3 | cpu/intel/notebook/	1	
108	2016-07-26 17:21:39.357365+07	1	10	12	12 | Мониторы | monitors | 1 | monitors/	1	
109	2016-07-26 17:21:57.915578+07	1	10	13	13 | 19` | 19 | 2 | monitors/19/	1	
110	2016-07-26 17:22:12.790995+07	1	10	14	14 | 21 | 21 | 2 | monitors/21/	1	
111	2016-07-26 17:23:36.562966+07	1	13	3	19' монитор noname 3	1	
112	2016-07-26 17:23:55.981656+07	1	13	4	19' монитор	1	
113	2016-07-26 17:24:09.067775+07	1	13	5	19' монитор noname 4	1	
114	2016-07-26 17:24:26.475894+07	1	13	6	21" монитор noname	1	
115	2016-07-26 17:28:53.067177+07	1	13	7	intel i3 notebook	1	
116	2016-07-26 17:30:39.365684+07	1	10	15	15 | 100 | 100 | 2 | monitors/100/	1	
117	2016-07-26 17:32:00.554315+07	1	10	15	15 | 100 | 100 | 2 | monitors/100/	3	
118	2016-07-26 17:33:13.971017+07	1	10	16	16 | amd notebook | amd-notebook | 3 | cpu/amd/amd-notebook/	1	
119	2016-07-26 17:33:53.903768+07	1	10	16	16 | notebook | amd-notebook | 3 | cpu/amd/amd-notebook/	2	Changed name.
120	2016-07-26 17:34:41.980256+07	1	10	16	16 | amd notebook | amd-notebook | 3 | cpu/amd/amd-notebook/	2	Changed name.
121	2016-07-26 17:36:23.075236+07	1	13	8	19' монитор asus	1	
122	2016-07-26 17:52:00.720916+07	1	13	9	amd notebook	1	
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 122, true);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: user
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	permission	auth	permission
2	group	auth	group
3	user	auth	user
4	content type	contenttypes	contenttype
5	session	sessions	session
6	site	sites	site
10	categories	testapp	categories
11	log entry	admin	logentry
12	images	testapp	images
13	product	testapp	product
14	test	testapp	test
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('django_content_type_id_seq', 14, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: user
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
a9ca8dd779c57d24101a253517461d79	YzA2NDFmYzQwMDNmYzMxMzYyMTUyMTQ1M2M0ZmFmMzgxNzkxNzA4YzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQRLAXUu\n	2016-08-05 15:21:15.898438+07
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: user
--

COPY django_site (id, domain, name) FROM stdin;
1	example.com	example.com
\.


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('django_site_id_seq', 1, true);


--
-- Data for Name: testapp_author; Type: TABLE DATA; Schema: public; Owner: user
--

COPY testapp_author (id, salutation, first_name, last_name, email, headshot) FROM stdin;
\.


--
-- Name: testapp_author_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('testapp_author_id_seq', 1, false);


--
-- Data for Name: testapp_book; Type: TABLE DATA; Schema: public; Owner: user
--

COPY testapp_book (id, title, publisher_id, publication_date) FROM stdin;
\.


--
-- Data for Name: testapp_book_authors; Type: TABLE DATA; Schema: public; Owner: user
--

COPY testapp_book_authors (id, book_id, author_id) FROM stdin;
\.


--
-- Name: testapp_book_authors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('testapp_book_authors_id_seq', 1, false);


--
-- Name: testapp_book_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('testapp_book_id_seq', 1, false);


--
-- Data for Name: testapp_categories; Type: TABLE DATA; Schema: public; Owner: user
--

COPY testapp_categories (id, name, parent_id, slug, default_image_id) FROM stdin;
5	Процессоры	\N	cpu	1
6	intel	5	intel	1
10	AMD	5	amd	1
11	notebook	6	notebook	1
12	Мониторы	\N	monitors	1
13	19`	12	19	1
14	21	12	21	1
16	amd notebook	10	amd-notebook	1
\.


--
-- Name: testapp_categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('testapp_categories_id_seq', 16, true);


--
-- Data for Name: testapp_images; Type: TABLE DATA; Schema: public; Owner: user
--

COPY testapp_images (id, image) FROM stdin;
1	pics/cpu.png
\.


--
-- Name: testapp_images_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('testapp_images_id_seq', 1, true);


--
-- Data for Name: testapp_product; Type: TABLE DATA; Schema: public; Owner: user
--

COPY testapp_product (id, name, category_id, count, price, image_id) FROM stdin;
1	intel i7	6	1	1	1
2	AMD Cpu	10	1	1	1
3	19' монитор noname 3	13	10	1	1
4	19' монитор	13	1	1	1
5	19' монитор noname 4	13	1	1	1
6	21" монитор noname	14	1	1	1
7	intel i3 notebook	11	1	1	1
8	19' монитор asus	13	1	1	1
9	amd notebook	16	1	1	1
\.


--
-- Name: testapp_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('testapp_product_id_seq', 9, true);


--
-- Data for Name: testapp_publisher; Type: TABLE DATA; Schema: public; Owner: user
--

COPY testapp_publisher (id, name, address, city, state_province, country, website) FROM stdin;
1	Addison-Wesley	75 Arlington Street	Boston	MA	U.S.A.	http://www.apress.com/
3	Addison-Wesley	75 Arlington Street	Boston	MA	U.S.A.	http://www.apress.com/
5	Addison-Wesley	75 Arlington Street	Boston	MA	U.S.A.	http://www.apress.com/
7	Addison-Wesley	75 Arlington Street	Boston	MA	U.S.A.	http://www.apress.com/
9	Addison-Wesley	75 Arlington Street	Boston	MA	U.S.A.	http://www.apress.com/
11	Addison-Wesley	75 Arlington Street	Boston	MA	U.S.A.	http://www.apress.com/
13	Addison-Wesley	75 Arlington Street	Boston	MA	U.S.A.	http://www.apress.com/
15	Addison-Wesley	75 Arlington Street	Boston	MA	U.S.A.	http://www.apress.com/
17	Addison-Wesley	75 Arlington Street	Boston	MA	U.S.A.	http://www.apress.com/
19	Addison-Wesley	75 Arlington Street	Boston	MA	U.S.A.	http://www.apress.com/
21	Addison-Wesley	75 Arlington Street	Boston	MA	U.S.A.	http://www.apress.com/
23	Addison-Wesley	75 Arlington Street	Boston	MA	U.S.A.	http://www.apress.com/
25	Addison-Wesley	75 Arlington Street	Boston	MA	U.S.A.	http://www.apress.com/
2	Apress Publishing	10 Fawcett St.	Cambridge	MA	U.S.A.	http://www.oreilly.com/
4	Apress Publishing	10 Fawcett St.	Cambridge	MA	U.S.A.	http://www.oreilly.com/
6	Apress Publishing	10 Fawcett St.	Cambridge	MA	U.S.A.	http://www.oreilly.com/
8	Apress Publishing	10 Fawcett St.	Cambridge	MA	U.S.A.	http://www.oreilly.com/
10	Apress Publishing	10 Fawcett St.	Cambridge	MA	U.S.A.	http://www.oreilly.com/
12	Apress Publishing	10 Fawcett St.	Cambridge	MA	U.S.A.	http://www.oreilly.com/
14	Apress Publishing	10 Fawcett St.	Cambridge	MA	U.S.A.	http://www.oreilly.com/
16	Apress Publishing	10 Fawcett St.	Cambridge	MA	U.S.A.	http://www.oreilly.com/
18	Apress Publishing	10 Fawcett St.	Cambridge	MA	U.S.A.	http://www.oreilly.com/
20	Apress Publishing	10 Fawcett St.	Cambridge	MA	U.S.A.	http://www.oreilly.com/
22	Apress Publishing	10 Fawcett St.	Cambridge	MA	U.S.A.	http://www.oreilly.com/
24	Apress Publishing	10 Fawcett St.	Cambridge	MA	U.S.A.	http://www.oreilly.com/
26	Apress Publishing	10 Fawcett St.	Cambridge	MA	U.S.A.	http://www.oreilly.com/
27	Addison-Wesley	75 Arlington Street	Boston	MA	U.S.A.	http://www.apress.com/
28	Apress Publishing	10 Fawcett St.	Cambridge	MA	U.S.A.	http://www.oreilly.com/
29	Addison-Wesley	75 Arlington Street	Boston	MA	U.S.A.	http://www.apress.com/
30	O'Reilly	10 Fawcett St.	Cambridge	MA	U.S.A.	http://www.oreilly.com/
\.


--
-- Name: testapp_publisher_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('testapp_publisher_id_seq', 30, true);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_model_key; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_key UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: testapp_author_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY testapp_author
    ADD CONSTRAINT testapp_author_pkey PRIMARY KEY (id);


--
-- Name: testapp_book_authors_book_id_author_id_key; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY testapp_book_authors
    ADD CONSTRAINT testapp_book_authors_book_id_author_id_key UNIQUE (book_id, author_id);


--
-- Name: testapp_book_authors_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY testapp_book_authors
    ADD CONSTRAINT testapp_book_authors_pkey PRIMARY KEY (id);


--
-- Name: testapp_book_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY testapp_book
    ADD CONSTRAINT testapp_book_pkey PRIMARY KEY (id);


--
-- Name: testapp_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY testapp_categories
    ADD CONSTRAINT testapp_categories_pkey PRIMARY KEY (id);


--
-- Name: testapp_categories_slug_key; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY testapp_categories
    ADD CONSTRAINT testapp_categories_slug_key UNIQUE (slug);


--
-- Name: testapp_images_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY testapp_images
    ADD CONSTRAINT testapp_images_pkey PRIMARY KEY (id);


--
-- Name: testapp_product_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY testapp_product
    ADD CONSTRAINT testapp_product_pkey PRIMARY KEY (id);


--
-- Name: testapp_publisher_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY testapp_publisher
    ADD CONSTRAINT testapp_publisher_pkey PRIMARY KEY (id);


--
-- Name: auth_group_permissions_group_id; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX auth_group_permissions_group_id ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX auth_group_permissions_permission_id ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX auth_permission_content_type_id ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX auth_user_groups_group_id ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX auth_user_groups_user_id ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX auth_user_user_permissions_permission_id ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX auth_user_user_permissions_user_id ON auth_user_user_permissions USING btree (user_id);


--
-- Name: django_admin_log_content_type_id; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX django_admin_log_content_type_id ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX django_admin_log_user_id ON django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX django_session_expire_date ON django_session USING btree (expire_date);


--
-- Name: testapp_book_authors_author_id; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX testapp_book_authors_author_id ON testapp_book_authors USING btree (author_id);


--
-- Name: testapp_book_authors_book_id; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX testapp_book_authors_book_id ON testapp_book_authors USING btree (book_id);


--
-- Name: testapp_book_publisher_id; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX testapp_book_publisher_id ON testapp_book USING btree (publisher_id);


--
-- Name: testapp_categories_default_image_id; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX testapp_categories_default_image_id ON testapp_categories USING btree (default_image_id);


--
-- Name: testapp_categories_parent_id; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX testapp_categories_parent_id ON testapp_categories USING btree (parent_id);


--
-- Name: testapp_product_category_id; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX testapp_product_category_id ON testapp_product USING btree (category_id);


--
-- Name: testapp_product_image_id; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX testapp_product_image_id ON testapp_product USING btree (image_id);


--
-- Name: auth_group_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: book_id_refs_id_cd1907c0; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY testapp_book_authors
    ADD CONSTRAINT book_id_refs_id_cd1907c0 FOREIGN KEY (book_id) REFERENCES testapp_book(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: content_type_id_refs_id_728de91f; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT content_type_id_refs_id_728de91f FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_content_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_fkey FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: group_id_refs_id_3cea63fe; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT group_id_refs_id_3cea63fe FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: parent_id_refs_id_7a48ab89; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY testapp_categories
    ADD CONSTRAINT parent_id_refs_id_7a48ab89 FOREIGN KEY (parent_id) REFERENCES testapp_categories(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: testapp_book_authors_author_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY testapp_book_authors
    ADD CONSTRAINT testapp_book_authors_author_id_fkey FOREIGN KEY (author_id) REFERENCES testapp_author(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: testapp_book_publisher_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY testapp_book
    ADD CONSTRAINT testapp_book_publisher_id_fkey FOREIGN KEY (publisher_id) REFERENCES testapp_publisher(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: testapp_categories_default_image_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY testapp_categories
    ADD CONSTRAINT testapp_categories_default_image_id_fkey FOREIGN KEY (default_image_id) REFERENCES testapp_images(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: testapp_product_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY testapp_product
    ADD CONSTRAINT testapp_product_category_id_fkey FOREIGN KEY (category_id) REFERENCES testapp_categories(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: testapp_product_image_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY testapp_product
    ADD CONSTRAINT testapp_product_image_id_fkey FOREIGN KEY (image_id) REFERENCES testapp_images(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_831107f1; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT user_id_refs_id_831107f1 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_f2045483; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT user_id_refs_id_f2045483 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

