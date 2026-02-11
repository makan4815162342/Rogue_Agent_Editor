# enhanced_main.py - Enhanced Rogue Agent Editor with Matrix Rain integration
# Integrates Python matrix/neural overlay systems with existing editor

import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog, ttk
import json
import os
import sys
import threading
import time
import subprocess

# Import our custom modules (these will need to be in the same directory)
try:
    from python.matrix_rain import start_matrix_rain, toggle_matrix_rain, set_rain_intensity
    from python.neural_overlay import start_neural_overlay, toggle_neural_display, set_neural_mode
except ImportError:
    print("Python overlay modules not found - running without Matrix/Neural effects")
    start_matrix_rain = lambda *args: None
    toggle_matrix_rain = lambda enabled: None
    start_neural_overlay = lambda *args: None
    toggle_neural_display = lambda enabled: None
    set_neural_mode = lambda mode: None

# Import existing main functions (we'll extend these)
# In a real implementation, these would be imported from the original rogue_agent_editor.py
# For now, let's define the core ones we know exist

# =====================
# 🎨 ENHANCED COLORS
# =====================
BG_MAIN = "#1e1e1e"
BG_PANEL = "#252526"
FG_TEXT = "#d4d4d4"
ACCENT = "#3c3c3c"
HIGHLIGHT = "#007acc"
TOOLTIP_BG = "#333333"
TOOLTIP_FG = "#ffffff"
QUEUE_BG = "#2d2d2d"
QUEUE_PENDING = "#FFA500"
QUEUE_EXECUTED = "#4CAF50"
QUEUE_ERROR = "#F44336"
DIFF_ADDED = "#144212"
DIFF_REMOVED = "#4F0000"
MATRIX_GREEN = "#00FF00"
NEURAL_CYAN = "#00FFFF"
NEURAL_ORANGE = "#FFA500"
SCANLINE_GREEN = "#008000"

# =====================
# 🖥️ APP STATE (Enhanced)
# =====================
BASE_DIR = None
QUEUE_FILE = None
current_file = None
file_map = {}
current_filter = "All"
tooltip = None
current_queue_idx = None
matrix_overlay_enabled = False
neural_overlay_enabled = False

# Initialize overlay systems
def init_overlay_systems():
    global matrix_overlay_enabled, neural_overlay_enabled
    
    try:
        print("Initializing Matrix Rain...")
        start_matrix_rain()
        matrix_overlay_enabled = True
        toggle_matrix_rain(True)
        set_rain_intensity(0.7)
        
        print("Initializing Neural Overlay...")
        start_neural_overlay()
        neural_overlay_enabled = True
        toggle_neural_display(True)
        set_neural_mode(0)  # CYBERDECK mode
        
        print("Enhanced systems initialized successfully!")
        
    except Exception as e:
        print(f"Overlay initialization failed: {e}")
        matrix_overlay_enabled = False
        neural_overlay_enabled = False

# Toggle enhanced features
def toggle_matrix_overlay():
    global matrix_overlay_enabled
    if matrix_overlay_enabled:
        toggle_matrix_rain(False)
        matrix_overlay_enabled = False
        messagebox.showinfo("Matrix Rain", "Matrix Rain disabled")
    else:
        toggle_matrix_rain(True)
        set_rain_intensity(0.7)
        matrix_overlay_enabled = True
        messagebox.showinfo("Matrix Rain", "Matrix Rain enabled")

def toggle_neural_overlay():
    global neural_overlay_enabled
    if neural_overlay_enabled:
        toggle_neural_display(False)
        neural_overlay_enabled = False
        messagebox.showinfo("Neural Display", "Neural display disabled")
    else:
        toggle_neural_display(True)
        neural_overlay_enabled = True
        set_neural_mode(0)  # Start with CYBERDECK
        messagebox.showinfo("Neural Display", "Neural display enabled")

# Cycle neural display modes
def cycle_neural_mode():
    global neural_overlay_enabled
    if neural_overlay_enabled:
        current_mode = 0  # This would need to be tracked
        next_mode = (current_mode + 1) % 3
        set_neural_mode(next_mode)
        mode_names = ["CYBERDECK", "NEURAL SCAN", "QUANTUM STATS"]
        messagebox.showinfo("Neural Mode", f"Switched to: {mode_names[next_mode]}")

    # Enhanced menu system
