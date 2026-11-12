
import pygame
import sys
import math

pygame.init()

# Window
WIDTH = 1200
HEIGHT = 750

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Printer Graphics Lab")

clock = pygame.time.Clock()

# Colors
BG = (22, 26, 37)
PANEL = (32, 38, 52)
WHITE = (240, 243, 250)
BLUE = (55, 145, 245)
GRAY = (165, 175, 190)
DARK = (55, 63, 78)
GREEN = (60, 190, 130)
ORANGE = (245, 165, 65)

# Fonts
font = pygame.font.SysFont("Arial", 23)
small = pygame.font.SysFont("Arial", 17)
tiny = pygame.font.SysFont("Arial", 14)

# Selected component
selected = "None"

# Component information
components = {
    "Printer Body": (
        "Main printer structure",
        "Contains internal components",
        "Material: Plastic",
        "Function: Main support"
    ),
    "Scanner Lid": (
        "Upper printer cover",
        "Protects scanner glass",
        "Function: Document scanning"
    ),
    "Paper": (
        "Paper input",
        "Used for printing documents",
        "Function: Paper supply"
    ),
    "Roller": (
        "Paper feeding roller",
        "Moves paper through printer",
        "Function: Paper movement"
    ),
    "Output Tray": (
        "Printed paper support",
        "Receives printed pages",
        "Function: Paper output"
    ),
    "Power Button": (
        "Printer power control",
        "Turns device on and off",
        "Function: Power management"
    )
}


def draw_text(text, x, y, color=WHITE, f=font):
    image = f.render(text, True, color)
    screen.blit(image, (x, y))


def draw_printer():

    # Paper
    paper_rect = pygame.Rect(515, 135, 180, 115)
    pygame.draw.rect(screen, WHITE, paper_rect, border_radius=4)
    pygame.draw.line(screen, GRAY, (540, 165), (670, 165), 2)
    pygame.draw.line(screen, GRAY, (540, 185), (650, 185), 2)

    # Scanner lid
    lid_rect = pygame.Rect(405, 235, 400, 55)
    pygame.draw.rect(screen, GRAY, lid_rect, border_radius=12)

    # Printer body
    body_rect = pygame.Rect(380, 280, 450, 265)
    pygame.draw.rect(screen, DARK, body_rect, border_radius=18)

    # Front panel
    pygame.draw.rect(
        screen, (75, 85, 105),
        (405, 315, 400, 195),
        border_radius=12
    )

    # Display
    pygame.draw.rect(
        screen, (15, 23, 35),
        (445, 345, 120, 55),
        border_radius=7
    )
    draw_text("READY", 470, 360, GREEN, small)

    # Power button
    button_center = (755, 375)
    pygame.draw.circle(screen, GREEN, button_center, 19)
    pygame.draw.circle(screen, WHITE, button_center, 8, 2)

    # Rollers
    pygame.draw.circle(screen, BLUE, (470, 465), 32)
    pygame.draw.circle(screen, WHITE, (470, 465), 11)

    pygame.draw.circle(screen, BLUE, (740, 465), 32)
    pygame.draw.circle(screen, WHITE, (740, 465), 11)

    # Output tray
    tray_rect = pygame.Rect(455, 545, 300, 25)
    pygame.draw.rect(
        screen, GRAY, tray_rect,
        border_radius=6
    )

    # Labels
    draw_text("PRINTER MODEL", 510, 610, BLUE, small)

    return {
        "Paper": paper_rect,
        "Scanner Lid": lid_rect,
        "Printer Body": body_rect,
        "Power Button": pygame.Rect(735, 355, 40, 40),
        "Output Tray": tray_rect,
        "Roller": pygame.Rect(435, 430, 340, 70)
    }


def draw_sidebar():

    pygame.draw.rect(
        screen, PANEL,
        (0, 70, 230, HEIGHT - 70)
    )

    draw_text("WORKSPACE", 25, 105, BLUE, small)

    menu = [
        "Main View",
        "Drawing Lab",
        "Transform Lab",
        "Animation Lab",
        "Clipping Lab"
    ]

    for i, item in enumerate(menu):
        y = 155 + i * 55

        if i == 0:
            pygame.draw.rect(
                screen, (48, 76, 115),
                (12, y - 8, 205, 40),
                border_radius=7
            )

        draw_text(item, 30, y, WHITE, small)


def draw_information_panel():

    pygame.draw.rect(
        screen, PANEL,
        (900, 70, 300, HEIGHT - 70)
    )

    draw_text("COMPONENT INFO", 925, 110, BLUE, small)

    pygame.draw.line(
        screen, DARK,
        (925, 145), (1175, 145), 2
    )

    if selected == "None":
        draw_text("Select a component", 925, 180, GRAY, small)
        draw_text("Click on the printer", 925, 210, GRAY, small)
        draw_text("to see its information.", 925, 235, GRAY, small)

    else:
        draw_text(selected, 925, 180, GREEN, font)

        info = components[selected]

        for i, line in enumerate(info):
            draw_text(line, 925, 230 + i * 42, WHITE, small)

    pygame.draw.line(
        screen, DARK,
        (925, 430), (1175, 430), 2
    )

    draw_text("INTERACTION", 925, 455, BLUE, small)
    draw_text("Mouse: Select parts", 925, 495, GRAY, small)
    draw_text("FPS: 60", 925, 530, GRAY, small)


def draw_header():

    pygame.draw.rect(
        screen, PANEL,
        (0, 0, WIDTH, 70)
    )

    draw_text(
        "PRINTER GRAPHICS LAB",
        25, 20, BLUE
    )

    draw_text(
        "Interactive Printer Model",
        870, 25, GRAY, small
    )


def draw_interface():

    screen.fill(BG)

    draw_header()
    draw_sidebar()

    hitboxes = draw_printer()

    # Highlight selected component
    if selected != "None":

        rect = hitboxes[selected]

        pygame.draw.rect(
            screen,
            ORANGE,
            rect,
            3,
            border_radius=8
        )

    draw_information_panel()

    pygame.display.flip()

    return hitboxes


# Main loop
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                mouse_x, mouse_y = event.pos

                hitboxes = {
                    "Paper": pygame.Rect(515, 135, 180, 115),
                    "Scanner Lid": pygame.Rect(405, 235, 400, 55),
                    "Printer Body": pygame.Rect(380, 280, 450, 265),
                    "Power Button": pygame.Rect(735, 355, 40, 40),
                    "Output Tray": pygame.Rect(455, 545, 300, 25),
                    "Roller": pygame.Rect(435, 430, 340, 70)
                }

                # Check specific parts before the body
                priority = [
                    "Power Button",
                    "Paper",
                    "Roller",
                    "Output Tray",
                    "Scanner Lid",
                    "Printer Body"
                ]

                selected = "None"

                for name in priority:
                    if hitboxes[name].collidepoint(mouse_x, mouse_y):
                        selected = name
                        break

    draw_interface()

    clock.tick(60)


pygame.quit()
sys.exit()
