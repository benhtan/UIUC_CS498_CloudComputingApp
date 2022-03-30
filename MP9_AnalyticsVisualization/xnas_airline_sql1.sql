SELECT airline, origin_airport, destination_airport FROM "cca-mp9-flights-table" 
WHERE origin_airport = 'ORD' AND month = 12 AND day = 25
AND scheduled_departure BETWEEN 800 and 1159