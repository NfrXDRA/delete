import amino
clint=amino.Client()
sid=input('SID ⟩⟩  ')
clint.login_sid(SID=sid.replace('sid=',''))
chatur=input('CHAT URL ⟩⟩  ')
chaturl=clint.get_from_code(chatur)
comId=chaturl.path[1:chaturl.path.index('/')]
chatId=chaturl.objectId
userId=clint.get_from_code(input('HOST URL ⟩⟩')).objectId
subclint=amino.SubClient(comId=comId,profile=clint.profile)
subclint.kick(chatId=chatId,userId=userId,allowRejoin=True)