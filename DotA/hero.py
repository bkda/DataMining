# coding=UTF-8
'''
    Created by Tracy on 2016/5/3
    Mail tracyliubai@gmail.com
'''
hero_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 31, 26, 27, 28, 29,
           30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
           58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
           85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 106, 107, 109, 110, 111,
           105, 112, 113]
hero_ZH_name = ['敌法师', '斧王', '祸乱之源', '嗜血狂魔', '水晶室女', '卓尔游侠', '撼地者', '主宰', '米拉娜', '影魔', '变体精灵', '幻影长矛手', '帕克', '帕吉',
                '剃刀',
                '沙王', '风暴之灵', '斯温', '小小', '复仇之魂', '风行者', '宙斯', '昆卡', '莉娜', '巫妖', '莱恩', '暗影萨满', '斯拉达', '潮汐猎人', '巫医',
                '力丸',
                '谜团', '修补匠', '狙击手', '瘟疫法师', '术士', '兽王', '痛苦女王', '剧毒术士', '虚空假面', '冥魂大帝', '死亡先知', '幻影刺客', '帕格纳', '圣堂刺客',
                '冥界亚龙', '露娜', '龙骑士', '戴泽', '发条技师', '拉席克', '先知', '噬魂鬼', '黑暗贤者', '克林克兹', '全能骑士', '魅惑魔女', '哈斯卡', '暗夜魔王',
                '育母蜘蛛', '赏金猎人', '编织者', '杰奇洛', '蝙蝠骑士', '陈', '幽鬼', '末日使者', '远古冰魄', '熊战士', '裂魂人', '矮人直升机', '炼金术士', '祈求者',
                '沉默术士', '殁境神蚀者', '狼人', '酒仙', '暗影恶魔', '德鲁伊', '混沌骑士', '米波', '树精卫士', '食人魔魔法师', '不朽尸王', '拉比克', '干扰者',
                '司夜刺客',
                '娜迦海妖', '光之守卫', '艾欧', '维萨吉', '斯拉克', '美杜莎', '巨魔战将', '半人马战行者', '马格纳斯', '伐木机', '钢背兽', '巨牙海民', '天怒法师',
                '亚巴顿',
                '上古巨神', '军团指挥官', '灰烬之灵', '大地之灵', '恐怖利刃', '凤凰', '神谕者', '工程师', '寒冬飞龙', '天穹守望者']
hero_EN_name = ['Anti-Mage', 'Axe', 'Bane', 'Bloodseeker', 'Crystal Maiden', 'Drow Ranger', 'Earthshaker', 'Juggernaut',
                'Mirana', 'Shadow Fiend', 'Morphling', 'Phantom Lancer', 'Puck', 'Pudge', 'Razor', 'Sand King',
                'Storm Spirit', 'Sven', 'Tiny', 'Vengeful Spirit', 'Windranger', 'Zeus', 'Kunkka', 'Lina', 'Lich',
                'Lion', 'Shadow Shaman', 'Slardar', 'Tidehunter', 'Witch Doctor', 'Riki', 'Enigma', 'Tinker', 'Sniper',
                'Necrophos', 'Warlock', 'Beastmaster', 'Queen of Pain', 'Venomancer', 'Faceless Void', 'Wraith King',
                'Death Prophet', 'Phantom Assassin', 'Pugna', 'Templar Assassin', 'Viper', 'Luna', 'Dragon Knight',
                'Dazzle', 'Clockwerk', 'Leshrac', "Nature's Prophet", 'Lifestealer', 'Dark Seer', 'Clinkz',
                'Omniknight', 'Enchantress', 'Huskar', 'Night Stalker', 'Broodmother', 'Bounty Hunter', 'Weaver',
                'Jakiro', 'Batrider', 'Chen', 'Spectre', 'Doom', 'Ancient Apparition', 'Ursa', 'Spirit Breaker',
                'Gyrocopter', 'Alchemist', 'Invoker', 'Silencer', 'Outworld Devourer', 'Lycan', 'Brewmaster',
                'Shadow Demon', 'Lone Druid', 'Chaos Knight', 'Meepo', 'Treant Protector', 'Ogre Magi', 'Undying',
                'Rubick', 'Disruptor', 'Nyx Assassin', 'Naga Siren', 'Keeper of the Light', 'Io', 'Visage', 'Slark',
                'Medusa', 'Troll Warlord', 'Centaur Warrunner', 'Magnus', 'Timbersaw', 'Bristleback', 'Tusk',
                'Skywrath Mage', 'Abaddon', 'Elder Titan', 'Legion Commander', 'Ember Spirit', 'Earth Spirit',
                'Terrorblade', 'Phoenix', 'Oracle', 'Techies', 'Winter Wyvern', 'Arc Warden']


def id2hero(_id, LANG):
    return dict(zip(hero_id, LANG)).get(_id, '')
