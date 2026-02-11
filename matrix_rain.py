# matrix_rain.py - Pure Python Matrix Rain effect (fallback when no C++ compiler)
# Integrated into Rogue Agent Editor via ctypes overlay

import ctypes
import random
import time
import threading
from collections import namedtuple

# Configuration
MAX_CHARS = 256
MAX_COLUMNS = 80
CHAR_FALL_SPEED = 2.0
GREEN_R, GREEN_G, GREEN_B = 0.0, 1.0, 0.0

# Matrix character set
MATRIX_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234567890!@#$%^&*()_+-=[]{}|;:<>?,./~` "
MATRIX_CHAR_COUNT = len(MATRIX_CHARS)

# Data structures
MatrixChar = namedtuple('MatrixChar', ['x', 'y', 'fall_speed', 'character', 'intensity', 'active'])

# Global matrix state  
active_count = 0
matrix_chars = []
rain_intensity = 0.7
matrix_enabled = True

# Initialize matrix characters
def init_chars():
    global matrix_chars
    matrix_chars = []
    for i in range(MAX_CHARS):
        matrix_chars.append(MatrixChar(
            x=0.0, y=0.0, 
            fall_speed=0.0, 
            character=' ', 
            intensity=1.0, 
            active=False
        ))

# Update matrix particles
def update_particles(delta_time):
    global matrix_chars, active_count, rain_intensity
    
    if not matrix_enabled:
        return
    
    # Update active characters
    for i in range(len(matrix_chars)):
        if matrix_chars[i].active:
            matrix_chars[i] = matrix_chars[i]._replace(
                y=matrix_chars[i].y + matrix_chars[i].fall_speed * delta_time * 60.0
            )
            
            # Reset character when it falls off screen
            if matrix_chars[i].y > 600:
                matrix_chars[i] = matrix_chars[i]._replace(active=False)
                active_count -= 1
    
    # Spawn new characters randomly
    spawn_rate = int(rain_intensity * 30)
    for _ in range(min(spawn_rate, MAX_CHARS - active_count)):
        for i in range(len(matrix_chars)):
            if not matrix_chars[i].active and random.random() < 0.01:
                matrix_chars[i] = matrix_chars[i]._replace(
                    x=random.random() * MAX_COLUMNS,
                    y=-20.0,
                    fall_speed=CHAR_FALL_SPEED + random.random() * 1.0,
                    character=random.choice(MATRIX_CHARS),
                    intensity=0.5 + random.random() * 0.5,
                    active=True
                )
                active_count += 1
                break

# Matrix rain main loop
def matrix_rain_loop():
    global matrix_chars, active_count, rain_intensity
    
    last_time = time.time()
    
    while matrix_enabled:
        current_time = time.time()
        delta_time = current_time - last_time
        last_time = current_time
        
        update_particles(delta_time)
        
        # Small delay to prevent excessive CPU usage
        time.sleep(0.016)  # ~60 FPS
        
        yield True

# Start matrix rain thread
def start_matrix_rain():
    matrix_thread = threading.Thread(target=matrix_rain_loop, daemon=True)
    matrix_thread.start()

# Control functions
def set_rain_intensity(intensity):
    global rain_intensity
    rain_intensity = max(0.0, min(1.0, intensity))

def toggle_matrix_rain(enabled):
    global matrix_enabled
    matrix_enabled = enabled

# Initialize
init_chars()

if __name__ == "__main__":
    print("Matrix Rain Python module loaded")
    print("Functions available:")
    print("- init_chars()")
    print("- start_matrix_rain()")
    print("- set_rain_intensity(float)")
    print("- toggle_matrix_rain(bool)")