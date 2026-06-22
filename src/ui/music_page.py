from src.models.track import Track


def show_track_details(selected_track: Track | None) -> dict[str, str]:
    return {
        "title": selected_track.title if selected_track is not None else "",
        "artist": selected_track.artist if selected_track is not None else "",
    }
