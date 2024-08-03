from crewai_tools import YoutubeChannelSearchTool
from dotenv import load_dotenv
load_dotenv()
#initalize
yt_tool=YoutubeChannelSearchTool(youtube_channel_handle='@EverythingMoney')
