CREATE TABLE comments (
	post_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	email TEXT NOT NULL,
	website_url TEXT NULL,
	comment TEXT NOT NULL );

#to insert table and rows#

INSERT INTO comments ( name, email, website_url, comment )
VALUES ( 'Shivam Mamgain', 'xyz@gmail.com',
'shivammg.blogspot.com', 'Great tutorial for beginners.' );

#to delete#
DELETE FROM comments
WHERE name = 'Bart Simpson' OR name = 'Homer Simpson';