import unicodedata

def generate_mails(filename: str, domain: str) -> None:
    with open('./mails.txt', 'w', newline='') as f:
        with open('./'+filename, 'r', newline='') as fi:
            for row in fi:
                name = unicodedata.normalize('NFD', row.replace("\r","").replace("\n","")).encode('utf-8','ignore').decode('ascii','ignore')
                f.write(name.lower().replace(" ",".")+f"@{domain}\n")
                
generate_mails("names.txt","student.uwm.edu.pl")