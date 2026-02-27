CREATE FUNCTION dbo.tvf_SecurityPredicatebyGeo(@GeoID AS INT)  
    RETURNS TABLE  
WITH SCHEMABINDING  
AS  
    RETURN	SELECT 1 AS result
			WHERE @GeoID = 255853;