import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    city = ''
    while city not in ('chicago', 'new york city', 'washington'):
        print('Enter the city')
        city = input().lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    while month not in ('all','january', 'february', 'march', 'april', 'may', 'june'):
        print('Enter the month')
        month = input().lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
        print('Enter the day')
        day = input().lower()

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
    df = pd.read_csv(CITY_DATA[city])

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print(popular_month)

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.weekday_name
    popular_day = df['day'].mode()[0]
    print(popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Popular Start Station: ',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Popular End Station: ',df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df["trip"] = df["Start Station"].map(str) + ' ' + df['End Station']
    print('Popular Station Combination: ',df['trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time: ", df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("Mean travel time: ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("User types: ", df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print(df['Gender'].value_counts())
    else:
        print("No gender column")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("Most Common Year: ", df['Birth Year'].mode()[0])
        print("Most Recent Year: ", df['Birth Year'].max())
        print("Earliest Year: ", df['Birth Year'].min())
    else:
        print("No birth year column data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
    i = 0
    while True:
        print(df.iloc[i: i+5])
        i +=5
        load_raw_data = input("\n Load raw 5 rows of raw data? Yes or No. \n")
        if load_raw_data.lower() != 'yes':
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
