select count(distinct REG_NO)
from amac_pof_org;

select count(distinct UNI_SOCIAL_CD)
from amac_pof_off;

select count(1)
from amac_pof_off;


select count(distinct REG_NO)
from amac_pof_abnormal;


select count(distinct REG_NO)
from amac_pof_missing;

select *
from information_schema.PROCESSLIST
where DB = 'capital_cloud_irm_uat'
order by HOST