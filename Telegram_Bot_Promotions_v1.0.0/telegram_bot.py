# """
# ******************************************************************************/ 
# *                                                                            *
# *                           Telegram Bot for Promotions                      *
# *                                                                            *
# * DESCRIPTION:                                                               *
# * Questo programma consente a un utente di inviare messaggi promozionali     *
# * riguardanti prodotti tramite un bot di Telegram. Presenta una generazione  *
# * di messaggi con contenuti dinamici basati sull'input dell'utente. Il bot   *
# * risponde solo agli utenti autorizzati e invia messaggi a una chat di gruppo*
# *                                                                            *
# * Copyright (c) 2024, Nico Fontani                                           *
# * Creation Date: 3 Dec 2024                                                  *
# *                                                                            *
# * Original Author: Nico Fontani                                              *
# * Last Modified: 13 Dec 2024                                                 *
# *                                                                            *
# * Supported by Python and python-telegram-bot library                        *
# *                                                                            *
# * I commenti saranno in italiano perché parte di un progetto italiano.       *
# ******************************************************************************/
# """

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import random

# 20 messaggi di esempio
messages = [
    "🚀 Offerta del giorno! Acquista ora {product_name} a soli {price}! 🎉 Scopri di più su {link} 🌟",
    "🚨 Offerta imperdibile! Ottieni subito {product_name} a soli {price}! 🎁 Clicca qui per maggiori dettagli: {link} 🔥",
    "💥 Super sconto per te! Compra {product_name} ora a {price}! 😍 Non perdere questa occasione! {link}",
    "🎉 La tua occasione è arrivata! {product_name} a soli {price} 💰 Clicca subito per acquistare: {link} 🚀",
    "🔥 Offerta limitata! {product_name} è disponibile a soli {price}! 🏃‍♂️ Non lasciarti sfuggire questa promozione! {link}",
    "🌟 Offerta esclusiva! Acquista {product_name} a {price} e ricevi un regalo speciale! 🎁 Scopri di più su {link}",
    "🎁 Non perdere questa fantastica offerta! {product_name} è ora in sconto a {price}! ⏰ Clicca qui per acquistare: {link}",
    "💸 Solo per oggi! {product_name} a soli {price} 💥 Approfitta subito di questa promozione imperdibile! {link}",
    "🚀 Fai shopping con noi! Acquista {product_name} a {price} e risparmia subito! 🏷️ Clicca qui per maggiori dettagli: {link}",
    "🚀 Promozione da non perdere! {product_name} ora a {price}! 🌟 Clicca per scoprire l'offerta: {link}",
    "🎉 Il prodotto che desideravi è ora in offerta! {product_name} a {price} 😍 Affrettati, clicca subito su {link}",
    "🎁 Un regalo per te! Sconto speciale su {product_name} a {price}! 🎊 Non perdere tempo, visita {link} ora!",
    "🔥 Offerta imperdibile su {product_name}! Solo {price} per te! 🏷️ Clicca su {link} e approfitta subito!",
    "🌟 Solo per oggi! {product_name} a {price}! ⏳ Approfitta dell'offerta su {link} prima che scada!",
    "💥 Ultima occasione! {product_name} in sconto a {price}! 🚨 Clicca su {link} per non perdere l'offerta!",
    "🎉 Sconto speciale per te, {product_name} a {price}! 🏷️ Acquista subito su {link}!",
    "🚨 Solo oggi! Acquista {product_name} a {price}! 🛍️ Scopri di più su {link}!",
    "🌟 La tua occasione è ora! {product_name} in offerta a {price}! 🎉 Clicca subito su {link}!",
    "💥 Sconto speciale! {product_name} ora a {price}! 🎁 Non lasciarti sfuggire questa occasione su {link}",
    "🎊 Offerta straordinaria! {product_name} a soli {price} 🔥 Scopri di più su {link}",
]

# Funzione che seleziona un messaggio casuale
def generate_message(product_name, link, price):
    message = random.choice(messages)
    return message.format(product_name=product_name, link=link, price=price)

# Funzione che gestisce i messaggi privati
async def handle_private_message(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id

    # Verifica se il messaggio proviene dall'utente autorizzato
    if user_id != 123456789:  # Sostituisci con l'ID dell'utente autorizzato
        await update.message.reply_text("EH VOLEVI! GUARDA CHE FACCIA!")
        return

    text = update.message.text
    parts = text.split("|")  # Separiamo il messaggio in 3 parti usando "|" come delimitatore

    if len(parts) < 3:
        await update.message.reply_text("Per favore, invia il messaggio nel formato: <nome> | <link> | <prezzo>")
        return

    product_name, link, price = [part.strip() for part in parts]  # Rimuoviamo gli spazi extra

    ai_message = generate_message(product_name, link, price)

    # Risponde direttamente nel gruppo
    group_chat_id = "111111111111"  # Sostituisci con l'ID o il nome del tuo gruppo
    await context.bot.send_message(chat_id=group_chat_id, text=ai_message)

# Funzione di avvio
async def start(update: Update, context: CallbackContext):
    if update.message.from_user.id == 123456789:  # Sostituisci con l'ID dell'utente autorizzato
        await update.message.reply_text("Ciao! Inviami un prodotto nel formato: <nome> | <link> | <prezzo>")
    else:
        await update.message.reply_text("Questo bot non è per te! 😎")

# Funzione principale
def main():
    application = Application.builder().token("11112222333334444555566667777888999000").build()

    # Gestore del comando /start
    application.add_handler(CommandHandler("start", start))

    # Gestore dei messaggi privati
    application.add_handler(MessageHandler(filters.TEXT & filters.ChatType.PRIVATE, handle_private_message))

    application.run_polling()

if __name__ == "__main__":
    main()
