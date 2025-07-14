import re
import pandas as pd

def preprocess(data):
    # Updated pattern to handle both 12-hour and 24-hour formats
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s(?:am|pm)?\s?-\s'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    
    # Clean the date strings and convert to datetime
    df['message_date'] = df['message_date'].str.strip()
    
    # Try to parse dates with different formats
    def parse_date(date_str):
        # Remove the trailing ' - '
        date_str = date_str.rstrip(' - ')
        
        # Try 12-hour format first
        try:
            return pd.to_datetime(date_str, format='%d/%m/%Y, %I:%M %p')
        except:
            try:
                # Try 24-hour format
                return pd.to_datetime(date_str, format='%d/%m/%Y, %H:%M')
            except:
                # If both fail, return None
                return pd.NaT
    
    df['message_date'] = df['message_date'].apply(parse_date)
    
    # Drop rows with invalid dates
    df = df.dropna(subset=['message_date'])
    
    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    messages = []
    for message in df['user_message']:
        # Updated regex to handle phone numbers with country codes
        entry = re.split(r'([\w\W]+?):\s', message)
        if entry[1:]:  # user name
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)

    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df