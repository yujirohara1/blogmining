--CREATE TABLE toko ( 
--    vendor_nm character varying(100) ,
--    system_nm character varying(100) ,
--    dantai_nm character varying(100) ,
--    tokosha_nm character varying(100),
--    rank1 integer,
--    comment1 character varying(200),
--    rank2 integer,
--    comment2 character varying(200),
--    ymdt timestamp without time zone 
--);
--
--CREATE TABLE toko_radar (
--    vendor_nm character varying(100) ,
--    system_nm character varying(100) ,
--    dantai_nm character varying(100) ,
--    tokosha_nm character varying(100),
--    hyoka_shubetu integer,
--    hyoka_value integer,
--    ymdt timestamp without time zone 
--);

CREATE TABLE kaito ( 
    vendor_nm character varying(100) ,
    system_nm character varying(100) ,
    dantai_nm character varying(100) ,
    tokosha_nm character varying(100),
    situmon_kb integer,
    hyoka_shubetu integer,
    hyoka_shubetu_sub integer,
    hyoka_value character varying(100),
    hyoka_comment character varying(200),
    ymdt timestamp without time zone 
);

/*
|| デモデータ作成
*/
insert into kaito (vendor_nm,system_nm,situmon_kb, hyoka_value, hyoka_comment, ymdt)
select
    vendor_nm,
    system_nm,
    1,
    rank1,
    comment1,
    ymdt
from
    toko
;


/*
|| トップの左上のグリッドに使われる。
|| アンケートの「他者の回答から選択」プルダウンにも使われる。
*/
drop view v_toko_groupby_vendor cascade;
CREATE VIEW v_toko_groupby_vendor AS
select
    vendor_nm,
    count(1) kensu,
    round(avg(hyoka_value::integer),2) rank1_avg
from
    kaito
where
    situmon_kb = 1 and
    hyoka_shubetu = 1
group by
    vendor_nm
;

select * from v_toko_groupby_vendor;





/*
|| アンケートの「他者の回答から選択」プルダウンに使われる。
*/
drop view v_toko_groupby_system cascade;
CREATE VIEW v_toko_groupby_system AS
select
    system_nm,
    count(1) kensu,
    round(avg(hyoka_value::integer),2) rank1_avg
from
    kaito
where
    situmon_kb = 1 and
    hyoka_shubetu = 1
group by
    system_nm
;

select * from v_toko_groupby_system;




delete from kaito where situmon_kb = 2;
insert into kaito (vendor_nm,situmon_kb, hyoka_shubetu, hyoka_value, ymdt)
select
    vendor_nm,
    2,
    hyoka_shubetu,
    hyoka_value,
    ymdt
from
    toko_radar
;



/*
|| レーダーチャートでの７軸評価に使われる。
*/
drop view v_tokoradar_groupby_vendor cascade;
CREATE VIEW v_tokoradar_groupby_vendor AS
select
    main.vendor_nm,
    sum(CASE
            WHEN main.hyoka_shubetu = 1 THEN main.hyoka_value::integer
            ELSE 0
        END) / sub1.kensu AS shubetu1_avg,
    sum(CASE
            WHEN main.hyoka_shubetu = 2 THEN main.hyoka_value::integer
            ELSE 0
        END) / sub1.kensu AS shubetu2_avg,
    sum(CASE
            WHEN main.hyoka_shubetu = 3 THEN main.hyoka_value::integer
            ELSE 0
        END) / sub1.kensu AS shubetu3_avg,
    sum(CASE
            WHEN main.hyoka_shubetu = 4 THEN main.hyoka_value::integer
            ELSE 0
        END) / sub1.kensu AS shubetu4_avg,
    sum(CASE
            WHEN main.hyoka_shubetu = 5 THEN main.hyoka_value::integer
            ELSE 0
        END) / sub1.kensu AS shubetu5_avg,
    sum(CASE
            WHEN main.hyoka_shubetu = 6 THEN main.hyoka_value::integer
            ELSE 0
        END) / sub1.kensu AS shubetu6_avg,
    sum(CASE
            WHEN main.hyoka_shubetu = 7 THEN main.hyoka_value::integer
            ELSE 0
        END) / sub1.kensu AS shubetu7_avg
from
    (select * from kaito where situmon_kb = 2) main,
    (select
        vendor_nm,
        count(1) kensu
    from
        kaito
    where
        situmon_kb = 2 and
        hyoka_shubetu = 1
    group by
        vendor_nm
    ) sub1
where
    main.vendor_nm = sub1.vendor_nm
group by
    main.vendor_nm,
    sub1.kensu
;

select * from v_tokoradar_groupby_vendor;




/*
      得意・不得意
*/


drop view v_bunyamap_groupby_vendor cascade;
CREATE VIEW v_bunyamap_groupby_vendor AS
select
    n.vendor_nm,
    m.bunya_cd,
    m.bunya_nm,
    n.kensu,
    m.ryaku_nm
