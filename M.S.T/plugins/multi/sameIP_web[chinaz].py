# -*- coding: cp936 -*-
class mstplugin:
    '''ͬIP��վ��ѯ::tool.chinaz.com/same��'''
    infos = [
        ['�������','ͬIP��վ��ѯ[chinaz]��'],
        ['�������','mst'],
        ['��������','2013/10/23'],
        ['������վ','http://mstoor.duapp.com']
        ]
    opts  = [
        ['RURL','mstoor.duapp.com','Ҫ��ѯ��Ŀ����ַ'],
        ['PAYLOAD','false','����Ҫ�󹥻����']
        ]
    def exploit(self):
        '''��ʼ��ѯ'''
        chinaz = 'http://tool.chinaz.com/Same/'
        value  = {'s':RURL}
        try:
            color.cprint("[*] Sending data..",YELLOW)
            tmp    = fuck.urlpost(chinaz,value).read()
            color.cprint("[+] Formate data..",YELLOW)
            tmp    = tmp.decode("utf-8")
            res    = fuck.find('.</span> <a href=[^>]+ target=_blank>',tmp)
            reslen = len(res)
            resiii = 1
            reslog = "sameIP_web[chinaz]_%s"%RURL
            for r in res:
                tmp= r[18:]
                tmp= tmp.split("'")
                ok = tmp[0]
                color.cprint("[%s/%s] %s"%(resiii,reslen,ok),GREEN)
                fuck.writelog(reslog,ok+"\n")
                resiii+=1
            color.cprint("[*] Get data Successful !LOG:output/%s.log"%reslog,CYAN)
        except Exception,e:
            color.cprint("[!] Err:%s"%e,RED)
