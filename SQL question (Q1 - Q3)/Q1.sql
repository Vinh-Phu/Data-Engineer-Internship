select *
from Performance
where Score = (select max(Score)
                  from Performance
                  where Score < (select max(Score)
                                 from Performance));