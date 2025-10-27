class StringUtils:
    """
    Класс с полезными утилитами для обработки и анализа строк
    """

    def capitalize(self, string: str) -> str:
        """
        Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
        Пример: capitalize("skypro") -> "Skypro"
        """
        return string.capitalize()

    def trim(self, string: str) -> str:
        """
        Принимает на вход текст и удаляет пробелы в начале и конце строки
        Пример: trim("   skypro   ") -> "skypro"
        """
        return string.strip()
    
    def to_list(self, string: str, delimiter=',') -> list[str]:
        """
        Принимает на вход текст с разделителем и возвращает список строк.
        Параметры:
            string - строка для обработки
            delimiter - разделитель строк. По умолчанию запятая (",")
        Пример 1: to_list("a,b,c,d") -> ["a", "b", "c", "d"]
        Пример 2: to_list("1:2:3", ":") -> ["1", "2", "3"]
        """
        if not string or self.is_empty(string):
            return []
        return string.split(delimiter)

    def contains(self, string: str, symbol: str) -> bool:
        """
        Возвращает True, если строка содержит искомый символ и False - если нет
        Пример 1: contains("SkyPro", "S") -> True
        Пример 2: contains("SkyPro", "U") -> False
        """
        return symbol in string

    def delete_symbol(self, string: str, symbol: str) -> str:
        """
        Удаляет все подстроки из переданной строки
        Параметры:
            string - строка для обработки
            symbol - искомый символ для удаления
        Пример 1: delete_symbol("SkyPro", "k") -> "SyPro"
        Пример 2: delete_symbol("SkyPro", "Pro") -> "Sky"
        """
        return string.replace(symbol, '')

    def starts_with(self, string: str, symbol: str) -> bool:
        """
        Возвращает True, если строка начинается с заданного символа и False - если нет
        Пример 1: starts_with("SkyPro", "S") -> True
        Пример 2: starts_with("SkyPro", "P") -> False
        """
        return string.startswith(symbol)

    def is_empty(self, string: str) -> bool:
        """
        Возвращает True, если строка пустая или состоит только из пробелов, и False - если нет
        Пример 1: is_empty("") -> True
        Пример 2: is_empty(" ") -> True
        Пример 3: is_empty("SkyPro") -> False
        """
        return string.strip() == ''