from
    (select  1 bunya_cd,'住民基本台帳'   bunya_nm , 0 kensu , '住基' ryaku_nm union all 
     select  2 bunya_cd,'選挙人名簿管理' bunya_nm , 0 kensu , '選挙' ryaku_nm union all 
     select  3 bunya_cd,'固定資産税'     bunya_nm , 0 kensu , '固定' ryaku_nm union all 
     select  4 bunya_cd,'個人住民税'     bunya_nm , 0 kensu , '民税' ryaku_nm union all 
     select  5 bunya_cd,'軽自動車税'     bunya_nm , 0 kensu , '軽自' ryaku_nm union all 
     select  6 bunya_cd,'国民健康保険'   bunya_nm , 0 kensu , '国保' ryaku_nm union all 
     select  7 bunya_cd,'国民年金'       bunya_nm , 0 kensu , '年金' ryaku_nm union all 
     select  8 bunya_cd,'障害者福祉'     bunya_nm , 0 kensu , '障害' ryaku_nm union all 
     select  9 bunya_cd,'後期高齢者医療' bunya_nm , 0 kensu , '後期' ryaku_nm union all 
     select 10 bunya_cd,'介護保険'       bunya_nm , 0 kensu , '介護' ryaku_nm union all 
     select 11 bunya_cd,'児童手当'       bunya_nm , 0 kensu , '児童' ryaku_nm union all 
     select 12 bunya_cd,'生活保護'       bunya_nm , 0 kensu , '生保' ryaku_nm union all 
     select 13 bunya_cd,'健康管理'       bunya_nm , 0 kensu , '健康' ryaku_nm union all 
     select 14 bunya_cd,'就学援助'       bunya_nm , 0 kensu , '就学' ryaku_nm union all 
     select 15 bunya_cd,'財務会計'       bunya_nm , 0 kensu , '財務' ryaku_nm union all 
     select 16 bunya_cd,'起債管理'       bunya_nm , 0 kensu , '起債' ryaku_nm union all 
     select 17 bunya_cd,'備品管理'       bunya_nm , 0 kensu , '備品' ryaku_nm union all 
     select 18 bunya_cd,'財産管理'       bunya_nm , 0 kensu , '財産' ryaku_nm union all 
     select 19 bunya_cd,'公会計'         bunya_nm , 0 kensu , '公会' ryaku_nm union all 
     select 20 bunya_cd,'行政評価'       bunya_nm , 0 kensu , '行政' ryaku_nm union all 
     select 21 bunya_cd,'実施計画'       bunya_nm , 0 kensu , '実計' ryaku_nm union all 
     select 22 bunya_cd,'源泉徴収'       bunya_nm , 0 kensu , '源泉' ryaku_nm union all 
     select 23 bunya_cd,'人事給与'       bunya_nm , 0 kensu , '給与' ryaku_nm union all 
     select 24 bunya_cd,'人事評価'       bunya_nm , 0 kensu , '評価' ryaku_nm union all 
     select 25 bunya_cd,'文書管理'       bunya_nm , 0 kensu , '文書' ryaku_nm union all 
     select 26 bunya_cd,'旅費管理'       bunya_nm , 0 kensu , '旅費' ryaku_nm union all 
     select 27 bunya_cd,'庶務事務'       bunya_nm , 0 kensu , '庶務' ryaku_nm union all 
     select 28 bunya_cd,'グループウェア' bunya_nm , 0 kensu , 'ＧＷ' ryaku_nm union all 
     select 29 bunya_cd,'水道料金'       bunya_nm , 0 kensu , '水道' ryaku_nm union all 
     select 30 bunya_cd,'企業会計'       bunya_nm , 0 kensu , '企業' ryaku_nm) m
left outer join
    (select
        vendor_nm,
        hyoka_shubetu,
        sum(CASE
            WHEN hyoka_value = 'true' THEN 1
            ELSE 0
        END) kensu
    from
        kaito
    where
        situmon_kb = 3
    group by
        vendor_nm,
        hyoka_shubetu
    union all
    select
        vendor_nm,
        hyoka_shubetu,
        0
    from
        (select
            distinct vendor_nm
        from
            kaito a
        where
            situmon_kb = 1 and
            not exists (select
                           1
                       from
                           (select * from kaito where situmon_kb = 3) b
                       where
                           a.vendor_nm = b.vendor_nm
                       )
        union all
        select
            'dummy'
        ) a
    left outer join (select  1  hyoka_shubetu union all
                     select  2  hyoka_shubetu union all
                     select  3  hyoka_shubetu union all
                     select  4  hyoka_shubetu union all
                     select  5  hyoka_shubetu union all
                     select  6  hyoka_shubetu union all
                     select  7  hyoka_shubetu union all
                     select  8  hyoka_shubetu union all
                     select  9  hyoka_shubetu union all
                     select 10  hyoka_shubetu union all
                     select 11  hyoka_shubetu union all
                     select 12  hyoka_shubetu union all
                     select 13  hyoka_shubetu union all
                     select 14  hyoka_shubetu union all
                     select 15  hyoka_shubetu union all
                     select 16  hyoka_shubetu union all
                     select 17  hyoka_shubetu union all
                     select 18  hyoka_shubetu union all
                     select 19  hyoka_shubetu union all
                     select 20  hyoka_shubetu union all
                     select 21  hyoka_shubetu union all
                     select 22  hyoka_shubetu union all
                     select 23  hyoka_shubetu union all
                     select 24  hyoka_shubetu union all
                     select 25  hyoka_shubetu union all
                     select 26  hyoka_shubetu union all
                     select 27  hyoka_shubetu union all
                     select 28  hyoka_shubetu union all
                     select 29  hyoka_shubetu union all
                     select 30  hyoka_shubetu 
                     ) b
    on
        1 = 1
    ) n
on
    m.bunya_cd = n.hyoka_shubetu
;

select * from v_bunyamap_groupby_vendor;





drop view v_todohuken_groupby_vendor cascade;
CREATE VIEW v_todohuken_groupby_vendor AS
select 
    vendor_nm, 
    hyoka_value, 
    count(1) kensu 
from 
    kaito 
where 
    situmon_kb = 1 and 
    hyoka_shubetu = 3 and
    hyoka_value <> 'mukaito'
group by 
    vendor_nm, 
    hyoka_value
;


select * from v_todohuken_groupby_vendor;










