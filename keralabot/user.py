from keralabot.buttonbase import TelegramObject

class User(TelegramObject):
    """This object represents a Telegram user or bot.

    Attributes:
        id (:obj:`int`): Unique identifier for this user or bot.
        is_bot (:obj:`bool`): True, if this user is a bot
        first_name (:obj:`str`): User's or bot's first name.
        last_name (:obj:`str`): Optional. User's or bot's last name.
        username (:obj:`str`): Optional. User's or bot's username.
        language_code (:obj:`str`): Optional. IETF language tag of the user's language.
        can_join_groups (:obj:`str`): Optional. True, if the bot can be invited to groups.
            Returned only in :attr:`telegram.Bot.get_me` requests.
        can_read_all_group_messages (:obj:`str`): Optional. True, if privacy mode is disabled
            for the bot. Returned only in :attr:`telegram.Bot.get_me` requests.
        supports_inline_queries (:obj:`str`): Optional. True, if the bot supports inline queries.
            Returned only in :attr:`telegram.Bot.get_me` requests.
        bot (:class:`telegram.Bot`): Optional. The Bot to use for instance methods.

    Args:
        id (:obj:`int`): Unique identifier for this user or bot.
        is_bot (:obj:`bool`): True, if this user is a bot
        first_name (:obj:`str`): User's or bot's first name.
        last_name (:obj:`str`, optional): User's or bot's last name.
        username (:obj:`str`, optional): User's or bot's username.
        language_code (:obj:`str`, optional): IETF language tag of the user's language.
        can_join_groups (:obj:`str`, optional): True, if the bot can be invited to groups.
            Returned only in :attr:`telegram.Bot.get_me` requests.
        can_read_all_group_messages (:obj:`str`, optional): True, if privacy mode is disabled
            for the bot. Returned only in :attr:`telegram.Bot.get_me` requests.
        supports_inline_queries (:obj:`str`, optional): True, if the bot supports inline queries.
            Returned only in :attr:`telegram.Bot.get_me` requests.
        bot (:class:`telegram.Bot`, optional): The Bot to use for instance methods.

    """

    def __init__(self,
                 id,
                 first_name,
                 is_bot,
                 last_name=None,
                 username=None,
                 language_code=None,
                 can_join_groups=None,
                 can_read_all_group_messages=None,
                 supports_inline_queries=None,
                 bot=None,
                 **kwargs):
        # Required
        self.id = int(id)
        self.first_name = first_name
        self.is_bot = is_bot
        # Optionals
        self.last_name = last_name
        self.username = username
        self.language_code = language_code
        self.can_join_groups = can_join_groups
        self.can_read_all_group_messages = can_read_all_group_messages
        self.supports_inline_queries = supports_inline_queries
        self.bot = bot

        self._id_attrs = (self.id,)
