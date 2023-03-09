# Formula 1 Data Analysis

<h1 align="center">
    <img src="https://logodownload.org/wp-content/uploads/2016/11/formula-1-logo-1-1.png" width="400px">    
</h1>

## Purpose

I am a Formula 1 nerd as well as a nerd that feels the need to understand my
passions to the fullest. I have a Computer Science background and would like to
put my long forgotten match and data science skills to the test as well as
udnerstand a bit better the world of engineering that goes into a Formula 1
weekend. In that sense, this projet is an attempt to make sense of the data that
the cars produce and perhaps preview the development cicles of the teams and
some race weekends result tendencies.

### Tools

#### Fastest Lap of Session Comparator

This tool allows to compare the fastest lap between two drivers in a specified
session of a also specified grand prix. The information provided goes from the
speed at any given time during the lap as well as brake and throttle percentages
at all times. Here is a usage example:

```bash
python3 fastest_session_lap_analysis.py -year 2023 -grand_prix Bahrain -session Q -driver_1 VER -driver_2 LEC
```

In this example where asking for a detailed comparison between Verstappen's and
Leclerc's fastest laps during the qualifying for the grand prix that took place
in Bahrain in the year of 2023.
