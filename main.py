''' SO Solution 1 '''
# authors=['a','b']
# new_item={'itemType': 'journalArticle',
#  'title': '',
#  'creators': [{'creatorType': 'author', 'firstName': '', 'lastName': ''}]}

# if type(authors) is list:
#     new_item['creators'] = [{'creatorType': 'author', 'name': name} for name in authors]
# else:
#     new_item['creators'] = [{'creatorType': 'author', 'name': authors}]

# print(new_item)

''' SO Solution 2 '''
# numbers = [int(input()) for _ in range(5)]
# print(': '.join(map(lambda x: f'number{x}',numbers))+': Sum: '+str(sum(numbers)))

'''SO Solution 3 '''
# d = {'weather': {'cloudy': 'yes', 'rainy': {'wind': {'strong': 'no', 'weak': 'yes'}}, 'sunny': {'humidity': {'high': 'no', 'normal': 'yes'}}}}
# def flatten(d, c = []):
#    for a, b in d.items():
#       yield from ([c+[a, b]] if not isinstance(b, dict) else flatten(b, c+[a]))

# print(list(flatten(d)))

'''SO Solution 4'''
# Creating new list called “usuarios”

# usuarios = []


# #Creating new user as dictionary with name, username e password

# usuario = {

#     "name": "Clark Kent",

#     "username" : "kent",

#     "password" : "6c70795dc50a2d6765a44bceda2699c48a8e81effe3f9e7cf3b6f8bb34ccb5b2"

# }
# # adds the user to the list

# usuarios.append(usuario)


# #Creating new user as dictionary with name, username e password
# usuario = {

#     "name": "Bruce Wayne",

#     "username" : "wayne",

#     "password" : "0bf3116d14ceeb7b8859abb9f5b90a7747913185930fed774a949cc8777a990a"

# }

# # adds the user to the list

# usuarios.append(usuario)


# #Creating new user as dictionary with name, username e password
# usuario = {

#     "name": "Christopher Walker",

#     "username" : "walker",

#     "password" : "db7e65b576f6b3db9041cbddff92f9a4b7253b795aab817d3f348977b014cd83"

# }

# adds the user to the list

# usuarios.append(usuario)

# validator = list(map(lambda x: {x['username']:x['password']},usuarios))
# username = input("Digite seu usuário: ")
# password = input("Digite sua senha: ")
# if any({username:password} == v for v in validator): # This condition makes sense
#     # import hashlib
#     # print(hashlib.sha256(password.encode()).hexdigest())
#     print(f"Bem-vindo {username}")
#     print("Logn Successful :)")
# else:
#     print("Usuário/senha inválidos")
#     print("Login Failed")


''' SO Solution 5 '''
# candGroup = ['a', 'b', 'c', 'd']
# votesEach = [0, 0, 1, 1]
# winners = {cand:votes for cand,votes in zip(candGroup,votesEach) if votes==max(votesEach)}
# for candidate, votes in winners.items():
#     print(candidate, 'has won the vote with', votes, 'votes')

''' SO Solution 6'''
# A1 = [1,2,3]
# A2 = [1]
# A3 = [1.2]
# print(min([A1,A2,A3],key=len))

'''SO Solution 7'''
# sA = f'machine1 volume1 Mon May 24 00:00:10 2021\n\
# machine2 volume1 Mon May 24 00:00:03 2021\n\
# machine2 volume2 Mon May 24 00:00:03 2021'

# sB = f'machine1 volume2 Mon May 23 00:00:10 2021 \n\
# machine2 volume1 Mon May 23 00:00:03 2021\n\
# machine2 volume2 Mon May 24 00:00:03 2021'
# print('\n'.join(x for x in sA.splitlines() if x not in sB.splitlines()))

'''SO Solution 8'''
# import requests
#     # Get a copy of the default headers that requests would use
# headers = requests.utils.default_headers()
# resp = requests.get(r"https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Daten/Fallzahlen_Kum_Tab.xlsx",
#                       params = {"__blob": "publicationFile"}, headers=headers)
# with open('demo.xlsx','wb') as f:
#     f.write(resp.content)

''' SO Solution 9 '''

# def checkNum(num):
#     return num if 1 < num < 99 and num % 2 == 0 else checkNum(int(input()))

# def main():
#     print([checkNum(int(input())) for _ in range(5)])

# main()

''' SO Solution 10'''

# import glob
# import json

# def processFiles():
#     Files = glob.glob('Files/*.json')
#     for i,singleFile in enumerate(Files):
#         if i==0:
#             with open(singleFile) as f:
#                 data = json.load(f)
#         else:
#             with open(singleFile) as f1:
#                 data['data'].extend(json.load(f1)['data'])
#     return data


