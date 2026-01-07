import pygame
import sys

pygame.init()

# testing
# testing2
# testing3
# testing4

# ----------------------------------------
# 基本設定
# ----------------------------------------
SCREEN_W, SCREEN_H = 640, 480
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("dirty / cache demo")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# ----------------------------------------
# dirty / cache を使った情報パネル
# ----------------------------------------
class InfoPanel:
    def __init__(self, font):
        self.font = font
        self.surface = pygame.Surface((300, 120), pygame.SRCALPHA)

        self.value = 0           # 表示する値
        self._dirty = True       # 再生成が必要か

    def mark_dirty(self):
        """状態が変わったときに呼ぶ"""
        self._dirty = True

    def update(self):
        """dirty のときだけ Surface を作り直す"""
        if not self._dirty:
            return

        self._dirty = False
        self.surface.fill((0, 0, 0, 0))  # 透明クリア

        text = f"value: {self.value}"
        text_surf = self.font.render(text, True, BLACK)
        self.surface.blit(text_surf, (10, 10))

    def draw(self, screen, pos):
        """描画は blit のみ"""
        screen.blit(self.surface, pos)


# ----------------------------------------
# メイン
# ----------------------------------------
def main():
    panel = InfoPanel(font)

    running = True
    while running:
        # ----------------------------
        # イベント処理
        # ----------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    panel.value += 1
                    panel.mark_dirty()   # ★ 状態変更 → dirty
                elif event.key == pygame.K_DOWN:
                    panel.value -= 1
                    panel.mark_dirty()

        # ----------------------------
        # update（重い処理はここ）
        # ----------------------------
        panel.update()

        # ----------------------------
        # draw（軽い処理のみ）
        # ----------------------------
        screen.fill(WHITE)
        panel.draw(screen, (20, 20))
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
