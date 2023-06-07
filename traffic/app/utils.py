def get_file_path(file, filename, file_type):
    """Возвращает путь до файлов."""
    if file_type in [
        "day_traffic_graph",
        "average_traffic_graph",
    ]:
        return "pictures/{file_type}/{id}_{filename}".format(
            id=file.id,
            filename=filename,
            file_type=file_type,
        )
    return "{file_type}/{id}_{filename}".format(
        id=file.id,
        filename=filename,
        file_type=file_type,
    )