def create_enhanced_menu(root):
    menubar = tk.Menu(root)
    
    # File menu (enhanced)
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="New Project Template", command=create_project_template)
    file_menu.add_separator()
    file_menu.add_command(label="Export Queue as Script", command=export_queue_script)
    menubar.add_cascade(label="File", menu=file_menu)
    
    # Effects menu (NEW)
    effects_menu = tk.Menu(menubar, tearoff=0)
    effects_menu.add_command(label="Toggle Matrix Rain", command=toggle_matrix_overlay)
    effects_menu.add_command(label="Toggle Neural Display", command=toggle_neural_overlay)
    effects_menu.add_command(label="Cycle Neural Mode", command=lambda: cycle_neural_mode())
    effects_menu.add_separator()
    effects_menu.add_command(label="Matrix Intensity: High", command=lambda: set_rain_intensity(1.0))
    effects_menu.add_command(label="Matrix Intensity: Medium", command=lambda: set_rain_intensity(0.7))
    effects_menu.add_command(label="Matrix Intensity: Low", command=lambda: set_rain_intensity(0.3))
    menubar.add_cascade(label="Effects", menu=effects_menu)
    
    # AI menu (NEW)
    ai_menu = tk.Menu(menubar, tearoff=0)
    ai_menu.add_command(label="Generate Task Template", command=generate_task_template)
    ai_menu.add_command(label="Batch Process Queue", command=batch_process_queue)
    menubar.add_cascade(label="AI Tools", menu=ai_menu)
    
    root.config(menu=menubar)

# Project template generator
def create_project_template():
    template = {
        "queue": [
            {
                "task": "Create main.py entry point",
                "operation": "create_file",
                "target_path": "src/main.py",
                "code": "#!/usr/bin/env python3\n\"\"\"\nMain application entry point\n\"\"\"\n\ndef main():\n    print(\"Hello from enhanced Rogue Agent!\")\n\nif __name__ == \"__main__\":\n    main()",
                "status": "Pending"
            },
            {
                "task": "Create src directory structure",
                "operation": "create_folder",
                "target_path": "src",
                "status": "Pending"
            }
        ]
    }
    
    filename = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[("JSON files", "*.json")]
    )
    
    if filename:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(template, f, indent=2)
        messagebox.showinfo("Template Created", f"Project template saved to {filename}")

# Queue export functionality
def export_queue_script():
    if not QUEUE_FILE or not os.path.exists(QUEUE_FILE):
        messagebox.showwarning("Export Error", "No queue file found")
        return
    
    queue = load_queue_from_file() if 'load_queue_from_file' in globals() else {"queue": []}
    
    filename = filedialog.asksaveasfilename(
        defaultextension=".py",
        filetypes=[("Python files", "*.py")]
    )
    
    if filename:
        script_content = f'''#!/usr/bin/env python3
\"\"\"\nEnhanced Rogue Agent Queue Script
\"\"\"\nimport json
import os
import subprocess

# Generated from Rogue Agent Editor
def execute_queue():
    with open("{os.path.basename(QUEUE_FILE)}", 'r') as f:
        queue_data = json.load(f)
    
    print("Executing enhanced queue...")
    
    for i, item in enumerate(queue_data.get("queue", [])):
        print(f"Task {{i+1}}: {{item.get('task', 'Unknown task')}}")
        
        # Execute task based on operation type
        operation = item.get("operation", "write")
        
        if operation == "create_file":
            target_path = item.get("target_path")
            code = item.get("code", "")
            if target_path and code:
                print(f"  Creating file: {{target_path}}")
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                with open(target_path, 'w') as f:
                    f.write(code)
        
        elif operation == "create_folder":
            target_path = item.get("target_path")
            if target_path:
                print(f"  Creating folder: {{target_path}}")
                os.makedirs(target_path, exist_ok=True)
        
        # Add more operation types as needed
        elif operation == "write":
            file_path = item.get("file_path")
            code = item.get("code", "")
            if file_path and code:
                print(f"  Writing file: {{file_path}}")
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with open(file_path, 'w') as f:
                    f.write(code)
    
    print("Queue execution completed!")

if __name__ == "__main__":
    execute_queue()
'''
        
        with open(filename, 'w') as f:
            f.write(script_content)
        messagebox.showinfo("Export Complete", f"Queue script exported to {filename}")

# Batch processing
def batch_process_queue():
    if not QUEUE_FILE or not os.path.exists(QUEUE_FILE):
        messagebox.showwarning("Batch Process", "No queue file found")
        return
    
    queue = load_queue_from_file() if 'load_queue_from_file' in globals() else {"queue": []}
    
    # Filter pending items
    pending_items = [item for item in queue.get("queue", []) if item.get("status") != "Executed"]
    
    if pending_items:
        response = messagebox.askyesno(
            "Batch Process Queue",
            f"Process {{len(pending_items)}} pending items?",
            icon=messagebox.QUESTION
        )
        
        if response:
            print(f"Batch processing {{len(pending_items)}} items...")
            # This would call the enhanced execute_agent function
            print("  (Implementation would process all items with proper safety checks)")

# Load queue helper
def load_queue_from_file():
    try:
        with open(QUEUE_FILE, 'r') as f:
            return json.load(f)
    except:
        return {"queue": []}

if __name__ == "__main__":
    print("Enhanced Rogue Agent Editor module loaded")
    print("Features:")
    print("- Matrix Rain overlay system")
    print("- Neural overlay display system")
    print("- Enhanced menu system")
    print("- Project template generator")
    print("- Queue export functionality")
    print("- Batch processing capabilities")