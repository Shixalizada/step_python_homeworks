class Film:
    def __init__(self, ad, il, reyting):
        self.ad = ad
        self.il = il
        self.reyting = reyting

    @property
    def reyting(self):
        return self._reyting

    @reyting.setter
    def reyting(self, value):
        if not 0 <= value <= 10:
            raise ValueError("Reyting 0-10 aralığında olmalıdır")
        self._reyting = value

    def __str__(self):
        return f"{self.ad} ({self.il}) - reyting {self.reyting}"

    @classmethod
    def from_string(cls, text):
        ad, il, reyting = text.split("|")
        return cls(ad, int(il), float(reyting))

    def __eq__(self, other):
        if not isinstance(other, Film):
            return NotImplemented
        return self.ad == other.ad and self.il == other.il

    def __hash__(self):
        return hash((self.ad, self.il))


class FilmSiyahisi:
    def __init__(self):
        self.filmler = []

    def elave_et(self, film):
        self.filmler.append(film)

    def __len__(self):
        return len(self.filmler)

    def en_yaxsi(self):
        if not self.filmler:
            return None
        return max(self.filmler, key=lambda f: f.reyting)


if __name__ == "__main__":
    print("=== DƏRS 3 ===")

    f = Film("Inception", 2010, 8.8)
    print(f)

    f2 = Film.from_string("Interstellar|2014|8.6")
    print(f2)

    siyahi = FilmSiyahisi()
    siyahi.elave_et(Film.from_string("Inception|2010|8.8"))
    siyahi.elave_et(Film.from_string("Interstellar|2014|8.6"))

    print("Film sayı:", len(siyahi))
    print("Ən yaxşı film:", siyahi.en_yaxsi())

    print("Eynilik yoxlaması:", Film("Inception", 2010, 7.0) == Film("Inception", 2010, 9.0))
    print("Set ölçüsü:", len({
        Film("Inception", 2010, 8.8),
        Film("Inception", 2010, 9.1)
    }))
