CREATE VIEW firearm_incident AS 
Select firearm_recovery.id, 
firearm_recovery.collection_date, 
incidents.occurred_on_date from firearm_recovery 
inner join incidents on firearm_recovery.collection_date =incidents.occurred_on_date
order by firearm_recovery.collection_date;

CREATE VIEW shooting_incident AS
Select shooting.incident_number, 
shooting.shooting_date, 
shooting.district_cd, 
shooting.shooting_type,
shooting.victim,
shooting.victim_gender,
shooting.victim_race, 
shooting.victim_ethnicity, 
shooting.multi_victim from shooting 
left join incidents on shooting.shooting_date = incidents.occurred_on_date 
order by shooting.shooting_date;

CREATE VIEW shots_fired_incidents AS
Select shots_fired.incident_number, 
shots_fired.incident_date, 
shots_fired.district_cd
from shots_fired left join incidents on shots_fired.incident_date = incidents.occurred_on_date 
order by shots_fired.incident_date;

CREATE VIEW top10_districts AS
Select count(incidents.incident_number) as total_incidents, 
incidents.district,
districts.district_name
from incidents 
inner join districts
on incidents.district = districts.district_cd
group by incidents.district 
order by total_incidents desc
limit 10;

CREATE VIEW district_shot_fired AS
Select count(shots_fired.incident_id) as total_incidents, 
shots_fired.district_cd, 
districts.district_name
from shots_fired
inner join districts
on shots_fired.district_cd = districts.district_cd 
group by shots_fired.district_cd
order by total_incidents desc;

CREATE VIEW mostshooting_districts AS
Select count(shooting.incident_number) as total_incidents, 
shooting.district_cd, 
districts.district_name, 
districts.phone 
from shooting 
join districts on shooting.district_cd = districts.district_cd 
group by district_cd 
order by total_incidents;

CREATE VIEW highest_number_of_guns AS
Select collection_date, 
(crimeguns_recovered + guns_recovered + buybackguns_recovered) as total_guns_recovered 
from firearm_recovery 
order by total_guns_recovered;

CREATE VIEW recovered_firearms_shooting AS
SELECT shooting.incident_number, 
shooting.shooting_date,
shooting.district_cd
from shooting 
left join firearm_recovery
on shooting.shooting_date = firearm_recovery.collection_date
order by shooting.shooting_date;

CREATE VIEW crime_related_firearms AS
SELECT shooting.incident_number, 
shooting.shooting_date,
shooting.district_cd
from shooting 
left join firearm_recovery
on shooting.shooting_date = firearm_recovery.collection_date
where firearm_recovery.crimeguns_recovered > 0
order by shooting.shooting_date;

CREATE view gender AS
Select shooting.victim_gender, 
count(shooting.victim_gender) as count,
offense.offense_desc
from shooting
inner join incidents
on shooting.incident_number = incidents.incident_number
inner join offense
on incidents.offense_code = offense.offense_code
group by shooting.victim_gender, offense.offense_desc;

CREATE VIEW race AS
Select shooting.victim_race, 
count(shooting.victim_race) as count,
offense.offense_desc
from shooting
inner join incidents
on shooting.incident_number = incidents.incident_number
inner join offense
on incidents.offense_code = offense.offense_code
group by shooting.victim_race, offense.offense_desc;

CREATE VIEW ethnicity AS
Select shooting.victim_ethnicity, 
count(shooting.victim_ethnicity) as count,
offense.offense_desc
from shooting
inner join incidents
on shooting.incident_number = incidents.incident_number
inner join offense
on incidents.offense_code = offense.offense_code
group by shooting.victim_ethnicity, offense.offense_desc;

CREATE VIEW most_recorded_offense AS
Select incidents.offense_code, 
count(incidents.offense_code) as count_of_offence, 
offense.offense_desc
from incidents 
Join offense
on incidents.offense_code = offense.offense_code
group by offense_code 
order by count_of_offence;

CREATE VIEW ballistic_evidence AS
Select shots_fired.incident_number,
Shots_fired.district_cd,
districts.district_name,
Shots_fired.ballistics_evidence 
From Shots_fired
Join districts 
on Shots_fired.district_cd = districts.district_cd
Where Shots_fired.ballistics_evidence = "t";

CREATE VIEW most_ballistic_evidence_districts AS
Select districts.district_cd,
count(shots_fired.district_cd) AS count
From districts
join shots_fired
on districts.district_cd = shots_fired.district_cd
Where Shots_fired.ballistics_evidence = "t"
Group by districts.district_cd
Order by count desc
LIMIT 1;

CREATE VIEW mutliple_victims AS
Select incidents.incident_number,
Shooting.multi_victim
From incidents inner join shooting
on incidents.incident_number = shooting.incident_number
Where shooting.multi_victim = "t"
Group by incidents.incident_number,
shooting.multi_victim;

CREATE VIEW more_than_one_victim AS
Select shooting.incident_number,
shooting.district_cd,
districts.district_name,
shooting.multi_victim
From shooting
Join districts
On shooting.district_cd = districts.district_cd
Where shooting.multi_victim = "t"
Group by 
shooting.incident_number,
shooting.district_cd,
districts.district_name,
shooting.multi_victim;

CREATE VIEW least_shooting AS
SELECT CASE DAYOFWEEK(incidents.occurred_on_date) 
    WHEN 1 THEN 'SUNDAY' 
    WHEN 2 THEN 'MONDAY' 
    WHEN 3 THEN 'TUESDAY' 
    WHEN 4 THEN 'WEDNESDAY' 
    WHEN 5 THEN 'THURSDAY' 
    WHEN 6 THEN 'FRIDAY' 
    WHEN 7 THEN 'SATURDAY'
END,
count(incidents.incident_number) as count
FROM incidents
join shooting
on incidents.incident_number = shooting.incident_number
GROUP BY incidents.occurred_on_date
ORDER BY count desc
LIMIT 1;

CREATE VIEW least_hour_shooting AS
SELECT incidents.hour,
count(incidents.incident_number) as count
FROM incidents
join shooting
on incidents.incident_number = shooting.incident_number
GROUP BY
incidents.hour
ORDER BY count desc
LIMIT 1;

CREATE VIEW highest_no_of_buyback_guns AS
SELECT firearm_recovery.collection_date,
firearm_recovery.buybackguns_recovered
FROM firearm_recovery
INNER JOIN incidents
ON firearm_recovery.collection_date = incidents.occurred_on_date
GROUP BY 
firearm_recovery.collection_date,
firearm_recovery.buybackguns_recovered
ORDER BY firearm_recovery.buybackguns_recovered;











