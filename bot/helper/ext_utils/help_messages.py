#!/usr/bin/env python3

YT_HELP_MESSAGE = """
<b>Send link along with command line</b>:
<code>/{cmd}</code> link -s -n new name -opt x:y|x1:y1

<b>By replying to link</b>:
<code>/{cmd}</code> -n new name -z password -opt x:y|x1:y1

<b>New Name</b>: -n
<code>/{cmd}</code> link -n new name
Note: Don't add file extension.

<b>Upload Custom Drive</b>: link -id -index
-id <code>drive_folder_link</code> or <code>drive_id</code> -index <code>https://anything.in/0:</code>
drive_id must be folder id and index must be url else it will not accept

<b>Quality Buttons</b>: -s
Incase default quality added from yt-dlp options using format option and you need to select quality for specific link or links with multi links feature.
<code>/{cmd}</code> link -s

<b>Zip</b>: -z password
<code>/{cmd}</code> link -z (zip)
<code>/{cmd}</code> link -z password (zip password protected)

<b>Options</b>: -opt
<code>/{cmd}</code> link -opt playliststart:^10|fragment_retries:^inf|matchtitle:S13|writesubtitles:true|live_from_start:true|postprocessor_args:{{"ffmpeg": ["-threads", "4"]}}|wait_for_video:(5, 100)
Note: Add `^` before integer or float, some values must be numeric and some string.
Like playlist_items:10 works with string, so no need to add `^` before the number but playlistend works only with integer so you must add `^` before the number like example above.
You can add tuple and dict also. Use double quotes inside dict.

<b>Multi links only by replying to first link</b>: -i
<code>/{cmd}</code> -i 10(number of links)

<b>Multi links within same upload directory only by replying to first link</b>: -m
<code>/{cmd}</code> -i 10(number of links) -m folder name

<b>Upload</b>: -up
<code>/{cmd}</code> link -up <code>rcl</code> (To select rclone config, remote and path)
You can directly add the upload path: -up remote:dir/subdir
If DEFAULT_UPLOAD is `rc` then you can pass up: `gd` to upload using gdrive tools to GDRIVE_ID.
If DEFAULT_UPLOAD is `gd` then you can pass up: `rc` to upload to RCLONE_PATH.
If you want to add path manually from your config (uploaded from usetting) add <code>mrcc:</code> before the path without space
<code>/{cmd}</code> link -up <code>mrcc:</code>main:dump

<b>Rclone Flags</b>: -rcf
<code>/{cmd}</code> link -up path|rcl -rcf --buffer-size:8M|--drive-starred-only|key|key:value
This will override all other flags except --exclude
Check here all <a href='https://rclone.org/flags/'>RcloneFlags</a>.

<b>Bulk Download</b>: -b
Bulk can be used by text message and by replying to text file contains links seperated by new line.
You can use it only by reply to message(text/file).
All options should be along with link!
Example:
link1 -n new name -up remote1:path1 -rcf |key:value|key:value
link2 -z -n new name -up remote2:path2
link3 -e -n new name -opt ytdlpoptions
Note: You can't add -m arg for some links only, do it for all links or use multi without bulk!
link pswd: pass(zip/unzip) opt: ytdlpoptions up: remote2:path2
Reply to this example by this cmd <code>/{cmd}</code> b(bulk)
You can set start and end of the links from the bulk with -b start:end or only end by -b :end or only start by -b start. The default start is from zero(first link) to inf.


Check all yt-dlp api options from this <a href='https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L184'>FILE</a> or use this <a href='https://t.me/mltb_official_channel/177'>script</a> to convert cli arguments to api options.
"""

MIRROR_HELP_MESSAGE = """
<b>To use the commands, follow this format:</b>
<code>/{cmd} link <options></code>

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
• <code>-b:</code> Perform bulk download by replying to a text file with links.
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