import csv
import tkinter as tk
from tkinter import filedialog

def wybierz_plik_csv():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="Wybierz plik CSV", filetypes=[("Pliki CSV", "*.csv")])

    return file_path

def main():
    path_to_csv = wybierz_plik_csv()

    if not path_to_csv:
        print("Nie wybrano pliku CSV. Przerwano program.")
        return

    with open(path_to_csv, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data2 = []
        data3 = {}
        ile_dup = 0
        different_translations_count = 0

        with open('duplicates.csv', 'w', newline='') as duplicates_file:
            csv_writer = csv.writer(duplicates_file)

            for line in csv_reader:
                data = [line['ID'], line['language'], line['source_text'], line['translated_text']]

                for duplicates in data:
                    if duplicates not in data2:
                        data2.append(duplicates)
                    else:
                        csv_writer.writerow([duplicates])
                        ile_dup += 1

            source = line['source_text']
            text = line['translated_text']
            if source in data3:
                if data3[source] != text:
                    print(f"Dla source_text {source}, różne tłumaczenia: '{data3[source]}' i '{text}'")
                    different_translations_count += 1
            else:
                data3[source] = text

    print(f"Ilość wykasowanych dubli to: {ile_dup}")
    print(f"Ilość tekstów z różnym tłumaczeniem to: {different_translations_count}")
    print(data2)

if __name__ == "__main__":
    main()







































