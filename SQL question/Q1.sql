select *
from Perfomance
where Score = (select max(Score)
                  from Perfomance
                  where Score < (select max(Score)
                                 from Perfomance));