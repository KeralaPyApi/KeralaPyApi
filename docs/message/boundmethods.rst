Message Handlers
================

Message handlers are used to register commands, regex, callbacks, etc

Message handler
---------------

Message Handler is used to recognize messages in pm.

.. code-block:: python
    
    @bot.message_handler(commands=['start'])
    # This registers a command /start

Example:

.. code-block:: python

    import keralabot

    bot = keralabot.bot("TOKEN")

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.reply_to(message, "Hello world!")

    # Starts the bot
    bot.polling()
