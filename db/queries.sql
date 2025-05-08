

CREATE TABLE IF NOT EXISTS contests (
    id INT PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT CHECK ( type IN ('CF', 'ICPC', 'IOI')) NOT NULL,
    phase TEXT CHECK ( phase IN ('PENDING_SYSTEM_TEST', 'BEFORE', 'FINISHED')),
    duration_seconds INT NOT NULL,
    start_time TIMESTAMP NOT NULL
);


select * from contests;

