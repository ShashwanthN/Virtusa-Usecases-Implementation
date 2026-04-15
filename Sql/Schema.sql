create table Students (
  StudentID int primary key,
  Name varchar(100),
  Email varchar(100),JoinDate date
);

create table Books (
  BookID int primary key,
  Title varchar(200),
  Author varchar(100),
  Category varchar(50)
);

create table IssuedBooks (
  IssueID int primary key,
  StudentID int,
  BookID int,IssueDate date,
  ReturnDate date,
  foreign key (StudentID) references Students(StudentID),
  foreign key (BookID) references Books(BookID)
);