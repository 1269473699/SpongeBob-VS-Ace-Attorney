import pygame


class RoleBuilder:

    def __init__(self, role, height):
        self.roles = []
        self.role_rects = []
        strs = []
        if role == "MayaSurprisedIntro":
            strs = ["resources/pics/MayaSurprised1.gif"]
        elif role == "MayaStand":
            strs = ["resources/pics/MayaStand1.gif", "resources/pics/MayaStand2.gif", "resources/pics/MayaStand3.gif"]
        elif role =="MayaLower":
            strs = ["resources/pics/MayaLower1.gif", "resources/pics/MayaLower2.gif", "resources/pics/MayaLower3.gif"]
        elif role == "MayaSmile":
            strs = ["resources/pics/MayaSmile1.gif", "resources/pics/MayaSmile2.gif", "resources/pics/MayaSmile2.gif","resources/pics/MayaSmile3.gif","resources/pics/MayaSmile2.gif"]
        elif role =="MayaShocked":
            strs = ["resources/pics/MayaSurprised1.gif", "resources/pics/MayaShocked1.gif", "resources/pics/MayaShocked2.gif", "resources/pics/MayaShocked3.gif",
                    "resources/pics/MayaShocked3.gif", "resources/pics/MayaShocked3.gif","resources/pics/MayaShocked3.gif","resources/pics/MayaShocked3.gif",
                    "resources/pics/MayaShocked3.gif","resources/pics/MayaShocked3.gif"]
        elif role =="MayaUpset":
            strs = ["resources/pics/MayaUpset1.gif", "resources/pics/MayaUpset2.gif", "resources/pics/MayaUpset3.gif"]
        elif role == "MayaSurprised":
            strs = ["resources/pics/MayaSurprised1.gif", "resources/pics/MayaSurprised2.gif"]
        elif role == "MayaExcited":
            strs = ["resources/pics/MayaExcited1.gif", "resources/pics/MayaExcited2.gif"]
        elif role == "MayaChin":
            strs = ["resources/pics/MayaChin1.gif", "resources/pics/MayaChin2.gif"]
        elif role == "SpongeBobCry":
            strs = ["resources/pics/SpongeBobCry1.png", "resources/pics/SpongeBobCry2.png", "resources/pics/SpongeBobCry3.png"]
        elif role == "SpongeBobSmile":
            strs = ["resources/pics/SpongeBobSmile1.png", "resources/pics/SpongeBobSmile2.png",
                    "resources/pics/SpongeBobSmile3.png"]
        elif role == "SpongeBobSmileIntro":
            strs = ["resources/pics/SpongeBobSmile1.png"]
        elif role == "JudgeNormal":
            strs = ["resources/pics/JudgeNormal1.gif", "resources/pics/JudgeNormal2.gif",
                    "resources/pics/JudgeNormal3.gif","resources/pics/JudgeNormal4.gif",
                    "resources/pics/JudgeNormal5.gif","resources/pics/JudgeNormal6.gif"]
        elif role == "JudgeNod":
            strs = ["resources/pics/JudgeNod1.gif", "resources/pics/JudgeNod2.gif",
                    "resources/pics/JudgeNod3.gif", "resources/pics/JudgeNod4.gif",
                    "resources/pics/JudgeNod5.gif"]
        elif role == "JudgeDeny":
            strs = ["resources/pics/JudgeDeny1.gif", "resources/pics/JudgeDeny2.gif",
                    "resources/pics/JudgeDeny3.gif", "resources/pics/JudgeDeny3.gif",
                    "resources/pics/JudgeDeny4.gif","resources/pics/JudgeDeny4.gif",
                    "resources/pics/JudgeDeny3.gif","resources/pics/JudgeDeny3.gif",
                    "resources/pics/JudgeDeny5.gif","resources/pics/JudgeDeny5.gif",
                    "resources/pics/JudgeDeny3.gif", "resources/pics/JudgeDeny3.gif",
                    "resources/pics/JudgeDeny4.gif", "resources/pics/JudgeDeny4.gif",
                    "resources/pics/JudgeDeny3.gif", "resources/pics/JudgeDeny3.gif",
                    "resources/pics/JudgeDeny2.gif","resources/pics/JudgeDeny1.gif"
                    ]
        elif role == "JudgeSurprised":
            strs = ["resources/pics/JudgeSurprised1.gif", "resources/pics/JudgeSurprised2.gif",
                    "resources/pics/JudgeSurprised3.gif", "resources/pics/JudgeSurprised4.gif",
                    "resources/pics/JudgeSurprised5.gif","resources/pics/JudgeSurprised6.gif"]

        elif role == "JudgeSerious":
            strs = ["resources/pics/JudgeSerious1.gif", "resources/pics/JudgeSerious2.gif",
                    "resources/pics/JudgeSerious3.gif", "resources/pics/JudgeSerious4.gif",
                    "resources/pics/JudgeSerious5.gif", "resources/pics/JudgeSerious6.gif",
                    ]

        elif role == "EdgeworthNormal":
            strs = ["resources/pics/EdgeworthNormal1.gif", "resources/pics/EdgeworthNormal2.gif",
                    "resources/pics/EdgeworthNormal3.gif"
                    ]
        elif role == "EdgeworthCross":
            strs = ["resources/pics/EdgeworthCross1.gif", "resources/pics/EdgeworthCross2.gif",
                    "resources/pics/EdgeworthCross3.gif", "resources/pics/EdgeworthCross4.gif",
                    "resources/pics/EdgeworthCross5.gif", "resources/pics/EdgeworthCross6.gif",
                    "resources/pics/EdgeworthCross7.gif", "resources/pics/EdgeworthCross8.gif",
                    ]

        elif role == "EdgeworthSlam":
            strs = ["resources/pics/EdgeworthSlam1.gif", "resources/pics/EdgeworthSlam2.gif",
                    "resources/pics/EdgeworthSlam3.gif"
                    ]

        elif role == "EdgeworthAngry":
            strs = ["resources/pics/EdgeworthAngry1.gif", "resources/pics/EdgeworthAngry2.gif",
                    "resources/pics/EdgeworthAngry3.gif"
                    ]

        elif role == "EdgeworthPoint":
            strs = ["resources/pics/EdgeworthPoint1.gif", "resources/pics/EdgeworthPoint2.gif",
                    "resources/pics/EdgeworthPoint3.gif", "resources/pics/EdgeworthPoint4.gif",
                    "resources/pics/EdgeworthPoint5.gif"
                    ]

        elif role == "PhoenixNormal":
            strs = ["resources/pics/PhoenixNormal1.gif", "resources/pics/PhoenixNormal2.gif",
                "resources/pics/PhoenixNormal3.gif", "resources/pics/PhoenixNormal4.gif",
                "resources/pics/PhoenixNormal5.gif"
                ]

        elif role == "PhoenixThink":
            strs = ["resources/pics/PhoenixThink1.gif", "resources/pics/PhoenixThink2.gif",
                "resources/pics/PhoenixThink3.gif", "resources/pics/PhoenixThink4.gif",
                "resources/pics/PhoenixThink5.gif", "resources/pics/PhoenixThink6.gif",
                "resources/pics/PhoenixThink7.gif"
                ]

        elif role == "PhoenixSweatQuiet":
            strs = ["resources/pics/PhoenixSweatQuiet1.gif", "resources/pics/PhoenixSweatQuiet2.gif",
                "resources/pics/PhoenixSweatQuiet3.gif", "resources/pics/PhoenixSweatQuiet4.gif",
                "resources/pics/PhoenixSweatQuiet5.gif", "resources/pics/PhoenixSweatQuiet6.gif",
                "resources/pics/PhoenixSweatQuiet7.gif"
                ]

        elif role == "MayaDespise":
            strs = ["resources/pics/MayaDespise1.gif", "resources/pics/MayaDespise2.gif"]

        elif role == "MayaSideNormal":
            strs = ["resources/pics/MayaSideNormal1.gif", "resources/pics/MayaSideNormal2.gif"
                    , "resources/pics/MayaSideNormal3.gif"]

        elif role == "MayaSideAngry":
            strs = ["resources/pics/MayaSideAngry1.gif", "resources/pics/MayaSideAngry2.gif"]

        elif role == "MayaSideAngryQuiet":
            strs = ["resources/pics/MayaSideAngry1.gif"]

        for i in range(len(strs)):
            self.roles.append(pygame.image.load(strs[i]).convert_alpha())
            self.roles[i] = pygame.transform.scale(self.roles[i], (int(height * 0.5 * 1.5), int(height * 0.5)))
            self.role_rects.append(self.roles[i].get_rect())
            self.role_rects[i].top = 0
            self.role_rects[i].left = 0

    def get_roles(self):
        return self.roles, self.role_rects


