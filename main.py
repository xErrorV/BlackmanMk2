import pygame

from PIL import Image


set = {
    "heavy": ["assets/heavy.gif", "assets/heavy.ogg"],
    "giganiga": ["assets/black.gif", "assets/black.ogg"]
}
image_path = set["heavy"][0]
music_path = set["heavy"][1]

def main():
    pygame.init()
    pygame.display.set_caption("Get PWNED")
    
    pygame.mixer.init()
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(-1)
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    prev_time = pygame.time.get_ticks()

    image_frames = []
    current_frame = 0

    with Image.open(image_path) as im:
        duration_ms = im.info.get("duration")

        for i in range(0, im.n_frames):
            im.seek(i)
            im2 = im.convert("RGBA")
            image_for_pygame = pygame.image.fromstring(im2.tobytes(), im2.size, im2.mode)
            image_for_pygame = pygame.transform.scale(image_for_pygame, (screen.get_width(), screen.get_height()))
            image_frames.append(image_for_pygame)


    while True:
        clock.tick(128)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - prev_time

        if elapsed_time > duration_ms:
            prev_time = current_time
            current_frame = (current_frame + 1) % (len(image_frames))

        screen.blit(image_frames[current_frame], (0, 0))

        pygame.display.update()


if __name__ == "__main__":
    main()
