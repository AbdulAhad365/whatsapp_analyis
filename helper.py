from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji

extract = URLExtract()

def fetch_stats(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # fetch the number of messages
    num_messages = df.shape[0]

    # fetch the total number of words
    words = []
    for message in df['message']:
        if isinstance(message, str):
            words.extend(message.split())

    # fetch number of media messages (handle different media formats)
    media_patterns = ['<Media omitted>', '<Media omitted>\n', 'null', 'This message was deleted']
    num_media_messages = df[df['message'].isin(media_patterns)].shape[0]

    # fetch number of links shared
    links = []
    for message in df['message']:
        if isinstance(message, str):
            links.extend(extract.find_urls(message))

    return num_messages,len(words),num_media_messages,len(links)

def most_busy_users(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'name', 'user': 'percent'})
    return x,df

def create_wordcloud(selected_user,df):

    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    # Filter out media messages and deleted messages
    media_patterns = ['<Media omitted>', '<Media omitted>\n', 'null', 'This message was deleted']
    temp = temp[~temp['message'].isin(media_patterns)]

    def remove_stop_words(message):
        y = []
        if isinstance(message, str):
            for word in message.lower().split():
                if word not in stop_words:
                    y.append(word)
        return " ".join(y)

    if temp.empty:
        # Return a blank wordcloud if no messages
        wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
        return wc.generate("No messages available")
    
    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    temp['message'] = temp['message'].apply(remove_stop_words)
    
    # Combine all messages
    all_messages = temp['message'].str.cat(sep=" ")
    if not all_messages.strip():
        all_messages = "No messages available"
    
    df_wc = wc.generate(all_messages)
    return df_wc

def most_common_words(selected_user,df):

    f = open('stop_hinglish.txt','r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    # Filter out media messages and deleted messages
    media_patterns = ['<Media omitted>', '<Media omitted>\n', 'null', 'This message was deleted']
    temp = temp[~temp['message'].isin(media_patterns)]

    words = []

    for message in temp['message']:
        if isinstance(message, str):
            for word in message.lower().split():
                if word not in stop_words:
                    words.append(word)

    if not words:
        return pd.DataFrame(columns=[0, 1])
    
    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df

def emoji_helper(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []
    for message in df['message']:
        if isinstance(message, str):
            # Updated emoji detection for newer versions
            try:
                emojis.extend([c for c in message if c in emoji.UNICODE_EMOJI['en']])
            except:
                # Fallback for older emoji versions
                emojis.extend([c for c in message if emoji.is_emoji(c)])

    if not emojis:
        return pd.DataFrame(columns=[0, 1])
    
    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
    return emoji_df

def monthly_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline

def daily_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()

    return daily_timeline

def week_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

def month_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()

def activity_heatmap(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    return user_heatmap















