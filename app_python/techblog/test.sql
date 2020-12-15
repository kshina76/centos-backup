SELECT *
FROM shohin;
SELECT shohin_bunrui,
  COUNT(*)
FROM shohin
GROUP BY shohin_bunrui;
