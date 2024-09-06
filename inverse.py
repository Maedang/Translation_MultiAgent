import os
import csv
import translation_agent as ta

def translate_text(source_lang, target_lang, country, source_text):
    translation = ta.translate(
        source_lang=source_lang,
        target_lang=target_lang,
        source_text=source_text,
        country=country,
    )
    return translation

def main():
    source_lang, target_lang, country = "English", "Vietnam", "Vietnamese"
    input_csv = '/Users/maidang/Desktop/MSDS/Capstone Project/translation-agent/examples/csv/eng.csv'
    output_csv = '/Users/maidang/Desktop/MSDS/Capstone Project/translation-agent/examples/csv/translation_agent_outputs_1.csv'
    translations = []

    # Read sentences from CSV
    with open(input_csv, 'r', encoding='utf-8') as infile:
        csv_reader = csv.reader(infile)
        # Assuming the CSV has a header
        header = next(csv_reader)
        
        count = 0
        for row in csv_reader:
            if count >= 100:
                break
            
            source_text = row[0]  # Assuming the sentence is in the first column
            print(f"Source text:\n\n{source_text}\n------------\n")
            translation = translate_text(source_lang, target_lang, country, source_text)
            print(f"Translation:\n\n{translation}\n------------\n")
            translations.append([source_text, translation])
            
            count += 1

    # Write translations to a new CSV file
    with open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(['Source Text', 'Translation'])  # Writing the header
        csv_writer.writerows(translations)
    
    print(f"Translations have been successfully written to {output_csv}")

if __name__ == "__main__":
    main()
