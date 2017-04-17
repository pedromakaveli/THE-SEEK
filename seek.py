#ecoding:utf-8

from os import system
import re
import requests
import time
import socket
import hashlib

dorks = "admin.%EXT% login.htm login.html login/ login.%EXT% adm/ admin/ admin/account.html admin/login.html admin/login.htm admin/home.%EXT% admin/controlpanel.html admin/controlpanel.htm admin/cp.%EXT% admin/adminLogin.html admin/adminLogin.htm admin/admin_login.%EXT% admin/controlpanel.%EXT% admin/admin-login.%EXT% admin-login.%EXT% admin/account.%EXT% admin/admin.%EXT% admin.htm admin.html adminitem/ adminitem.%EXT% adminitems/ adminitems.%EXT% administrator/ administrator/login.%EXT% administrator.%EXT% administration/ administration.%EXT% adminLogin/ adminlogin.%EXT% admin_area/admin.%EXT% admin_area/ admin_area/login.%EXT% manager/ manager.%EXT% letmein/ letmein.%EXT% superuser/ superuser.%EXT% access/ access.%EXT% sysadm/ sysadm.%EXT% superman/ supervisor/ panel.%EXT% control/ control.%EXT% member/ member.%EXT% members/ members.%EXT% user/ user.%EXT% cp/ uvpanel/ manage/ manage.%EXT% management/ management.%EXT% signin/ signin.%EXT% log-in/ log-in.%EXT% log_in/ log_in.%EXT% sign_in/ sign_in.%EXT% sign-in/ sign-in.%EXT% users/ users.%EXT% accounts/ accounts.%EXT% wp-login.php bb-admin/login.%EXT% bb-admin/admin.%EXT% bb-admin/admin.html administrator/account.%EXT% relogin.htm relogin.html check.%EXT% relogin.%EXT% blog/wp-login.%EXT% user/admin.%EXT% users/admin.%EXT% registration/ processlogin.%EXT% checklogin.%EXT% checkuser.%EXT% checkadmin.%EXT% isadmin.%EXT% authenticate.%EXT% authentication.%EXT% auth.%EXT% authuser.%EXT% authadmin.%EXT% cp.%EXT% modelsearch/login.%EXT% moderator.%EXT% moderator/ controlpanel/ controlpanel.%EXT% admincontrol.%EXT% adminpanel.%EXT% fileadmin/ fileadmin.%EXT% sysadmin.%EXT% admin1.%EXT% admin1.html admin1.htm admin2.%EXT% admin2.html yonetim.%EXT% yonetim.html yonetici.%EXT% yonetici.html phpmyadmin/ myadmin/ ur-admin.%EXT% ur-admin/ Server.%EXT% Server/ wp-admin/ administr8.%EXT% administr8/ webadmin/ webadmin.%EXT% administratie/ admins/ admins.%EXT% administrivia/ Database_Administration/ useradmin/ sysadmins/ admin1/ system-administration/ administrators/ pgadmin/ directadmin/ staradmin/ ServerAdministrator/ SysAdmin/ administer/ LiveUser_Admin/ sys-admin/ typo3/ panel/ cpanel/ cpanel_file/ platz_login/ rcLogin/ blogindex/ formslogin/ autologin/ support_login/ meta_login/ manuallogin/ simpleLogin/ loginflat/ utility_login/ showlogin/ memlogin/ login-redirect/ sub-login/ wp-login/ login1/ dir-login/ login_db/ xlogin/ smblogin/ customer_login/ UserLogin/ login-us/ acct_login/ bigadmin/ project-admins/ phppgadmin/ pureadmin/ sql-admin/ radmind/ openvpnadmin/ wizmysqladmin/ vadmind/ ezsqliteadmin/ hpwebjetadmin/ newsadmin/ adminpro/ Lotus_Domino_Admin/ bbadmin/ vmailadmin/ Indy_admin/ ccp14admin/ irc-macadmin/ banneradmin/ sshadmin/ phpldapadmin/ macadmin/ administratoraccounts/ admin4_account/ admin4_colon/ radmind-1/ Super-Admin/ AdminTools/ cmsadmin/ SysAdmin2/ globes_admin/ cadmins/ phpSQLiteAdmin/ navSiteAdmin/ server_admin_small/ logo_sysadmin/ power_user/ system_administration/ ss_vms_admin_sm/ bb-admin/ panel-administracion/ instadmin/ memberadmin/ administratorlogin/ adm.%EXT% admin_login.%EXT% panel-administracion/login.%EXT% pages/admin/admin-login.%EXT% pages/admin/ acceso.%EXT% admincp/login.%EXT% admincp/ adminarea/ admincontrol/ affiliate.%EXT% adm_auth.%EXT% memberadmin.%EXT% administratorlogin.%EXT% modules/admin/ administrators.%EXT% siteadmin/ siteadmin.%EXT% adminsite/ kpanel/ vorod/ vorod.%EXT% vorud/ vorud.%EXT% adminpanel/ PSUser/ secure/ webmaster/ webmaster.%EXT% autologin.%EXT% userlogin.%EXT% admin_area.%EXT% cmsadmin.%EXT% security/ usr/ root/ secret/ admin/login.%EXT% admin/adminLogin.%EXT% moderator.php moderator.html moderator/login.%EXT% moderator/admin.%EXT% yonetici.%EXT% 0admin/ 0manager/ aadmin/ cgi-bin/login%EXT% login1%EXT% login_admin/ login_admin%EXT% login_out/ login_out%EXT% login_user%EXT% loginerror/ loginok/ loginsave/ loginsuper/ loginsuper%EXT% login%EXT% logout/ logout%EXT% secrets/ super1/ super1%EXT% super_index%EXT% super_login%EXT% supermanager%EXT% superman%EXT% superuser%EXT% supervise/ supervise/Login%EXT% super%EXT% "
dorks = dorks.split()

