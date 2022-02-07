import sys
import Filecheck

filen,nameim = sys.argv[1],sys.argv[2] #Toma los argumentos 1 y 2, archivo e imagen
Filecheck.CheckFile(filen)
Filecheck.CheckImage(nameim)
Filecheck.Metadata(filen,nameim)
