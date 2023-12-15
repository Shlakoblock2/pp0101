create table Users(
	id integer PRIMARY KEY autoincrement,
	login varchar(16) not null unique,
	password varchar(16) not null,
	power_level integer
);

create table city(
	id integer primary key autoincrement,
	name varchar (250)
);

create table children(
	id integer primary key autoincrement,
	cityID integer,
	name varchar (250),
	surname varchar (250),
	age integer,
	foreign key(cityID) references city(id)
);

create table Applications(
	id integer primary key autoincrement,
	add_date Date,
	UserID integer,
	childID integer,
	comments varchar (250),
	date_completion date,
	foreign key(UserID) references Users(id),
	foreign key(childID) references children(id)
);