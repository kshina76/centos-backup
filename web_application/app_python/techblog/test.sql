SELECT *
FROM shohin;
SELECT shohin_bunrui,
  shohin_mei,
  hanbai_tanka
FROM shohin AS S1
WHERE hanbai_tanka > (
    SELECT AVG(hanbai_tanka)
    FROM shohin AS S2
    WHERE S1.shohin_bunrui = S2.shohin_bunrui
    GROUP BY shohin_bunrui
  );
