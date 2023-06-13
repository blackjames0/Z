#!/usr/bin/env python3

YT_HELP_MESSAGE = """
<b>To use the commands, follow this format:</b>
<code>/{cmd} link options</code> or replying to link </b>
<code>/{cmd} options</code>

• <code>-s:</code> Select quality for specific link or links.
• <code>-z password:</code> Create a password-protected zip file.
• <code>-n new_name:</code> Rename the file.
• <code>-id drive_folder_link or drive_id -index https://anything.in/0:</code> Upload to a custom drive.
• <code>-opt playliststart:^10|fragment_retries:^inf|matchtitle:S13|writesubtitles:true|live_from_start:true|postprocessor_args:{{"ffmpeg": ["-threads", "4"]}}|wait_for_video:(5, 100):</code> Set additional options.
• <code>-i 10:</code> Process multiple links.
• <code>-b:</code> Perform bulk download by replying to a text message or file with links separated with new line.

<b>Check all yt-dlp api options from this <a href='https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L184'>FILE</a> or use this <a href='https://t.me/mltb_official_channel/177'>script</a> to convert cli arguments to api options.</b>
"""

MIRROR_HELP_MESSAGE = """
<b>To use the commands, follow this format:</b>
<code>/{cmd} link options</code> or replying to link </b>
<code>/{cmd} options</code>

<b>Options:</b>
• <code>-n new name:</code> Rename the file or folder.
• <code>-z or -z password:</code> Zip the file or folder with or without password.
• <code>-e or -e password:</code> Extract the file or folder with or without password.
• <code>-up upload destination:</code> Upload the file or folder to a specific destination.
• <code>-id drive_folder_link</code> or <code>-id drive_id -index https://anything.in/0:</code>: Upload to a custom Google Drive folder or ID.
• <code>-au username -ap password:</code> Provide authorization for a direct link.
• <code>-s:</code> Select a torrent file.
• <code>-d ratio:seed_time:</code> Set the seeding ratio and time for a torrent.
• <code>-i number of links/files:</code> Process multiple links or files.
• <code>-m folder name:</code> Process multiple links or files within the same upload directory.
• <code>-b:</code> Perform bulk download by replying to a text message or file with multiple links separated with new line.
• <code>-j:</code> Join split files together before extracting or zipping.
• <code>-rcf:</code> Set Rclone flags for the command.
• <code>main:dump/ubuntu.iso</code> or <code>rcl:</code> Treat a path as an rclone download.

<b>Note:</b>
• <b>Commands starting with qb are specifically for torrents.</b>
• Some commands may require additional user access or settings.
"""

RSS_HELP_MESSAGE = """
Use this format to add feed URL:
Title1 link (required)
Title2 link -c cmd -inf xx -exf xx
Title3 link -c cmd -d ratio:time -z password

-c command + any arg
-inf: For included words filter.
-exf: For excluded words filter.

Example: Title <code>https://www.rss-url.com</code> inf: 1080 or 720 or 144p|mkv or mp4|hevc exf: flv or web|xxx opt: up: mrcc:remote:path/subdir rcf: --buffer-size:8M|key|key:value
This filter will parse links that have titles containing "(1080 or 720 or 144p) and (mkv or mp4) and hevc" and don't contain (flv or web) and xxx words. You can add whatever you want.

Another example: inf: 1080 or 720p|.web. or .webrip.|hevc or x264
This will parse titles that contain (1080 or 720p) and (.web. or .webrip.) and (hevc or x264). 
Note: I added spaces before and after "1080" to avoid wrong matching. If there is a number like "10805695" in the title, it won't match "1080" without spaces after it.

<b>Filter Notes:</b>
1. | means "and."
2. Add "or" between similar keys. For example, you can add it between qualities or between extensions. Avoid filters like "f: 1080|mp4 or 720|web" because this will parse "1080" and (mp4 or 720) and web, instead of (1080 and mp4) or (720 and web).
3. You can add "or" and "|" as much as you want.
4. Check the title for static special characters before or after the qualities, extensions, or other elements, and use them in the filter to avoid wrong matches.

<b>Timeout:</b> 60 sec.

<b>Please apply the same formatting to this message:</b>
"""

CLONE_HELP_MESSAGE = """
Send Gdrive|Gdot|Filepress|Filebee|Appdrive|Gdflix link or rclone path along with command or by replying to the link/rc_path by command.

<b>Multi links only by replying to first gdlink or rclone_path:</b>
<code>/{cmd}</code> -i 10 (number of links/pathies)

<b>Gdrive:</b>
<code>/{cmd}</code> gdrivelink

<b>Upload Custom Drive:</b> link -id -index
-id <code>drive_folder_link</code> or <code>drive_id</code> -index <code>https://anything.in/0:</code>
drive_id must be a folder ID, and index must be a URL, otherwise it will not accept.

<b>Rclone:</b>
<code>/{cmd}</code> (rcl or rclone_path) -up (rcl or rclone_path) -rcf flagkey:flagvalue|flagkey|flagkey:flagvalue

Note: If -up is not specified, the rclone destination will be the RCLONE_PATH from config.env.
"""

CATEGORY_HELP_MESSAGE = """
Reply to an active /{cmd} which was used to start the download or add gid along with {cmd}.
This command is mainly for changing the category in case you decide to change the category of an already added download.
But you can always use /{mir} with to select the category before the download starts.

<b>Upload Custom Drive:</b>
<code>/{cmd}</code> -id <code>drive_folder_link</code> or <code>drive_id</code> -index <code>https://anything.in/0:</code> gid or by replying to an active download.
drive_id must be a folder ID, and index must be a URL, otherwise, it will not be accepted.
"""