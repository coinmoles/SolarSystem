import pygame as pg
import helper as hlp
import vector as vec


class Planet:
    """행성 개체 클래스

    Attributes:
        img (pg.Surface): 이미지
        width (int): 너비
        height (int): 높이
        radius (int): 반지름
        center (vec.Vector): 중심 좌표
        loc (vec.Vector): 왼쪽 위 좌표, blit 기준점
    """
    def __init__(self, img, loc_list):
        """__init__ 메소드
        Args:
            img (pg.Surface): 이미지
            loc_list (list): 이동할 좌표 리스트
        """
        self.img, self.width, self.height, self.radius = img, None, None, None

        self.center = loc_list[0]
        self.loc = self.center - vec.Vector(self.width, self.height) // 2

        self.loc_list = loc_list

    def set_center(self, center):
        """center 설정
        center가 변화하면 loc도 변경해야 하기 때문에 따로 함수를 설정해 준다

        Args:
            center (Vector): 설정할 center 위치
        """
        self.center = center
        self.loc = self.center - vec.Vector(self.width, self.height) // 2

    def act(self):
        """한 프레임마다 하는 행동
        """
        self.set_center(loc_list[hlp.t])
        hlp.screen.blit(self.img, self.loc)
