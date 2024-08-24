Str="kalyani"
print("\nConverted String:",Str.capitalize())
print("\nConverted String:",Str.casefold())
print("\n String:",Str.center(1))

Str2="MayuriKalyani"
print("\ncount:",Str2.count('a'))
print("\nEncoded string:",Str.encode())
print("\nEndswith String:",Str2.endswith('i'))
print("\n Find_opr:",Str2.find('K'))
print("\nFormat String:",Str2.format()) 
print("\nisalnum String:",Str2.isalnum())  
print("\nAscii String:",Str.isascii())
print("\nisalpha String:",Str.isalpha())
print("\nisadecimal String:",Str.isdecimal())
print("\nisDigit String:",Str2.isdigit())
print("\nisidentifier String:",Str.isidentifier())
print("\nislower String:",Str.islower())
print("\nisnumric String:",Str.isnumeric())
print("\nisprintable String:",Str2.isprintable())
print("\n isspace String:",Str2.isspace())
print("\n istitle String:",Str2.istitle())
print("\n isupper String:",Str2.isupper())
print("\n rfind String:",Str2.rfind('l'))
#print("\n join String:",Str2.join('n'))

str='-'.join("Hello")
print( "join_opr:",str)
print("\n ljust String:",Str2.ljust(1))

str3="SWATI is a good girl"
print("\n lower String:",str3.lower())
print("\n partition String:",str3.partition("is"))

txt="hello mayur"
mytable=str.maketrans("m","k")
print(txt.translate(mytable))

print("\n replace String:",txt.replace("y","i"))
print("\n rindex String:",txt.rindex('m'))
print("\n rjust String:",txt.rjust(1))
print("\n rpartition String:",str3.rpartition("good"))
print("\n rsplit String:",str3.rsplit('is'))
print("\n split String:",txt.split())
print("\n splitlines String:",txt.splitlines())
print("\n swapcase String:",txt.swapcase())
print("\n title String:",txt.title())
print("\n translate String:",txt.translate("m"))
print("\n zfill String:",txt.zfill(1))