# with open('output.json','w') as out:
#     json.dump(processFiles(),out)

''' SO Solution 11 '''
# sentences = "hello how are you. I am good. that's good.".split('.');
# [print(f'{sen}. {len(sen.split())} words;',end=' ') for sen in sentences if sen]

# hello how are you. 4 words; I am good. 3 words; that's good. 2 words;

''' SO Solution 12 '''
# employees =
# myNewDict1=dict.fromkeys(employees,"Hi")
# finalres = [('Hi', emp)for emp in employees]
# print(finalres)
# print(list(map(lambda x: ('Hi',x),['Kelly', 'Emma', 'John'])))

'''SO Solution 13 '''
# import re
# from itertools import zip_longest
# s1 = 'sample1'
# s2 = 'sampee231'
# # print(sum(i==j for i,j in zip_longest(input(),input())))

# ''' SO SOlution 14 '''
# prevtag_pair = [[[['challenge', 'D'], ['opportunity', 'D'], ['overcoming', 'P'], ['challenge', 'D'], ['opportunity', 'D'], ['higher', 'D'], ['levelthan', 'A']], [['country', 'D'], ['face', 'P'],
#                                                                                                                                                                   ['levels', 'N'], ['challenges', 'A'], [
#                                                                                                                                                                       'democracy', 'A'],
#                                                                                                                                                                   ['foundational', 'P'], ['progress', 'A']], [['challenges', 'A'], ['democracy', 'P'], ['faces', 'N'], ['world', 'D'], ['level', 'A']], [['challenge', 'D'], ['opportunity', 'D'], ['progress', 'A'], ['statement', 'D'], ['reveals', 'N'], ['idea', 'D'],
#                                                                                                                                                                                                                                                                                                          ['challenge', 'D'], [
#                                                                                                                                                                                                                                                                                                              'difficulty', 'D'], ['hardship', 'A'],
#                                                                                                                                                                                                                                                                                                          ['opportunity', 'D'], [
#                                                                                                                                                                                                                                                                                                              'progress', 'A'], ['challenge', 'D'],
#                                                                                                                                                                                                                                                                                                          ['overcome', 'A'], [
#                                                                                                                                                                                                                                                                                                              'challenge', 'D'], ['succeed', 'P'],
#                                                                                                                                                                                                                                                                                                          ['overcoming', 'A'], [
#                                                                                                                                                                                                                                                                                                              'rise', 'A'], ['higher', 'D'],
#                                                                                                                                                                                                                                                                                                          ['level', 'A'], ['progess', 'A']], [['challenges', ['o']],
#                                                                                                                                                                                                                                                                                                                                              ['enlight', 'N'], ['deal', 'P'], ['ways', 'D'], ['like', 'A'], ['obstacles', 'A'], ['enlights', 'P'], ['afford', 'P'], ['best', 'P'], ['result', 'D'], [
#                                                                                                                                                                                                                                                                                                              'challenges', 'P'], ['like', 'A'], ['opportunity', 'D'], ['progress', 'P'], ['want', 'P'], ['deal', 'P'], ['smartly', 'P'], ['victorious', 'V'],
#     ['looser', 'C'], ['life', 'P']], [['challenge', 'D'],
#                                       ['problem', 'D'], ['opportunity', 'D'], [
#         'progress', 'A'],
#     ['meansa', 'N'], ['challenge', 'P'], ['problem', 'D'],
#     ['help', 'D'], ['development', 'D'], ['ex', 'P'], ['farmer', 'D'], [
#         'challenging', 'A'], ['grow', 'P'], ['plants', 'A'],
#     ['set', 'P'], ['target', 'P'], ['help', 'V'], ['development', 'A']]]]
# for row in prevtag_pair:
#     word_tag = [[f'{pair[0]}_{pair[1]}' if len(
#         pair[1]) > 0 else f'{pair[0]}_' for pair in col] for col in row]
#     print(word_tag)

''' SO SOlution 15 '''

# import json
# mylist = ['{"data": {"id": "854652314", "value": "854652314", "name": "854652314"}}', '{"data": {"id": "B2", "value": "B2", "name": "B2"}}', '{"data": {"id": "457856954", "value": "457856954", "name": "457856954"}}']
# res = [json.loads(idx) for idx in mylist]
# print(res)

''' SO SOlution 16 '''
import urllib.parse
url = "https://www.some.com/8343b54b1a55dbf1a003af0d0c7e9ba4ea762245?redirect=http%3A%2F%2Ffacebook.com%2F782596948538540".split('redirect=')[-1]
print(urllib.parse.unquote(url))

