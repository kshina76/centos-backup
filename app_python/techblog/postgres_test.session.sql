SELECT *
FROM shohin;
select CASE
    WHEN hanbai_tanka > 500 THEN 'A :' || shohin_bunrui
    ELSE 'B :' || shohin_bunrui
  END AS shohin_grade
FROM shohin
GROUP BY shohin_grade
