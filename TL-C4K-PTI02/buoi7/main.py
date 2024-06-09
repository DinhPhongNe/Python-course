import operator

from data_io import load_json_data, write_json_data

class AnimeItem:
    def __init__(self, title, release_date, rating):
        self.title = title
        self.release_date = release_date
        self.rating = rating

    def get_info(self):
        return f"{self.title} phat hanh vao {self.release_date} co thu hang {self.rating}"


class AnimeDatabase:
    def __init__(self):
        # danh sách các anime mang kiểu dữ liệu đối tương (dùng để thao tác với chương trình, show lên ứng dụng)
        self.anime_item_list = list()
        # danh sách anime dưới dạng dữ liệu json (dùng để ghi dữ liệu xuống db)
        self.anime_dict_data = load_json_data()

    def items_to_json_data(self):
        json_data = list()
        for anime in self.anime_item_list:
            json_data.append(anime.__dict__)
        return json_data

    def load_data_from_json(self):
        for anime_dict in self.anime_dict_data:
            anime = AnimeItem(
                title = anime_dict["title"],
                release_date = anime_dict["release_date"],
                rating = anime_dict["rating"])
            self.anime_item_list.append(anime) 

    def show_list_anime(self):
        print("Danh sach cac anime hien tai: ")
        for anime in self.anime_item_list:
            print(anime.get_info())

    def get_first_item_by_title(self, anime_title):
        for anime in self.anime_item_list:
            if anime.title == anime_title:
                return anime
        # No item found
        return False

    def add_item(self, anime_dict):
        
        new_item = AnimeItem(
            title = anime_dict["title"],
            release_date = anime_dict["release_date"],
            rating = anime_dict["rating"])
        
        self.anime_item_list.append(new_item) 


        self.anime_dict_data.append(anime_dict)

        write_json_data(self.anime_dict_data)

    def edit_item(self, edit_title, new_dict):
        matched = self.get_first_item_by_title(edit_title)

        if matched:
            matched.update(new_dict)
            self.anime_dict_data = self.items_to_json_data()
            write_json_data(self.anime_dict_data)
    
    def delete_item(self, delete_item):
        matched = self.get_first_item_by_title(delete_item)

        if matched:
            self.anime_item_list.remove(matched)
            self.anime_dict_data = self.items_to_json_data()

            write_json_data(self.anime_dict_data)

    def sort_item_by_rating(self, top=None):
        self.anime_item_list = sorted(self.anime_item_list, 
                key=operator.attrgetter('rating'), reverse=True
        )
        if top:
            return self.anime_item_list[top]


anime_management = AnimeDatabase()

anime_management.load_data_from_json()
anime_management.show_list_anime()

anime_management.add_item({"title": "Pokem", "release_date": "2023-02-23", "rating": 12})