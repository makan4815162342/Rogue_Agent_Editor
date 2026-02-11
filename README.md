# Rogue_Agent_Editor
A Free Editor with Agentic Features.

<img width="781" height="511" alt="Rogue_Agent_Editor_1" src="https://github.com/user-attachments/assets/c5ddc3c4-4b47-4973-9033-7c21f559599b" />

The Link for Downloading: https://makan-ansari.itch.io/rogue-agent-editor

The idea for making Rogue Agent Editor was for when I hit the bottom and yet be able to use AI for coding with Agents.

Rogue Agent Editor does this with it you can train Chat AI Models to act as Agent for you, and you can edit your codes in this Editor at ease, I remember to spent 4 month from 6 to 15 hours every day with Gemini, Copy, Pasting codes to make my Rogue SDF Modeler! before Agents were available or I knew about them! but with Rogue Agent Editor I can make this process almost automatic.

Agents are expensive and some only work if you pay up, the free versions have limited Queue, Tokens! for example, Anti-Gravity IDE has a limited Token that resets its Allowance each week for the free user, or GitHub Copilot you have to wait a month! and so forth...

Even Open Code AI the free solution has 200K limited Tokens with weaker models to work with!

Agents for free users are not in a good shape that much TBH and if you work on a serious project and on a budget or don't have access to internet or can't pay because of restrictions to your country, you are in a tough situation! 

Also let's be honest AI Tools are expensive even if you can afford them and you are okay with it, it's not that cheap! one AI model is not enough for Vibe Coding, you need to use Chat-GPT, Gemini, Claude and other models to fix a problem sometimes one AI Model can't fix the problem, I personally experienced this it. 

So, I thought hey AI Google Studio for example gives you one million Tokens for FREE for each conversation! Chat-GPT if you don't Generate Images or Videos can talk to you like forever? we have Qwen, DeepSeek, Local AI Models... you name it these AI Chat Models have a generous Tokens, if you just Train them with JSON language you can use them as Agents.

So, if you are like me, sometimes you hit the bottom and need Agents for free, Rogue Agent Editor will help you.

Below is an AI Description that goes into detail explaining the Editor, you can read it to help you better, later on, I will try to make a tutorial about it too.

# Rogue Agent Editor

**An Agentic Code Editor for the Cyberpunk Era.**

Rogue Agent Editor is a high-fidelity, agentic code editor designed to bridge the gap between human creativity and AI execution. Unlike traditional editors, it features a native "Agentic Queue" system that allows AI models to safely plan, review, and execute complex multi-file operations via JSON tasks, all wrapped in an immersive, neural-interface-inspired environment.

---

## 🤖 Core Features: The Agentic Workflow

The Rogue Agent Editor is built from the ground up to serve as the "hands" for your AI coding assistants. It exposes a robust JSON-based API that AI models can use to interact with your file system safely and deterministically.

### 1. The Agentic Task Queue
Instead of blindly applying code patches, Rogue Agent Editor maintains a structured **Task Queue**. AI agents can populate this queue with precise operations:
- **Write**: Create or overwrite files with new code.
- **Create**: Generate directory structures and files.
- **Refactor**: Move, rename, or copy files/folders with conflict detection.
- **Delete**: Remove obsolete assets with safety checks.

### 2. Human-in-the-Loop Safety
You remain in control. The editor provides:
- **Review Popups**: Inspect every line of code before it touches your disk.
- **Conflict Resolution**: Choose to overwrite, skip, or backup files when conflicts arise.
- **Undo/Redo**: Roll back changes if an agent hallucinates or makes a mistake.
- **Destructive Action Confirmation**: High-risk operations (like bulk deletes) require explicit approval.

### 3. AI Context Generation
The editor helps your AI understand your project:
- **Project Reports**: Generate one-click summaries of your file structure and content to paste into LLM contexts.
- **Token-Aware**: Optimized to provide maximum context with minimum token usage.

---

## ⚡ Additional Features

While the Agentic capabilities are the core, the Rogue Agent Editor delivers a fully immersive cyberpunk experience.

