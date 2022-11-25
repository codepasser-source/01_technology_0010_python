delimiter ;;
drop table if exists irm_amac_cert;
create table `irm_amac_cert`
(
    `id`                varchar(100) not null default '1' comment '数据id',
    `state`             varchar(20)  not null default 'OK' comment '数据状态：OK,DELETE,EXPIRED',
    `create_time`       datetime     not null default current_timestamp comment '数据更新时间',
    `update_time`       datetime              default current_timestamp on update current_timestamp comment '数据创建时间',
    `oid`               varchar(100)          default null,
    `pid`               varchar(100)          default null,
    `cid`               varchar(100)          default null,
    `org_id`            varchar(100)          default null,
    `org_name`          varchar(255)          default null,
    `cert_label`        varchar(100)          default null,
    `cert_serial`       varchar(100)          default null,
    `cert_start_date`   date                  default null,
    `cert_end_date`     date                  default null,
    `cert_change_date`  date                  default null,
    `cert_status`       varchar(20)           default null,
    `cert_status_label` varchar(100)          default null,
    primary key (`id`)
) engine = innodb
  default charset = utf8mb4
  collate = utf8mb4_general_ci;

ALTER TABLE `irm_amac_cert`
    ADD INDEX `idx_oid` (`oid`);
ALTER TABLE `irm_amac_cert`
    ADD INDEX `idx_pid` (`pid`);
ALTER TABLE `irm_amac_cert`
    ADD INDEX `idx_cid` (`cid`);

delimiter ;;
drop trigger if exists `irm_amac_cert_guid`;
create trigger `irm_amac_cert_guid`
    before insert
    on `irm_amac_cert`
    for each row
begin
    if new.id = '1' then
        set new.id = (select uuid_short());
    end if;
end