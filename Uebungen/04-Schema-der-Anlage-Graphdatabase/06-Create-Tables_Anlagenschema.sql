USE HSKAGraphAnlagenschema;
GO

-- Create NODE tables

CREATE TABLE Assets (
  ID INTEGER PRIMARY KEY,
  AssetType VARCHAR(100),
  AKZ VARCHAR(100)
) AS NODE;

-- Create EDGE tables.
CREATE TABLE connectedTo AS EDGE;
