1. *Where did you find the code and why did you choose it? (Provide the link)*

- I found this code in the pygame community examples. Link: https://github.com/pygame-community/pygame-ce/blob/main/examples/aliens.py
---

1. *What does the program do? What's the general structure of the program?* 

- The program loads an aliens pygame loading other files from the repository
---

1. *Function analysis: pick one function and analyze it in detail:*
def load_image(file):
    """loads an image, prepares it for play"""
    file = os.path.join(main_dir, "data", file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit(f'Could not load image "{file}" {pygame.get_error()}')
    return surface.convert()

- *What does this function do?*
- Thanks to a good practice by the coder, explains that it prepares an image for the game.
- *What are the inputs and outputs?*
- File and surface. The coder is setting the foundation to load images into the game. He´s also managing error functions.
- *How does it work (step by step)?*
- He loads the image file by creating the function file = os.path.join(main_dir, "data", file)
- He prevents error messages that crash the game if the image file is missing with 
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit(f'Could not load image "{file}" {pygame.get_error()}')
    return surface.convert()

---

1. *Takeaways: are there anything you can learn from the code? (How to structure your code, a clean solution for some function you might also need...)*
- It helps me know how to structure the code in a cleaner way! Also to know that every block is different from the other

1. *What parts of the code were confusing or difficult at the beginning to understand?*
- Were you able to understand what it is doing after your own research?
- Thanks to the explanations of the coder in every group, I understood the purpose of everything!
