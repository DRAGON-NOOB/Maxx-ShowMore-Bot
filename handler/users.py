from telethon import custom, events
from garnet import FSMContext, MessageText
from garnet.router import Router
import logging
from const import CONSTANTS

logging.basicConfig(level = logging.ERROR)

user_router = Router(event = events.NewMessage())


@user_router.on(MessageText.commands('start'))
async def start_rout_hndlr(update: custom.Message, context: FSMContext):
	await update.reply("**Hey Bruh!Currently, bot is in beta version**"
	                   "\n\n**𝗨𝗦𝗔𝗚𝗘𝗦👇:**"
	                   "\n\t➕ Add this bot to the channel (preferrably, a test channel)"
	                   "\n\n📮𝗜𝗻𝘀𝗽𝗶𝗿𝗮𝘁𝗶𝗼𝗻,"
	                   "\n\t`Like in blogs/sites, I will add a showmore button at the bottom of posts.` "
	                   "`if user is interested in reading the full posts, they can read it by pressing **ShowMore** button`"
	                   f"\n\n**Note**: "
	                   f"\n\t✅ Bot will only shrunk the posts if the post length is greater than {CONSTANTS.TRUNC+20}words",
	                   buttons = [[custom.Button.url(text = "👲 𝗗𝗘𝗩𝗟𝗢𝗣𝗘𝗥 👲",
	                                                 url = 't.me/MaxxRider')],
	                              [custom.Button.url(text = "🏷️𝗧𝗵𝗲 𝗣𝗼𝘀𝘁𝗔𝗽𝗽𝗲𝗻𝗱𝗲𝗿🏷️",
	                                                 url = 't.me/PostAppender_Bot')],
	                              [custom.Button.url(text = "📌 𝗕𝗢𝗧 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 📌",
	                                                 url = 'https://t.me/MaxxBots')]])

@user_router.on(MessageText.commands('about'))
async def about_rout_hndlr(update: custom.Message, context: FSMContext):
	await update.reply("**TESTING 😄**"
	                   buttons = [[custom.Button.url(text = "👲 𝗗𝗘𝗩𝗟𝗢𝗣𝗘𝗥 👲",
	                                                 url = 't.me/MaxxRider')],
	                              [custom.Button.url(text = "🏷️𝗧𝗵𝗲 𝗣𝗼𝘀𝘁𝗔𝗽𝗽𝗲𝗻𝗱𝗲𝗿🏷️",
	                                                 url = 't.me/PostAppender_Bot')],
	                              [custom.Button.url(text = "📌 𝗕𝗢𝗧 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 📌",
	                                                 url = 'https://t.me/MaxxBots')]])
