-- assert lua script
-- ===================|
-- note to escape path for winodws (c:\\users\\user\\...)

local utils = require 'mp.utils'

-- Log function: log to both terminal and MPV OSD (On-Screen Display)
function log(string,secs)
	secs = secs or 2.5
	mp.msg.warn(string)
	mp.osd_message(string,secs)
end
-- extract string between colons
function extract_between_colons(input_string)
    local start_index = 0
    local end_index = 0
    local count = 0
    for i = 1, #input_string do
        if input_string:sub(i, i) == ":" then
            count = count + 1
            if count == 2 then
                start_index = i
            elseif count == 3 then
                end_index = i
                break
            end
        end
    end
    if start_index > 0 and end_index > 0 then
        return input_string:sub(start_index + 1, end_index - 1)
    else
        return nil
    end
end

-- download/load function
function assert()

	--get sn number
	local url = mp.get_property('path')
	--get second ":" to third ":" from url
	log(url)
	if string.find(url, "bahamut")
	then
		local sn = extract_between_colons(url)
		log(sn)


		-- get script directory 
		local directory = mp.get_script_directory()

		-- under windows platform, convert path format
		if string.find(directory, "\\")
		then
			string.gsub(directory, "/", "\\")
		end
		log('彈幕')
		local py_path = ''..directory..'\\Danmu2Ass_baha.py'
		
		-- choose to use python or .exe
		log('彈幕正在準備')
		-- run python to get comments
		local args = {sn, directory}  -- 請將這裡的參數更改為你需要傳入的參數

		utils.subprocess({args={''..directory..'\\Danmu2Ass_baha.exe', unpack(args)}})

		log('彈幕下載完成')
		log(directory)
		local subtitle_path = ''..directory..'\\123.ass'
		mp.commandv('sub-add', subtitle_path)

		log('彈幕匯入完成')
	end
end

-- toggle_subtitles.lua
local subtitles_visible = true

function toggle_subtitles()
	if subtitles_visible then
		mp.set_property("sub-visibility", "no")
	else
		mp.set_property("sub-visibility", "yes")
	end
	subtitles_visible = not subtitles_visible
end

mp.add_key_binding('j',	"toggle_subtitles", toggle_subtitles)
mp.register_event("start-file", assert)
