delimiter ;;
drop table if exists irm_amac_per;
create table `irm_amac_per`
(
    `id`                varchar(100) not null default '1' comment '数据id',
    `state`             varchar(20)  not null default 'OK' comment '数据状态：OK,DELETE,EXPIRED',
    `create_time`       datetime     not null default current_timestamp comment '数据更新时间',
    `update_time`       datetime              default current_timestamp on update current_timestamp comment '数据创建时间',
    `oid`               varchar(100)          default null,
    `pid`               varchar(100)          default null,
    `name`              varchar(255)          default null,
    `sex`               varchar(20)           default null,
    `sex_label`         varchar(100)          default null,
    `cert_label`        varchar(100)          default null,
    `cert_serial`       varchar(100)          default null,
    `cert_start_date`   date                  default null,
    `cert_end_date`     date                  default null,
    `cert_status_times` int                   default null,
    `cert_status`       varchar(20)           default null,
    `cert_status_label` varchar(100)          default null,
    `education`         varchar(20)           default null,
    `education_label`   varchar(100)          default null,
    `office_state`      varchar(20)           default null,
    `avatar_url`        varchar(255)          default null,
    `is_pq`             bit(1)                default false,
    `is_sq`             bit(1)                default false,
    `is_fm`             bit(1)                default false,
    `is_im`             bit(1)                default false,
    primary key (`id`)
) engine = innodb
  default charset = utf8mb4
  collate = utf8mb4_general_ci;

ALTER TABLE `irm_amac_per`
    ADD INDEX `idx_oid` (`oid`);
ALTER TABLE `irm_amac_per`
    ADD INDEX `idx_pid` (`pid`);

delimiter ;;
drop trigger if exists `irm_amac_per_guid`;
create trigger `irm_amac_per_guid`
    before insert
    on `irm_amac_per`
    for each row
begin
    if new.id = '1' then
        set new.id = (select uuid_short());
    end if;
end