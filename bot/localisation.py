#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) PublicLeech Author(s)
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "Hello , \n\nThis Is A Telegram Video Compress Bot \n\n<b>Please Send Me Any Telegram Big File I Will Try My Best To Convert It To Small File</b> \n\n/help for more details ... \n\nBy @David9010"
   
    ABS_TEXT = " Please Dont Be Selfish."
    
    FORMAT_SELECTION = "Select The Format To Convert Or Download: <a href='{}'>File Size Might Be Approximate</a> \nSend Photo To Set custom thumbnail Or Use /deletethumbnail To Clear Thumbnail Data."
    
    
    DOWNLOAD_START = "<b>Downloading ⬇️</b>"
    
    UPLOAD_START = "<b>Uploading⬆️</b>"
    
    COMPRESS_START = "<b>Compressing The File..⏳</b>"
    
    RCHD_BOT_API_LIMIT = "<b>Size Greater Than Maximum Allowed Size (50MB). Neverthless, Trying To Upload.</b>"
    
    RCHD_TG_API_LIMIT = "⭕<b>Downloaded In</b> {} </b>Seconds</b>.\n⭕<b>Detected File Size</b> : {}\n</b>Sorry. But, I Cannot Upload Files Greater Than 1.9GB Due To Telegram API Limitations.<b>"
    
    COMPRESS_SUCCESS = "⭕<b>Downloaded In</b> {}\n⭕<b>Compressed In</b> {}\n</b>⭕Uploaded In</b> {}\n<b>Thanks For Using Me Please Join @David_Botz</b>"

    COMPRESS_PROGRESS = "<b>⭕ETA</b> : {}\n⭕<b>Progress </b>: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "<b>Custom Video / File Thumbnail Saved. This Image Will Be Used In The Video / File.</b>"
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "<b>✓ Custom Thumbnail Cleared Successfully.</b>"
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "<b>✓ Media cleared succesfully.</b>"
    
    SAVED_RECVD_DOC_FILE = "<b>✓ Downloaded Successfully.</b>"
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "<b>No Custom ThumbNail Found.</b>"
    
    NO_VOID_FORMAT_FOUND = "<b>Sorry You Cant Use It , Please Try Again With Correct One\n{}</b>"
    
    USER_ADDED_TO_DB = "⭕User <a href='tg://user?id={}'>{}</a> Added To {} Till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "<b>Already One Person Using Me"
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "<b>Hi I Am Video Compressor Bot \n\n1. Please Send Me Any Telegram Big File I Will Try My Best To Convert It On To Small File \n2. Reply To The File - /compress And Persentage \nEg:- <code>/compress 50</code> \n\nAny Doubts Ask My Master :- @David_Botz</b>"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "Current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
