from xml.dom.minidom import parse as xml_parser

class MyAnimeListXml(object):

    def __init__(self, filename):
        self.__file = xml_parser(filename)
        self.user_id = self.__get_items_by_tag_name("user_id")[0]
        self.anime_id = self.__get_items_by_tag_name("series_animedb_id")
        self.series_type = self.__get_items_by_tag_name("series_type")
        self.series_title = self.__get_items_by_tag_name("series_title")
        self.series_episodes = self.__get_items_by_tag_name("series_episodes")
        self.my_watched_episodes = self.__get_items_by_tag_name("my_watched_episodes")
        self.my_status = self.__get_items_by_tag_name("my_status")
        self.my_score = self.__get_items_by_tag_name("my_score")

    def __get_items_by_tag_name(self, tag):

        items = self.__file.getElementsByTagName(tag)
        return [item.firstChild.data for item in items]
