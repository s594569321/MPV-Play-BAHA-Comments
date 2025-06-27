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
    local start_index = input_string:find("%%3A")
    if not start_index then return nil end
    start_index = start_index + 3 -- move past %3A

    local end_index = input_string:find("%%3A", start_index)
    if not end_index then return nil end

    local result = input_string:sub(start_index, end_index - 1)
    if result:match("^%d+$") and #result <= 10 then
        return result
    else
        return nil
    end
end

-- download/load function
function assert()
	--mp.set_property('ytdl-raw-options', 'cookies=' .. mp.command_native({'expand-path', '~~/cookies.txt'}))
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
		local CK_ = ""
		local info = debug.getinfo(1, "S")
		local script_path = info.source:sub(2)  -- 移除開頭的 @ 字元
		print("完整路徑：", script_path)

		-- 取出資料夾路徑（去掉檔名）
		local dir = script_path:match("^(.*[\\/])")  -- 可處理 Windows 和 Linux 的路徑分隔符
		local handle = io.popen('dir "' .. dir .. '" /b')  -- /b = 只列檔名，不加額外資訊
		if handle then
			
    	for file in handle:lines() do
			
        	if file:match("%.txt$") and file:find("cookies") then
           		log("Found cookie file: " .. file)
				os.execute("sleep " .. tonumber(2))
            	local f = io.open(file, "r")
            	if f then
                	for line in f:lines() do
                    	if line:find("BAHARUNE\t") then
                        	local value = line:match("BAHARUNE\t(.+)")
                        	CK_ = "BAHARUNE=" .. (value or ""):gsub("\n", "") .. ";"
							log('Cookie: ' .. CK_)
							break
                    	end
                	end
                	f:close()
            	end
        	end
    	end
    	handle:close()
		end
	
	
		local args = {sn, directory,CK_}  -- 請將這裡的參數更改為你需要傳入的參數

		utils.subprocess({args={''..directory..'\\Danmu2Ass_baha.exe', unpack(args)}})
		
		--utils.subprocess({args={'python', py_path, unpack(args)}})
		--log('彈幕下載完成')
		--log(directory)
		local subtitle_path = ''..directory..'\\123.ass'
		mp.commandv('sub-add', subtitle_path)

		--log('彈幕匯入完成')
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