### 🎧 Audio-Reactive Environment
- **Generative Soundscapes**: Real-time procedural audio engine generating Blade Runner-esque blues, dark industrial synths, and ethereal pads.
- **Reactive SFX**: UI interactions trigger satisfying, futuristic sound effects.
- **Local Audio Player**: Integrated MP3/WAV player for your own hacking playlists.

### 👁️ Neural Interface Visuals
- **Matrix Rain**: Customizable digital rain overlay with multiple color schemes (Neon, Hacker Green, Cyberpunk Pink).
- **CRT Simulation**: Optional CRT monitor effects with scanlines, RGB separation, and screen curvature.
- **Neural Overlay**: Animated headers and system status metrics that react to editor activity.

### 🛠️ Professional Editing Tools
- **Syntax Highlighting**: Full support for Python, JSON, C/C++, JavaScript, HTML/CSS, Rust, Go, and more.
- **Project Management**: Hierarchical file tree with real-time search and filtering.
- **Integrated Terminal**: Built-in command line for running scripts and git commands without leaving the immersion.

---

## 📥 Installation and Setup

### Requirements
- **OS**: Windows 10/11 (Primary support), Linux/macOS (Experimental)
- **Python**: 3.8 or higher
- **Dependencies**: `tkinter`, `Pillow`, `winsound` (Windows only)

### Quick Start
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/rogue-agent-editor.git
   cd rogue-agent-editor
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   # Or manually: pip install pillow
   ```

3. **Run the Editor**
   ```bash
   python rogue_agent_editor.py
   ```

*Note: A standalone `.exe` version is available in the Releases section for Windows users who prefer a portable application.*

---

## 📝 Usage Examples: Controlling the Agent

The Rogue Agent Editor accepts a specific JSON structure for its task queue. You can copy-paste these structures directly into the "Agent Queue" tab or have your AI generate them.

### Example 1: Creating a Python Script
```json
{
  "queue": [
    {
      "operation": "create_file",
      "target_path": "src/main.py",
      "code": "print('System Online')\nstart_sequence()",
      "task": "Initialize main application entry point",
      "conflict_resolution": "ask"
    }
  ]
}
```

### Example 2: Refactoring a Project Structure
```json
{
  "queue": [
    {
      "operation": "create_folder",
      "target_path": "assets/images",
      "conflict_resolution": "skip"
    },
    {
      "operation": "move",
      "source_path": "logo.png",
      "target_path": "assets/images/logo.png",
      "require_confirmation": false
    }
  ]
}
```

### Example 3: Running a Shell Command
```json
{
  "queue": [
    {
      "operation": "execute_command",
      "command": "pip install -r requirements.txt",
      "task": "Install dependencies",
      "require_confirmation": true
    }
  ]
}
```

---

## 🔧 Technical Details

For the netrunners and code cowboys interested in the architecture:
- **Core Framework**: Built on Python's `tkinter` for maximum portability and native OS integration without the bloat of Electron.
- **Audio Engine**: Custom-written procedural audio generation using raw wave manipulation and `winsound`/`ctypes` for low-latency playback.
- **Rendering**: Custom canvas rendering pipeline for Matrix rain and CRT effects, optimized for 60FPS on standard hardware.
- **State Management**: JSON-driven state for both application settings and the agentic task queue, ensuring persistence and human-readability.

---

## 🤝 Contributing Guidelines

The Rogue Agent Editor is open source and thrives on community contributions.
1. **Fork the Repository**: Create your own branch of the project.
2. **Create a Feature Branch**: `git checkout -b feature/AmazingFeature`
3. **Commit Your Changes**: `git commit -m 'Add some AmazingFeature'`
4. **Push to the Branch**: `git push origin feature/AmazingFeature`
5. **Open a Pull Request**: We welcome everything from bug fixes to new audio themes and visual effects.

---

## 📜 License Information

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 📞 Contact and Support

- **Bug Reports**: Open an issue on the [GitHub Issues](https://github.com/yourusername/rogue-agent-editor/issues) page.
- **Community**: Join our Discord server (link coming soon) to discuss features and share your agent workflows.
- **Developer**: Follow the development progress on [itch.io](https://yourusername.itch.io/rogue-agent-editor).

---

*System Status: ONLINE*  
*Neural Link: STABLE*  
*Happy Hacking.*