good_access = [200,201,202,203,204,205,206,207,208,226]
bad_access = [400,401,402,403,404,405,406,407,408,409,410,411,412,413,451,429]

extencoes = ["php","asp","html","htm"]

system("reset")

time.sleep(3)
print("../Loading")
print("\n\n")
time.sleep(1)
print("\033[34m\033[1m[-]\033[0;0m\033[0;0m Coded by: Pedro Hoffmann (SadStan), EkosFox, Diogo Fernando")
time.sleep(1)
print("\033[34m\033[1m[-]\033[0;0m\033[0;0m Versao 1.0")
time.sleep(1)
print("\033[34m\033[1m[-]\033[0;0m\033[0;0m TheSeeker")
time.sleep(1)
print("\033[34m\033[1m[-]\033[0;0m\033[0;0m Greetz: Hospeda Host")
time.sleep(1)
print("\033[34m\033[1m[-]\033[0;0m\033[0;0m Criptografias")
time.sleep(1)
print("\033[34m\033[1m[-]\033[0;0m\033[0;0m Portscanning")
time.sleep(1)
print("\033[34m\033[1m[-]\033[0;0m\033[0;0m Admin Search")
time.sleep(1)
def banner():
	print("""
 _   _                   _          \033[31m\033[1mv_1.0\033[0;0m\033[0;0m
| |_| |_ ___ ___ ___ ___| |_ ___ ___
|  _|   | -_|_ -| -_| -_| '_| -_|  _|
|_| |_|_|___|___|___|___|_,_|___|_|
	""")

banner()

