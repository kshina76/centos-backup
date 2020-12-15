SELECT *
FROM shohin;
SELECT hanbai_tanka,
  COUNT(*)
FROM shohin
GROUP BY hanbai_tanka
HAVING COUNT(*) = 2;
