from pygame import font, Surface

from COLORS import Colors

class Restart():
    def show(self, surface: Surface, removed: int, round: int) -> None:
        self.font = font.SysFont(None, 32)
        self.message_1 = self.font.render(f"Blocos removidos: {removed} - Turnos jogados: {round}", True, Colors.YELLOW)
        self.message_2 = self.font.render("Começar de novo?", True, Colors.YELLOW)
        self.message_3 = self.font.render("Pressione ESPAÇO!!!", True, Colors.YELLOW)
        height_diff = self.message_1.get_height()/2 + self.message_2.get_height()/2 + self.message_3.get_height()/2
        surface.blit(self.message_1, (surface.get_width()/2 - self.message_1.get_width()/2, (surface.get_height()/2 - self.message_1.get_height()/2) - height_diff))
        surface.blit(self.message_2, (surface.get_width()/2 - self.message_2.get_width()/2, ((surface.get_height()/2 - self.message_2.get_height()/2) + 30) - height_diff))
        surface.blit(self.message_3, (surface.get_width()/2 - self.message_3.get_width()/2, ((surface.get_height()/2 - self.message_3.get_height()/2) + 60) - height_diff))
