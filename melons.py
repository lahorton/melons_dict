import robots


class Melon(object):
    """Melon."""
    def __init__(self, melon_type):
        """Initialize melon.

        melon_type: type of melon being built.
        """

        self.melon_type = melon_type
        self.weight = 0.0
        self.color = None
        self.stickers = []



    def prep(self):
        """Prepare the melon."""

        robots.cleanerbot.clean(self)
        robots.stickerbot.apply_logo(self)


    def __str__(self):
        """Print out information about melon."""

        if self.weight <= 0:
            return self.melon_type
        else:
            return "{} {:.2f} lbs {}".format(self.color,
                                             self.weight,
                                             self.melon_type)

class Squash(Melon):
    "Squash"""


    def __init___(self, squash_type):
        """Initialize squash"""
        """ sqush_type: type of squash being processed"""
        self.sqush_type = squash_type
        self.weight = 0.0
        self.color = None
        self.stickers = []


    def prep_painting(self):
        """paints the squashes to look like melons"""
        robots.cleanerbot.clean(self)
        robots.stickerbot.apply_logo(self)
        robots.painterbot.paint(self)


    def __str__(self):
        """Print out information about squash"""
        if self.weight <= 0:
            return self.melon_type
        else:
            return "{} {:.2f} lbs {}".format(self.color,
                                             self.weight,
                                             self.melon_type)
