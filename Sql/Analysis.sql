select s.StudentID, s.Name, b.Title, i.IssueDate from IssuedBooks i
join Students s on i.StudentID = s.StudentID
join Books b on i.BookID = b.BookID
where i.ReturnDate is null and i.IssueDate <= date('now', '-14 days');

select b.Category, count(*) as NoOfBorrows from IssuedBooks i
join Books b on i.BookID = b.BookID
group by b.Category order by NoOfBorrows desc;


delete from Students where StudentID not in (
    select distinct StudentID from IssuedBooks
    where IssueDate >= date('now', '-3 years')
);
 