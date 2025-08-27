import requests
import time
from datetime import datetime
from termcolor import cprint

# ┌─────────────────────────────────────────────┐
# │           🔥 Roshan Control Panel 🔥         │
# │     Cinematic Multi-Token Messenger v1.0     │
# └─────────────────────────────────────────────┘

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'referer': 'www.google.com'
}

def send_messages(tokens, thread_id, prefix, messages, delay):
    cycle = 1
    while True:
        for token in tokens:
            # 🔥 Cinematic Cycle Banner
            cprint("\n╔══════════════════════════════════════╗", "cyan")
            cprint("║         🔥 Roshan Control Panel 🔥        ║", "cyan", attrs=["bold"])
            cprint("║     Multi-Token :: Cinematic Cycle     ║", "cyan")
            cprint("╚══════════════════════════════════════╝\n", "cyan")
            cprint(f"🎬 Launching Cycle {cycle} with token: {token[:10]}...", "magenta")

            for msg in messages:
                full_msg = f"{prefix} {msg}"
                api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                params = {'access_token': token, 'message': full_msg}
                timestamp = datetime.now().strftime('%H:%M:%S')

                try:
                    response = requests.post(api_url, data=params, headers=headers)
                    if response.status_code == 200:
                        # ✅ Roshan Legend Banner
                        cprint("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", "green")
                        cprint("🚀 Roshan Legend Here :: Message Deployed", "green", attrs=["bold"])
                        cprint(f"🕒 {timestamp}", "green")
                        cprint(f"📨 Sent: {full_msg}", "green")
                        cprint("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", "green")
                    else:
                        cprint(f"[{timestamp}] ❌ Failed: {full_msg}", "red")
                    time.sleep(delay)
                except Exception as e:
                    cprint(f"[{timestamp}] ⚠️ Error: {e}", "yellow")
                    time.sleep(30)

            cycle += 1
            cprint(f"\n✅ Cycle {cycle - 1} complete for token: {token[:10]}...\n", "cyan")

if __name__ == "__main__":
    print("\n╔════════════════════════════════════════════╗")
    print("║        🔥 ROSHAN RULEX :: LOADER PANEL 🔥       ║")
    print("╚════════════════════════════════════════════╝\n")

    tokens_input = input("🔑 Enter tokens (comma-separated): ").strip()
    thread_id = input("📨 Enter thread ID: ").strip()
    prefix = input("😈 Enter hater name/prefix: ").strip()
    txt_path = input("📄 Enter path to .txt file: ").strip()
    delay = int(input("⏱️ Enter delay in seconds: ").strip())

    try:
        with open(txt_path, 'r', encoding='utf-8') as f:
            messages = [line.strip() for line in f if line.strip()]
        tokens = [t.strip() for t in tokens_input.split(',') if t.strip()]
        send_messages(tokens, thread_id, prefix, messages, delay)
    except Exception as e:
        cprint(f"🚫 Failed to load file or inputs: {e}", "red")
