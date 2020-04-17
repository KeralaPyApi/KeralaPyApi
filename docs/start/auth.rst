Authorization
=============

Bots are a special kind of users that are authorized via their tokens (instead of phone numbers), which are created by
the `Bot Father`_. Bot tokens replace the users' phone numbers only — you still need to
:doc:`configure a Telegram API key <../intro/setup>` with KeralaPyApi, even when using bots.

.. code-block:: python

    import keralabot

    bot = keralabot.bot("TOKEN")
    # Replace TOKEN With Token you got from @BotFather
    
    bot.polling()
