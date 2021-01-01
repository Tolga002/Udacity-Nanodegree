import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv','new york city': 'new_york_city.csv','washington': 'washington.csv' }
MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

def get_filters():
    """Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter"""

    print('Hello! Let\'s explore some US bikeshare data!')
    city_n = ''

    while city_n.lower() not in CITY_DATA: # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        city_n= input("\nWhich city would you like to filter? Washington, New York City, or Chicago?\n")
        if city_n.lower() in CITY_DATA:
            city = CITY_DATA[city_n.lower()]
        else:
            print("Sorry, I didn't get this. Could You Please Try Again.\n")


    month_n = '' # TO DO: get user input for month (all, january, february, ... , june)
    while month_n.lower() not in MONTH_DATA:
        month_n = input("\nWhich month would you like to filter by? January, February, March, April, May, June or type 'all' if you do not have any preference?\n")
        if month_n.lower() in MONTH_DATA:
            month = month_n.lower()
        else:
            print("Sorry, I didn't get this. Could You Please Try Again.\n")


    day_n = '' # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day_n.lower() not in DAY_DATA:
        day_n = input("\nAre you looking for a particular day? If so, kindly enter the day as follows: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you do not have any preference.\n")
        if day_n.lower() in DAY_DATA:
            day = day_n.lower()
        else:
            print("Sorry, I didn't get this. Could You Please Try Again.\n")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day"""
    # load data file into a dataframe
    df = pd.read_csv(city)

    df['Start Time'] = pd.to_datetime(df['Start Time']) # convert the Start Time column to datetime

    ######################### Extract month and day of week from Start Time to create new columns ##########################

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTH_DATA.index(month)

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    ################### TO DO: display the most common month ##########################

    pop_month = df['month'].mode()[0]
    print("Most Common Month : " + MONTH_DATA[pop_month].title())

    # TO DO: display the most common day of week
    pop_day = df['day_of_week'].mode()[0]
    print("Most Common Day : " + pop_day)

    # TO DO: display the most common start hour
    pop_hour = df['hour'].mode()[0]
    print("Most Common Hour : " + str(pop_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    ####################### TO DO: display most commonly used start station ###########################

    Start_Station = df['Start Station'].mode()[0]
    print("Most Commonly used start station : " + Start_Station)

    ########################## TO DO: display most commonly used end station ################################

    End_Station = df['End Station'].mode()[0]
    print("Most Commonly used end station : " + End_Station)

    ############## TO DO: display most frequent combination of start station and end station trip ################

    Combination_Station = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("Most Commonly used combination of start station and end station trip : " + str( Combination_Station.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    ######################### TO DO: display total travel time ################################

    Total_Travel_Time = df['Trip Duration'].sum()
    print("Total travel time : " + str(Total_Travel_Time))

    ########################## TO DO: display mean travel time #########################

    Mean_Travel_Time = df['Trip Duration'].mean()
    print("Mean travel time : " + str(Mean_Travel_Time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    ###################### TO DO: Display counts of user types ############################

    user_types = df['User Type'].value_counts()
    print("User Types : \n" + str(user_types))

    ####################### TO DO: Display counts of gender ###############################

    if city == 'chicago.csv' or city == 'new_york_city.csv':
        gender = df['Gender'].value_counts()
        print("Gender Types : \n" + str(gender))

        ####################### TO DO: Display earliest, most recent, and most common year of birth ########################

        Earliest_Year = df['Birth Year'].min()
        Most_Recent_Year = df['Birth Year'].max()
        Most_Common_Year = df['Birth Year'].mode()[0]
        print('Earliest Year : {}\n'.format(Earliest_Year))
        print('Most Recent Year : {}\n'.format(Most_Recent_Year))
        print('Most Common Year : {}\n'.format(Most_Common_Year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Displays raw data on user request."""
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])

######################### MAIN FUNCTION ################################

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            view_raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()