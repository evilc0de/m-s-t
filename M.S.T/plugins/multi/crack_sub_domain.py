# -*- coding: cp936 -*-
'''
Mst=>multi=>plugin
'''
class mstplugin:
    '''crack sub_domain'''
    infos = [
        ['���','���ƶ���������������'],
        ['����','mst'],
        ['����','2013/10/21'],
        ['��ַ','http://mstoor.duapp.com']
        ]
    opts  = [
        ['DOMAIN','google.com','Ҫ���ƵĶ�������'],
        ['SUBDIC','dicts/sub_domain.lst','���ƶ����������ֵ�·��'],
        ['PAYLOAD','false','����Ҫ�󹥻����']
        ]
    def exploit(self):
        dicts=open(SUBDIC).readlines()
        color.cprint("SCANN %s =>SUB DOMAINS"%DOMAIN.upper(),YELLOW)
        color.cprint("===================="+"="*len(DOMAIN),GREY)
        color.cprint("%-35s %-25s %-10s"%("FULL DOMAIN","RESULT","SCHEDULE"),YELLOW)
        color.cprint("%-35s %-25s %-10s"%("-"*35,"-"*25,"-"*10),GREY)
        ll = len(dicts)
        li = 1
        for dic in dicts:
            sub    = dic.strip("\n")
            domain = sub+"."+DOMAIN
            try:
                res = fuck.urltoip(domain)
                log="%-35s %-25s %-10s"%(domain,res,"%s/%s"%(li,ll))
                color.cprint(log,GREEN)
                fuck.writelog('sub_domain_%s'%DOMAIN,log)
            except:
                color.cprint("%-35s %-25s %-10s"%(domain,"ERROR","%s/%s"%(li,ll)),RED)
            li += 1
        color.cprint("[*] ALL SCAN DONE ! SAVE TO output/sub_domain_%s.log!"%DOMAIN,YELLOW)
