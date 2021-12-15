
from pyrogram import __version__
from InlineBot import (
    OWNER_ID,
    FILTER_COMMAND,
    DELETE_COMMAND,
    CUSTOM_START_MESSAGE
)

if CUSTOM_START_MESSAGE:
    START_MESSAGE = CUSTOM_START_MESSAGE
else:
    START_MESSAGE = """<b>您好 {mention}爸爸,

我是您的数据筛选机器人</b> 
"""

HELP_MESSAGE = f"""<b><u>命令列表</u></b>

○ <b>/{FILTER_COMMAND.lower()}</b> <i>[keyword] [message or reply to message]</i>
    <i>添加 Inline 过滤器，可以使用 MarkDown 进行格式化</i>
    
○ <b>/{DELETE_COMMAND.lower()}</b> <i>[keyword]</i>
    <i>删除现有过滤器</i>
    
○ <b>/filters</b>
    <i>查看过滤器</i>
    
○ <b>/export</b>
    <i>导出过滤器的备份文件，这可以由其他人导入</i>
    
○ <b>/stats</b>
    <i>查看机器人的统计数据</i>
    
○ <b>/broadcast</b> <i>[reply to any message]</i>
    <i>向所有用户通知任何消息</i>
    
<b><u>仅所有者命令</u></b>

○ <b>/delall</b>
    <i>删除所有数据</i>
    
○ <b>/import</b> <i>[reply to an exported file]</i>
    <i>从备份文件导入数据库</i>
"""

ABOUT_MESSAGE = f"""<b><u>ABOUT ME</u></b>

<b>○ Maintained by : <a href='tg://user?id={OWNER_ID}'>This Person</a>
○ Channel : <a href='https://t.me/CodeXBotz'>Code 𝕏 Botz</a>
○ Support : <a href='https://t.me/CodeXBotzSupport'>Code 𝕏 Botz Support</a>
○ Source Code : <a href='https://github.com/CodeXBotz/Inline-Filter-Bot'>Click here</a>
○ Language : <a href='https://www.python.org/'>Python 3</a>
○ Library : <a href='https://github.com/pyrogram/pyrogram'>Pyrogram Asyncio {__version__}</a></b>
"""

MARKDOWN_HELP = """<b><u>Markdown Formatting</u></b>

○ <b>Bold Words</b> :
    format: <code>*Bold Text*</code>
    show as: <b>粗体</b>
    
○ <b>Italic Text</b>
    format: <code>_Italic Text_</code>
    show as: <i>斜体</i>
    
○ <b>Code Words</b>
    format: <code>`Code Text`</code>
    show as: <code>代码</code>
    
○ <b>Under Line</b>
    format: <code>__UnderLine Text__</code>
    show as: <u>下划线</u>
    
○ <b>StrikeThrough</b>
    format: <code>~StrikeThrough Text~</code>
    show as: <s>删除线</s>
    
○ <b>Hyper Link</b>
    format: <code>[Text](https://t.me/ffpphh)</code>
    show as: <a href='https://t.me/ffpphh'>Text</a>
    
○ <b>Buttons</b>
    <u>Url Button</u>:
    <code>[Button Text](buttonurl:https://t.me/ffpphh)</code>
    <u>Alert Button</u>:
    <code>[Button Text](buttonalert:重要事项)</code>
    <u>In Sameline</u>:
    <code>[Button Text](buttonurl:https://t.me/ffpphh:same)</code></i>

○ <b>Notes:</b>
    <i>格式化时将每个按钮保持在同行</i>
    <i>您的提醒消息文本必须少于 200 个字符，否则机器人将忽略该按钮</i>

○ <b>提示：</b> <i>您可以在/+命令中添加贴纸和视频笔记按钮</i>"""
