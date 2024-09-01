from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
    ContextTypes,
)

from telegram_bot.utils import load_token, create_keyboard, fetch_results

(
    JOB_SITE,
    POSITION,
    EXPERIENCE,
    LOCATION,
    SALARY,
    TECHNOLOGIES,
    RESULTS,
    BACK,
    START_OVER,
) = range(9)

TOKEN = load_token()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    reply_markup = create_keyboard(["Work.ua", "Robota.ua", "Both"])
    await update.message.reply_text(
        "Please choose the job site:", reply_markup=reply_markup
    )
    return JOB_SITE


async def job_site(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_text = update.message.text
    if user_text.lower() in ["work.ua", "robota.ua", "both"]:
        context.user_data["job_site"] = user_text.lower().replace(".", "_")
    else:
        await update.message.reply_text(
            "Invalid site. Please choose one of the options:"
        )
        return JOB_SITE

    await update.message.reply_text(
        "You selected: {}. Now, please enter the job position:".format(user_text)
    )
    reply_markup = create_keyboard(["Skip"])
    await update.message.reply_text(
        "Please enter the job position:", reply_markup=reply_markup
    )
    return POSITION


async def position(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_text = update.message.text
    if user_text.lower() != "skip":
        context.user_data["position"] = user_text
    else:
        context.user_data["position"] = None

    keyboard = [[KeyboardButton("Skip")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    await update.message.reply_text(
        "Position recorded. Please enter the required experience:",
        reply_markup=reply_markup,
    )
    return EXPERIENCE


async def experience(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_text = update.message.text
    if user_text.lower() != "skip":
        try:
            context.user_data["experience"] = int(user_text)
        except ValueError:
            await update.message.reply_text(
                "Invalid input. Please enter a number or 'skip':"
            )
            return EXPERIENCE
    else:
        context.user_data["experience"] = None

    keyboard = [[KeyboardButton("Skip")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    await update.message.reply_text(
        "Please enter the location:", reply_markup=reply_markup
    )
    return LOCATION


async def location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_text = update.message.text
    if user_text.lower() != "skip":
        context.user_data["location"] = user_text
    else:
        context.user_data["location"] = None

    keyboard = [[KeyboardButton("Skip")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    await update.message.reply_text(
        "Please enter the salary expectations:", reply_markup=reply_markup
    )
    return SALARY


async def salary(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_text = update.message.text
    if user_text.lower() != "skip":
        try:
            salary_expectation = list(map(int, user_text.split("-")))
            context.user_data["salary"] = salary_expectation
        except ValueError:
            await update.message.reply_text(
                "Invalid input. Please enter a valid salary range or 'skip':"
            )
            return SALARY
    else:
        context.user_data["salary"] = None

    keyboard = [[KeyboardButton("Enter Technologies")], [KeyboardButton("Start Over")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    await update.message.reply_text(
        "Please enter the technologies (comma-separated) or choose 'Start Over':",
        reply_markup=reply_markup,
    )
    return TECHNOLOGIES


async def technologies(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_text = update.message.text
    if user_text.lower() == "start over":
        return await start(update, context)

    if user_text.lower() != "enter technologies":
        context.user_data["technologies"] = [
            tech.strip() for tech in user_text.split(",")
        ]
    else:
        await update.message.reply_text(
            "Please enter the technologies (comma-separated):"
        )
        return TECHNOLOGIES

    await update.message.reply_text(
        "Searching for candidates based on your criteria..."
    )
    links = fetch_results(context.user_data)
    result_text = "\n".join(links)
    await update.message.reply_text(f"Here are the top 5 resumes:\n{result_text}")
    return ConversationHandler.END


def main():
    application = ApplicationBuilder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            JOB_SITE: [MessageHandler(filters.TEXT & ~filters.COMMAND, job_site)],
            POSITION: [MessageHandler(filters.TEXT & ~filters.COMMAND, position)],
            EXPERIENCE: [MessageHandler(filters.TEXT & ~filters.COMMAND, experience)],
            LOCATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, location)],
            SALARY: [MessageHandler(filters.TEXT & ~filters.COMMAND, salary)],
            TECHNOLOGIES: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, technologies)
            ],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == "__main__":
    main()
