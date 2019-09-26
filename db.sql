PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTO_INCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO django_migrations VALUES(1,'contenttypes','0001_initial','2019-08-05 14:12:11.093270');
INSERT INTO django_migrations VALUES(2,'contenttypes','0002_remove_content_type_name','2019-08-05 14:12:11.119892');
INSERT INTO django_migrations VALUES(3,'auth','0001_initial','2019-08-05 14:12:11.146223');
INSERT INTO django_migrations VALUES(4,'auth','0002_alter_permission_name_max_length','2019-08-05 14:12:11.164362');
INSERT INTO django_migrations VALUES(5,'auth','0003_alter_user_email_max_length','2019-08-05 14:12:11.176874');
INSERT INTO django_migrations VALUES(6,'auth','0004_alter_user_username_opts','2019-08-05 14:12:11.185255');
INSERT INTO django_migrations VALUES(7,'auth','0005_alter_user_last_login_null','2019-08-05 14:12:11.195898');
INSERT INTO django_migrations VALUES(8,'auth','0006_require_contenttypes_0002','2019-08-05 14:12:11.200429');
INSERT INTO django_migrations VALUES(9,'auth','0007_alter_validators_add_error_messages','2019-08-05 14:12:11.214535');
INSERT INTO django_migrations VALUES(10,'auth','0008_alter_user_username_max_length','2019-08-05 14:12:11.236139');
INSERT INTO django_migrations VALUES(11,'auth','0009_alter_user_last_name_max_length','2019-08-05 14:12:11.250582');
INSERT INTO django_migrations VALUES(12,'auth','0010_alter_group_name_max_length','2019-08-05 14:12:11.271578');
INSERT INTO django_migrations VALUES(13,'auth','0011_update_proxy_permissions','2019-08-05 14:12:11.289035');
INSERT INTO django_migrations VALUES(14,'users','0001_initial','2019-08-05 14:12:11.313959');
INSERT INTO django_migrations VALUES(15,'admin','0001_initial','2019-08-05 14:12:11.347911');
INSERT INTO django_migrations VALUES(16,'admin','0002_logentry_remove_auto_add','2019-08-05 14:12:11.369420');
INSERT INTO django_migrations VALUES(17,'admin','0003_logentry_add_action_flag_choices','2019-08-05 14:12:11.395704');
INSERT INTO django_migrations VALUES(18,'admin','0004_auto_20190804_1625','2019-08-05 14:12:11.415826');
INSERT INTO django_migrations VALUES(19,'admin','0005_auto_20190805_1358','2019-08-05 14:12:11.433291');
INSERT INTO django_migrations VALUES(20,'sessions','0001_initial','2019-08-05 14:12:11.439058');
INSERT INTO django_migrations VALUES(21,'users','0002_chair_delegation','2019-08-06 11:19:31.029384');
INSERT INTO django_migrations VALUES(22,'users','0003_auto_20190806_1434','2019-08-06 14:35:02.754577');
INSERT INTO django_migrations VALUES(23,'delegation','0001_initial','2019-08-06 14:45:23.787844');
INSERT INTO django_migrations VALUES(24,'users','0004_delegation_delegation_contact_number','2019-08-08 07:33:05.727554');
INSERT INTO django_migrations VALUES(25,'delegation','0002_auto_20190808_0912','2019-08-08 09:12:19.107844');
INSERT INTO django_migrations VALUES(26,'delegation','0003_auto_20190808_0913','2019-08-08 09:14:03.063397');
INSERT INTO django_migrations VALUES(27,'secretariat','0001_initial','2019-08-09 13:50:14.169871');
INSERT INTO django_migrations VALUES(28,'secretariat','0002_auto_20190809_1400','2019-08-09 14:00:46.755764');
INSERT INTO django_migrations VALUES(29,'secretariat','0003_auto_20190809_1400','2019-08-09 14:00:46.779900');
INSERT INTO django_migrations VALUES(30,'secretariat','0004_logisticsrequest','2019-08-10 12:59:03.290996');
INSERT INTO django_migrations VALUES(31,'secretariat','0005_auto_20190810_1310','2019-08-10 13:10:38.081745');
INSERT INTO django_migrations VALUES(32,'secretariat','0006_chair','2019-08-12 08:20:34.278139');
INSERT INTO django_migrations VALUES(33,'users','0005_delete_chair','2019-08-12 08:20:34.286146');
INSERT INTO django_migrations VALUES(34,'secretariat','0007_auto_20190812_1422','2019-08-12 14:22:09.396016');
INSERT INTO django_migrations VALUES(35,'delegation','0004_auto_20190814_1513','2019-08-14 15:14:00.134487');
INSERT INTO django_migrations VALUES(36,'secretariat','0008_auto_20190814_1513','2019-08-14 15:14:00.154022');
INSERT INTO django_migrations VALUES(37,'delegation','0005_positionpaper','2019-08-16 11:26:41.108286');
INSERT INTO django_migrations VALUES(38,'secretariat','0009_auto_20190816_1126','2019-08-16 11:26:41.135783');
INSERT INTO django_migrations VALUES(39,'delegation','0006_auto_20190818_1046','2019-08-18 11:01:13.945819');
INSERT INTO django_migrations VALUES(40,'delegation','0007_auto_20190818_1109','2019-08-18 11:09:20.261329');
INSERT INTO django_migrations VALUES(41,'delegation','0008_auto_20190818_1118','2019-08-18 11:18:54.581442');
INSERT INTO django_migrations VALUES(42,'delegation','0009_auto_20190818_1123','2019-08-18 11:23:58.875196');
INSERT INTO django_migrations VALUES(43,'users','0006_auto_20190818_1144','2019-08-18 11:44:07.017464');
INSERT INTO django_migrations VALUES(44,'users','0007_auto_20190818_1149','2019-08-18 11:49:17.974980');
INSERT INTO django_migrations VALUES(45,'delegation','0010_auto_20190820_1525','2019-08-20 15:25:45.931216');
INSERT INTO django_migrations VALUES(46,'secretariat','0010_auto_20190902_1054','2019-09-02 10:54:49.440451');
CREATE TABLE IF NOT EXISTS "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
INSERT INTO django_content_type VALUES(1,'admin','logentry');
INSERT INTO django_content_type VALUES(2,'auth','permission');
INSERT INTO django_content_type VALUES(3,'auth','group');
INSERT INTO django_content_type VALUES(4,'contenttypes','contenttype');
INSERT INTO django_content_type VALUES(5,'sessions','session');
INSERT INTO django_content_type VALUES(6,'users','user');
INSERT INTO django_content_type VALUES(7,'users','chair');
INSERT INTO django_content_type VALUES(8,'users','delegation');
INSERT INTO django_content_type VALUES(9,'delegation','delegate');
INSERT INTO django_content_type VALUES(10,'delegation','countrycommitteeallocation');
INSERT INTO django_content_type VALUES(11,'delegation','committee');
INSERT INTO django_content_type VALUES(12,'delegation','country');
INSERT INTO django_content_type VALUES(13,'secretariat','progresssheet');
INSERT INTO django_content_type VALUES(14,'secretariat','logisticsrequest');
INSERT INTO django_content_type VALUES(15,'secretariat','chair');
INSERT INTO django_content_type VALUES(16,'delegation','positionpaper');
INSERT INTO django_content_type VALUES(17,'delegation','allocation');
CREATE TABLE IF NOT EXISTS "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
INSERT INTO auth_permission VALUES(1,1,'add_logentry','Can add log entry');
INSERT INTO auth_permission VALUES(2,1,'change_logentry','Can change log entry');
INSERT INTO auth_permission VALUES(3,1,'delete_logentry','Can delete log entry');
INSERT INTO auth_permission VALUES(4,1,'view_logentry','Can view log entry');
INSERT INTO auth_permission VALUES(5,2,'add_permission','Can add permission');
INSERT INTO auth_permission VALUES(6,2,'change_permission','Can change permission');
INSERT INTO auth_permission VALUES(7,2,'delete_permission','Can delete permission');
INSERT INTO auth_permission VALUES(8,2,'view_permission','Can view permission');
INSERT INTO auth_permission VALUES(9,3,'add_group','Can add group');
INSERT INTO auth_permission VALUES(10,3,'change_group','Can change group');
INSERT INTO auth_permission VALUES(11,3,'delete_group','Can delete group');
INSERT INTO auth_permission VALUES(12,3,'view_group','Can view group');
INSERT INTO auth_permission VALUES(13,4,'add_contenttype','Can add content type');
INSERT INTO auth_permission VALUES(14,4,'change_contenttype','Can change content type');
INSERT INTO auth_permission VALUES(15,4,'delete_contenttype','Can delete content type');
INSERT INTO auth_permission VALUES(16,4,'view_contenttype','Can view content type');
INSERT INTO auth_permission VALUES(17,5,'add_session','Can add session');
INSERT INTO auth_permission VALUES(18,5,'change_session','Can change session');
INSERT INTO auth_permission VALUES(19,5,'delete_session','Can delete session');
INSERT INTO auth_permission VALUES(20,5,'view_session','Can view session');
INSERT INTO auth_permission VALUES(21,6,'add_user','Can add user');
INSERT INTO auth_permission VALUES(22,6,'change_user','Can change user');
INSERT INTO auth_permission VALUES(23,6,'delete_user','Can delete user');
INSERT INTO auth_permission VALUES(24,6,'view_user','Can view user');
INSERT INTO auth_permission VALUES(25,7,'add_chair','Can add chair');
INSERT INTO auth_permission VALUES(26,7,'change_chair','Can change chair');
INSERT INTO auth_permission VALUES(27,7,'delete_chair','Can delete chair');
INSERT INTO auth_permission VALUES(28,7,'view_chair','Can view chair');
INSERT INTO auth_permission VALUES(29,8,'add_delegation','Can add delegation');
INSERT INTO auth_permission VALUES(30,8,'change_delegation','Can change delegation');
INSERT INTO auth_permission VALUES(31,8,'delete_delegation','Can delete delegation');
INSERT INTO auth_permission VALUES(32,8,'view_delegation','Can view delegation');
INSERT INTO auth_permission VALUES(33,9,'add_delegate','Can add delegate');
INSERT INTO auth_permission VALUES(34,9,'change_delegate','Can change delegate');
INSERT INTO auth_permission VALUES(35,9,'delete_delegate','Can delete delegate');
INSERT INTO auth_permission VALUES(36,9,'view_delegate','Can view delegate');
INSERT INTO auth_permission VALUES(37,10,'add_countrycommitteeallocation','Can add country committee allocation');
INSERT INTO auth_permission VALUES(38,10,'change_countrycommitteeallocation','Can change country committee allocation');
INSERT INTO auth_permission VALUES(39,10,'delete_countrycommitteeallocation','Can delete country committee allocation');
INSERT INTO auth_permission VALUES(40,10,'view_countrycommitteeallocation','Can view country committee allocation');
INSERT INTO auth_permission VALUES(41,11,'add_committee','Can add committee');
INSERT INTO auth_permission VALUES(42,11,'change_committee','Can change committee');
INSERT INTO auth_permission VALUES(43,11,'delete_committee','Can delete committee');
INSERT INTO auth_permission VALUES(44,11,'view_committee','Can view committee');
INSERT INTO auth_permission VALUES(45,12,'add_country','Can add country');
INSERT INTO auth_permission VALUES(46,12,'change_country','Can change country');
INSERT INTO auth_permission VALUES(47,12,'delete_country','Can delete country');
INSERT INTO auth_permission VALUES(48,12,'view_country','Can view country');
INSERT INTO auth_permission VALUES(49,13,'add_progresssheet','Can add progress sheet');
INSERT INTO auth_permission VALUES(50,13,'change_progresssheet','Can change progress sheet');
INSERT INTO auth_permission VALUES(51,13,'delete_progresssheet','Can delete progress sheet');
INSERT INTO auth_permission VALUES(52,13,'view_progresssheet','Can view progress sheet');
INSERT INTO auth_permission VALUES(53,14,'add_logisticsrequest','Can add logistics request');
INSERT INTO auth_permission VALUES(54,14,'change_logisticsrequest','Can change logistics request');
INSERT INTO auth_permission VALUES(55,14,'delete_logisticsrequest','Can delete logistics request');
INSERT INTO auth_permission VALUES(56,14,'view_logisticsrequest','Can view logistics request');
INSERT INTO auth_permission VALUES(57,15,'add_chair','Can add chair');
INSERT INTO auth_permission VALUES(58,15,'change_chair','Can change chair');
INSERT INTO auth_permission VALUES(59,15,'delete_chair','Can delete chair');
INSERT INTO auth_permission VALUES(60,15,'view_chair','Can view chair');
INSERT INTO auth_permission VALUES(61,16,'add_positionpaper','Can add position paper');
INSERT INTO auth_permission VALUES(62,16,'change_positionpaper','Can change position paper');
INSERT INTO auth_permission VALUES(63,16,'delete_positionpaper','Can delete position paper');
INSERT INTO auth_permission VALUES(64,16,'view_positionpaper','Can view position paper');
INSERT INTO auth_permission VALUES(65,17,'add_allocation','Can add allocation');
INSERT INTO auth_permission VALUES(66,17,'change_allocation','Can change allocation');
INSERT INTO auth_permission VALUES(67,17,'delete_allocation','Can delete allocation');
INSERT INTO auth_permission VALUES(68,17,'view_allocation','Can view allocation');
CREATE TABLE IF NOT EXISTS "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS "users_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "users_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "action_time" datetime NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO django_admin_log VALUES(1,'2019-08-05 14:16:15.981803','2','sachit1',1,'[{"added": {}}]',6,1);
INSERT INTO django_admin_log VALUES(2,'2019-08-06 11:02:48.035877','3','sachit2',1,'[{"added": {}}]',6,1);
INSERT INTO django_admin_log VALUES(3,'2019-08-06 11:19:41.306898','2','sachit1',3,'',6,1);
INSERT INTO django_admin_log VALUES(4,'2019-08-06 11:19:41.312657','3','sachit2',3,'',6,1);
INSERT INTO django_admin_log VALUES(5,'2019-08-06 11:36:55.268904','1','Dubai College',1,'[{"added": {}}]',8,1);
INSERT INTO django_admin_log VALUES(6,'2019-08-06 11:37:15.429530','1','sachit',2,'[{"changed": {"fields": ["is_delegation"]}}]',6,1);
INSERT INTO django_admin_log VALUES(7,'2019-08-06 14:58:09.567766','1','UNSC',1,'[{"added": {}}]',11,1);
INSERT INTO django_admin_log VALUES(8,'2019-08-06 14:58:12.979815','2','UNHRC',1,'[{"added": {}}]',11,1);
INSERT INTO django_admin_log VALUES(9,'2019-08-06 14:58:19.360646','3','ECOSOC',1,'[{"added": {}}]',11,1);
INSERT INTO django_admin_log VALUES(10,'2019-08-06 14:58:26.884405','1','USA',1,'[{"added": {}}]',12,1);
INSERT INTO django_admin_log VALUES(11,'2019-08-06 14:58:29.517742','2','UK',1,'[{"added": {}}]',12,1);
INSERT INTO django_admin_log VALUES(12,'2019-08-06 14:58:35.939798','3','China',1,'[{"added": {}}]',12,1);
INSERT INTO django_admin_log VALUES(13,'2019-08-07 11:59:52.489039','4','abc',3,'',6,1);
INSERT INTO django_admin_log VALUES(14,'2019-08-08 08:52:13.185193','6','sachit2',2,'[{"changed": {"fields": ["password"]}}]',6,1);
INSERT INTO django_admin_log VALUES(15,'2019-08-08 09:01:12.141386','6','sachit2',2,'[{"changed": {"fields": ["password"]}}]',6,1);
INSERT INTO django_admin_log VALUES(16,'2019-08-08 09:11:36.971512','4','ECOSOC',1,'[{"added": {}}]',11,1);
INSERT INTO django_admin_log VALUES(17,'2019-08-08 09:11:44.333785','4','ECOSOC',3,'',11,1);
INSERT INTO django_admin_log VALUES(18,'2019-08-09 06:34:12.959415','1','sachit',2,'[{"changed": {"fields": ["is_chair", "is_secretariat"]}}]',6,1);
INSERT INTO django_admin_log VALUES(19,'2019-08-09 13:36:04.973468','7','chair1',1,'[{"added": {}}]',6,1);
INSERT INTO django_admin_log VALUES(20,'2019-08-09 13:37:13.604734','7','chair1',2,'[{"changed": {"fields": ["is_staff"]}}]',6,1);
INSERT INTO django_admin_log VALUES(21,'2019-08-09 14:01:02.595747','1','ProgressSheet object (1)',1,'[{"added": {}}]',13,1);
INSERT INTO django_admin_log VALUES(22,'2019-08-10 07:54:26.456912','2','Progress Sheet: UNHRC',1,'[{"added": {}}]',13,1);
INSERT INTO django_admin_log VALUES(23,'2019-08-10 07:56:50.925222','2','Progress Sheet: UNHRC',2,'[{"changed": {"fields": ["data"]}}]',13,1);
INSERT INTO django_admin_log VALUES(24,'2019-08-10 08:00:54.080505','2','Progress Sheet: UNHRC',2,'[{"changed": {"fields": ["data"]}}]',13,1);
INSERT INTO django_admin_log VALUES(25,'2019-08-10 12:33:57.298314','1','UNHRC-UK',1,'[{"added": {}}]',10,1);
INSERT INTO django_admin_log VALUES(26,'2019-08-10 16:17:22.087509','1','LogisticsRequest object (1)',1,'[{"added": {}}]',14,1);
INSERT INTO django_admin_log VALUES(27,'2019-08-12 08:21:00.395398','7','chair1',3,'',6,1);
INSERT INTO django_admin_log VALUES(28,'2019-08-12 08:21:00.399367','8','chair2',3,'',6,1);
INSERT INTO django_admin_log VALUES(29,'2019-08-12 08:21:00.402715','6','sachit2',3,'',6,1);
INSERT INTO django_admin_log VALUES(30,'2019-08-12 08:21:00.405685','5','sachit3',3,'',6,1);
INSERT INTO django_admin_log VALUES(31,'2019-08-12 08:22:07.571845','9','chair1',3,'',6,1);
INSERT INTO django_admin_log VALUES(32,'2019-08-12 13:44:26.514495','2','Chair: sachit - UNSC',1,'[{"added": {}}]',15,1);
INSERT INTO django_admin_log VALUES(33,'2019-08-12 13:44:44.789598','2','Request: UNSC - 2019-08-12 13:44:43+00:00',1,'[{"added": {}}]',14,1);
INSERT INTO django_admin_log VALUES(34,'2019-08-14 15:14:43.492992','3','Progress Sheet: UNSC',1,'[{"added": {}}]',13,1);
INSERT INTO django_admin_log VALUES(35,'2019-08-17 21:06:30.660724','2','Chair: sachit - UNHRC',2,'[{"changed": {"fields": ["committee"]}}]',15,1);
INSERT INTO django_admin_log VALUES(36,'2019-08-18 16:05:38.516212','2','UNSC-USA',1,'[{"added": {}}]',17,1);
INSERT INTO django_admin_log VALUES(37,'2019-08-19 19:36:49.638501','2','UNSC-USA',2,'[{"changed": {"fields": ["delegate"]}}]',17,1);
INSERT INTO django_admin_log VALUES(38,'2019-08-19 19:38:46.073642','2','UNSC-USA',2,'[{"changed": {"fields": ["delegate"]}}]',17,1);
INSERT INTO django_admin_log VALUES(39,'2019-08-26 13:40:53.710918','3','DISEC-USA',1,'[{"added": {}}]',17,1);
INSERT INTO django_admin_log VALUES(40,'2019-09-01 07:36:22.598382','11','del1',3,'',6,1);
INSERT INTO django_admin_log VALUES(41,'2019-09-02 10:23:27.628260','2','Progress Sheet: UNHRC',2,'[{"changed": {"fields": ["data"]}}]',13,1);
INSERT INTO django_admin_log VALUES(42,'2019-09-02 10:24:50.026233','2','Progress Sheet: UNHRC',2,'[{"changed": {"fields": ["data"]}}]',13,1);
INSERT INTO django_admin_log VALUES(43,'2019-09-02 10:25:25.110212','2','Progress Sheet: UNHRC',2,'[{"changed": {"fields": ["data"]}}]',13,1);
INSERT INTO django_admin_log VALUES(44,'2019-09-04 05:32:37.962415','6','Nigeria',1,'[{"added": {}}]',12,1);
INSERT INTO django_admin_log VALUES(45,'2019-09-04 05:32:40.518895','4','UNSC-Nigeria',1,'[{"added": {}}]',17,1);
INSERT INTO django_admin_log VALUES(46,'2019-09-10 17:34:34.176162','2','Position Paper: Kaivalya Vohra - 2019-08-21 16:08:27.978755+00:00',3,'',16,1);
INSERT INTO django_admin_log VALUES(47,'2019-09-10 18:33:45.265801','5','DISEC-India',1,'[{"added": {}}]',17,1);
INSERT INTO django_admin_log VALUES(48,'2019-09-12 08:06:13.933065','7','Oman',1,'[{"added": {}}]',12,1);
INSERT INTO django_admin_log VALUES(49,'2019-09-12 08:06:36.186629','6','DISEC-Oman',1,'[{"added": {}}]',17,1);
INSERT INTO django_admin_log VALUES(50,'2019-09-19 08:34:17.274904','3','Position Paper: Kaivalya Vohra - 2019-09-19 08:27:20.262962+00:00',3,'',16,1);
INSERT INTO django_admin_log VALUES(51,'2019-09-20 08:26:12.208391','7','UNHRC-Germany',1,'[{"added": {}}]',17,1);
INSERT INTO django_admin_log VALUES(52,'2019-09-20 08:28:35.084984','8','UNHRC-China',1,'[{"added": {}}]',17,1);
INSERT INTO django_admin_log VALUES(53,'2019-09-20 08:28:41.588632','8','Belguim',1,'[{"added": {}}]',12,1);
INSERT INTO django_admin_log VALUES(54,'2019-09-20 08:28:43.984726','9','UNHRC-Belguim',1,'[{"added": {}}]',17,1);
CREATE TABLE IF NOT EXISTS "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
INSERT INTO django_session VALUES('mpkqwomaiy1zlikuqodd3ik38me0u7ir','ZjczNjg3YjJkMDFlMWQ3MTdiYmI1YzhlNjg3MzI1NzU0NzEyZTg1Yjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmMDE5ZDgzOGQ4NmJmNTY5YTdlNjllYTc3Y2RkOWU2NjUzZWVmYzNiIn0=','2019-08-20 14:04:50.685567');
INSERT INTO django_session VALUES('cj6mhewt1ho9k0yfbl7pgno8s4y3is4m','MTdmNWRjZDAyYWY5YjJlNGE1ZmQ4MGZjNzlhNDM2YWIyOWFhZDUwMjp7Il9hdXRoX3VzZXJfaWQiOiI2IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxNDYzOWY4YjVjZjBiZjljMzMxNGI4MGZkNjczYTlmMWE5NGMyMzYzIn0=','2019-08-22 08:29:16.416054');
INSERT INTO django_session VALUES('gqr69qw2rtx6v53z4ajuq0n03ab4f3ax','NDI1NjFmNzAyN2QyNDk5ZWJlMzNlMjdhNjRjN2MyNGMxMmRkOGY2MTp7Il9hdXRoX3VzZXJfaWQiOiI2IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4N2U1ZDMwMTAwYzI0ODFjY2RmMTg2MDhkYTM2MjU3Y2EzZmNjMmE5In0=','2019-08-22 08:53:11.126490');
INSERT INTO django_session VALUES('qi5zu1iiqe78i3jm6gn5pb3pct54fnaf','NzJiNzAxMmQyMGJiZTYwOGM4MDcyNTZhZjVkNzVhYzM1OTk5NDM0YTp7Il9hdXRoX3VzZXJfaWQiOiI2IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjM2Q1NjllOWI4NWVjNDJkMTk4OGQ5M2FjZDM1ODY5MGNjOGZmZDZmIn0=','2019-08-22 09:01:45.883513');
INSERT INTO django_session VALUES('7oe1x78kx57rkwbd6rm9x8xzc1qexf4e','ZGYwZDI1ZTg3ZmM3ZTYxYjkxMWEzYjQ5YWRiZmNmYzQ1OTMyOTMxNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjNjlmYjc2OTRhNWMzNmNiYTA5YjA2ZGFlNTBhYWMzOWMzNDc2ZmU2In0=','2019-09-28 05:04:00.161206');
INSERT INTO django_session VALUES('v7nj9k5krh9b1lg3kmjv7cd70dr4a7oo','ZGYwZDI1ZTg3ZmM3ZTYxYjkxMWEzYjQ5YWRiZmNmYzQ1OTMyOTMxNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjNjlmYjc2OTRhNWMzNmNiYTA5YjA2ZGFlNTBhYWMzOWMzNDc2ZmU2In0=','2019-10-09 06:39:49.772786');
CREATE TABLE IF NOT EXISTS "users_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "last_name" varchar(150) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "is_delegation" bool NOT NULL, "is_chair" bool NOT NULL, "is_secretariat" bool NOT NULL, "email" varchar(254) NOT NULL UNIQUE);
INSERT INTO users_user VALUES(1,'pbkdf2_sha256$150000$7HBlVhtqAVBb$uJo8OdjHmU/d3IcVMopI6E+e2PlfNNtbB3qQa24sDXs=','2019-09-25 06:39:49.768782',1,'sachit','Sachit','Lumba',1,1,'2019-08-05 14:13:05.747543',1,1,1,'sachitlumba@gmail.com');
INSERT INTO users_user VALUES(10,'pbkdf2_sha256$150000$Sq3WnUhlCvNo$577lFoB0IGwR0oog3Gl93Iwqw1EzE/YVJfM8S/PQQv4=','2019-08-14 15:18:40.474197',0,'chair1','','',0,1,'2019-08-12 08:22:24.704196',0,1,0,'abc@gmail.com');
INSERT INTO users_user VALUES(12,'pbkdf2_sha256$150000$bRd2QBGGO7kK$dRigFcVMDaQAcP2EKKht42lGmrdbq+iorblw6ZrDixo=','2019-09-25 06:38:55.135172',0,'delegation1','Seyhan van','Khan',0,1,'2019-08-29 11:58:05.754282',1,0,0,'email@gmail.com');
CREATE TABLE IF NOT EXISTS "delegation_committee" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(200) NOT NULL UNIQUE);
INSERT INTO delegation_committee VALUES(1,'UNSC');
INSERT INTO delegation_committee VALUES(2,'UNHRC');
INSERT INTO delegation_committee VALUES(3,'ECOSOC');
INSERT INTO delegation_committee VALUES(4,'DISEC');
CREATE TABLE IF NOT EXISTS "delegation_country" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(200) NOT NULL UNIQUE);
INSERT INTO delegation_country VALUES(1,'USA');
INSERT INTO delegation_country VALUES(2,'UK');
INSERT INTO delegation_country VALUES(3,'China');
INSERT INTO delegation_country VALUES(4,'Germany');
INSERT INTO delegation_country VALUES(5,'India');
INSERT INTO delegation_country VALUES(6,'Nigeria');
INSERT INTO delegation_country VALUES(7,'Oman');
INSERT INTO delegation_country VALUES(8,'Belguim');
CREATE TABLE IF NOT EXISTS "secretariat_chair" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "committee_id" integer NULL REFERENCES "delegation_committee" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL UNIQUE REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO secretariat_chair VALUES(1,2,10);
INSERT INTO secretariat_chair VALUES(2,2,1);
CREATE TABLE IF NOT EXISTS "delegation_positionpaper" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "document" varchar(100) NOT NULL, "uploaded_at" datetime NOT NULL, "delegate_id" integer NOT NULL UNIQUE REFERENCES "delegation_delegate" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO delegation_positionpaper VALUES(1,'documents/unwomen_1_lcl14Ic.pdf','2019-08-16 11:29:47.807145',3);
CREATE TABLE IF NOT EXISTS "secretariat_logisticsrequest" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "description" varchar(200) NOT NULL, "committee_id" integer NOT NULL REFERENCES "delegation_committee" ("id") DEFERRABLE INITIALLY DEFERRED, "completed" bool NOT NULL, "timestamp" datetime NOT NULL);
INSERT INTO secretariat_logisticsrequest VALUES(1,'Water required',3,1,'2019-08-10 16:16:10');
INSERT INTO secretariat_logisticsrequest VALUES(2,'Wifi Issue',1,1,'2019-08-12 13:44:43');
INSERT INTO secretariat_logisticsrequest VALUES(3,'Water bottles',1,1,'2019-08-12 14:22:18.193853');
INSERT INTO secretariat_logisticsrequest VALUES(8,'Test',1,1,'2019-08-14 10:55:18.523935');
INSERT INTO secretariat_logisticsrequest VALUES(10,'Yee',1,0,'2019-08-16 11:31:54.443747');
INSERT INTO secretariat_logisticsrequest VALUES(11,'a',1,0,'2019-08-16 11:32:06.601293');
CREATE TABLE IF NOT EXISTS "delegation_allocation" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "committee_id" integer NOT NULL REFERENCES "delegation_committee" ("id") DEFERRABLE INITIALLY DEFERRED, "delegate_id" integer NULL UNIQUE REFERENCES "delegation_delegate" ("id") DEFERRABLE INITIALLY DEFERRED, "country_id" integer NOT NULL REFERENCES "delegation_country" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO delegation_allocation VALUES(1,2,3,2);
INSERT INTO delegation_allocation VALUES(2,1,NULL,1);
INSERT INTO delegation_allocation VALUES(3,4,NULL,1);
INSERT INTO delegation_allocation VALUES(4,1,NULL,6);
INSERT INTO delegation_allocation VALUES(5,4,NULL,5);
INSERT INTO delegation_allocation VALUES(6,4,NULL,7);
INSERT INTO delegation_allocation VALUES(7,2,NULL,4);
INSERT INTO delegation_allocation VALUES(8,2,NULL,3);
INSERT INTO delegation_allocation VALUES(9,2,NULL,8);
CREATE TABLE IF NOT EXISTS "delegation_delegate" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(200) NOT NULL, "last_name" varchar(200) NOT NULL, "email" varchar(254) NOT NULL UNIQUE, "dob" date NULL, "committee_preference_id" integer NULL REFERENCES "delegation_committee" ("id") DEFERRABLE INITIALLY DEFERRED, "country_preference_id" integer NULL REFERENCES "delegation_country" ("id") DEFERRABLE INITIALLY DEFERRED, "delegation_id" integer NOT NULL REFERENCES "users_delegation" ("id") DEFERRABLE INITIALLY DEFERRED, "past_conferences" integer NULL);
INSERT INTO delegation_delegate VALUES(3,'Sachit','Lumba','sachitlumba@gmail.com','2001-08-28',2,2,1,9);
INSERT INTO delegation_delegate VALUES(4,'Kaivalya','Vohra','kaivalya8111@dubaicollege.org','2001-04-03',1,1,1,2);
INSERT INTO delegation_delegate VALUES(5,'Jai','Hindocha','jai@gmail.com','2002-08-05',1,3,1,0);
INSERT INTO delegation_delegate VALUES(6,'John','Doe','johndoe@gmail.com','2001-01-01',2,6,5,4);
INSERT INTO delegation_delegate VALUES(9,'Samar','Aswani','Samar@gmail.com','2002-08-23',1,5,1,3);
CREATE TABLE IF NOT EXISTS "users_delegation" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(200) NULL, "user_id" integer NOT NULL UNIQUE REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "contact_number" varchar(200) NULL, "size" integer NOT NULL);
INSERT INTO users_delegation VALUES(1,'Dubai College',1,'+971561138064',4);
INSERT INTO users_delegation VALUES(5,'Test Delegation',12,'+971561234567',9);
CREATE TABLE IF NOT EXISTS "secretariat_progresssheet" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "committee_id" integer NOT NULL UNIQUE REFERENCES "delegation_committee" ("id") DEFERRABLE INITIALLY DEFERRED, "data" text NULL);
INSERT INTO secretariat_progresssheet VALUES(1,3,'<p>h</p>');
INSERT INTO secretariat_progresssheet VALUES(2,2,replace(replace('<p><span style="font-family: ''Open Sans'', Arial, sans-serif; text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse a facilisis dui. Maecenas ornare erat vel arcu mollis efficitur. Integer sodales mattis eros, vitae fermentum sem tincidunt in. Pellentesque quis est ut mauris rutrum eleifend. Phasellus lobortis dolor id metus pretium maximus. Suspendisse ipsum ipsum, accumsan consectetur nunc pellentesque, vestibulum pulvinar metus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed commodo leo in nisi tempor blandit. Proin auctor leo ligula, sed pharetra tellus tincidunt sed. In sed est ut tortor volutpat iaculis vitae nec ante. Phasellus vitae mi posuere, ultricies quam a, ornare dui. Duis ultrices ornare bibendum.</span></p>\r\n<p>&nbsp;</p>\r\n<pre class="language-python"><code>print("Sup KV")</code></pre>','\r',char(13)),'\n',char(10)));
INSERT INTO secretariat_progresssheet VALUES(3,1,'dsjkhjk');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('django_migrations',46);
INSERT INTO sqlite_sequence VALUES('django_content_type',17);
INSERT INTO sqlite_sequence VALUES('auth_permission',68);
INSERT INTO sqlite_sequence VALUES('auth_group',0);
INSERT INTO sqlite_sequence VALUES('django_admin_log',54);
INSERT INTO sqlite_sequence VALUES('users_user',12);
INSERT INTO sqlite_sequence VALUES('delegation_committee',4);
INSERT INTO sqlite_sequence VALUES('delegation_country',8);
INSERT INTO sqlite_sequence VALUES('secretariat_chair',2);
INSERT INTO sqlite_sequence VALUES('secretariat_logisticsrequest',12);
INSERT INTO sqlite_sequence VALUES('delegation_positionpaper',3);
INSERT INTO sqlite_sequence VALUES('delegation_allocation',9);
INSERT INTO sqlite_sequence VALUES('delegation_delegate',9);
INSERT INTO sqlite_sequence VALUES('users_delegation',5);
INSERT INTO sqlite_sequence VALUES('secretariat_progresssheet',3);
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE UNIQUE INDEX "users_user_groups_user_id_group_id_b88eab82_uniq" ON "users_user_groups" ("user_id", "group_id");
CREATE INDEX "users_user_groups_user_id_5f6f5a90" ON "users_user_groups" ("user_id");
CREATE INDEX "users_user_groups_group_id_9afc8d0e" ON "users_user_groups" ("group_id");
CREATE UNIQUE INDEX "users_user_user_permissions_user_id_permission_id_43338c45_uniq" ON "users_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "users_user_user_permissions_user_id_20aca447" ON "users_user_user_permissions" ("user_id");
CREATE INDEX "users_user_user_permissions_permission_id_0b93982e" ON "users_user_user_permissions" ("permission_id");
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
CREATE INDEX "secretariat_chair_committee_id_0dd18197" ON "secretariat_chair" ("committee_id");
CREATE INDEX "secretariat_logisticsrequest_committee_id_a025ec53" ON "secretariat_logisticsrequest" ("committee_id");
CREATE UNIQUE INDEX "delegation_allocation_country_id_committee_id_214b3598_uniq" ON "delegation_allocation" ("country_id", "committee_id");
CREATE INDEX "delegation_allocation_committee_id_8547940a" ON "delegation_allocation" ("committee_id");
CREATE INDEX "delegation_allocation_country_id_58806bab" ON "delegation_allocation" ("country_id");
CREATE INDEX "delegation_delegate_committee_preference_id_61dd6d9e" ON "delegation_delegate" ("committee_preference_id");
CREATE INDEX "delegation_delegate_country_preference_id_136f470f" ON "delegation_delegate" ("country_preference_id");
CREATE INDEX "delegation_delegate_delegation_id_5f923783" ON "delegation_delegate" ("delegation_id");
COMMIT;