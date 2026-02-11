# neural_overlay.py - Cyberpunk neural terminal headers (Python fallback)
# Integrated into Rogue Agent Editor with overlay capabilities

import time
import threading
from collections import namedtuple

# Configuration
MAX_NEURAL_LINES = 20
MAX_LINE_LENGTH = 80
TERMINAL_WIDTH = 60
TERMINAL_HEIGHT = 15

# Animation variables
neural_time = 0.0
current_neural_line = 0
neural_active = True
text_fade = 0.0
display_mode = 0  # 0: CYBERDECK, 1: NEURAL_SCAN, 2: QUANTUM_STATS

# Neural text content for different modes
CYBERDECK_TEXT = [
    "═══════════════════════════════════",
    "║ ROGUE_AGENT_NEURAL_TERMINAL v2.1.7 ONLINE ║",
    "║ MEMORY: 78.3TB FREE // PROCESSOR: QUANTUM X9      ║",  
    "║ ALIEN_ARTIFACTS: 0 // THREAT_LEVEL: MINIMAL            ║",
    "║ SCANNING FOR NEURAL ANOMALIES...                   ║",
    "╚═══════════════════════════════════"
]

NEURAL_SCAN_TEXT = [
    "NEURAL PROTOCOLS ACTIVE",
    "ENHANCING VISUAL INTERFACE...",
    "MATRIX RAIN: ONLINE",
    "QUANTUM PROCESSING: OPERATIONAL"
]

QUANTUM_STATS = [
    "QUANTUM ENTANGLEMENT: 98.7%",
    "TEMPORAL SYNCHRONIZATION: STABLE",
    "DATA INTEGRITY: 99.3%",
    "NEURAL RESPONSE TIME: 1.2ms"
]

# Data structures
NeuralLine = namedtuple('NeuralLine', ['text', 'fade_in_time', 'display_duration', 'text_length'])

# Neural lines
neural_lines = []

# Initialize neural lines
def init_lines():
    global neural_lines
    neural_lines = []
    for i in range(MAX_NEURAL_LINES):
        neural_lines.append(NeuralLine(
            text='', fade_in_time=0.0, display_duration=3.0, text_length=0
        ))

# Update neural display animations
def update_neural_display(delta_time):
    global neural_time, current_neural_line, neural_active, text_fade, display_mode
    
    if not neural_active:
        return
    
    neural_time += delta_time
    
    # Update animations
    for i in range(len(neural_lines)):
        if neural_lines[i].text_length > 0:
            # Handle fade in
            if neural_lines[i].fade_in_time < 1.0:
                neural_lines[i] = neural_lines[i]._replace(
                    fade_in_time=min(1.0, neural_lines[i].fade_in_time + delta_time * 2.0)
                )
            
            # Handle fade out
            if neural_time - neural_lines[i].fade_in_time > neural_lines[i].display_duration:
                fade_progress = min(1.0, 
                    (neural_time - neural_lines[i].fade_in_time - neural_lines[i].display_duration) * 0.5)
                text_fade = 1.0 - fade_progress
            else:
                text_fade = 1.0

# Set neural display mode
def set_neural_mode(mode):
    global display_mode, current_neural_line
    display_mode = max(0, min(2, mode))
    current_neural_line = max(0, current_neural_line - 1)
    
    switch display_mode:
        case 0:  # CYBERDECK
            set_neural_text("═══════════════════════════════════", 0)
            set_neural_text("║ ROGUE_AGENT_NEURAL_TERMINAL v2.1.7 ONLINE ║", 1)
            set_neural_text("║ MEMORY: 78.3TB FREE // PROCESSOR: QUANTUM X9      ║", 2)
            set_neural_text("║ ALIEN_ARTIFACTS: 0 // THREAT_LEVEL: MINIMAL            ║", 3)
            break
            
        case 1:  # NEURAL SCAN
            set_neural_text("NEURAL PROTOCOLS ACTIVE", 0)
            set_neural_text("ENHANCING VISUAL INTERFACE...", 1)
            set_neural_text("MATRIX RAIN: ONLINE", 2)
            break
            
        case 2:  # QUANTUM STATS
            set_neural_text("QUANTUM ENTANGLEMENT: 98.7%", 0)
            set_neural_text("TEMPORAL SYNCHRONIZATION: STABLE", 1)
            set_neural_text("DATA INTEGRITY: 99.3%", 2)
            break

# Set neural text for specific line
def set_neural_text(text, line_index):
    global neural_lines, current_neural_line
    
    if line_index < 0 or line_index >= len(neural_lines):
        return
    
    # Clear existing text
    current_neural_line = max(current_neural_line, line_index + 1)
    
    # Set new text with animation
    text_len = min(len(text), MAX_LINE_LENGTH)
    neural_lines[line_index] = neural_lines[line_index]._replace(
        text=text[:text_len],
        text_length=text_len,
        fade_in_time=neural_time,
        display_duration=3.0
    )

# Toggle neural display
def toggle_neural_display(enabled):
    global neural_active
    neural_active = enabled

# Start neural overlay
def start_neural_overlay():
    init_lines()
    set_neural_mode(0)  # Start with CYBERDECK
    neural_time = 0.0
    neural_active = True

# Neural display main loop
def neural_overlay_loop():
    global neural_time, neural_active
    
    last_time = time.time()
    
    while neural_active:
        current_time = time.time()
        delta_time = current_time - last_time
        last_time = current_time
        
        update_neural_display(delta_time)
        
        # Small delay to prevent excessive CPU usage
        time.sleep(0.016)  # ~60 FPS
        
        yield True

# Start neural overlay thread
def start_neural_overlay():
    neural_thread = threading.Thread(target=neural_overlay_loop, daemon=True)
    neural_thread.start()

# Initialize
start_neural_overlay()

if __name__ == "__main__":
    print("Neural Overlay Python module loaded")
    print("Functions available:")
    print("- init_lines()")
    print("- start_neural_overlay()")
    print("- set_neural_mode(int)")
    print("- set_neural_text(text, line)")
    print("- toggle_neural_display(bool)")