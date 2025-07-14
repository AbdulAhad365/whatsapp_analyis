# WhatsApp Chat Analysis Tool

A comprehensive Streamlit-based web application for analyzing WhatsApp chat exports. This tool provides detailed insights into your chat patterns, user activity, and content analysis.

## 🚀 Features

- **📊 Statistical Analysis**: Message counts, word counts, media sharing, and link sharing statistics
- **📈 Timeline Analysis**: Monthly and daily message trends
- **🗺️ Activity Maps**: Most busy days, months, and weekly activity heatmaps
- **👥 User Analysis**: Most active users and their contribution percentages
- **☁️ Word Cloud**: Visual representation of most frequently used words
- **📝 Content Analysis**: Most common words with filtering
- **😊 Emoji Analysis**: Emoji usage statistics and distribution
- **🔍 Multi-format Support**: Handles both 12-hour and 24-hour time formats

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/AbdulAhad365/whatsapp_analyis.git
cd whatsapp_analyis
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 📱 Usage

1. **Export your WhatsApp chat**:
   - Open WhatsApp on your phone
   - Go to the chat you want to analyze
   - Tap on the chat name → Export Chat → Without Media
   - Save the .txt file

2. **Run the application**:
```bash
streamlit run app.py
```

3. **Analyze your chat**:
   - Upload your WhatsApp chat .txt file using the sidebar
   - Select a user or "Overall" for group analysis
   - Click "Show Analysis" to generate insights

## 📋 Supported Chat Formats

The tool supports WhatsApp chat exports in the following formats:

- **12-hour format**: `27/05/2025, 7:12 pm - Username: Message`
- **24-hour format**: `27/05/2025, 19:12 - Username: Message`
- **International phone numbers**: `+92 312 0119537: Message`
- **Various media formats**: `<Media omitted>`, `null`, `This message was deleted`

## 🔧 Key Components

### `app.py`
Main Streamlit application with user interface and visualization components.

### `preprocessor.py`
Handles data preprocessing including:
- Date parsing (both 12-hour and 24-hour formats)
- User extraction
- Message cleaning
- Time period calculations

### `helper.py`
Contains analysis functions:
- Statistical calculations
- Timeline generation
- Activity mapping
- Word cloud creation
- Emoji analysis

### `stop_hinglish.txt`
Contains stop words for filtering common words in Hinglish (Hindi-English mix).

## 📊 Analytics Available

### 1. Top Statistics
- Total messages sent
- Total words used
- Media files shared
- Links shared

### 2. Timeline Analysis
- Monthly message trends
- Daily activity patterns

### 3. Activity Maps
- Most busy day of the week
- Most busy month
- Weekly activity heatmap

### 4. User Analysis (Group Chats)
- Most active users
- Message contribution percentages

### 5. Content Analysis
- Word cloud visualization
- Most frequently used words
- Emoji usage statistics

## 🐛 Debugging Features

- File size and format validation
- Processing status information
- Date range verification
- User count display
- Sample data preview

## 🔧 Recent Improvements

- ✅ Fixed date format parsing issues
- ✅ Enhanced media message detection
- ✅ Improved phone number handling
- ✅ Added comprehensive error handling
- ✅ Updated emoji detection methods
- ✅ Added debugging information

## 📦 Dependencies

- streamlit
- pandas
- matplotlib
- seaborn
- wordcloud
- urlextract
- emoji
- collections

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with Streamlit for the web interface
- Uses matplotlib and seaborn for visualizations
- WordCloud library for text visualization
- Emoji library for emoji analysis

## 📞 Support

If you encounter any issues or have questions:
1. Check the debugging information in the sidebar
2. Ensure your chat export format matches the supported formats
3. Open an issue on GitHub with your problem description

## 🔮 Future Enhancements

- [ ] Sentiment analysis
- [ ] Language detection
- [ ] Export analysis reports
- [ ] Multiple file analysis
- [ ] Advanced filtering options
- [ ] Real-time chat monitoring

---

**Note**: This tool is designed for personal use and educational purposes. Always respect privacy and obtain necessary permissions before analyzing chat data.
