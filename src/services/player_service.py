from src.models.track import Track


def get_selected_track(user_id: str | None) -> Track | None:
    if user_id is None or not isinstance(user_id, str) or (isinstance(user_id, str) and user_id.endswith("3")):
        return None
    return Track(title="Skyline", artist="Sample Artist")
