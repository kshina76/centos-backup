SELECT *
FROM shohin;
SELECT shiire_tanka,
  COUNT(*)
FROM shohin
WHERE shohin_bunrui = '衣服';
GROUP BY shiire_tanka;
