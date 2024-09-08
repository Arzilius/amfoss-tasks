from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

TOKEN: Final= 'v7276859865:AAEhxOuZ81Vq1t6RA5M3RyGicclmJajIuvY'
BOT_USERNAME: Final = '@pagepal90210bot'

BOOK_NAME = 1

#commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! Welcome to PagePal! Feeling confused about what to read? "
        "Well, don't worry, I'll suggest books based on what YOU feel like reading. "
        "Type in /book to find a suitable book."
    )

#book
async def book_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I see you're looking for a book to read. Please enter a genre:")
    return BOOK_NAME  # Proceed to the next step where the bot expects the genre input

#preview
async def preview_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Enter the name of the book you want a preview for:")

#list
async def list_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please type in the name of your book:")
    return BOOK_NAME  # Wait for the user to input the book name

# Handling book name
async def receive_book_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    book_name = update.message.text
    
    # Storing the book name in the context for future use (optional)
    context.user_data['book_name'] = book_name
    
    await update.message.reply_text(f"You've entered: {book_name}")
    await update.message.reply_text("Now do /reading_list to proceed further.")
    return ConversationHandler.END  # End the conversation at this point

def handle_response(text: str) -> str:
    processed: str = text.lower()
    
    if 'hello' in processed:
        return 'Hey, wassup?'
            
    if 'how are you' in processed:
        return 'I am doing well, thank you!'
        
    if 'what do you do' in processed:
        return 'I recommend books based on your preferences.'
    
    return 'Please use /book to explore book recommendations.'

def main():
    # Create the Application and pass the bot token
    app = Application.builder().token(TOKEN).build()

    # Handlers for different commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('book', book_command))
    app.add_handler(CommandHandler('preview', preview_command))
    app.add_handler(CommandHandler('list', list_command))
    
    # Conversation handler to manage book name input
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('list', list_command)],
        states={
            BOOK_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_book_name)],
        },
        fallbacks=[],
    )
    
    app.add_handler(conv_handler)

    # Start polling for updates
    app.run_polling()

if __name__ == '__main__':
    main()

