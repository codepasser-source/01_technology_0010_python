# gmjjglgs,138
# gmjjglgszgzgs,80
# syyh,154
# zqgs,245
# smjjglr,23848
# bxgs,12
# qhgszgzgs,12
# jwjg,1
# qt,492
DROP TABLE IF EXISTS AMAC_ORF_ORG;
CREATE TABLE `AMAC_ORF_ORG`
(
    `ID`                       VARCHAR(100) NOT NULL DEFAULT '1' COMMENT '数据ID',
    `STATE`                    VARCHAR(20)  NOT NULL DEFAULT 'OK' COMMENT '数据状态：OK,DELETE,EXPIRED',
    `CREATE_TIME`              DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '数据更新时间',
    `UPDATE_TIME`              DATETIME              DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '数据创建时间',
    `POSITION`                 INT                   DEFAULT 0 COMMENT '爬虫内容定位序列',
    `OID`                      VARCHAR(100)          DEFAULT NULL COMMENT 'AMAC-ID',
    `CATEGORY`                 VARCHAR(100)          DEFAULT NULL COMMENT '机构类型-代码',
    `CATEGORY_LABEL`           VARCHAR(255)          DEFAULT NULL COMMENT '机构类型',
    `NAME`                     VARCHAR(255)          DEFAULT NULL COMMENT '机构名称',
    `NAME_SPELL`               VARCHAR(255)          DEFAULT NULL COMMENT '机构名称-SPELL',
    `WORKER_TOTAL`             INT                   DEFAULT NULL COMMENT '员工人数',
    `WORKER_CREDENTIALS_TOTAL` INT                   DEFAULT NULL COMMENT '基金从业资格',
    `WORKER_SALES_TOTAL`       INT                   DEFAULT NULL COMMENT '基金销售业务资格',
    `MGR_FUND_TOTAL`           INT                   DEFAULT NULL COMMENT '基金经理',
    `MGR_INVESTMENT_TOTAL`     INT                   DEFAULT NULL COMMENT '投资经理',
    PRIMARY KEY (`ID`)
) ENGINE = INNODB
  DEFAULT CHARSET = UTF8MB4
  COLLATE = UTF8MB4_GENERAL_CI;

DROP TRIGGER IF EXISTS `AMAC_ORF_ORG_GUID`;
CREATE TRIGGER `AMAC_ORF_ORG_GUID`
    BEFORE INSERT
    ON `AMAC_ORF_ORG`
    FOR EACH ROW
BEGIN
    IF NEW.ID = '1' THEN
        SET NEW.ID = (SELECT UUID_SHORT());
    END IF;
END

