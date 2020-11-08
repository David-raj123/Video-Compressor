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
    
    
    DOWNLOAD_START = "Iam Downloading ⬇️... \n"
    
    UPLOAD_START = "Iam Uploading⬆️... \n"
    
    COMPRESS_START = "Compressing The File.."
    
    RCHD_BOT_API_LIMIT = "Size Greater Than Maximum Allowed Size (50MB). Neverthless, Trying To Upload."
    
    RCHD_TG_API_LIMIT = "Downloaded In {} Seconds.\nDetected File Size: {}\nSorry. But, I Cannot Upload Files Greater Than 1.5GB Due To Telegram API Limitations."
    
    COMPRESS_SUCCESS = "⭕Downloaded in {}\n\n⭕Compressed In {}\n\n⭕Uploaded In {}\n\nThanks For Using Me Please Join @TeluguCartoonWorld❤️"

    COMPRESS_PROGRESS = "⭕ ETA: {}\n⭕ Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom Video / File Thumbnail Saved. This Image Will Be Used In The Video / File."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom Thumbnail Cleared Successfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    
    SAVED_RECVD_DOC_FILE = "✅ Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail Found."
    
    NO_VOID_FORMAT_FOUND = "Sorry You Cant Use It Use Please Try Again With Correct One\n{}"
    
    USER_ADDED_TO_DB = "⭕User <a href='tg://user?id={}'>{}</a> Added To {} Till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "Already One Process Is Going On. \n Or \n A Media Already Exists. \n  Please Send /cancel To Delete Existingng Media."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Hi I Am Video Compressor Bot \n\n1. Please Send Me Any Telegram Big File I Will Try My Best To Convert It On To Small File \n2. Reply To The File - /compress And Persentage \nEg:- <code>/compress 50</code> \n\nAny Doubts Ask My Master :- @David9010"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "Current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
