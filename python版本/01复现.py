import random

rules = """
复合句子 = 句子 , 连词 复合句子 | 句子
连词 = 而且 | 但是 | 不过
句子 = 主语 谓语 宾语
主语 = 你| 我 | 他 
谓语 = 吃| 玩 
宾语 = 桃子| 皮球

"""

def target_of_grammar(rules):
    str1 = [t.split('=') for t in rules.split('\n') if t.strip()]
    str2 = [(title,body.split('|')) for title,body in str1]
    grammar = {t.strip():[ex.strip() for ex in e]for t,e in str2}
    return grammar

def target_of_description(grammar,target='句子'):
    if target not in grammar:
        return target

    return ''.join([target_of_description(grammar,t) for t in random.choice(grammar[target]).split()])




grammar = target_of_grammar(rules)

sentence = target_of_description(grammar,target='复合句子')
print(sentence)