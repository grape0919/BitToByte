create table DESCRIPTION(
	DOWNLOAD_ID INTEGER not null,
	DOWNLOAD_DATE DATE not null
	PRIMARY KEY(COM_ID, DESC_ID)
);

INSERT INTO USER (ID, PWD)
VALUES ('admin', '1111');