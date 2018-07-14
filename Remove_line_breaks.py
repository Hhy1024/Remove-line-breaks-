import win32clipboard as wc
import win32con

wc.OpenClipboard()
copy_text = wc.GetClipboardData(win32con.CF_TEXT)
wc.CloseClipboard()
#print(copy_text,type(copy_text))

copy_text = copy_text.decode("gb2312")
#print(copy_text,type(copy_text))

copy_text = copy_text.replace('\r\n',' ')
#print(copy_text,type(copy_text))

copy_text = copy_text.encode(encoding="gb2312")

wc.OpenClipboard()
wc.EmptyClipboard()
wc.SetClipboardData(win32con.CF_TEXT, copy_text)
wc.CloseClipboard()
print('done')