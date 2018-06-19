import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new_york_city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    

   # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city = input("Choose the City you want to see the bikeshare statistics. 1.chicago 2.new_york_city 3.washington\n")
      if city=='chicago' or city=='washington' or city=='new_york_city':
        break
        
    # TO DO: get user input for month (all, january, february, ... , june)   
    while True:
      month = input("Enter the Month. If you want to see the statistics for all the months Enter 'all'.\n")
      if month=='january' or month=='february' or month=='march' or month=='april' or month=='may' or month=='june' or month=='all':
        break
     
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("Enter the day of the week. To choose the whole week enter 'all'.\n")
      if day=='monday' or day=='tuesday' or day=='wednesday' or day=='thursday' or day=='friday' or day=='saturday' or day=='sunday' or day=='all':
        break
           
    print('-'*40)
    return city, month, day
    
 

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    if city == 'chicago':
        df = pd.read_csv('chicago.csv')
    elif city == 'new_york_city':
      df = pd.read_csv('new_york_city.csv')
    elif city == 'washington':
      df = pd.read_csv('washington.csv')

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df



def time_stats(df):
  """Displays statistics on the most frequent times of travel."""
  print('\nCalculating The Most Frequent Times of Travel...\n')
  start_time = time.time()
  
  
  # convert the Start Time column to datetime
  df['Start Time'] = pd.to_datetime(df['Start Time'])
  
  # TO DO: display the most common month
  df['month'] = df['Start Time'].dt.month
  popular_month = df['month'].mode()[0]
  print('Most Popular Month:', popular_month)
  
  # TO DO: display the most common day of week
  df['dayofweek'] = df['Start Time'].dt.weekday
  popular_DayOfWeek = df['dayofweek'].mode()[0]
  print('Most Popular Day of The Week:', popular_DayOfWeek)
  
  
  # TO DO: display the most common start hour
  df['hour'] = df['Start Time'].dt.hour
  popular_hour = df['hour'].mode()[0]
  print('Most Popular Start Hour:', popular_hour)
  
  
  print("\nThis took %s seconds." % (time.time() - start_time))
  print('-'*40)


def station_stats(df):
  """Displays statistics on the most popular stations and trip."""
  print('\nCalculating The Most Popular Stations and Trip...\n')
  start_time = time.time()

  # TO DO: display most commonly used start station
  
  StartStation = df['Start Station'].mode()[0]
  print("Most Popular Start Station is ",StartStation)
  
  # TO DO: display most commonly used end station
  EndStation = df['End Station'].mode()[0]
  print("Most Popular End Station is ",EndStation)
  df['Concat Table']=df['Start Station'] + " and " + df['End Station']
  
  # TO DO: display most frequent combination of start station and end station trip
  Start_End =  df['Concat Table'].mode()[0]
  print("Most frequent combination of start station and end station trip is ",Start_End)
  print("\nThis took %s seconds." % (time.time() - start_time))
  print('-'*40)


def trip_duration_stats(df):
  """Displays statistics on the total and average trip duration."""

  print('\nCalculating Trip Duration...\n')
  start_time = time.time()

  # TO DO: display total travel time
  total_traveltime = df['Trip Duration'].sum()
  print("Total Travel Time", total_traveltime)
  
  # TO DO: display mean travel time
  traveltime_mean = df['Trip Duration'].mean()
  print("Mean Travel Time", traveltime_mean)

  print("\nThis took %s seconds." % (time.time() - start_time))
  print('-'*40)


def user_stats(df):
  """Displays statistics on bikeshare users."""

  print('\nCalculating User Stats...\n')
  start_time = time.time()

  # TO DO: Display counts of user types
  user_types = df['User Type'].value_counts()
  print(user_types)
  
  # TO DO: Display counts of gender
  Gender = df['Gender'].value_counts()
  print(Gender)
  
  # TO DO: Display earliest, most recent, and most common year of birth
  Earliest_year = df['Birth Year'].min()
  print("The Earliest Birth Year is ", Earliest_year)
  Recent_year = df['Birth Year'].max()
  print("The Most Recent Birth Year is ", Recent_year)
  Common_year = df['Birth Year'].mode()[0]
  print("The Most Common Birth Year is ", Common_year)
  


  print("\nThis took %s seconds." % (time.time() - start_time))
  print('-'*40)


def main():
  while True:
      city, month, day = get_filters()
      df = load_data(city, month, day)

      time_stats(df)
      station_stats(df)
      trip_duration_stats(df)
      user_stats(df)


      restart = input('\nWould you like to restart? Enter yes or no.\n')
      if restart.lower() != 'yes':
          break


if __name__ == "__main__":
    main()
