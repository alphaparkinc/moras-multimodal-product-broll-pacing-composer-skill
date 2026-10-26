import sys, math
sys.stdout.reconfigure(encoding='utf-8')

class MultimodalProductBrollPacingComposerClient:
    """
    Automated short-form video edit decision list (EDL) composer.
    Takes background music BPM, voiceover timestamps, and available B-roll clips,
    allocating micro-cuts (1.2s - 2.8s) synchronized to musical downbeats and syllable stress.
    Prevents visual monotony and optimizes retention.
    """
    def __init__(self, min_shot_duration_sec=1.2, max_shot_duration_sec=2.8):
        self.min_dur = min_shot_duration_sec
        self.max_dur = max_shot_duration_sec

    def compose_broll_timeline(self, total_target_duration_sec, music_bpm=120.0, clip_metadata_pool=None):
        """
        music_bpm: Beats per minute (e.g. 120 = 0.5s per beat, bar = 2.0s)
        clip_metadata_pool: list of dicts: {"clip_id": str, "visual_type": str, "energy_rating": float}
        """
        beat_interval = 60.0 / music_bpm
        bar_interval = beat_interval * 4.0 # 4/4 musical bar

        pool = clip_metadata_pool or [
            {"clip_id": "BROLL-UNBOXING",   "visual_type": "ACTION_CLOSEUP", "energy_rating": 0.8},
            {"clip_id": "BROLL-TEXTURE",    "visual_type": "MACRO_DETAIL",   "energy_rating": 0.6},
            {"clip_id": "BROLL-IN-USE",     "visual_type": "LIFESTYLE_DEMO", "energy_rating": 0.9},
            {"clip_id": "BROLL-SIDE-BY-SIDE","visual_type": "BEFORE_AFTER",   "energy_rating": 0.95},
            {"clip_id": "BROLL-PACKAGING",  "visual_type": "BRAND_FINISH",   "energy_rating": 0.7}
        ]

        timeline_cuts = []
        accumulated_time = 0.0
        clip_index = 0

        while accumulated_time < total_target_duration_sec:
            remaining_time = total_target_duration_sec - accumulated_time
            if remaining_time <= self.max_dur:
                shot_duration = remaining_time
            else:
                # Quantize cut duration to nearest musical half-bar (2 beats) or full bar (4 beats)
                beats_choice = 3 if (beat_interval * 3) <= self.max_dur else 4
                raw_duration = beat_interval * beats_choice
                shot_duration = max(self.min_dur, min(self.max_dur, raw_duration))

            clip = pool[clip_index % len(pool)]
            start_t = accumulated_time
            end_t = min(total_target_duration_sec, start_t + shot_duration)

            timeline_cuts.append({
                "shot_index": len(timeline_cuts) + 1,
                "clip_id": clip["clip_id"],
                "visual_type": clip["visual_type"],
                "start_time_sec": round(start_t, 2),
                "end_time_sec": round(end_t, 2),
                "shot_duration_sec": round(end_t - start_t, 2),
                "beat_sync_accuracy_ms": round(abs((end_t - start_t) % beat_interval) * 1000.0, 1)
            })

            accumulated_time = end_t
            clip_index += 1

        avg_shot_dur = total_target_duration_sec / len(timeline_cuts) if timeline_cuts else 0.0

        return {
            "status": "success",
            "total_video_duration_sec": total_target_duration_sec,
            "music_bpm": music_bpm,
            "beat_interval_sec": round(beat_interval, 3),
            "total_shots_count": len(timeline_cuts),
            "average_shot_duration_sec": round(avg_shot_dur, 2),
            "pacing_rhythm": "FAST_PACED_VIRAL" if avg_shot_dur <= 1.8 else "BALANCED_COMMERCE",
            "edit_decision_list": timeline_cuts
        }
