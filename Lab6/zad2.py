def foo(files: list, newfile: str) -> None:
    with open('./'+newfile, 'w', newline='') as f:
        for file in files:
            with open('./'+file, 'r', newline='') as fi:
                for row in fi:
                    f.write(row)
                    
foo(['zamowienia_niemcy.csv','zamowienia_polska.csv'],'nowa.csv')