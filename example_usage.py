from client import MultimodalProductBrollPacingComposerClient
import sys
sys.stdout.reconfigure(encoding='utf-8')

def main():
    composer = MultimodalProductBrollPacingComposerClient()
    print("=== MORAS MULTIMODAL B-ROLL PACING COMPOSER ===")

    # Compose 20-second dynamic commerce video at 128 BPM
    res = composer.compose_broll_timeline(total_target_duration_sec=20.0, music_bpm=128.0)
    print()
    print(f"Target Duration  : {res['total_video_duration_sec']}s @ {res['music_bpm']} BPM (Beat: {res['beat_interval_sec']}s)")
    print(f"Total Cuts       : {res['total_shots_count']} shots (Avg Duration: {res['average_shot_duration_sec']}s)")
    print(f"Pacing Rhythm    : {res['pacing_rhythm']}")
    print()
    print("Timeline Edit Decision List (EDL):")
    for shot in res['edit_decision_list']:
        print(f"  Shot #{shot['shot_index']:02d}: {shot['start_time_sec']:4.1f}s - {shot['end_time_sec']:4.1f}s ({shot['shot_duration_sec']}s) | {shot['visual_type']:<15} | ID: {shot['clip_id']}")

if __name__ == "__main__":
    main()
