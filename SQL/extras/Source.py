import re
import time
from datetime import datetime
from Arab import StartTime, iqthon
from Arab.Config import Config
from Arab.plugins import mention
help1 = ("**🝳 ⦙ كيفيه التنصيب :**")
help2 = ("**🝳 ⦙ قـائمـه الاوامـر :**\n**🝳 ⦙ قنـاه السـورس :** @JIBTHON\n**🝳 ⦙ شـرح اوامـر السـورس : @JIBTHON**\n**🝳 ⦙ شـرح فـارات السـورس : @czziii** \n - اوامر الاونلاين تشتغل فقط في المجموعات ")
TG_BOT = Config.TG_BOT_USERNAME
TM = time.strftime("%I:%M")
Sour = f"**‎⿻┊My 𖠄 {mention} ٫ **\n‌‎**⿻┊BoT 𖠄 {TG_BOT} ٫**\n**‌‎⿻┊TimE 𖠄 {TM} ٫**\n**‌‎⿻┊‌‎VeRsIoN 𖠄 (7.7) ,** \n**⿻┊‌‎TeLeThoN AraB 𖠄** @IQTHON"
