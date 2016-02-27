USE citadel;

SET sql_mode='NO_BACKSLASH_ESCAPES';
CREATE TABLE `django_migrations` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `app` varchar(255) NOT NULL, `name` varchar(255) NOT NULL, `applied` datetime NOT NULL);

INSERT INTO `django_migrations` VALUES(1,'contenttypes','0001_initial','2016-02-27 17:07:55.884000');

INSERT INTO `django_migrations` VALUES(2,'auth','0001_initial','2016-02-27 17:07:56.114000');

INSERT INTO `django_migrations` VALUES(3,'Citadel','0001_initial','2016-02-27 17:07:56.356000');

INSERT INTO `django_migrations` VALUES(4,'admin','0001_initial','2016-02-27 17:07:56.571000');

INSERT INTO `django_migrations` VALUES(5,'admin','0002_logentry_remove_auto_add','2016-02-27 17:07:56.811000');

INSERT INTO `django_migrations` VALUES(6,'contenttypes','0002_remove_content_type_name','2016-02-27 17:07:57.063000');

INSERT INTO `django_migrations` VALUES(7,'auth','0002_alter_permission_name_max_length','2016-02-27 17:07:57.338000');

INSERT INTO `django_migrations` VALUES(8,'auth','0003_alter_user_email_max_length','2016-02-27 17:07:57.590000');

INSERT INTO `django_migrations` VALUES(9,'auth','0004_alter_user_username_opts','2016-02-27 17:07:57.849000');

INSERT INTO `django_migrations` VALUES(10,'auth','0005_alter_user_last_login_null','2016-02-27 17:07:58.113000');

INSERT INTO `django_migrations` VALUES(11,'auth','0006_require_contenttypes_0002','2016-02-27 17:07:58.265000');

INSERT INTO `django_migrations` VALUES(12,'auth','0007_alter_validators_add_error_messages','2016-02-27 17:07:58.547000');

INSERT INTO `django_migrations` VALUES(13,'captcha','0001_initial','2016-02-27 17:07:58.763000');

INSERT INTO `django_migrations` VALUES(14,'registration','0001_initial','2016-02-27 17:07:59.004000');

INSERT INTO `django_migrations` VALUES(15,'registration','0002_registrationprofile_activated','2016-02-27 17:07:59.239000');

INSERT INTO `django_migrations` VALUES(16,'registration','0003_migrate_activatedstatus','2016-02-27 17:07:59.342000');

INSERT INTO `django_migrations` VALUES(17,'sessions','0001_initial','2016-02-27 17:07:59.572000');

INSERT INTO `django_migrations` VALUES(18,'Citadel','0002_auto_20160227_1946','2016-02-27 19:55:23.245000');

CREATE TABLE `auth_group` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `name` varchar(80) NOT NULL UNIQUE);

CREATE TABLE `auth_group_permissions` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `group_id` integer NOT NULL REFERENCES `auth_group` (`id`), `permission_id` integer NOT NULL REFERENCES `auth_permission` (`id`));

CREATE TABLE `auth_user_groups` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `user_id` integer NOT NULL REFERENCES `auth_user` (`id`), `group_id` integer NOT NULL REFERENCES `auth_group` (`id`));

CREATE TABLE `auth_user_user_permissions` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `user_id` integer NOT NULL REFERENCES `auth_user` (`id`), `permission_id` integer NOT NULL REFERENCES `auth_permission` (`id`));

CREATE TABLE `Citadel_newsmessage` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `message` varchar(2048) NOT NULL, `time` datetime NOT NULL, `poster_id` integer NOT NULL REFERENCES `auth_user` (`id`));

CREATE TABLE `django_admin_log` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `object_id` text NULL, `object_repr` varchar(200) NOT NULL, `action_flag` smallint unsigned NOT NULL, `change_message` text NOT NULL, `content_type_id` integer NULL REFERENCES `django_content_type` (`id`), `user_id` integer NOT NULL REFERENCES `auth_user` (`id`), `action_time` datetime NOT NULL);

CREATE TABLE `django_content_type` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `app_label` varchar(100) NOT NULL, `model` varchar(100) NOT NULL);

INSERT INTO `django_content_type` VALUES(1,'admin','logentry');

INSERT INTO `django_content_type` VALUES(2,'auth','permission');

INSERT INTO `django_content_type` VALUES(3,'auth','group');

INSERT INTO `django_content_type` VALUES(4,'auth','user');

INSERT INTO `django_content_type` VALUES(5,'contenttypes','contenttype');

INSERT INTO `django_content_type` VALUES(6,'sessions','session');

INSERT INTO `django_content_type` VALUES(7,'registration','registrationprofile');

INSERT INTO `django_content_type` VALUES(8,'Citadel','userprofile');

INSERT INTO `django_content_type` VALUES(9,'Citadel','bankingdetails');

