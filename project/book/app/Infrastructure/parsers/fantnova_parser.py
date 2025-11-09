import requests
from bs4 import BeautifulSoup

from ...Application.dto import ParsedBookDTO


class FantNovaParser:
    def parse(self, url: str) -> ParsedBookDTO:
        html = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).text

        soup = BeautifulSoup(html, "html.parser")

        # Заголовок
        title = soup.find("h1").get_text(strip=True)

        # Картинка
        img_tag = soup.select_one(".pmovie__poster img")
        image_url = img_tag.get("data-src") if img_tag else None

        # Основные параметры
        year = author = reader = time = cycle = None
        genres = []

        for li in soup.select(".pmovie__header-list li"):
            label = li.find("div").get_text(strip=True)
            value = li.get_text(strip=True).replace(label, "").strip()

            if label.startswith("Год"):
                year = value
            elif label.startswith("Автор"):
                author = li.find("a").get_text(strip=True)
            elif label.startswith("Читает"):
                reader = li.find("a").get_text(strip=True)
            elif label.startswith("Время"):
                time = value
            elif label.startswith("Цикл"):
                raw_cycle = li.get_text(strip=True).replace("Цикл:", "").strip()
                if "№" in raw_cycle:
                    cycle_name, cycle_number = raw_cycle.split("№", 1)
                    cycle_name = cycle_name.strip()
                    cycle_number = cycle_number.strip()
                else:
                    cycle_name = raw_cycle
                    cycle_number = None

                cycle = cycle_name

            elif label.startswith("Жанр"):
                genres = [a.get_text(strip=True) for a in li.find_all("a")]

        desc_block = soup.select_one(".page__text")
        description = desc_block.get_text(" ", strip=True) if desc_block else None

        return ParsedBookDTO(
            title=title,
            age=year,
            author_name=author,
            reader_name=reader,
            time=time,
            cycle_name=cycle,
            cycle_number=cycle_number,
            category=genres,
            # image_url=image_url,
            description=description,
        )