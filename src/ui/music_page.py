from src.models.track import Track


def show_track_details(selected_track: Track | None) -> dict[str, str]:
    if selected_track is None:
        return {
            "title": "",
            "artist": "",
        }
    return {
        "title": selected_track.title,
        "artist": selected_track.artist,
    }