INSERT INTO `django_content_type` VALUES(10,'Citadel','newsmessage');

INSERT INTO `django_content_type` VALUES(11,'captcha','captchastore');

CREATE TABLE `auth_permission` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `content_type_id` integer NOT NULL REFERENCES `django_content_type` (`id`), `codename` varchar(100) NOT NULL, `name` varchar(255) NOT NULL);

INSERT INTO `auth_permission` VALUES(1,1,'add_logentry','Can add log entry');

INSERT INTO `auth_permission` VALUES(2,1,'change_logentry','Can change log entry');

INSERT INTO `auth_permission` VALUES(3,1,'delete_logentry','Can delete log entry');

INSERT INTO `auth_permission` VALUES(4,2,'add_permission','Can add permission');

INSERT INTO `auth_permission` VALUES(5,2,'change_permission','Can change permission');

INSERT INTO `auth_permission` VALUES(6,2,'delete_permission','Can delete permission');

INSERT INTO `auth_permission` VALUES(7,3,'add_group','Can add group');

INSERT INTO `auth_permission` VALUES(8,3,'change_group','Can change group');

INSERT INTO `auth_permission` VALUES(9,3,'delete_group','Can delete group');

INSERT INTO `auth_permission` VALUES(10,4,'add_user','Can add user');

INSERT INTO `auth_permission` VALUES(11,4,'change_user','Can change user');

INSERT INTO `auth_permission` VALUES(12,4,'delete_user','Can delete user');

INSERT INTO `auth_permission` VALUES(13,5,'add_contenttype','Can add content type');

INSERT INTO `auth_permission` VALUES(14,5,'change_contenttype','Can change content type');

INSERT INTO `auth_permission` VALUES(15,5,'delete_contenttype','Can delete content type');

INSERT INTO `auth_permission` VALUES(16,6,'add_session','Can add session');

INSERT INTO `auth_permission` VALUES(17,6,'change_session','Can change session');

INSERT INTO `auth_permission` VALUES(18,6,'delete_session','Can delete session');

INSERT INTO `auth_permission` VALUES(19,7,'add_registrationprofile','Can add registration profile');

INSERT INTO `auth_permission` VALUES(20,7,'change_registrationprofile','Can change registration profile');

INSERT INTO `auth_permission` VALUES(21,7,'delete_registrationprofile','Can delete registration profile');

INSERT INTO `auth_permission` VALUES(22,8,'add_userprofile','Can add user profile');

INSERT INTO `auth_permission` VALUES(23,8,'change_userprofile','Can change user profile');

INSERT INTO `auth_permission` VALUES(24,8,'delete_userprofile','Can delete user profile');

INSERT INTO `auth_permission` VALUES(25,9,'add_bankingdetails','Can add banking details');

INSERT INTO `auth_permission` VALUES(26,9,'change_bankingdetails','Can change banking details');

INSERT INTO `auth_permission` VALUES(27,9,'delete_bankingdetails','Can delete banking details');

INSERT INTO `auth_permission` VALUES(28,10,'add_newsmessage','Can add news message');

INSERT INTO `auth_permission` VALUES(29,10,'change_newsmessage','Can change news message');

INSERT INTO `auth_permission` VALUES(30,10,'delete_newsmessage','Can delete news message');

INSERT INTO `auth_permission` VALUES(31,11,'add_captchastore','Can add captcha store');

INSERT INTO `auth_permission` VALUES(32,11,'change_captchastore','Can change captcha store');

INSERT INTO `auth_permission` VALUES(33,11,'delete_captchastore','Can delete captcha store');

CREATE TABLE `auth_user` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `password` varchar(128) NOT NULL, `last_login` datetime NULL, `is_superuser` bool NOT NULL, `first_name` varchar(30) NOT NULL, `last_name` varchar(30) NOT NULL, `email` varchar(254) NOT NULL, `is_staff` bool NOT NULL, `is_active` bool NOT NULL, `date_joined` datetime NOT NULL, `username` varchar(30) NOT NULL UNIQUE);

INSERT INTO `auth_user` VALUES(1,'pbkdf2_sha256$24000$Pogve2kdY8md$cfd+57iwdYMg0+sSSDtNMCMP6WRdXpx4RLaAi3+OMks=','2016-02-27 18:07:50.279000',0,'','','please@dont-hack.me',0,1,'2016-02-27 18:07:43.088000','pablo');

INSERT INTO `auth_user` VALUES(2,'pbkdf2_sha256$24000$Wg36fwcn7Lpx$eiptdHta5QGKNa4IeqGoyUHKUk9k11AgJBRsPl6C9l4=',NULL,0,'','','please@dont-hack.me',0,1,'2016-02-27 18:31:24.010000','pdhm');

