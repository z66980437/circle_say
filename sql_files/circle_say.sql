/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2019\1\29 ÐÇÆÚ¶þ 6:35:26                        */
/*==============================================================*/


drop table if exists circle;

drop table if exists circle_rec;

drop table if exists city;

drop table if exists com_img;

drop table if exists comment;

drop table if exists friends;

drop table if exists post;

drop table if exists post_comment;

drop table if exists province;

drop table if exists region;

drop table if exists sce_img;

drop table if exists scenic;

drop table if exists user;

drop table if exists user_circle;

drop table if exists user_rec;

/*==============================================================*/
/* Table: circle                                                */
/*==============================================================*/
create table circle
(
   circle_id            int not null auto_increment,
   city_id              int,
   name                 varchar(128) not null,
   level                int not null default 1,
   avatar               varchar(512),
   abstract             varchar(512),
   user_nums            int not null default 0,
   is_delete            bool default 0,
   primary key (circle_id)
);

/*==============================================================*/
/* Table: circle_rec                                            */
/*==============================================================*/
create table circle_rec
(
   circle_rec_id        int not null auto_increment,
   scenic_id            int,
   circle_id            int,
   rec_nums             int not null default 0,
   month                date not null,
   primary key (circle_rec_id)
);

/*==============================================================*/
/* Table: city                                                  */
/*==============================================================*/
create table city
(
   city_id              int not null auto_increment,
   province_id          int,
   name                 varchar(128) not null,
   sce_nums             int not null default 0,
   primary key (city_id)
);

/*==============================================================*/
/* Table: com_img                                               */
/*==============================================================*/
create table com_img
(
   com_img_id           int not null auto_increment,
   comment_id           int,
   img_url              varchar(512) not null,
   primary key (com_img_id)
);

/*==============================================================*/
/* Table: comment                                               */
/*==============================================================*/
create table comment
(
   comment_id           int not null auto_increment,
   user_id              int,
   scenic_id            int,
   time                 datetime not null,
   mark                 int not null,
   content              varchar(1024) not null,
   clap                 int default 0,
   primary key (comment_id)
);

/*==============================================================*/
/* Table: friends                                               */
/*==============================================================*/
create table friends
(
   friends_id           int not null auto_increment,
   user_id              int,
   add_time             datetime not null,
   is_show              bool default 0,
   is_delete            bool default 0,
   primary key (friends_id)
);

/*==============================================================*/
/* Table: post                                                  */
/*==============================================================*/
create table post
(
   post_id              int not null auto_increment,
   user_id              int,
   time                 datetime not null,
   abstract             varchar(128) not null,
   content              text not null,
   score                int not null,
   clap                 int default 0,
   primary key (post_id)
);

/*==============================================================*/
/* Table: post_comment                                          */
/*==============================================================*/
create table post_comment
(
   post_com_id          int not null auto_increment,
   post_id              int,
   user_id              int,
   content              text not null,
   time                 datetime not null,
   clap                 int default 0,
   primary key (post_com_id)
);

/*==============================================================*/
/* Table: province                                              */
/*==============================================================*/
create table province
(
   province_id          int not null auto_increment,
   name                 varchar(128) not null,
   sce_nums             int not null default 0,
   primary key (province_id)
);

/*==============================================================*/
/* Table: region                                                */
/*==============================================================*/
create table region
(
   region_id            int not null auto_increment,
   city_id              int,
   name                 varchar(128) not null,
   sce_nums             int not null default 0,
   primary key (region_id)
);

/*==============================================================*/
/* Table: sce_img                                               */
/*==============================================================*/
create table sce_img
(
   sce_img_id           int not null auto_increment,
   scenic_id            int not null,
   img_url              varchar(512) not null,
   primary key (sce_img_id)
);

/*==============================================================*/
/* Table: scenic                                                */
/*==============================================================*/
create table scenic
(
   scenic_id            int not null auto_increment,
   region_id            int,
   name                 varchar(512) not null,
   abstract             varchar(4096) not null,
   detail               text,
   addr                 varchar(512) not null,
   longitude            numeric(9,6) not null,
   latitude             numeric(9,6) not null,
   cover                varchar(512),
   primary key (scenic_id)
);

/*==============================================================*/
/* Table: user                                                  */
/*==============================================================*/
create table user
(
   user_id              int not null auto_increment,
   region_id            int,
   username             varchar(16) not null,
   password             varchar(512) not null,
   nickname             varchar(16) not null,
   real_name            varchar(16),
   age                  int,
   gender               int default 0,
   card_id              varchar(18),
   tel                  varchar(16),
   email                varchar(32),
   avatar               varchar(512),
   signature            varchar(256),
   is_delete            bool default 0,
   primary key (user_id)
);

/*==============================================================*/
/* Table: user_circle                                           */
/*==============================================================*/
create table user_circle
(
   circle_id            int not null,
   user_id              int not null,
   primary key (circle_id, user_id)
);

/*==============================================================*/
/* Table: user_rec                                              */
/*==============================================================*/
create table user_rec
(
   user_rec_id          int not null auto_increment,
   user_id              int,
   scenic_id            int,
   time                 datetime not null,
   primary key (user_rec_id)
);

alter table circle add constraint FK_Relationship_9 foreign key (city_id)
      references city (city_id) on delete restrict on update restrict;

alter table circle_rec add constraint FK_Relationship_18 foreign key (scenic_id)
      references scenic (scenic_id) on delete restrict on update restrict;

alter table circle_rec add constraint FK_Relationship_19 foreign key (circle_id)
      references circle (circle_id) on delete restrict on update restrict;

alter table city add constraint FK_Relationship_3 foreign key (province_id)
      references province (province_id) on delete restrict on update restrict;

alter table com_img add constraint FK_Relationship_20 foreign key (comment_id)
      references comment (comment_id) on delete restrict on update restrict;

alter table comment add constraint FK_Relationship_10 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

alter table comment add constraint FK_Relationship_11 foreign key (scenic_id)
      references scenic (scenic_id) on delete restrict on update restrict;

alter table friends add constraint FK_Relationship_21 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

alter table post add constraint FK_Relationship_13 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

alter table post_comment add constraint FK_Relationship_14 foreign key (post_id)
      references post (post_id) on delete restrict on update restrict;

alter table post_comment add constraint FK_Relationship_15 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

alter table region add constraint FK_Relationship_2 foreign key (city_id)
      references city (city_id) on delete restrict on update restrict;

alter table sce_img add constraint FK_Relationship_1 foreign key (scenic_id)
      references scenic (scenic_id) on delete restrict on update restrict;

alter table scenic add constraint FK_Relationship_4 foreign key (region_id)
      references region (region_id) on delete restrict on update restrict;

alter table user add constraint FK_Relationship_5 foreign key (region_id)
      references region (region_id) on delete restrict on update restrict;

alter table user_circle add constraint FK_Relationship_7 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

alter table user_circle add constraint FK_Relationship_8 foreign key (circle_id)
      references circle (circle_id) on delete restrict on update restrict;

alter table user_rec add constraint FK_Relationship_16 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

alter table user_rec add constraint FK_Relationship_17 foreign key (scenic_id)
      references scenic (scenic_id) on delete restrict on update restrict;

