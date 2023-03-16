def fight(heroes, villain):
    for hero in heroes:
        if hero['category'] == villain['category']:
            if hero['health'] == villain['health'] or hero['health'] > villain['health']:
                hero['score'] += 1
                return '{} defeated the villain and now has a score of {}'.format(hero['name'], hero['score'])
            else:
                villain['health'] -= hero['health'] / 2
    return '{} prevailed with {}HP left'.format(villain['name'], villain['health'])
