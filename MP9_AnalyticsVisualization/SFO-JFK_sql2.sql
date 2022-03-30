SELECT f1.airline, f1.origin_airport, f1.destination_airport as stopover_airport, f2.destination_airport, f1.departure_delay as origin_departure_delay, f1.arrival_delay as stopover_arrival_delay, f2.departure_delay as stopover_departure_delay, f2.arrival_delay as destination_arrival_delay
FROM
(SELECT * FROM "cca-mp9-flights-table" WHERE origin_airport = 'SFO' and cancelled=0) as f1
INNER JOIN
(SELECT * FROM "cca-mp9-flights-table" WHERE destination_airport = 'JFK' and cancelled=0) as f2
ON f1.destination_airport = f2.origin_airport
WHERE 60 <= f2.day*24*60 + (f2.scheduled_departure / 100)*60 + (f2.scheduled_departure % 100) + f2.departure_delay - (f1.day*24*60 + (f1.scheduled_departure / 100)*60 + (f1.scheduled_departure % 100) + f1.departure_delay + f1.elapsed_time + ((f1.scheduled_arrival / 100)*60 + (f1.scheduled_arrival % 100) - ((f1.scheduled_departure / 100)*60 + (f1.scheduled_departure % 100) + f1.scheduled_time)%(24*60)))
AND f2.day*24*60 + (f2.scheduled_departure / 100)*60 + (f2.scheduled_departure % 100) + f2.departure_delay - (f1.day*24*60 + (f1.scheduled_departure / 100)*60 + (f1.scheduled_departure % 100) + f1.departure_delay + f1.elapsed_time + ((f1.scheduled_arrival / 100)*60 + (f1.scheduled_arrival % 100) - ((f1.scheduled_departure / 100)*60 + (f1.scheduled_departure % 100) + f1.scheduled_time)%(24*60))) <= 180
AND f1.airline=f2.airline