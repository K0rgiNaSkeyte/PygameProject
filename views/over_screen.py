import pygame


def draw_game_over(screen):
    pygame.init()
    font = pygame.font.Font(None, 72)
    text_surface = font.render("УВЫ, НО ВЫ ПРОИГРАЛИ", True, (255, 0, 0))
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(text_surface, text_rect)
