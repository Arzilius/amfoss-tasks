import csv
import os
import requests
from typing import Final
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes, ConversationHandler

# Replace with your tokens
TOKEN: Final = 'your_telegram_token'
GOOGLE_BOOKS_API_KEY: Final = 'your_google_books_api_key'
GOOGLE_BOOKS_API_URL: Final = 'https://www.googleapis.com/books/v1/volumes'

BOOK_NAME = 1  # For state management
READING_LIST = "reading_list.csv"  # For the reading list

# Start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! Welcome to PagePal! Feeling confused on what to read? "
        "Well, don't worry, I'll be here to suggest you books based on what YOU feel like reading.\n"
        "Type in /book to find a suitable book."
    )

# Book command to get genre and fetch books
async def book_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I see you're looking for a book to read. Enter a genre:")
    return BOOK_NAME

# Fetch books and return a CSV file
async def receive_genre(update: Update, context: ContextTypes.DEFAULT_TYPE):
    genre = update.message.text
    query = f'subject:{genre}'

    # Call Google Books API to fetch books of the given genre
    response = requests.get(GOOGLE_BOOKS_API_URL, params={
        'q': query,
        'key': GOOGLE_BOOKS_API_KEY,
        'maxResults': 5,
    })

    if response.status_code == 200:
        data = response.json()
        if 'items' in data:
            books = data['items']

            # Prepare CSV data
            with open('book_list.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Author', 'Description', 'Year', 'Language', 'Preview Link', 'Rating'])

                for book in books:
                    title = book['volumeInfo'].get('title', 'Unknown Title')
                    authors = book['volumeInfo'].get('authors', ['Unknown Author'])
                    description = book['volumeInfo'].get('description', 'No description available.')
                    published_date = book['volumeInfo'].get('publishedDate', 'Unknown Year')
                    language = book['volumeInfo'].get('language', 'Unknown Language')
                    preview_link = book['volumeInfo'].get('previewLink', 'No Preview')
                    rating = book['volumeInfo'].get('averageRating', 'No Rating')

                    writer.writerow([title, ', '.join(authors), description, published_date, language, preview_link, rating])

            await update.message.reply_document(open('book_list.csv', 'rb'))
        else:
            await update.message.reply_text("No books found for this genre.")
    else:
        await update.message.reply_text("Error fetching data from Google Books API.")

    return ConversationHandler.END

# Preview command
async def preview_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Enter the name of the book (case sensitive) for which you want the preview link:")

# Handle book preview
async def receive_preview_book(update: Update, context: ContextTypes.DEFAULT_TYPE):
    book_name = update.message.text
    query = f'intitle:{book_name}'

    # Call Google Books API to fetch book preview
    response = requests.get(GOOGLE_BOOKS_API_URL, params={
        'q': query,
        'key': GOOGLE_BOOKS_API_KEY,
        'maxResults': 1,
    })

    if response.status_code == 200:
        data = response.json()
        if 'items' in data:
            book = data['items'][0]
            preview_link = book['volumeInfo'].get('previewLink', 'No Preview Available')
            await update.message.reply_text(f"Preview link: {preview_link}")
        else:
            await update.message.reply_text("No preview available for this book.")
    else:
        await update.message.reply_text("Error fetching data from Google Books API.")

# List and reading list management
async def list_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please type in the name of your book:")
    return BOOK_NAME

async def reading_list_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Display options: Add, Delete, View
    keyboard = [
        [InlineKeyboardButton("Add a Book", callback_data='add')],
        [InlineKeyboardButton("Delete a Book", callback_data='delete')],
        [InlineKeyboardButton("View Reading List", callback_data='view')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Choose an option:', reply_markup=reply_markup)

# Callback for the inline buttons
async def reading_list_action(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    action = query.data

    if action == 'add':
        await query.edit_message_text(text="Enter the name of the book to add to your reading list:")
        return BOOK_NAME
    elif action == 'delete':
        await query.edit_message_text(text="Enter the name of the book to delete from your reading list:")
        return BOOK_NAME
    elif action == 'view':
        if os.path.exists(READING_LIST):
            await query.edit_message_text(text=f"Your reading list:\n{open(READING_LIST).read()}")
        else:
            await query.edit_message_text(text="Your reading list is empty.")

# Add to the reading list
async def add_to_reading_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    book_name = update.message.text
    with open(READING_LIST, 'a', newline='', encoding='utf-8') as file:
        file.write(f'{book_name}\n')

    await update.message.reply_text(f"{book_name} added to your reading list.")

# Delete from the reading list
async def delete_from_reading_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    book_name = update.message.text
    if os.path.exists(READING_LIST):
        with open(READING_LIST, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(READING_LIST, 'w', encoding='utf-8') as file:
            for line in lines:
                if line.strip("\n") != book_name:
                    file.write(line)

        await update.message.reply_text(f"{book_name} deleted from your reading list.")
    else:
        await update.message.reply_text("Your reading list is empty.")

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "/start - Start the bot\n"
        "/book - Search for books by genre and receive a CSV file with book details\n"
        "/preview - Get a preview link for a specific book\n"
        "/list - Manage your reading list (add, delete, view)\n"
        "/help - Display this help message"
    )
    await update.message.reply_text(help_text)

# Main function to run the bot
def main():
    # Create the Application and pass the bot token
    app = Application.builder().token(TOKEN).build()

    # Handlers for commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('book', book_command))
    app.add_handler(CommandHandler('preview', preview_command))
    app.add_handler(CommandHandler('list', list_command))
    app.add_handler(CommandHandler('reading_list', reading_list_command))
    app.add_handler(CommandHandler('help', help_command))

    # Callback handler for buttons
    app.add_handler(CallbackQueryHandler(reading_list_action))

    # Conversation handler for adding and deleting books
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('book', book_command)],
        states={
            BOOK_NAME: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, receive_genre),
                MessageHandler(filters.TEXT & ~filters.COMMAND, add_to_reading_list),
                MessageHandler(filters.TEXT & ~filters.COMMAND, delete_from_reading_list)
            ],
        },
        fallbacks=[CommandHandler('cancel', help_command)],
    )

    # Add the conversation handler
    app.add_handler(conv_handler)

    # Start polling for updates
    app.run_polling()

if __name__ == '__main__':
   main()
