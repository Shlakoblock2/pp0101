create table Users(
	id integer PRIMARY KEY autoincrement,
	login varchar(16) not null unique,
	password varchar(16) not null,
	power_level: integer
);

create table Applications(
	id integer primary key autoincrement,
	add_date Date,
	UserID integer,
	child_data varchar (250),
	comments varchar (250),
	date_completion date,
	foreign key(UserID) referenced Users(id)
);



