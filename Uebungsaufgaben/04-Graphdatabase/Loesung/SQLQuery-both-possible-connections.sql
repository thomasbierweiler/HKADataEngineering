--SELECT assets5.AKZ AS ConnectedName
SELECT CONCAT(asset1.AKZ,'->',asset2.AKZ,'->',asset3.AKZ,'->',asset4.AKZ,'->',asset5.AKZ)
FROM Assets asset1, connectedTo c1, Assets asset2,connectedTo c2, Assets asset3,connectedTo c3, Assets asset4,connectedTo c4, Assets asset5
WHERE MATCH(asset1-(c1)->asset2-(c2)->asset3-(c3)->asset4-(c4)->asset5)
AND asset1.AKZ = 'VE1000'
AND asset2.AKZ != asset1.AKZ
AND asset3.AKZ != asset2.AKZ
AND asset4.AKZ != asset3.AKZ
AND asset5.AKZ != asset4.AKZ
AND asset5.AKZ = 'T5'

SELECT DISTINCT CONCAT(asset1.AKZ,'->',asset2.AKZ,'->',asset3.AKZ,'->',asset4.AKZ,'->',asset5.AKZ,'->',asset6.AKZ)
FROM Assets asset1, connectedTo c1, Assets asset2,connectedTo c2, Assets asset3,connectedTo c3, Assets asset4,connectedTo c4, Assets asset5
 ,connectedTo c5, Assets asset6
WHERE MATCH(asset1-(c1)->asset2-(c2)->asset3-(c3)->asset4-(c4)->asset5-(c5)->asset6)
AND asset1.AKZ = 'VE1000'
AND asset2.AKZ != asset1.AKZ
AND asset3.AKZ != asset2.AKZ
AND asset4.AKZ != asset3.AKZ
AND asset5.AKZ != asset4.AKZ
AND asset6.AKZ != asset5.AKZ
--AND asset6.AKZ = 'T5'

SELECT DISTINCT CONCAT(asset1.AKZ,'->',asset2.AKZ,'->',asset3.AKZ,'->',asset4.AKZ,'->',asset5.AKZ,'->',asset6.AKZ,'->',asset7.AKZ)
FROM Assets asset1, connectedTo c1, Assets asset2,connectedTo c2, Assets asset3,connectedTo c3, Assets asset4,connectedTo c4, Assets asset5
 ,connectedTo c5, Assets asset6,connectedTo c6, Assets asset7
WHERE MATCH(asset1-(c1)->asset2-(c2)->asset3-(c3)->asset4-(c4)->asset5-(c5)->asset6-(c6)->asset7)
AND asset1.AKZ = 'VE1000'
AND asset2.AKZ != asset1.AKZ
AND asset3.AKZ != asset2.AKZ
AND asset4.AKZ != asset3.AKZ
AND asset5.AKZ != asset4.AKZ
AND asset6.AKZ != asset5.AKZ
AND asset7.AKZ != asset6.AKZ
--AND asset7.AKZ = 'T5'

SELECT DISTINCT CONCAT(asset1.AKZ,'->',asset2.AKZ,'->',asset3.AKZ,'->',asset4.AKZ,'->',asset5.AKZ,'->',asset6.AKZ,'->',asset7.AKZ,'->',asset8.AKZ)
FROM Assets asset1, connectedTo c1, Assets asset2,connectedTo c2, Assets asset3,connectedTo c3, Assets asset4,connectedTo c4, Assets asset5
 ,connectedTo c5, Assets asset6,connectedTo c6, Assets asset7,connectedTo c7, Assets asset8
WHERE MATCH(asset1-(c1)->asset2-(c2)->asset3-(c3)->asset4-(c4)->asset5-(c5)->asset6-(c6)->asset7-(c7)->asset8)
AND asset1.AKZ = 'VE1000'
AND asset2.AKZ != asset1.AKZ
AND asset3.AKZ != asset2.AKZ
AND asset4.AKZ != asset3.AKZ
AND asset5.AKZ != asset4.AKZ
AND asset6.AKZ != asset5.AKZ
AND asset7.AKZ != asset6.AKZ
AND asset8.AKZ != asset7.AKZ
--AND asset8.AKZ = 'T5'

SELECT DISTINCT CONCAT(asset1.AKZ,'->',asset2.AKZ,'->',asset3.AKZ,'->',asset4.AKZ,'->',asset5.AKZ,'->',asset6.AKZ,'->',asset7.AKZ,'->',asset8.AKZ,'->',asset9.AKZ)
FROM Assets asset1, connectedTo c1, Assets asset2,connectedTo c2, Assets asset3,connectedTo c3, Assets asset4,connectedTo c4, Assets asset5
 ,connectedTo c5, Assets asset6,connectedTo c6, Assets asset7,connectedTo c7, Assets asset8,connectedTo c8, Assets asset9
WHERE MATCH(asset1-(c1)->asset2-(c2)->asset3-(c3)->asset4-(c4)->asset5-(c5)->asset6-(c6)->asset7-(c7)->asset8-(c8)->asset9)
AND asset1.AKZ = 'VE1000'
AND asset2.AKZ != asset1.AKZ
AND asset3.AKZ != asset2.AKZ
AND asset4.AKZ != asset3.AKZ
AND asset5.AKZ != asset4.AKZ
AND asset6.AKZ != asset5.AKZ
AND asset7.AKZ != asset6.AKZ
AND asset8.AKZ != asset7.AKZ
AND asset9.AKZ != asset8.AKZ
--AND asset9.AKZ = 'T5'

