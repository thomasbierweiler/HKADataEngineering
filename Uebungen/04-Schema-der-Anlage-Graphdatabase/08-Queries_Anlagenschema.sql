USE HSKAGraphAnlagenschema;
GO

-- Find connections of pump PL1200
SELECT CONCAT(asset1.AKZ,'->',asset2.AKZ)
FROM Assets asset1, connectedTo, Assets asset2
WHERE MATCH (asset1-(connectedTo)->asset2)
AND asset1.AKZ='PL1200'

-- Find shortest path from vessel 'VE1000' to all other assets (nodes)
SELECT
	asset1.AKZ AS AKZ,
	STRING_AGG(asset2.AKZ, '->') WITHIN GROUP (GRAPH PATH) AS ConnectedAssets
FROM
	Assets AS asset1,
	connectedTo FOR PATH AS cTo,
	Assets FOR PATH  AS asset2
WHERE MATCH(SHORTEST_PATH(asset1(-(cTo)->asset2)+))
AND asset1.AKZ = 'VE1000'

-- Find shortest path from vessel VE1000 to valve YC14001
SELECT AKZ1, ConnectedAssets
FROM (
	SELECT
		asset1.AKZ AS AKZ1,
		STRING_AGG(asset2.AKZ, '->') WITHIN GROUP (GRAPH PATH) AS ConnectedAssets,
		LAST_VALUE(asset2.AKZ) WITHIN GROUP (GRAPH PATH) AS LastNode
	FROM
		Assets AS asset1,
		connectedTo FOR PATH AS cTo,
		Assets FOR PATH  AS asset2
	WHERE MATCH(SHORTEST_PATH(asset1(-(cTo)->asset2)+))
	AND asset1.AKZ = 'VE1000'
) AS Q
WHERE Q.LastNode = 'YC14001'

-- Find all shortest paths from and to vessel VE1000
SELECT
    StartNode, [Edges Path], FinalNode, Levels
FROM (
    SELECT 
        asset1.AKZ as AKZ1, 
        asset1.AKZ as StartNode, 
        STRING_AGG(asset2.AKZ,'->') WITHIN GROUP (GRAPH PATH) AS [Edges Path],
        LAST_VALUE(asset2.AKZ) WITHIN GROUP (GRAPH PATH) AS FinalNode,
        COUNT(asset2.AKZ) WITHIN GROUP (GRAPH PATH) AS Levels
    FROM
        Assets asset1,
        Assets FOR PATH asset2,
        connectedTo FOR PATH cTo
    WHERE 
        MATCH(SHORTEST_PATH(asset1(-(cTo)->asset2)+))
 ) AS Q
 WHERE Q.FinalNode = 'VE1000'