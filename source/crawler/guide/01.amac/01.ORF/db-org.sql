delimiter ;;
set global log_bin_trust_function_creators = 1;

delimiter ;;
drop table if exists irm_amac_org;
create table `irm_amac_org`
(
    `id`                       varchar(100) not null default '1' comment '数据id',
    `state`                    varchar(20)  not null default 'OK' comment '数据状态：OK,DELETE,EXPIRED',
    `create_time`              datetime     not null default current_timestamp comment '数据更新时间',
    `update_time`              datetime              default current_timestamp on update current_timestamp comment '数据创建时间',
    `oid`                      varchar(100)          default null,
    `category`                 varchar(100)          default null,
    `category_label`           varchar(255)          default null,
    `name`                     varchar(255)          default null,
    `name_spell`               varchar(255)          default null,
    `worker_total`             int                   default null,
    `worker_credentials_total` int                   default null,
    `worker_sales_total`       int                   default null,
    `mgr_fund_total`           int                   default null,
    `mgr_investment_total`     int                   default null,
    primary key (`id`)
) engine = innodb
  default charset = utf8mb4
  collate = utf8mb4_general_ci;

ALTER TABLE `irm_amac_org`
    ADD INDEX `idx_oid` (`oid`);

ALTER TABLE `irm_amac_org`
    ADD INDEX `idx_category_state` (`category`, `state`);

delimiter ;;
drop trigger if exists `irm_amac_org_guid`;
create trigger `irm_amac_org_guid`
    before insert
    on `irm_amac_org`
    for each row
begin
    if new.id = '1' then
        set new.id = (select uuid_short());
    end if;
end

