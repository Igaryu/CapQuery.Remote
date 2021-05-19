#!/usr/bin/env python
import  sys, os, getpass
""" 

Procedura per l'interrogazione del database C.A.P sfruttando database
in remoto. Per determinare l'host ed il nome database modificare le variabili 
	Host
	DbName
Le variabili 
	User
	Passwd
vengono invece richieste all'operatore al momento dell'avvio.
Questo chiaramente per motivi di sicurezza legati alla password.

"""
try:
        import  pymysql
except ImportError:
    print("")
    print("")
    print("*** Attenzione !!!")
    print("\tPer poter utilizzare questo script devi avere installato il modulo:")
    print("\tPyMysql. Da un analisi del tuo sistema non riuslta installato.")
    print("\tPer installarlo da gentoo esegui da root il seguente comando:")
    print("\tpip install pumysq. Dopo l'esecuzione rilancia GesRemTrad")
    print("")
    sys.exit(-1)



def getlogin():
#        name=eval(input('Username: '))
	user=input('Username: ')
	passwd=getpass.getpass('Password: ')
	return user,passwd

def cls():
	if os.name=='posix':
		os.system('clear')
	else:
		os.system('cls')

def intesta():
	cls()
	print("\nC.A.P							Ver 1.0")
	print("\nInterrogazione remota  database Codici Avviamento\n\n")


def menu():
	risp=0
	while ((risp < 1) or (risp > 4)):
		intesta()
		print("\n\n\n\n\n")
		print("\t\t\t(1) Cerca Per Cap\n\n")
		print("\t\t\t(2) Cerca Per Comune\n\n")
		print("\t\t\t(3) Cerca Per Provincia e/o Comune\n\n")
		print("\t\t\t(4) Esci\n\n")
		risp=eval(input('\n\n Seleziona voce menu [ 1 - 4 ] '))
		if (risp=="1") or (risp=="2") or (risp=="3") or (risp=="4"):
			if int(risp) in range(1,5):
				risp=int(risp)
			else:
				risp=0
    
	return risp

def displ_rec(d):
	intesta()
	if (len(d) == 1):
		Stringa=""
		Stringa='CAP : ' +d[0][1]+ ' - Prov: ' +d[0][3] +' - Comune: ' +d[0][5]
		print(Stringa)
	else:
		for i in range(0,len(d)):
			Stringa=""
			Stringa='CAP : ' +d[i][1]+ ' - Prov: ' +d[i][3] +' - Comune: ' +d[i][5]
			print(Stringa)



def Search_Cap(db):
	risp=0
	try:
		risp=int(input("\nCodice Avviamento postale ? [0 per uscire] "))
	except:
		input("\nDevi dare un valore numerico !!\nPremi INVIO per continuare...")
		risp=int(input("\nCodice Avviamento postale ? [0 per uscire] "))
	
	if (risp==0):
	   return
	c=db.cursor()
	req="SELECT * from CAP where Codice='"+str(risp)+"';"
	db=pymysql.connect("localhost",User,Password,"Test")
	c=db.cursor()
	c.execute(req)
	d=c.fetchall()
	if (len(d)==0):
		input("\nRecord inesistente !!!\nPremi INVIO per continuare...")
		sel=99
	else:
		sel=100
		
	while (sel!=99):
		displ_rec(d)
		try:
			sel=int(input('\n\nDigita 99 per uscire '))
		except:
			print("\nDevi dare un valore numerico !!")
			sel=100
		if (sel==99):
			break

		selval=""
		upd=1


def Search_Comune(db):
	risp=""
	risp=input("\nNome (o parte) del comune ? [0 per uscire] ")
	if (len(risp) == 0):
		input("\nDigta 0 per uscre !!\nPremi INVIO per continuare...")
		Search_Comune(db)
	if (risp=="0"):
	   return
	c=db.cursor()
	req="SELECT * from CAP where Comune Like '%"+str(risp)+"%' Order by Comune;"
	db=pymysql.connect("localhost",User,Password,"Test")
	c=db.cursor()
	c.execute(req)
	d=c.fetchall()
	if (len(d)==0):
		input("\nRecord inesistente !!!\nPremi INVIO per continuare...")
		sel=99
	else:
		sel=100
		
	while (sel!=99):
		displ_rec(d)
		try:
			sel=int(input('\n\nDigita 99 per uscire '))
		except:
			print("\nDevi dare un valore numerico !!")
			sel=100
		if (sel==99):
			break

		selval=""
		upd=1


def Search_Prov_Comune(db):
	rispP=""
	rispC=""
	print("\nPossono essere selezionati la PRVOINCIA e/o il Comune (o parte di esso)\nNON sono ammessi entrabi campi vuoti.\n\n")
	rispP=input("\n Digta la sigla della provincia [0 per uscire] ")
	if (rispP=="0"):
	   return
	rispC=input("\n Digta il comune, o parte di esso [0 per uscire] ")
	if (rispC=="0"):
	   return
	if (len(rispP) == 0 and len(rispC) == 0):
		input("\nDigta 0 per uscre !!\nPremi INVIO per continuare...")
		Search_Prov_Comune(db)
	if (len(rispP) == 0):
		req="SELECT * from CAP where Comune Like '%"+str(rispC)+"%';"
	else:
		req="SELECT * from CAP where Prov='" + str(rispP) +"' and Comune Like '%"+str(rispC)+"%' Order By Prov;"
	
	db=pymysql.connect("localhost",User,Password,"Test")
	c=db.cursor()
	c.execute(req)
	d=c.fetchall()

	if (len(d)==0):
		input("\nRecord inesistente !!!\nPremi INVIO per continuare...")
		sel=99
	else:
		sel=100
		
	while (sel!=99):
		displ_rec(d)
		try:
			sel=int(input('\n\nDigita 99 per uscire '))
		except:
			print("\nDevi dare un valore numerico !!")
			sel=100
		if (sel==99):
			break

		selval=""
		upd=1




#***************************************************
intesta()

User=""
Password=""
Host="localhost"
DbName="Test"

User,Password=getlogin()
#if (len(User)==0 or len(Password)==0):
if (len(User)==0 ):
	print("\nIl campo User deve contenere un valore !!\n\n")
	sys.exit(-2)


print("\n\nConnesione al server remoto in corso: attendere prego ....")

try:
	db=pymysql.connect(Host,User,Password,DbName)

except:
	print("")
	print("")
	print("*** Attenzione !!!")
	print("")
	print("Connessione al database Traduzioni fallito ...")
	print("Verifica Username e Password e si riprova. ")
	print("\n\n")
	sys.exit(-2)

c=db.cursor()
risp=0
while(risp!=4):
	risp=menu()
	if (risp==1):
	   Search_Cap(db)
	if (risp==2):
	   Search_Comune(db)
	if (risp==3):
		Search_Prov_Comune(db)
	if (risp==4):
		print("\n\nFine sessione.")
		sys.exit(0)

