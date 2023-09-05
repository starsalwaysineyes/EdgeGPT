import asyncio, json
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle

from EdgeGPT.EdgeUtils import Query, Cookie
Cookie.dir_path="/workspaces/EdgeGPT/bing_cookies"
async def main():
    bot = await Chatbot.create() # 导入 cookie 是“可选”的，如前所述
    response = await bot.ask(prompt="Hello world", conversation_style=ConversationStyle.creative, simplify_response=True)
    print(json.dumps(response, indent=2)) # 返回下面这些
    """
{
    "text": str,
    "author": str,
    "sources": list[dict],
    "sources_text": str,
    "suggestions": list[str],
    "messages_left": int
}
    """
    await bot.close()

if __name__ == "__main__":
    asyncio.run(main())