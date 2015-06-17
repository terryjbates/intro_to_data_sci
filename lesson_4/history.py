from pandas import *
from ggplot import *
import pandas
hr_year_df  = pd.read_csv('../lesson_4/hr_year.csv')
hr_year_df  = pandas.read_csv('../lesson_4/hr_year.csv')
gg = ggplot(aes(x='yearID', y='HR'), data = hr_year_df) + geom_point(color='red')) +
gg = ggplot(aes(x='yearID', y='HR'), data = hr_year_df) + geom_point(color='red'))
gg = ggplot(aes(x='yearID', y='HR'), data = hr_year_df))
gg = ggplot(aes(x='yearID', y='HR'), data = hr_year_df)
print gg
print (gg)
gg = ggplot(aes(x='yearID', y='HR'), data = hr_year_df) + geom_point(color='coral') +
gg = ggplot(aes(x='yearID', y='HR'), data = hr_year_df) + geom_point(color='coral') + \
gg = ggplot(aes(x='yearID', y='HR'), data = hr_year_df) + geom_point(color='coral') + geom_line(color = 'red') + ggtitle ('HR vs Year') + xlab('Year') + ylab('Num of Homeruns')
print (gg)
hr_by_team_year_sf_la_csv  = pandas.read_csv('../lesson_4/hr_by_team_year_sf_la.csv')
test_plot = ggplot(hr_by_team_year_sf_la_csv, aes(x='yearID', y='HR', color='teamID')) + geom_point()
print(test_plot)
test_plot = ggplot(hr_by_team_year_sf_la_csv, aes(x='yearID', y='HR', color='teamID')) + geom_point() + xlab("Year") + ylab("Home Runs")
print(test_plot)
import pandas
from ggplot import *
def lineplot_compare(hr_by_team_year_sf_la_csv):
        # Write a function, lineplot_compare, that will read a csv file
        # called hr_by_team_year_sf_la.csv and plot it using pandas and ggplot.
        #
        # This csv file has three columns: yearID, HR, and teamID. The data in the
        # file gives the total number of home runs hit each year by the SF Giants 
        # (teamID == 'SFN') and the LA Dodgers (teamID == "LAN"). Produce a 
        # visualization comparing the total home runs by year of the two teams. 
        # 
        # You can see the data in hr_by_team_year_sf_la_csv
        # at the link below:
        # https://www.dropbox.com/s/wn43cngo2wdle2b/hr_by_team_year_sf_la.csv
        #
        # Note that to differentiate between multiple categories on the 
        # same plot in ggplot, we can pass color in with the other arguments
        # to aes, rather than in our geometry functions. For example, 
        # ggplot(data, aes(xvar, yvar, color=category_var)). This should help you 
        # in this exercise.
        hr_by_team_year_sf_la_csv = pandas.read_csv(hr_by_team_year_sf_la_csv)
        gg = ggplot(hr_by_team_year_sf_la_csv, aes(x='yearID', y='HR', color='teamID'))\
            + geom_point() + geom_line() + xlab("Year") + ylab("Home Runs")
        return gg
test_plot = ggplot(hr_by_team_year_sf_la_csv, aes(x='yearID', y='HR', color='teamID')) + geom_point() + geom_line() + xlab("Year") + ylab("Home Runs")
print(test_plot)
print In
print( In)
type(In)
type(Out)
%lsmagic
%history -f /tmp/history.py
