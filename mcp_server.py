import sys, json
from client import MultimodalProductBrollPacingComposerClient
sys.stdout.reconfigure(encoding='utf-8')

def handle_mcp():
    composer = MultimodalProductBrollPacingComposerClient()
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps({"status": "ready", "skill": "moras-multimodal-product-broll-pacing-composer-skill"}))
        return
    req = json.loads(sys.stdin.read() or "{}")
    dur = req.get("total_target_duration_sec", 15.0)
    bpm = req.get("music_bpm", 120.0)
    res = composer.compose_broll_timeline(dur, bpm)
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    handle_mcp()