while True:
	comand_line = raw_input("\033[32m\033[1mConsole\033[0;0m \033[0;0m\033[31m\033[1m(Digite o site)\033[0;0m\033[0;0m >")
	if comand_line == "-h":
		print("\n\n\n\n")
		print("Data-Coded:\033[32m\033[1m16/04/2017\033[0;0m\033[0;0m")
		print"Coded by \033[32m\033[1mPedro Hoffmann (SadStan), Diogo Fernando, EkosFox\033[0;0m\033[0;0m"
		print("Versao: \033[32m\033[1m1.0\033[0;0m\033[0;0m")
		print("Codigos: \033[32m\033[1mAjuda\033[0;0m\033[0;0m")
		print"""
	-h		ajuda
	-exit 		sair
	-reset		limpar tela
	-banner
	-credits	creditos
	-criptografia
	-portscanning
	
		"""
	elif comand_line == "-exit":
		exit()
	elif comand_line == "-banner":
		banner()
	elif comand_line == "-reset":
		system("reset")
	elif comand_line == "-criptografia":
		dec = raw_input("\033[34m\033[1mMd5\033[0;0m\033[0;0m or \033[34m\033[1mSha256\033[0;0m\033[0;0m > ")
		if dec == "Md5":
			while True:
				hashes = hashlib.md5()
				hash_console = raw_input("\033[32m\033[1mCriptografia >\033[0;0m\033[0;0m ")
				hashes.update(hash_console)
				system("reset")
				print hashes.hexdigest()

				if hash_console == "-exit":
					exit()
		else:
			hashes = hashlib.sha256()
			hash_console = raw_input("\033[32m\033[1mCriptografia >\033[0;0m\033[0;0m ")
			hashes.update(hash_console)
			system("reset")
			print hashes.hexdigest()

			if hash_console == "-exit":
				exit()		
	
	elif comand_line == "-portscanning":
		system("reset")
		time.sleep(2)

		quantidade = raw_input("Quantas portas deseja fazer scan? ")
		ip = raw_input("\033[34m\033[1m[+]\033[0;0m\033[0;0m Ip ou endereço > ")
		ports = []
		count = 0
		while count <= int(quantidade):
	    		ports.append(int(raw_input("\033[34m\033[1m[+]\033[0;0m\033[0;0m Port > ")))
 	    		count +=1
		print("\n")
		for port in ports:
    			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    			client.settimeout(0.15)
    			code = client.connect_ex((ip, port))
		
   			if code == 0:
        			print str(port) +"\033[32m\033[1mPorta aberta\033[0;0m\033[0;0m"
    			else:
        			print str(port) +"\033[31m\033[1mPorta Fechada\033[0;0m\033[0;0m"
	else:
		continue_process = raw_input("Deseja prosseguir com esta operacao? \033[34m\033[1m(S/N)\033[0;0m\033[0;0m")
		if continue_process == "N":
			print "Cancelando..."
			pass
		elif continue_process == "S":
			system("reset")
			print "\033[34m\033[1m[*] Testando o seguinte site: \033[0;0m\033[0;0m", comand_line
			time.sleep(1)
			print "\033[34m\033[1m[*] Aguarde! SITE: \033[0;0m\033[0;0m", comand_line
			time.sleep(1)
			print "\033[34m\033[1m[*] OK \033[0;0m\033[0;0m"
			if re.search("[a-z]+$", comand_line, re.IGNORECASE):
				comand_line = comand_line + "/"
			for dork in dorks:
				for ext in extencoes:
					var_dork = dork
					try:
						var_dork = var_dork.replace("%EXT%",ext)
					except:
						pass
					site = comand_line + var_dork
					request = requests.get(site)
					status = request.status_code
					if status in good_access:
						print "\033[32m\033[1mPAGINA ENCONTRADA: A pagina \033[0;0m\033[0;0m", site, "\033[32m\033[1m retornou uma pagina ativa!\033[0;0m\033[0;0m"
					elif status in bad_access:
						print "\033[32mA pagina \033[0;0m", site, " \033[31mnao foi encontrada ou acesso foi negado!\033[0;0m"
					else:
						print "Status desconhecido: ", status
			print "Finalizando..."
