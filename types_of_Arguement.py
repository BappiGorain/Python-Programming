def position_Arguement(f_name, l_name):
	print(f"hello {f_name} {l_name}")

def keyword_Arguement(f_name, l_name):
        print(f"hello {f_name} {l_name}")



def default_Arguement(f_name = "Bappi", l_name = "Gorian"):
        print(f"hello {f_name} {l_name}")


position_Arguement("Bappi","Gorain")
keyword_Arguement(l_name = "Gorain",f_name = "Bappi")
default_Arguement()