INSERT INTO `auth_user` VALUES(3,'pbkdf2_sha256$24000$S99qH7SZQDbk$mnouDD4KZle8OiJc3yDDXXgte9hHd1j61cBAKc+9BKw=',NULL,0,'','','d@d.com',0,1,'2016-02-27 18:40:47.936000','C');

INSERT INTO `auth_user` VALUES(4,'pbkdf2_sha256$24000$4AOpXPTidzMC$u7b8vuOMkiz2kBPIFJiEshuffj8yiH/AAf3UVIr/cA0=',NULL,0,'','','d@a.com',0,1,'2016-02-27 19:57:14.203000','CCC');

INSERT INTO `auth_user` VALUES(5,'ASDASD',NULL,0,'','','a@b.com',0,1,'2016-02-27 20:00:05.768000','KASD');

INSERT INTO `auth_user` VALUES(6,'AA',NULL,0,'','','pa@b.com',0,1,'2016-02-27 20:01:31.612000','aiosdnoaisjd');

INSERT INTO `auth_user` VALUES(7,'pbkdf2_sha256$24000$TRyMOrMUlwwT$ds7ndJ03Ewy2je8IVKi/go5rEoCTtBk6FYt7mfeS1uo=',NULL,0,'','','a@b.com',0,1,'2016-02-27 20:02:13.581000','asasdw');

INSERT INTO `auth_user` VALUES(8,'pbkdf2_sha256$24000$lkr3CmgKKvaA$mvEMuPZ4NIzNqM+tclr065twALG1vhnCU3iH4czzVFY=',NULL,0,'','','a@b.com',0,1,'2016-02-27 20:07:07.018000','papapapa');

CREATE TABLE `captcha_captchastore` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `challenge` varchar(32) NOT NULL, `response` varchar(32) NOT NULL, `hashkey` varchar(40) NOT NULL UNIQUE, `expiration` datetime NOT NULL);

CREATE TABLE `registration_registrationprofile` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `activation_key` varchar(40) NOT NULL, `user_id` integer NOT NULL UNIQUE REFERENCES `auth_user` (`id`), `activated` bool NOT NULL);

CREATE TABLE `django_session` (`session_key` varchar(40) NOT NULL PRIMARY KEY, `session_data` text NOT NULL, `expire_date` datetime NOT NULL);

CREATE TABLE `Citadel_bankingdetails` (`Balance` decimal NOT NULL, `user_id` integer NOT NULL PRIMARY KEY REFERENCES `Citadel_userprofile` (`id`));

CREATE TABLE `Citadel_userprofile` (`name` varchar(64) NOT NULL, `surname` varchar(128) NOT NULL, `user_id` integer NOT NULL PRIMARY KEY REFERENCES `auth_user` (`id`));

INSERT INTO `Citadel_userprofile` VALUES('OII','OII',1);

CREATE UNIQUE INDEX `auth_group_permissions_group_id_0cd325b0_uniq` ON `auth_group_permissions` (`group_id`, `permission_id`);

CREATE INDEX `auth_group_permissions_0e939a4f` ON `auth_group_permissions` (`group_id`);

CREATE INDEX `auth_group_permissions_8373b171` ON `auth_group_permissions` (`permission_id`);

CREATE UNIQUE INDEX `auth_user_groups_user_id_94350c0c_uniq` ON `auth_user_groups` (`user_id`, `group_id`);

CREATE INDEX `auth_user_groups_e8701ad4` ON `auth_user_groups` (`user_id`);

CREATE INDEX `auth_user_groups_0e939a4f` ON `auth_user_groups` (`group_id`);

CREATE UNIQUE INDEX `auth_user_user_permissions_user_id_14a6b632_uniq` ON `auth_user_user_permissions` (`user_id`, `permission_id`);

CREATE INDEX `auth_user_user_permissions_e8701ad4` ON `auth_user_user_permissions` (`user_id`);

CREATE INDEX `auth_user_user_permissions_8373b171` ON `auth_user_user_permissions` (`permission_id`);

CREATE INDEX `Citadel_newsmessage_9b86e5fe` ON `Citadel_newsmessage` (`poster_id`);

CREATE INDEX `django_admin_log_417f1b1c` ON `django_admin_log` (`content_type_id`);

CREATE INDEX `django_admin_log_e8701ad4` ON `django_admin_log` (`user_id`);

CREATE UNIQUE INDEX `django_content_type_app_label_76bd3d3b_uniq` ON `django_content_type` (`app_label`, `model`);

CREATE UNIQUE INDEX `auth_permission_content_type_id_01ab375a_uniq` ON `auth_permission` (`content_type_id`, `codename`);

CREATE INDEX `auth_permission_417f1b1c` ON `auth_permission` (`content_type_id`);

CREATE INDEX `django_session_de54fa62` ON `django_session` (`expire_date`);

