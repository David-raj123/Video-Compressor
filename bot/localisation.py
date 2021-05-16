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
    START_TEXT = "**Hai , I Am Video Compress Bot.**"
   
    ABS_TEXT = "**It's Abs Text, I Can't Do That.**"
    
    FORMAT_SELECTION = "Select The Format To Convert Or Download: <a href='{}'>File Size Might Be Approximate</a> \nSend Photo To Set custom thumbnail Or Use /deletethumbnail To Clear Thumbnail Data."
    
    DOWNLOAD_START = "**Downloading ⬇️**"
    
    UPLOAD_START = "**Uploading ⬆️**"
    
    COMPRESS_START = "**Compressing The File..⏳**"
    
    RCHD_BOT_API_LIMIT = "**Size Greater Than Maximum Allowed Size (50MB). Neverthless, Trying To Upload.**"
    
    RCHD_TG_API_LIMIT = "⭕**Downloaded In** {} **Seconds**.\n⭕**Detected File Size** : {}\n**Sorry. But, I Cannot Upload Files Greater Than 1.9GB Due To Telegram API Limitations.**"
    
    COMPRESS_SUCCESS = "⭕**Downloaded In** {}\n⭕**Compressed In** {}\n**⭕Uploaded In** {}\n**© David_Botz**"

    COMPRESS_PROGRESS = "**⭕ETA** : {}\n⭕**Progress** : {}%"

    SAVED_CUSTOM_THUMB_NAIL = "**Custom Video / File Thumbnail Saved. This Image Will Be Used In The Video / File.**"
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "**✓ Custom Thumbnail Cleared Successfully.**"
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "**✓ Media cleared succesfully.**"
    
    SAVED_RECVD_DOC_FILE = "**✓ Downloaded Successfully.**"
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "**No Custom ThumbNail Found.**"
    
    NO_VOID_FORMAT_FOUND = "**Sorry You Cant Use It , Please Try Again With Correct One\n{}**"
    
    USER_ADDED_TO_DB = "⭕User <a href='tg://user?id={}'>{}</a> Added To {} Till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "**Already One Person Using Me**""
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "<b>Hi I Am Video Compressor Bot \n\n1. Please Send Me Any Telegram Big File I Will Try My Best To Convert It On To Small File \n2. Reply To The File - /compress And Persentage \nEg:- <code>/compress 50</code> \n\nAny Doubts Ask My Master :- @David_Botz</b>"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "Current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
