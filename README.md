# csvubereats
oprogramowanie do obliczania csv

Po krótce jak ma wyglądać nasz program, spiszmy to co ustaliliśmy na urodzinach Pawła:

1. Uber, raz w tygodniu wystawia plik csv, w którym jest zestawienie zarobków naszych kierowców. Uber generuje plik na nasze życzenie, nie wiem czy jest jakieś API. Na ten moment będziemy wrzucać na ręcznie plik na nasz serwer.

2. Uruchamiamy program.

* program przetwarza plik csv
* na podstawie danych z csv tworzy odpowiednie rekordy w pliku excel
* tworzymy kopie pliku do bazy danych ( baza dany sqlite )

3. Biblioteki

* tablib [link](http://docs.python-tablib.org/en/latest/)

* openpyxl [link](https://bitbucket.org/openpyxl/openpyxl/src)

* PyQt5 [link](http://pyqt.sourceforge.net/Docs/PyQt5/)

* wszystko piszemy w pythonie > 3.3 - u siebie akutalnie mam 3.5.2.  

4. Na przyszłość:

* integracja z gdocs

* możliwość sterowania wypłatami w okienku

5. Wzorce

* wzorce projektowe w pythonie [link](https://www.youtube.com/watch?v=tJXhtncDBu4&feature=youtu.be)

* MVC [link](https://realpython.com/blog/python/the-model-view-controller-mvc-paradigm-summarized-with-legos/)


