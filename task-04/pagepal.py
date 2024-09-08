from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

TOKEN: Final= 'v7276859865:AAEhxOuZ81Vq1t6RA5M3RyGicclmJajIuvY'
BOT_USERNAME: Final = '@pagepal90210bot'

book_name = 1

#commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #start command
    await update.message.reply_text("Hello! Welcome to Pagepal! Feeling confused on what to read? Well don't worry, I'll be here to suggest you books based on what YOU feel like reading. Type in /book to find a suitable book")
    
async def book_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #book command
    await update.message.reply_text("I see you're looking for a book to read. Please enter a genre:")
    book_name
async def preview_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #preview command
    await update.message.reply_text("Enter the name of the book you want a preview for:")
    
async def list_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #list command
    await update.message.reply_text("Type in your book name")
    return book_name  

async def receive_book_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    book_name = update.message.text
    
    await update.message.reply_text(f"You've entered: {book_name}")
    await update.message.reply_text("now do /reading_list to proceed further")
    return ConversationHandler.END  # End the conversation
    
def handle_response(text: str) -> str:
    processed: str = text.lower()
    
    if  'hello' in text:
        return 'Hey wassup'
            
    if 'how are you' in text:
        return 'I am doing well'
        
    if 'What do you do' in text:
        return 'I recommend you books'
    
    return 'Please do /books to use my abilities'
    
    
