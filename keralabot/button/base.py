try:
    import ujson as json
except ImportError:
    import json

from abc import ABCMeta


class TelegramObject(object):
    """Base class for most telegram objects."""

    __metaclass__ = ABCMeta
    _id_attrs = ()

    def __str__(self):
        return str(self.to_dict())

    def __getitem__(self, item):
        return self.__dict__[item]

    @classmethod
    def de_json(cls, data, bot):
        if not data:
            return None

        data = data.copy()

        return data

    def to_json(self):
        """
        Returns:
            :obj:`str`

        """

        return json.dumps(self.to_dict())

    def to_dict(self):
        data = dict()

        for key in iter(self.__dict__):
            if key in ('bot',
                       '_id_attrs',
                       '_credentials',
                       '_decrypted_credentials',
                       '_decrypted_data',
                       '_decrypted_secret'):
                continue

            value = self.__dict__[key]
            if value is not None:
                if hasattr(value, 'to_dict'):
                    data[key] = value.to_dict()
                else:
                    data[key] = value

        if data.get('from_user'):
            data['from'] = data.pop('from_user', None)
        return data

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._id_attrs == other._id_attrs
        return super(TelegramObject, self).__eq__(other)  # pylint: disable=no-member

    def __hash__(self):
        if self._id_attrs:
            return hash((self.__class__, self._id_attrs))  # pylint: disable=no-member
        return super(TelegramObject, self).__hash__()
