from src.models.track import Track


def get_selected_track(user_id: str) -> Track | None:
    if not isinstance(user_id, str):
        return None
    if user_id.endswith("3"):
        return None
    return Track(title="Skyline", artist="Sample Artist")
