"""
import win32com.client
cat  = win32com.client.Dispatch("SAPI.SpObjectTokenCategory")
cat.SetID(r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices", False)
for token in cat.EnumerateTokens():
    print(token.GetDescription())
"""

import win32com.client
sapi = win32com.client.Dispatch("SAPI.SpVoice")
cat  = win32com.client.Dispatch("SAPI.SpObjectTokenCategory")
cat.SetID(r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices", False)
v = [t for t in cat.EnumerateTokens() if t.GetAttribute("Name") == "Microsoft Sayaka"]
if v:
    oldv = sapi.Voice
    sapi.Voice = v[0]
    sapi.Speak("今日もいちにち頑張りましょう")
    sapi.Voice = oldv
